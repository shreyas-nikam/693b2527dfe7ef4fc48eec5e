
from streamlit.testing.v1 import AppTest
import pandas as pd
import numpy as np
import pytest

# It is assumed that 'source.py' is available in the same directory
# and contains all necessary functions and constants.
# For testing purposes, we assume create_simulated_data()
# successfully creates the required CSVs or they already exist.
# The AppTest.from_file("app.py").run() call will execute
# initialize_session_state() which, in turn, calls create_simulated_data().

def get_app_test_instance():
    """Helper function to get a fresh AppTest instance."""
    return AppTest.from_file("app.py")

def test_initial_app_load_and_session_state_init():
    """
    Verify initial app load, page configuration, and session state initialization.
    This also implicitly tests the 'Introduction' tab's content.
    """
    at = get_app_test_instance().run()

    # Verify page config elements
    assert at.title[0].value == "QuLab: AI Readiness score"
    assert at.sidebar.image[0].image_source == "https://www.quantuniversity.com/assets/img/logo5.jpg"

    # Verify session state is initialized with expected dataframes
    assert 'idiosyncratic_df' in at.session_state
    assert isinstance(at.session_state['idiosyncratic_df'], pd.DataFrame)
    assert not at.session_state['idiosyncratic_df'].empty

    assert 'alice_profile' in at.session_state
    assert at.session_state['alice_profile']['persona_id'] == 'Alice'
    assert at.session_state['alice_profile']['experience_years'] == 7 # Default value

    assert 'target_roles' in at.session_state
    assert 'AI Quant Analyst' in at.session_state['target_roles'] # Default value

    # Verify initial calculated scores are None or empty before computation
    assert at.session_state['alice_ai_fluency_score'] is None
    assert at.session_state['alice_vr_score'] is None
    assert not at.session_state['hr_scores']
    assert at.session_state['air_df'].empty

    # Verify Introduction tab content (Tab 0)
    assert at.tabs[0].header[0].value == "Welcome to the AI-Readiness Career Navigator!"
    assert "Your Persona: Alice, a Senior Quantitative Analyst" in at.tabs[0].subheader[0].value
    assert "The AI-Readiness Score (AI-R) Framework" in at.tabs[0].subheader[1].value
    # Check for a specific formula rendering
    assert r"$$AI-R_{{i,t}} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{{i}}^R(t) + \beta \cdot Synergy\%(V_i^R, H_{{i}}^R)$$" in at.tabs[0].markdown[5].value


def test_profile_and_goals_tab_interactions_and_calculation():
    """
    Test interactions on the 'Profile & Goals' tab (Tab 1),
    including updating profile details and triggering the initial readiness calculation.
    """
    at = get_app_test_instance()
    at.run() # Initial run on Tab 0

    # Interact with widgets in Tab 1: Profile & Goals
    # 1.1. Professional Background - modify values
    at.tabs[1].selectbox[0].set_value("PhD in target field").run() # Education Level
    at.tabs[1].number_input[0].set_value(10).run() # Years of Experience

    # Modify an AI-Fluency sub-factor: 'prompting' is slider[0]
    at.tabs[1].slider[0].set_value(0.8).run() # ai_fluency_prompting

    # Modify a Domain-Expertise sub-factor: 'portfolio' is slider[7] (after 7 ai_fluency sliders)
    at.tabs[1].slider[7].set_value(0.9).run() # domain_expertise_portfolio

    # Modify an Adaptive-Capacity sub-factor: 'cognitive_flexibility' is slider[10] (after 7 ai_fluency + 3 domain_expertise sliders)
    at.tabs[1].slider[10].set_value(0.95).run() # adaptive_capacity_cognitive_flexibility

    # 1.2. Current Skill Levels - modify a skill: 'Python' is slider[13] (after 7 ai_fluency + 3 domain_expertise + 3 adaptive_capacity sliders)
    at.tabs[1].slider[13].set_value(9).run() # current_skill_Python

    # 1.3. Target AI-Enabled Financial Roles - modify selected roles
    at.tabs[1].multiselect[0].set_value(['AI Quant Analyst', 'AI Risk Analyst', 'ML Engineer in Trading']).run()

    # Click the "Calculate Initial Readiness & Opportunity" button
    at.tabs[1].button[0].click().run() # This triggers a rerun and updates session state

    # Assert success message is displayed on Tab 1
    assert at.tabs[1].success[0].value == "Initial Readiness & Opportunity calculated! Proceed to the next tab."

    # Assert session state updates after calculation
    assert at.session_state['alice_profile']['education_level'] == "PhD in target field"
    assert at.session_state['alice_profile']['experience_years'] == 10
    assert at.session_state['alice_profile']['ai_fluency_subfactors']['prompting'] == 0.8
    assert at.session_state['alice_profile']['domain_expertise_subfactors']['portfolio'] == 0.9
    assert at.session_state['alice_profile']['adaptive_capacity_subfactors']['cognitive_flexibility'] == 0.95
    assert at.session_state['alice_profile']['current_skills']['Python'] == 9
    assert 'ML Engineer in Trading' in at.session_state['target_roles']

    assert at.session_state['alice_ai_fluency_score'] is not None and at.session_state['alice_ai_fluency_score'] > 0
    assert at.session_state['alice_domain_expertise_score'] is not None and at.session_state['alice_domain_expertise_score'] > 0
    assert at.session_state['alice_adaptive_capacity_score'] is not None and at.session_state['alice_adaptive_capacity_score'] > 0
    assert at.session_state['alice_vr_score'] is not None and at.session_state['alice_vr_score'] > 0
    assert len(at.session_state['hr_scores']) == 3 # For the three roles selected


def test_opportunity_evaluation_tab_content():
    """
    Test that the 'Opportunity Evaluation' tab (Tab 2) correctly displays scores and charts
    after initial readiness calculation from Tab 1.
    """
    at = get_app_test_instance()
    # Simulate having run the 'Profile & Goals' calculations to populate necessary session state
    at.tabs[1].selectbox[0].set_value("Master's in Finance").run()
    at.tabs[1].number_input[0].set_value(7).run()
    at.tabs[1].multiselect[0].set_value(['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst']).run()
    at.tabs[1].button[0].click().run() # This populates the necessary session_state for Tab 2 content

    # Assert on Tab 2's content (index 2 for the tabs list)
    assert at.tabs[2].header[0].value == "2. Opportunity Evaluation: AI-Readiness, VR, HR & Skill Gaps"
    assert "Total VR Score" in at.tabs[2].metric[0].label
    assert float(at.tabs[2].metric[0].value) == pytest.approx(at.session_state['alice_vr_score'], abs=0.01)

    assert "AI-Fluency" in at.tabs[2].metric[1].label
    assert float(at.tabs[2].metric[1].value) == pytest.approx(at.session_state['alice_ai_fluency_score'], abs=0.01)

    assert not at.tabs[2].dataframe[0].empty # HR scores dataframe
    assert 'Role' in at.tabs[2].dataframe[0].columns
    assert 'HR_Score' in at.tabs[2].dataframe[0].columns
    assert len(at.tabs[2].dataframe[0]) == len(at.session_state['target_roles'])

    assert not at.tabs[2].dataframe[1].empty # AI-R scores dataframe
    assert 'AI_R_Score' in at.tabs[2].dataframe[1].columns
    assert at.session_state['top_role']['AI_R_Score'] == pytest.approx(at.tabs[2].dataframe[1]['AI_R_Score'].max(), abs=0.01)

    # Check for text indicating the top role, assuming default markdown ordering.
    # The exact markdown index might shift, so a partial string check is safer.
    assert f"Alice's Top AI-R Role: **{at.session_state['top_role']['Role']}**" in at.tabs[2].markdown[14].value

    assert at.tabs[2].pyplot[0] is not None # AI-R bar chart is displayed
    assert at.tabs[2].pyplot[1] is not None # Skill gaps radar chart is displayed

    assert 'all_skill_gaps' in at.session_state
    assert at.session_state['top_role']['Role'] in at.session_state['all_skill_gaps']


def test_learning_optimization_tab_interactions_and_results():
    """
    Test interactions on the 'Learning Optimization' tab (Tab 3),
    including setting constraints and optimizing learning pathways.
    """
    at = get_app_test_instance()
    # Ensure session state is prepared (from Tab 1 and Tab 2 calculations for a complete flow)
    at.tabs[1].selectbox[0].set_value("Master's in Finance").run()
    at.tabs[1].number_input[0].set_value(7).run()
    at.tabs[1].multiselect[0].set_value(['AI Quant Analyst']).run() # Focus on one role for optimization
    at.tabs[1].button[0].click().run() # This calculates VR/HR and triggers a rerun
    at.run() # Rerun one more time to ensure all Tab 2 calculations (AI-R, top_role) are finalized

    # Assert top_role is set, so Tab 3's optimization logic can proceed
    assert 'top_role' in at.session_state
    assert at.session_state['top_role'] is not None
    assert not isinstance(at.session_state['top_role'], dict) # should be a Series-like object if from df.loc
    assert 'AI_R_Score' in at.session_state['top_role']

    # Navigate to Tab 3: Learning Optimization (index 3 for the tabs list)
    # 3.1. Set Learning Constraints - modify values
    at.tabs[3].number_input[0].set_value(200).run() # Max Learning Time (hours)
    at.tabs[3].number_input[1].set_value(2000).run() # Max Learning Budget (USD)
    at.tabs[3].slider[0].set_value(0.2).run() # Cost Weight (Lambda)

    # Click "Optimize Learning Pathway" button
    at.tabs[3].button[0].click().run() # This triggers a rerun and updates session state

    # Assert success message is displayed on Tab 3
    assert at.tabs[3].success[0].value == "Learning pathway optimized!"

    # Assert session state updates with optimization results
    assert 'recommended_paths' in at.session_state
    assert 'total_time_invested' in at.session_state and at.session_state['total_time_invested'] >= 0
    assert 'total_cost_invested' in at.session_state and at.session_state['total_cost_invested'] >= 0
    assert 'projected_air' in at.session_state and at.session_state['projected_air'] is not None
    
    # Expect projected AI-R to be greater than initial AI-R if pathways are found
    if at.session_state['recommended_paths']:
        assert at.session_state['projected_air'] > at.session_state['initial_air_optimal_role']

    # Assert recommended paths and summary details are displayed
    assert "Total estimated time investment:" in at.tabs[3].markdown[5].value
    assert "Total estimated cost investment:" in at.tabs[3].markdown[6].value
    assert "Projected AI-R after pathways:" in at.tabs[3].markdown[8].value

    # Assert plot is displayed
    assert at.tabs[3].pyplot[0] is not None


def test_what_if_analysis_tab_interactions_and_results():
    """
    Test interactions on the 'What-If Analysis' tab (Tab 4),
    including defining custom scenarios and running the analysis.
    """
    at = get_app_test_instance()
    # Ensure session state is prepared (from Tab 1, 2, and 3 calculations for a comprehensive flow)
    at.tabs[1].selectbox[0].set_value("Master's in Finance").run()
    at.tabs[1].number_input[0].set_value(7).run()
    at.tabs[1].multiselect[0].set_value(['AI Quant Analyst', 'Financial Data Scientist']).run()
    at.tabs[1].button[0].click().run() # Calculates VR/HR
    at.run() # Rerun to ensure top_role is calculated and available for optimization
             # Also triggers Tab 2 content, ensuring air_df is populated

    # Run optimization to have a baseline scenario available for comparison in What-If
    at.tabs[3].number_input[0].set_value(100).run()
    at.tabs[3].number_input[1].set_value(1000).run()
    at.tabs[3].button[0].click().run()
    at.run() # Rerun after optimization to update session state

    # Navigate to Tab 4: What-If Analysis (index 4 for the tabs list)
    assert at.tabs[4].header[0].value == "4. 'What-If' Scenario Analysis"

    # 4.1. Define Custom Scenarios
    # Select a different target role for the custom scenario
    at.tabs[4].selectbox[0].set_value("Financial Data Scientist").run()

    # Select some learning pathways for this scenario
    # Get actual pathway names from session_state['learning_pathways_df'] for robustness
    pathway_names = at.session_state['learning_pathways_df']['pathway_name'].tolist()
    selected_pathways_for_scenario = []
    # Try to pick pathways that are likely to exist
    if 'Python for Data Science' in pathway_names:
        selected_pathways_for_scenario.append('Python for Data Science')
    if 'Generative AI Tools for Finance' in pathway_names:
        selected_pathways_for_scenario.append('Generative AI Tools for Finance')
    if 'AI Ethics Course' in pathway_names:
        selected_pathways_for_scenario.append('AI Ethics Course')

    # Fallback if specific pathways aren't guaranteed in simulated data, take first few
    if not selected_pathways_for_scenario and len(pathway_names) >= 2:
        selected_pathways_for_scenario = [pathway_names[0], pathway_names[1]]
    elif not selected_pathways_for_scenario and len(pathway_names) == 1:
        selected_pathways_for_scenario = [pathway_names[0]]

    if selected_pathways_for_scenario:
        at.tabs[4].multiselect[0].set_value(selected_pathways_for_scenario).run()
    else:
        pytest.skip("Not enough learning pathways available to select for what-if scenario.")


    # Click "Run Custom Scenario Analysis"
    at.tabs[4].button[0].click().run() # This triggers a rerun and updates session state

    # Assert success message is displayed on Tab 4
    assert at.tabs[4].success[0].value == "Custom scenario analysis complete!"

    # Assert scenario_results_df and roi_df are populated in session state
    assert 'scenario_results_df' in at.session_state
    assert not at.session_state['scenario_results_df'].empty
    assert 'roi_df' in at.session_state
    assert not at.session_state['roi_df'].empty

    # Assert dataframes and plots are displayed on Tab 4
    assert not at.tabs[4].dataframe[0].empty # Scenario analysis results dataframe
    assert at.tabs[4].pyplot[0] is not None # Scenario bar chart
    assert not at.tabs[4].dataframe[1].empty # ROI results dataframe
    assert at.tabs[4].pyplot[1] is not None # ROI bar chart


def test_summary_report_tab_content():
    """
    Test that the 'Summary Report' tab (Tab 5) correctly consolidates and displays
    information from all previous steps of the application.
    """
    at = get_app_test_instance()
    # Simulate a full user flow to ensure all session state variables are populated
    # Tab 1: Profile & Goals interactions & calculations
    at.tabs[1].selectbox[0].set_value("Master's in Finance").run()
    at.tabs[1].number_input[0].set_value(7).run()
    at.tabs[1].multiselect[0].set_value(['AI Quant Analyst', 'Financial Data Scientist']).run()
    at.tabs[1].button[0].click().run()
    at.run() # Rerun to propagate state after button click and ensure Tab 2 is ready

    # Tab 3: Learning Optimization interactions & calculations
    at.tabs[3].number_input[0].set_value(100).run()
    at.tabs[3].number_input[1].set_value(1000).run()
    at.tabs[3].button[0].click().run()
    at.run() # Rerun after optimization

    # Tab 4: What-If Analysis interactions & calculations
    pathway_names = at.session_state['learning_pathways_df']['pathway_name'].tolist()
    selected_pathways_for_scenario = []
    if 'Python for Data Science' in pathway_names:
        selected_pathways_for_scenario.append('Python for Data Science')
    if 'Generative AI Tools for Finance' in pathway_names:
        selected_pathways_for_scenario.append('Generative AI Tools for Finance')

    if selected_pathways_for_scenario:
        at.tabs[4].selectbox[0].set_value("Financial Data Scientist").run()
        at.tabs[4].multiselect[0].set_value(selected_pathways_for_scenario).run()
        at.tabs[4].button[0].click().run()
        at.run() # Rerun after scenario analysis
    else:
        # If no pathways were available, scenario results might be empty, skip relevant checks
        pass


    # Assert on Tab 5's content (index 5 for the tabs list)
    assert at.tabs[5].header[0].value == "5. Personalized AI Career Strategy Report for Alice"

    # Assert Current AI-Readiness Profile section
    assert "Idiosyncratic Readiness (VR):" in at.tabs[5].markdown[0].value
    assert "AI-Fluency:" in at.tabs[5].markdown[1].value
    assert "Systematic Opportunity (HR) by Role:" in at.tabs[5].markdown[4].value
    assert at.session_state['alice_vr_score'] is not None

    # Assert Top AI-Enabled Career Path Recommendation section
    assert "Top AI-Enabled Career Path Recommendation" in at.tabs[5].subheader[1].value
    assert "Recommended Role:" in at.tabs[5].markdown[7].value
    assert "Initial AI-Readiness Score (AI-R):" in at.tabs[5].markdown[8].value
    if at.session_state['projected_air'] is not None:
        assert "Projected AI-Readiness Score (AI-R) after Optimal Learning:" in at.tabs[5].markdown[9].value
        assert "Estimated AI-R Improvement:" in at.tabs[5].markdown[10].value

    # Assert Detailed Skill Gaps section
    assert "Detailed Skill Gaps for" in at.tabs[5].subheader[2].value
    assert not at.tabs[5].dataframe[0].empty # Skill gaps dataframe is displayed

    # Assert Recommended Optimal Learning Pathway section
    assert "Recommended Optimal Learning Pathway" in at.tabs[5].subheader[3].value
    if at.session_state['recommended_paths']:
        assert "Total Estimated Time Investment:" in at.tabs[5].markdown[13].value
        assert "Total Estimated Cost Investment:" in at.tabs[5].markdown[14].value
    else:
        assert "No optimal learning pathways identified" in at.tabs[5].markdown[13].value

    # Assert 'What-If' Scenario Analysis Summary section
    assert "'What-If' Scenario Analysis Summary" in at.tabs[5].subheader[4].value
    if not at.session_state['scenario_results_df'].empty:
        assert not at.tabs[5].dataframe[1].empty # Scenario results dataframe is displayed
        assert "Insight: The 'Optimized for AI Quant Analyst' pathway" in at.tabs[5].markdown[17].value
    else:
        assert "*(Run 'What-If Analysis' to see comparative scenarios)*" in at.tabs[5].markdown[17].value

