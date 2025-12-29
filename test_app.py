
from streamlit.testing.v1 import AppTest
import pandas as pd
import numpy as np
import os

# Helper function to create dummy data files for testing
def create_dummy_csv_files():
    # Only create if they don't exist to avoid overwriting during actual app run
    if not os.path.exists('idiosyncratic_data.csv'):
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}).to_csv('idiosyncratic_data.csv', index=False)
    if not os.path.exists('systematic_opportunity_data.csv'):
        pd.DataFrame({
            'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
            'projected_jobs_10yr': [1000, 800, 700, 900],
            'current_jobs': [500, 400, 350, 450],
            'ai_skilled_wage': [150000, 140000, 130000, 120000],
            'median_wage': [100000, 95000, 90000, 85000],
            'education_years_required': [18, 18, 16, 16],
            'experience_years_required': [5, 4, 3, 3],
            'ai_enhancement_potential': [0.9, 0.85, 0.8, 0.75],
            'remote_work_factor': [0.7, 0.6, 0.5, 0.65]
        }).to_csv('systematic_opportunity_data.csv', index=False)
    if not os.path.exists('job_postings_data.csv'):
        pd.DataFrame({
            'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
            'job_postings_t': [500, 450, 400, 380],
            'job_postings_t_minus_1': [400, 350, 300, 280]
        }).to_csv('job_postings_data.csv', index=False)
    if not os.path.exists('regional_demand_data.csv'):
        pd.DataFrame({
            'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
            'local_demand': [0.8, 0.7, 0.6, 0.75],
            'national_avg_demand': [0.7, 0.6, 0.5, 0.7]
        }).to_csv('regional_demand_data.csv', index=False)
    if not os.path.exists('skill_requirements.csv'):
        pd.DataFrame({
            'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
            'Python': [9, 8, 7, 8],
            'SQL': [7, 7, 8, 7],
            'ML_basics': [8, 9, 6, 7],
            'Risk_Analysis': [9, 6, 10, 7],
            'Financial_Modeling': [8, 5, 9, 8],
            'Data_Viz': [7, 8, 7, 9],
            'Quant_Models': [8, 9, 7, 6],
            'AI_Ethics': [7, 7, 8, 6],
            'GenAI_Tools': [6, 8, 5, 7],
            'Cloud_Platforms': [6, 8, 5, 7]
        }).to_csv('skill_requirements.csv', index=False)
    if not os.path.exists('learning_pathways.csv'):
        pd.DataFrame({
            'pathway_id': [1, 2, 3, 4, 5],
            'pathway_name': ['Advanced Python for Finance', 'Machine Learning Foundations', 'Cloud for AI', 'AI Ethics & Governance', 'GenAI in Finance'],
            'type': ['Course', 'Course', 'Certification', 'Workshop', 'Course'],
            'estimated_time_hours': [40, 60, 80, 20, 50],
            'estimated_cost_usd': [500, 1000, 1500, 300, 800],
            'skills_gained': ['Python,Data_Viz', 'ML_basics,Quant_Models', 'Cloud_Platforms', 'AI_Ethics', 'GenAI_Tools'],
            'vr_component_boosts': ['ai_fluency:0.1,domain_expertise:0.05', 'ai_fluency:0.15,domain_expertise:0.1', 'adaptive_capacity:0.05', 'ai_fluency:0.05', 'ai_fluency:0.1,domain_expertise:0.05'],
            'prerequisites': ['', '1', '2', '', '2']
        }).to_csv('learning_pathways.csv', index=False)

# Call this once before running tests, or at the start of each test if files might be deleted.
create_dummy_csv_files()

# Define dummy constants that would usually come from source.py
ALPHA = 0.5
BETA = 0.2
VR_W1_AI_FLUENCY = 0.33
VR_W2_DOMAIN_EXPERTISE = 0.33
VR_W3_ADAPTIVE_CAPACITY = 0.33
AI_FLUENCY_THETA_WEIGHTS = {'prompting': 0.2, 'ai_tools': 0.2, 'understanding': 0.2, 'data_literacy': 0.2, 'ai_augmented_productivity': 0.1, 'critical_ai_judgment': 0.05, 'appropriate_trust_decisions': 0.05}
GAMMA_EXPERIENCE_DECAY = 0.01
HBASE_WEIGHTS = {'ai_enhancement_potential': 0.4, 'growth_normalized': 0.3, 'wage_premium': 0.2, 'entry_accessibility': 0.1}
LAMBDA_GROWTH_MULTIPLIER = 1.05
GAMMA_REMOTE_WORK = 0.1
VR_COMPONENT_WEIGHTS = {'ai_fluency': 0.33, 'domain_expertise': 0.33, 'adaptive_capacity': 0.33}
MAX_LEARNING_TIME_HOURS = 100
MAX_LEARNING_BUDGET_USD = 1000
LAMBDA_COST_WEIGHT = 0.1

# Mock functions from source.py needed for AppTest to run.
# These implementations are simplified to allow the app's control flow to be tested,
# assuming the correctness of the actual calculations in source.py is verified via unit tests.
def calculate_ai_fluency(subfactors, weights):
    return sum(subfactors[k] * weights.get(k, 0) for k in subfactors if k in weights) * 100 / sum(weights.values()) if weights else 0

def calculate_domain_expertise(education_level, experience_years, subfactors, decay):
    edu_score = {'Master\'s in Finance': 90, 'PhD in target field': 100, 'Master\'s in target field': 90, 'Bachelor\'s in target field': 70, 'Associate\'s/Certificate': 50, 'HS + significant coursework': 30}.get(education_level, 0)
    exp_score = min(experience_years * 5, 100)
    subfactor_score = sum(subfactors.values()) / len(subfactors) * 100 if subfactors else 0
    return (edu_score * 0.4 + exp_score * 0.3 + subfactor_score * 0.3)

def calculate_adaptive_capacity(subfactors):
    return sum(subfactors.values()) / len(subfactors) * 100 if subfactors else 0

def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, weights):
    return (ai_fluency * weights['ai_fluency'] +
            domain_expertise * weights['domain_expertise'] +
            adaptive_capacity * weights['adaptive_capacity'])

def normalize_growth(growth_rate):
    return max(0, min(100, (growth_rate + 0.05) * 1000))

def calculate_wage_premium(ai_skilled_wage, median_wage):
    return (ai_skilled_wage - median_wage) / median_wage * 100 if median_wage > 0 else 0

def calculate_entry_accessibility(education_years_required, experience_years_required):
    return 100 - (education_years_required * 5 + experience_years_required * 3)

def calculate_hbase(ai_enhancement_potential, growth_normalized, wage_premium, entry_accessibility, weights):
    return (ai_enhancement_potential * weights['ai_enhancement_potential'] * 100 +
            growth_normalized * weights['growth_normalized'] +
            wage_premium * weights['wage_premium'] +
            entry_accessibility * weights['entry_accessibility'])

def calculate_mgrowth(jp_t, jp_t_minus_1, multiplier):
    return (jp_t / jp_t_minus_1) * multiplier * 100 if jp_t_minus_1 > 0 else 0

def calculate_mregional(local_demand, national_avg_demand, remote_work_factor, remote_gamma):
    return (local_demand / national_avg_demand) * 100 * (1 + remote_work_factor * remote_gamma) if national_avg_demand > 0 else 0

def calculate_hr(hbase, mgrowth, mregional):
    return (hbase * 0.4 + mgrowth * 0.3 + mregional * 0.3)

def calculate_skills_match_score(current_skills, required_skills_for_role, max_possible_match_for_role):
    skill_gaps = {}
    total_current = 0
    total_required = 0
    matched_score = 0
    # Ensure required_skills_for_role is a Series/dict and handle 'role' column if present
    skills_data = required_skills_for_role.drop('role', errors='ignore') if isinstance(required_skills_for_role, pd.Series) else required_skills_for_role
    for skill, required_level in skills_data.items():
        current_level = current_skills.get(skill, 0)
        skill_gaps[skill] = {'current': current_level, 'required': required_level, 'gap': max(0, required_level - current_level)}
        total_current += current_level
        total_required += required_level
        matched_score += min(current_level, required_level)

    required_skills_dict = skills_data.to_dict() if isinstance(skills_data, pd.Series) else skills_data
    if max_possible_match_for_role == 0:
        return 0, skill_gaps, required_skills_dict, total_current, total_required
    return matched_score / max_possible_match_for_role, skill_gaps, required_skills_dict, total_current, total_required

def calculate_timing_factor(experience_years):
    return min(1.0, experience_years / 10.0)

def calculate_alignment(skills_match, timing_factor):
    return (skills_match * 0.7 + timing_factor * 0.3)

def calculate_synergy(vr_score, hr_score, alignment_score):
    return (vr_score * hr_score / 100) * alignment_score

def calculate_air(vr_score, hr_score, synergy_score, alpha, beta):
    return alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_score

def parse_skill_string(skills_str):
    return [s.strip() for s in skills_str.split(',')] if skills_str else []

def parse_vr_boost_string(boost_str):
    boosts = {}
    if boost_str:
        for item in boost_str.split(','):
            key, value = item.split(':')
            boosts[key.strip()] = float(value)
    return boosts

def optimize_learning_pathways(
    initial_air_optimal_role,
    initial_vr_score,
    initial_vr_subscores_normalized,
    current_hr_for_top_role,
    learning_pathways_df,
    max_learning_time_hours,
    max_learning_budget_usd,
    alpha, beta, lambda_cost_weight,
    experience_years,
    current_skills
):
    recommended_paths = []
    total_time = 0
    total_cost = 0
    projected_air = initial_air_optimal_role
    final_vr = initial_vr_score
    final_vr_subscores_normalized = initial_vr_subscores_normalized.copy()
    final_skills_after_paths = current_skills.copy()

    for _, path_row in learning_pathways_df.iterrows():
        path = path_row.to_dict()
        if total_time + path['estimated_time_hours'] <= max_learning_time_hours and \
           total_cost + path['estimated_cost_usd'] <= max_learning_budget_usd:
            
            recommended_paths.append(path)
            total_time += path['estimated_time_hours']
            total_cost += path['estimated_cost_usd']

            for skill_gained in parse_skill_string(path['skills_gained']):
                final_skills_after_paths[skill_gained] = min(10, final_skills_after_paths.get(skill_gained, 0) + 1)

            vr_boosts = parse_vr_boost_string(path['vr_component_boosts'])
            for component, boost_value in vr_boosts.items():
                final_vr_subscores_normalized[component] = min(100, final_vr_subscores_normalized.get(component, 0) + boost_value * 100)
            
            # Recalculate VR based on boosted subscores (simplified)
            final_vr = calculate_vr(
                final_vr_subscores_normalized.get('ai_fluency', 0),
                final_vr_subscores_normalized.get('domain_expertise', 0),
                final_vr_subscores_normalized.get('adaptive_capacity', 0),
                VR_COMPONENT_WEIGHTS
            )
            projected_air += 5 # Arbitrary boost for demonstration

    return recommended_paths, total_time, total_cost, projected_air, final_vr, final_vr_subscores_normalized, final_skills_after_paths

def run_what_if_scenario(
    initial_vr_score, 
    initial_vr_subscores_normalized,
    initial_current_skills,
    scenario_target_role, hr_scores_all, 
    skill_requirements_df, 
    custom_scenario_pathways,
    experience_years, 
    alpha, beta
):
    current_vr = initial_vr_score
    current_vr_subscores_normalized = initial_vr_subscores_normalized.copy()
    current_skills = initial_current_skills.copy()

    total_time_invested = 0
    total_cost_invested = 0

    for path in custom_scenario_pathways:
        total_time_invested += path['estimated_time_hours']
        total_cost_invested += path['estimated_cost_usd']

        for skill_gained in parse_skill_string(path['skills_gained']):
            current_skills[skill_gained] = min(10, current_skills.get(skill_gained, 0) + 1)

        vr_boosts = parse_vr_boost_string(path['vr_component_boosts'])
        for component, boost_value in vr_boosts.items():
            current_vr_subscores_normalized[component] = min(100, current_vr_subscores_normalized.get(component, 0) + boost_value * 100)

    current_vr = calculate_vr(
        current_vr_subscores_normalized.get('ai_fluency', 0),
        current_vr_subscores_normalized.get('domain_expertise', 0),
        current_vr_subscores_normalized.get('adaptive_capacity', 0),
        VR_COMPONENT_WEIGHTS
    )

    current_hr_score = hr_scores_all.get(scenario_target_role, 0)

    required_skills_for_role_df = skill_requirements_df[skill_requirements_df['role'] == scenario_target_role]
    if not required_skills_for_role_df.empty:
        required_skills_for_role = required_skills_for_role_df.iloc[0]
        max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum()
        
        skills_match, _, _, _, _ = calculate_skills_match_score(
            current_skills,
            required_skills_for_role,
            max_possible_match_for_role
        )
    else:
        skills_match = 0 # No skill requirements found for the role

    timing_factor = calculate_timing_factor(experience_years)
    alignment_score = calculate_alignment(skills_match, timing_factor)
    synergy_score = calculate_synergy(current_vr, current_hr_score, alignment_score)
    projected_air = calculate_air(current_vr, current_hr_score, synergy_score, alpha, beta)

    return projected_air, total_time_invested, total_cost_invested, current_vr, current_hr_score, synergy_score

# Ensure the mock create_simulated_data is defined
def create_simulated_data():
    create_dummy_csv_files()


def test_1_initial_app_load_and_introduction_tab():
    at = AppTest.from_file("app.py").run()
    assert at.title[0].value == "QuLab: AI Readiness score"
    assert "Welcome to the AI-Readiness Career Navigator!" in at.markdown[0].value
    assert "Your Persona: Alice, a Senior Quantitative Analyst" in at.subheader[0].value
    assert "The AI-Readiness Score (AI-R) Framework" in at.subheader[1].value
    assert at.tabs[0].label == "Introduction"
    assert at.tabs[1].label == "Profile & Goals"
    assert at.tabs[2].label == "Opportunity Evaluation"

def test_2_profile_and_goals_tab_interactions_and_calculation():
    at = AppTest.from_file("app.py").run()

    # Navigate to Tab 2
    at.tabs[1].click().run()

    # Verify initial state of widgets
    assert at.selectbox[0].value == "Master's in Finance"
    assert at.number_input[0].value == 7
    assert at.slider[0].value == 0.6 # 'prompting' ai_fluency_subfactors

    # Change some values
    at.selectbox[0].set_value("PhD in target field").run()
    at.number_input[0].set_value(10).run()
    at.slider[0].set_value(0.8).run() # 'prompting'
    at.multiselect[0].set_value(['AI Quant Analyst', 'Financial Data Scientist']).run()

    # Click the calculate button
    at.button[0].click().run()

    # Assert success message and session state updates
    assert at.success[0].value == "Initial Readiness & Opportunity calculated! Proceed to the next tab."
    assert at.session_state['alice_vr_score'] is not None
    assert 'AI Quant Analyst' in at.session_state['hr_scores']
    assert 'Financial Data Scientist' in at.session_state['hr_scores']

def test_3_opportunity_evaluation_tab_display():
    at = AppTest.from_file("app.py").run()

    # First, run tab 2 calculations to populate session state
    at.tabs[1].click().run()
    at.selectbox[0].set_value("PhD in target field").run()
    at.number_input[0].set_value(10).run()
    at.multiselect[0].set_value(['AI Quant Analyst', 'Financial Data Scientist']).run()
    at.button[0].click().run() # Calculate Initial Readiness & Opportunity

    # Navigate to Tab 3
    at.tabs[2].click().run()

    # Assert that scores and dataframes are displayed
    assert "Total VR Score" in at.subheader[0].value
    assert at.metric[0].value is not None # Check VR score
    assert "AI-Readiness Scores Across Target Roles" in at.pyplot[0]._key # Check for plot title
    assert not at.session_state['air_df'].empty
    assert at.dataframe[0].value is not None
    assert "Top AI-R Role:" in at.markdown[-3].value # Verify top role is identified
    assert "Skill Gaps for Recommended Role:" in at.subheader[4].value
    assert "Skill Gaps for" in at.pyplot[1]._key # Check for radar plot title

def test_4_learning_optimization_tab_interactions():
    at = AppTest.from_file("app.py").run()

    # First, run tab 2 & 3 calculations to populate session state and get top_role
    at.tabs[1].click().run()
    at.multiselect[0].set_value(['AI Quant Analyst']).run()
    at.button[0].click().run() # Calculate Initial Readiness & Opportunity
    at.tabs[2].click().run()
    # Trigger AI-R calculation within tab 3 to set 'top_role'
    # The app automatically runs this when tab 3 is accessed and VR/HR exist
    assert at.session_state['top_role'] is not None

    # Navigate to Tab 4
    at.tabs[3].click().run()

    # Verify initial optimization parameters
    assert at.number_input[1].value == MAX_LEARNING_TIME_HOURS # Max Learning Time (hours)
    assert at.number_input[2].value == MAX_LEARNING_BUDGET_USD # Max Learning Budget (USD)
    assert at.slider[at.slider.len - 1].value == LAMBDA_COST_WEIGHT # Cost Weight Lambda

    # Change parameters
    at.number_input[1].set_value(120).run()
    at.number_input[2].set_value(1500).run()

    # Click optimize button
    at.button[1].click().run() # Optimize Learning Pathway button

    # Assert success message and session state updates
    assert at.success[0].value == "Learning pathway optimized!"
    assert at.session_state['recommended_paths'] is not None
    assert at.session_state['projected_air'] is not None
    assert at.session_state['total_time_invested'] > 0
    assert at.session_state['total_cost_invested'] > 0
    assert "Recommended Optimal Learning Pathway" in at.subheader[2].value
    assert "Current vs. Projected AI-R for" in at.pyplot[0]._key # Check for optimization plot

def test_5_what_if_analysis_tab_interactions():
    at = AppTest.from_file("app.py").run()

    # First, run tab 2, 3, and 4 calculations to set up session state
    at.tabs[1].click().run()
    at.multiselect[0].set_value(['AI Quant Analyst', 'Financial Data Scientist']).run()
    at.button[0].click().run() # Calculate Initial Readiness & Opportunity
    at.tabs[2].click().run()
    assert at.session_state['top_role'] is not None
    at.tabs[3].click().run()
    at.button[1].click().run() # Optimize Learning Pathway

    # Navigate to Tab 5
    at.tabs[4].click().run()

    # Select a target role and some learning pathways
    at.selectbox[at.selectbox.len - 1].set_value("Financial Data Scientist").run() # scenario_role_select
    at.multiselect[at.multiselect.len - 1].set_value(['Machine Learning Foundations', 'Advanced Python for Finance']).run() # scenario_pathways_select

    # Click to run custom scenario
    at.button[at.button.len - 1].click().run() # Run Custom Scenario Analysis button

    # Assert success message and session state updates
    assert at.success[0].value == "Custom scenario analysis complete!"
    assert not at.session_state['scenario_results_df'].empty
    assert not at.session_state['roi_df'].empty
    assert "Scenario Analysis Results" in at.subheader[2].value
    assert "Comparative Projected AI-R for Different Career/Learning Scenarios" in at.pyplot[0]._key
    assert "Return on Learning Investment (ROI)" in at.subheader[3].value
    assert "Return on Learning Investment for Different Scenarios" in at.pyplot[1]._key

def test_6_summary_report_tab_display():
    at = AppTest.from_file("app.py").run()

    # First, run all previous calculations to populate session state fully
    at.tabs[1].click().run()
    at.multiselect[0].set_value(['AI Quant Analyst', 'Financial Data Scientist']).run()
    at.button[0].click().run() # Calculate Initial Readiness & Opportunity

    at.tabs[2].click().run() # This tab's logic will calculate AI-R, skill gaps, and top_role

    at.tabs[3].click().run()
    at.button[1].click().run() # Optimize Learning Pathway

    at.tabs[4].click().run()
    at.multiselect[at.multiselect.len - 1].set_value(['Machine Learning Foundations']).run()
    at.button[at.button.len - 1].click().run() # Run Custom Scenario Analysis

    # Navigate to Tab 6
    at.tabs[5].click().run()

    # Assert that key summary information is displayed
    assert "Personalized AI Career Strategy Report for Alice" in at.header[0].value
    assert "Current AI-Readiness Profile" in at.subheader[0].value
    assert at.session_state['alice_vr_score'] is not None
    assert at.session_state['hr_scores'] is not None
    assert "Top AI-Enabled Career Path Recommendation" in at.subheader[1].value
    assert at.session_state['top_role']['Role'] is not None
    assert at.session_state['projected_air'] is not None
    assert "Detailed Skill Gaps for" in at.subheader[2].value
    assert at.dataframe[0].value is not None # Skill gaps dataframe
    assert "Recommended Optimal Learning Pathway" in at.subheader[3].value
    assert at.session_state['recommended_paths'] is not None
    assert "What-If' Scenario Analysis Summary" in at.subheader[4].value
    assert not at.session_state['scenario_results_df'].empty

