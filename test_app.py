
from streamlit.testing.v1 import AppTest
import pandas as pd
import numpy as np
import os

# To ensure 'source.py' is found during testing,
# we might need to create a dummy source.py or ensure the actual one is in the path.
# For the purpose of this test generation, we assume 'source.py' exists and
# provides the necessary dataframes and functions as outlined in the app code.

# Create dummy source.py if it doesn't exist for testing environment setup
# In a real test setup, you'd ensure source.py is accessible or mocked.
dummy_source_content = """
import pandas as pd
import numpy as np

# Dummy dataframes for testing
df_employees = pd.DataFrame({
    'employee_id': ['EMP001', 'EMP002'],
    'job_role': ['Data Scientist', 'Business Analyst'],
    'department': ['AI Research', 'Analytics'],
    'current_ai_r_score': [75.0, 60.0],
    'vr_score': [70.0, 55.0],
    'hr_r_score': [80.0, 65.0],
    'ai_fluency_score': [75.0, 50.0],
    'domain_expertise_score': [80.0, 60.0],
    'adaptive_capacity_score': [65.0, 55.0],
})

df_occupations = pd.DataFrame({
    'occupation_id': ['DS001', 'BA001'],
    'occupation_name': ['Data Scientist', 'Business Analyst'],
    'ai_enhancement_potential': [0.8, 0.6],
    'job_growth_normalized': [90, 70],
    'wage_premium': [0.2, 0.1],
    'entry_accessibility': [0.7, 0.8],
    'remote_work_factor': [0.9, 0.7],
})

df_pathways = pd.DataFrame({
    'pathway_id': ['P001', 'P002', 'P003'],
    'pathway_name': ['Advanced ML', 'Data Visualization', 'Cloud AI Basics'],
    'impact_ai_fluency': [10, 3, 7],
    'impact_domain_expertise': [5, 2, 4],
    'impact_adaptive_capacity': [3, 5, 6],
    'time_hours': [100, 40, 60],
    'cost_usd': [1000, 300, 500],
})

PARAMS = {
    'alpha': 0.6,
    'beta': 0.15,
    'w_hr1': 0.30, 'w_hr2': 0.30, 'w_hr3': 0.25, 'w_hr4': 0.15,
    'w_vr1': 0.45, 'w_vr2': 0.35, 'w_vr3': 0.20,
    'theta1': 0.30, 'theta2': 0.35, 'theta3': 0.20, 'theta4': 0.15,
    'gamma_exp': 0.15,
    'w_port': 0.4, 'w_recog': 0.3, 'w_cred': 0.3,
    'lambda_growth': 0.3, 'gamma_regional': 0.2,
}

def calculate_vr_score(employee_data, params):
    # Simplified calculation for testing
    ai_fluency = employee_data['ai_fluency_score']
    domain_expertise = employee_data['domain_expertise_score']
    adaptive_capacity = employee_data['adaptive_capacity_score']
    return (params['w_vr1'] * ai_fluency +
            params['w_vr2'] * domain_expertise +
            params['w_vr3'] * adaptive_capacity)

def calculate_hr_score(employee_data, occupations_df, params):
    # Simplified calculation for testing
    job_role = employee_data['job_role']
    occupation_data = occupations_df[occupations_df['occupation_name'] == job_role].iloc[0]
    base_hr = (params['w_hr1'] * occupation_data['ai_enhancement_potential'] * 100 +
               params['w_hr2'] * occupation_data['job_growth_normalized'] +
               params['w_hr3'] * occupation_data['wage_premium'] * 100 +
               params['w_hr4'] * occupation_data['entry_accessibility'] * 100) / (params['w_hr1'] + params['w_hr2'] + params['w_hr3'] + params['w_hr4'])
    # Assume multipliers are 1 for simplicity in this dummy
    return base_hr

def calculate_synergy_score(vr_score, hr_score, employee_data):
    # Simplified calculation for testing
    # Assume a static alignment factor for dummy data
    alignment_factor = 0.9 if employee_data['job_role'].iloc[0] == 'Data Scientist' else 0.7
    return (vr_score * hr_score / 100) * alignment_factor

def calculate_ai_r_score(vr_score, hr_score, synergy_score, params):
    return (params['alpha'] * vr_score +
            (1 - params['alpha']) * hr_score +
            params['beta'] * synergy_score)

def generate_ai_r_report_summary(df_employees):
    return df_employees.groupby('job_role')['current_ai_r_score'].mean().reset_index()

def simulate_pathway_impact(employee_id, pathway_id, completion_rate, mastery_score, df_employees, df_occupations, df_pathways, PARAMS):
    employee = df_employees[df_employees['employee_id'] == employee_id].iloc[0]
    pathway = df_pathways[df_pathways['pathway_id'] == pathway_id].iloc[0]

    # Simulate updated VR components
    updated_ai_fluency = employee['ai_fluency_score'] + pathway['impact_ai_fluency'] * completion_rate * mastery_score
    updated_domain_expertise = employee['domain_expertise_score'] + pathway['impact_domain_expertise'] * completion_rate * mastery_score
    updated_adaptive_capacity = employee['adaptive_capacity_score'] + pathway['impact_adaptive_capacity'] * completion_rate * mastery_score

    # Create a dummy employee df for VR calculation
    updated_employee_data = employee.copy()
    updated_employee_data['ai_fluency_score'] = updated_ai_fluency
    updated_employee_data['domain_expertise_score'] = updated_domain_expertise
    updated_employee_data['adaptive_capacity_score'] = updated_adaptive_capacity

    # Recalculate VR and then AI-R
    updated_vr_score = calculate_vr_score(updated_employee_data, PARAMS)
    hr_score = calculate_hr_score(employee, df_occupations, PARAMS) # HR is static here
    synergy_score = calculate_synergy_score(updated_vr_score, hr_score, employee.to_frame().T) # Pass as DataFrame
    projected_ai_r = calculate_ai_r_score(updated_vr_score, hr_score, synergy_score, PARAMS)
    
    delta_ai_r = projected_ai_r - employee['current_ai_r_score']
    return projected_ai_r, delta_ai_r, pathway['pathway_name']

def optimize_pathway_sequence(employee_id, current_ai_r, df_pathways, T_max_hours, cost_weight_lambda, df_employees, df_occupations, PARAMS):
    employee_data = df_employees[df_employees['employee_id'] == employee_id].iloc[0]
    
    recommended_sequence = []
    total_cost = 0
    total_time_hours = 0
    
    # Simple greedy approach for dummy - pick the best AI-R improvement per unit time adjusted for cost
    available_pathways = df_pathways.copy()
    
    projected_final_ai_r = current_ai_r
    ai_r_improvement = 0

    # Simulate taking one pathway for simplicity
    if not available_pathways.empty:
        # For a greedy choice, we'd need to simulate all and pick the best.
        # Here, let's just pick the first pathway if it fits time and cost.
        best_pathway = None
        best_score = -np.inf

        for idx, pathway in available_pathways.iterrows():
            if pathway['time_hours'] <= T_max_hours:
                # Calculate potential impact of this single pathway
                temp_proj_ai_r, temp_delta_ai_r, _ = simulate_pathway_impact(
                    employee_id, pathway['pathway_id'], 1.0, 1.0, # Assume full completion/mastery for greedy
                    df_employees, df_occupations, df_pathways, PARAMS
                )
                score = temp_delta_ai_r - cost_weight_lambda * pathway['cost_usd']
                if score > best_score:
                    best_score = score
                    best_pathway = pathway

        if best_pathway is not None:
            recommended_sequence.append(best_pathway['pathway_name'])
            total_cost += best_pathway['cost_usd']
            total_time_hours += best_pathway['time_hours']
            
            # Recalculate with the chosen pathway
            projected_final_ai_r, delta_ai_r, _ = simulate_pathway_impact(
                employee_id, best_pathway['pathway_id'], 1.0, 1.0,
                df_employees, df_occupations, df_pathways, PARAMS
            )
            ai_r_improvement = delta_ai_r

    return {
        "recommended_sequence": recommended_sequence,
        "projected_final_ai_r": projected_final_ai_r,
        "total_cost": total_cost,
        "total_time_hours": total_time_hours,
        "ai_r_improvement": ai_r_improvement
    }

import matplotlib.pyplot as plt
def plot_current_vs_projected_ai_r(current_ai_r, projected_ai_r_list, pathway_names, fig=None, ax=None):
    if fig is None and ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
    
    labels = ['Current AI-R'] + pathway_names
    values = [current_ai_r] + projected_ai_r_list
    
    bars = ax.bar(labels, values, color=['skyblue'] + ['lightcoral'] * len(projected_ai_r_list))
    ax.set_ylabel('AI-R Score')
    ax.set_title('Current vs. Projected AI-R Score')
    ax.set_ylim(0, 100)
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')
    
    # Ensure the figure is properly returned/displayed if created internally
    if fig is not None:
        return fig, ax
"""

# Write the dummy_source_content to source.py in the current directory
with open("source.py", "w") as f:
    f.write(dummy_source_content)

# Now proceed with the actual tests
# Note: Streamlit app code is assumed to be in 'app.py'

def test_initial_app_load_and_introduction():
    """
    Test if the app loads correctly and displays the introductory content.
    """
    at = AppTest.from_file("app.py").run()
    assert at.title[0].value == "QuLab: AI Readiness score"
    assert "Workforce AI-Readiness & Upskilling Strategizer" in at.markdown[0].value
    assert "Story Flow" in at.markdown[0].value
    assert at.session_state["current_page"] == "Dashboard"

def test_dashboard_page():
    """
    Test the Dashboard page content and interactions.
    """
    at = AppTest.from_file("app.py").run()
    at.button[0].click().run() # Click Dashboard button (already default but for explicit test)
    assert at.session_state["current_page"] == "Dashboard"
    assert at.title[0].value == "Workforce AI-Readiness Dashboard"
    
    # Check default grouping
    assert at.session_state["report_group_by"] == "job_role"
    
    # Change grouping to department
    at.selectbox[0].set_value("department").run()
    assert at.session_state["report_group_by"] == "department"
    
    # Verify dataframe and heatmap are present
    assert len(at.dataframe) > 0
    assert len(at.pyplot) > 0

def test_what_if_scenario_page():
    """
    Test navigation to What-If Scenario page, interactions, and results display.
    """
    at = AppTest.from_file("app.py").run()
    
    # Navigate to What-If Scenario page
    at.button[1].click().run() # Click "What-If Scenario Engine" button in sidebar
    assert at.session_state["current_page"] == "What-If Scenario"
    assert at.title[0].value == "What-If Scenario Engine"
    
    # Check initial selections and sliders
    assert at.session_state["selected_employee_id_whatif"] == "EMP001"
    assert at.session_state["selected_pathway_id_whatif"] == "P001"
    assert at.session_state["completion_rate_whatif"] == 0.9
    assert at.session_state["mastery_score_whatif"] == 0.85

    # Change employee and pathway
    at.selectbox[0].set_value("EMP002").run() # Employee selectbox
    assert at.session_state["selected_employee_id_whatif"] == "EMP002"
    at.selectbox[1].set_value("Data Visualization").run() # Pathway selectbox (by name)
    assert at.session_state["selected_pathway_id_whatif"] == "P002" # P002 is for Data Visualization

    # Change completion rate and mastery score
    at.slider[0].set_value(0.7).run() # Completion Rate
    assert at.session_state["completion_rate_whatif"] == 0.7
    at.slider[1].set_value(0.95).run() # Mastery Score
    assert at.session_state["mastery_score_whatif"] == 0.95

    # Simulate pathway impact
    at.button[0].click().run() # Click "Simulate Pathway Impact" button
    
    # Verify results are displayed
    assert at.session_state["whatif_results"] is not None
    assert at.session_state["whatif_results"]["selected_employee_id"] == "EMP002"
    assert at.markdown[5].value.startswith("Employee ID: **EMP002**") # Check for results markdown
    assert len(at.pyplot) > 0 # Check for plot

def test_pathway_optimization_page():
    """
    Test navigation to Pathway Optimization page, interactions, and results display.
    """
    at = AppTest.from_file("app.py").run()
    
    # Navigate to Pathway Optimization page
    at.button[2].click().run() # Click "Pathway Optimization" button in sidebar
    assert at.session_state["current_page"] == "Pathway Optimization"
    assert at.title[0].value == "Multi-Step Pathway Optimization"

    # Check initial selections and sliders
    assert at.session_state["selected_employee_id_opt"] == "EMP001"
    assert at.session_state["T_max_hours_opt"] == 300
    assert at.session_state["cost_weight_lambda_opt"] == 0.005

    # Change employee
    at.selectbox[0].set_value("EMP002").run() # Employee selectbox
    assert at.session_state["selected_employee_id_opt"] == "EMP002"

    # Change max time and cost weight
    at.slider[0].set_value(400).run() # Maximum Time (hours)
    assert at.session_state["T_max_hours_opt"] == 400
    at.slider[1].set_value(0.008).run() # Cost Weight
    assert at.session_state["cost_weight_lambda_opt"] == 0.008

    # Optimize Pathways
    at.button[0].click().run() # Click "Optimize Pathways" button
    
    # Verify results are displayed
    assert at.session_state["optimization_results"] is not None
    assert at.session_state["optimization_results"]["selected_employee_id"] == "EMP002"
    assert at.markdown[5].value.startswith("Employee ID: **EMP002**") # Check for results markdown
    assert len(at.pyplot) > 0 # Check for plot

def test_strategic_recommendations_page():
    """
    Test navigation to Strategic Recommendations page and content.
    """
    at = AppTest.from_file("app.py").run()
    
    # Navigate to Strategic Recommendations page
    at.button[3].click().run() # Click "Strategic Recommendations" button in sidebar
    assert at.session_state["current_page"] == "Strategic Recommendations"
    assert at.title[0].value == "Strategic Recommendations & Conclusion"
    
    # Check for presence of key markdown elements and dataframes
    assert "Target Low AI-R Cohorts" in at.markdown[3].value
    assert len(at.dataframe) > 0 # For low AI-R cohorts
    assert "Address Critical Skills Gaps" in at.markdown[5].value
    assert "Implement Optimized Multi-Step Learning Pathways" in at.markdown[6].value
    
    # Test conditional rendering for optimization results if available
    # Run an optimization first to populate session_state
    at_opt = AppTest.from_file("app.py").run()
    at_opt.button[2].click().run() # Navigate to Pathway Optimization
    at_opt.button[0].click().run() # Click "Optimize Pathways"
    
    # Now load the app again and navigate to recommendations to see the effect
    at_rec = AppTest.from_file("app.py")
    at_rec.session_state["optimization_results"] = at_opt.session_state["optimization_results"]
    at_rec.run()
    at_rec.button[3].click().run() # Navigate to Strategic Recommendations
    
    assert f"For employee **{at_rec.session_state['optimization_results']['selected_employee_id']}**" in at_rec.markdown[7].value
    assert "Recommended Pathway Sequence:" in at_rec.markdown[8].value


def test_framework_details_pages():
    """
    Test navigation and basic content check for all framework details pages.
    """
    pages = {
        "AI-R Overview": ("nav_air_overview", "The AI-Readiness Framework: Core Concepts", "AI-Readiness Score (AI-R) is a novel parametric framework"),
        "Systematic Opportunity ($H^R$)": ("nav_hrr", "Systematic Opportunity ($H^R$) Component", "Systematic Opportunity ($H^R$) represents the macro-level demand"),
        "Idiosyncratic Readiness ($V^R$)": ("nav_vr", "Idiosyncratic Readiness ($V^R$) Component", "Idiosyncratic Readiness ($V^R$) measures an individual's specific preparation"),
        "Synergy Function": ("nav_synergy", "Synergy Function", "The Synergy function captures the multiplicative benefits")
    }

    for page_name, (button_key, expected_title, expected_markdown_snippet) in pages.items():
        at = AppTest.from_file("app.py").run()
        at.button[button_key].click().run() # Click the respective sidebar button
        assert at.session_state["current_page"] == page_name
        assert at.title[0].value == expected_title
        assert expected_markdown_snippet in at.markdown[1].value # Check for key introductory text
