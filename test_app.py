
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import types
from streamlit.testing.v1 import AppTest

# --- Mocking source.py content for testing purposes ---
# This creates a mock 'source' module and injects it into sys.modules.
# When 'app.py' runs and does 'from source import *', it will import
# these mocked objects instead of a real source.py file.

# Mock dataframes
mock_df_employees = pd.DataFrame({
    'employee_id': ['E001', 'E002', 'E003'],
    'job_role': ['Data Scientist', 'HR Specialist', 'Software Engineer'],
    'department': ['IT', 'HR', 'IT'],
    'current_ai_r_score': [75.0, 45.0, 80.0],
    'vr_score': [70.0, 40.0, 85.0],
    'hr_r_score': [80.0, 50.0, 75.0],
    'ai_fluency_score': [80.0, 30.0, 90.0],
    'domain_expertise_score': [70.0, 50.0, 80.0],
    'adaptive_capacity_score': [60.0, 40.0, 70.0],
    'education_level': ['Master\'s', 'Bachelor\'s', 'Master\'s'],
    'years_experience': [5, 10, 7],
    'ai_augmented_productivity_norm': [0.8, 0.5, 0.9],
    'errors_caught_norm': [0.9, 0.6, 0.85],
    'trust_decisions_norm': [0.8, 0.7, 0.9],
    'learning_rate': [0.7, 0.4, 0.8],
    'hours_invested': [100, 50, 120],
    'skill_a': [0.8, 0.5, 0.9], 'skill_b': [0.7, 0.6, 0.8], 'skill_c': [0.6, 0.7, 0.75],
    'skill_d': [0.9, 0.4, 0.85], 'skill_e': [0.7, 0.5, 0.9], 'skill_f': [0.8, 0.6, 0.7],
    'skill_g': [0.75, 0.55, 0.82], 'skill_h': [0.65, 0.7, 0.78], 'skill_i': [0.88, 0.52, 0.91],
    'skill_j': [0.72, 0.68, 0.83],
    'ai_enhancement_potential': [0.8, 0.6, 0.9],
    'job_growth_normalized': [0.7, 0.5, 0.8],
    'wage_premium_normalized': [0.75, 0.55, 0.85],
    'entry_accessibility_normalized': [0.6, 0.8, 0.7],
    'remote_work_factor': [0.9, 0.5, 0.8],
    'occupational_hr_r_score': [80.0, 50.0, 75.0]
})

mock_df_occupations = pd.DataFrame({
    'occupation_id': ['OCC001', 'OCC002', 'OCC003'],
    'job_role': ['Data Scientist', 'HR Specialist', 'Software Engineer'],
    'ai_enhancement_potential': [0.85, 0.6, 0.9],
    'growth_normalized': [0.9, 0.5, 0.8],
    'wage_premium_normalized': [0.8, 0.6, 0.85],
    'entry_accessibility_normalized': [0.7, 0.8, 0.75],
    'remote_work_factor': [0.8, 0.4, 0.7]
})

mock_df_pathways = pd.DataFrame({
    'pathway_id': ['P001', 'P002', 'P003'],
    'pathway_name': ['Advanced ML', 'HR Analytics', 'Cloud AI Basics'],
    'impact_ai_fluency': [10.0, 5.0, 7.0],
    'impact_domain_expertise': [5.0, 8.0, 3.0],
    'impact_adaptive_capacity': [3.0, 2.0, 5.0],
    'cost': [1000, 500, 750],
    'time_hours': [80, 40, 60]
})

mock_PARAMS = {
    'alpha': 0.6,
    'beta': 0.15,
    'vr_weights': {'ai_fluency': 0.45, 'domain_expertise': 0.35, 'adaptive_capacity': 0.20},
    'hr_base_weights': {'ai_enhancement': 0.30, 'growth': 0.30, 'wage': 0.25, 'access': 0.15},
    'ai_fluency_weights': {'technical_ai_skills': 0.30, 'ai_augmented_productivity': 0.35, 'critical_ai_judgment': 0.20, 'ai_learning_velocity': 0.15},
    'exp_gamma': 0.15,
    'specialization_weights': {'portfolio': 0.4, 'recognition': 0.3, 'credentials': 0.3},
    'growth_lambda': 0.3,
    'regional_gamma': 0.2
}

# Mock functions from source.py
def mock_generate_ai_r_report_summary(df, group_by):
    return df.groupby(group_by)['current_ai_r_score'].mean().reset_index()

def mock_calculate_synergy_score(vr_score, hr_score, employee_data):
    alignment_factor = 0.9 # Simplified for mock
    return (vr_score * hr_score / 100) * alignment_factor

def mock_calculate_ai_r_score(vr_score, hr_score, synergy_score, params):
    alpha = params['alpha']
    beta = params['beta']
    return alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_score

def mock_simulate_pathway_impact(employee_id, pathway_id, completion_rate, mastery_score, df_employees, df_occupations, df_pathways, params):
    employee = df_employees[df_employees['employee_id'] == employee_id].iloc[0]
    pathway = df_pathways[df_pathways['pathway_id'] == pathway_id].iloc[0]

    current_vr = employee['vr_score']
    current_hr = employee['hr_r_score']
    current_ai_r = employee['current_ai_r_score']

    impacted_ai_fluency = pathway['impact_ai_fluency'] * completion_rate * mastery_score
    impacted_domain_expertise = pathway['impact_domain_expertise'] * completion_rate * mastery_score
    impacted_adaptive_capacity = pathway['impact_adaptive_capacity'] * completion_rate * mastery_score

    projected_ai_fluency = min(100, employee['ai_fluency_score'] + impacted_ai_fluency)
    projected_domain_expertise = min(100, employee['domain_expertise_score'] + impacted_domain_expertise)
    projected_adaptive_capacity = min(100, employee['adaptive_capacity_score'] + impacted_adaptive_capacity)

    projected_vr_weights = params['vr_weights']
    projected_vr = (
        projected_ai_fluency * projected_vr_weights['ai_fluency'] +
        projected_domain_expertise * projected_vr_weights['domain_expertise'] +
        projected_adaptive_capacity * projected_vr_weights['adaptive_capacity']
    )
    projected_vr = min(100, projected_vr)

    projected_hr = current_hr # Assume HR is constant for what-if
    projected_synergy = mock_calculate_synergy_score(projected_vr, projected_hr, employee)
    projected_ai_r = mock_calculate_ai_r_score(projected_vr, projected_hr, projected_synergy, params)

    delta_ai_r = projected_ai_r - current_ai_r
    pathway_name_res = pathway['pathway_name']

    return projected_ai_r, delta_ai_r, pathway_name_res

def mock_optimize_pathway_sequence(employee_id, current_ai_r_opt_val, df_pathways, T_max_hours, cost_weight_lambda, df_employees, df_occupations, params):
    employee = df_employees[df_employees['employee_id'] == employee_id].iloc[0]
    
    available_pathways = df_pathways.copy()
    completion_rate = 0.9
    mastery_score = 0.85

    pathway_impacts = []
    for idx, pathway in available_pathways.iterrows():
        projected_ai_r_temp, delta_ai_r_temp, _ = mock_simulate_pathway_impact(
            employee_id, pathway['pathway_id'], completion_rate, mastery_score, df_employees, df_occupations, df_pathways, params
        )
        score = delta_ai_r_temp - (cost_weight_lambda * pathway['cost']) - (0.1 * pathway['time_hours']) # Arbitrary time penalty
        pathway_impacts.append({
            'pathway_id': pathway['pathway_id'],
            'pathway_name': pathway['pathway_name'],
            'delta_ai_r': delta_ai_r_temp,
            'cost': pathway['cost'],
            'time_hours': pathway['time_hours'],
            'score': score
        })
    
    sorted_pathways = sorted(pathway_impacts, key=lambda x: x['score'], reverse=True)
    
    recommended_sequence = []
    projected_final_ai_r = current_ai_r_opt_val
    total_cost = 0
    total_time_hours = 0
    ai_r_improvement = 0

    for pathway in sorted_pathways:
        if total_time_hours + pathway['time_hours'] <= T_max_hours:
            recommended_sequence.append(pathway['pathway_name'])
            total_cost += pathway['cost']
            total_time_hours += pathway['time_hours']
            projected_final_ai_r += pathway['delta_ai_r']
            ai_r_improvement += pathway['delta_ai_r']
            projected_final_ai_r = min(100, projected_final_ai_r)
        else:
            break

    return {
        "recommended_sequence": recommended_sequence,
        "projected_final_ai_r": projected_final_ai_r,
        "total_cost": total_cost,
        "total_time_hours": total_time_hours,
        "ai_r_improvement": ai_r_improvement
    }

# Create a mock module and populate it
mock_source_module = types.ModuleType("source")
mock_source_module.df_employees = mock_df_employees
mock_source_module.df_occupations = mock_df_occupations
mock_source_module.df_pathways = mock_df_pathways
mock_source_module.PARAMS = mock_PARAMS
mock_source_module.generate_ai_r_report_summary = mock_generate_ai_r_report_summary
mock_source_module.simulate_pathway_impact = mock_simulate_pathway_impact
mock_source_module.optimize_pathway_sequence = mock_optimize_pathway_sequence
# Make matplotlib and seaborn available in the mock module as they are used in the app
mock_source_module.plt = plt
mock_source_module.sns = sns

sys.modules["source"] = mock_source_module

# --- End of Mocking ---


def test_initial_load():
    at = AppTest.from_file("app.py").run()
    assert at.title[0].value == "QuLab: AI Readiness score"
    assert "Framework Introduction" in at.markdown[1].value
    assert at.session_state["current_page"] == "Dashboard"
    assert at.session_state["report_group_by"] == "job_role"
    assert at.session_state["selected_employee_id_whatif"] == mock_df_employees['employee_id'].iloc[0]
    assert at.session_state["selected_pathway_id_whatif"] == mock_df_pathways['pathway_id'].iloc[0]
    assert at.session_state["completion_rate_whatif"] == 0.9
    assert at.session_state["mastery_score_whatif"] == 0.85
    assert at.session_state["selected_employee_id_opt"] == mock_df_employees['employee_id'].iloc[0]
    assert at.session_state["T_max_hours_opt"] == 300
    assert at.session_state["cost_weight_lambda_opt"] == 0.005


def test_navigate_to_what_if_scenario():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_whatif").click().run()
    assert at.session_state["current_page"] == "What-If Scenario"
    assert at.title[0].value == "What-If Scenario Engine"
    assert "Simulate the impact of learning pathways on individual employee AI-Readiness scores." in at.markdown[1].value


def test_navigate_to_pathway_optimization():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_optimization").click().run()
    assert at.session_state["current_page"] == "Pathway Optimization"
    assert at.title[0].value == "Multi-Step Pathway Optimization"
    assert "Generate an optimized sequence of learning pathways" in at.markdown[1].value


def test_navigate_to_strategic_recommendations():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_recommendations").click().run()
    assert at.session_state["current_page"] == "Strategic Recommendations"
    assert at.title[0].value == "Strategic Recommendations & Conclusion"
    assert "Leverage data-driven insights to formulate actionable strategies" in at.markdown[1].value


def test_navigate_to_air_overview():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_air_overview").click().run()
    assert at.session_state["current_page"] == "AI-R Overview"
    assert at.title[0].value == "The AI-Readiness Framework: Core Concepts"
    assert "The AI-Readiness Score (AI-R) is a novel parametric framework" in at.markdown[1].value


def test_navigate_to_hrr_overview():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_hrr").click().run()
    assert at.session_state["current_page"] == "Systematic Opportunity (HR^R)"
    assert at.title[0].value == "Systematic Opportunity ($H^R$) Component"
    assert "Systematic Opportunity ($H^R$) represents the macro-level demand" in at.markdown[1].value


def test_navigate_to_vr_overview():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_vr").click().run()
    assert at.session_state["current_page"] == "Idiosyncratic Readiness (V^R)"
    assert at.title[0].value == "Idiosyncratic Readiness ($V^R$) Component"
    assert "Idiosyncratic Readiness ($V^R$) measures an individual's specific preparation" in at.markdown[1].value


def test_navigate_to_synergy_function():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_synergy").click().run()
    assert at.session_state["current_page"] == "Synergy Function"
    assert at.title[0].value == "Synergy Function"
    assert "The Synergy function captures the multiplicative benefits" in at.markdown[1].value


def test_dashboard_group_by_department():
    at = AppTest.from_file("app.py").run()
    at.selectbox(key="dashboard_group_by_select").set("department").run()
    assert at.session_state["report_group_by"] == "department"
    assert at.dataframe[0].value.columns.tolist() == ['department', 'current_ai_r_score']
    assert at.pyplot[0].figure is not None


def test_what_if_scenario_simulation():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_whatif").click().run()

    # Ensure initial values are set from session state
    assert at.selectbox[0].value == mock_df_employees['employee_id'].iloc[0]
    assert at.selectbox[1].value == mock_df_pathways['pathway_name'].iloc[0]
    assert at.slider[0].value == 0.9  # Completion Rate
    assert at.slider[1].value == 0.85 # Mastery Score

    at.button("Simulate Pathway Impact").click().run()

    # Check if results are displayed
    assert at.subheader[0].value == "Simulation Results:"
    assert "Current AI-R Score:" in at.markdown[3].value
    assert "Projected AI-R Score:" in at.markdown[5].value
    assert at.pyplot[0].figure is not None

    # Test changing employee and pathway
    at.selectbox[0].set(mock_df_employees['employee_id'].iloc[1]).run() # Select E002
    at.selectbox[1].set(mock_df_pathways['pathway_name'].iloc[1]).run() # Select HR Analytics
    at.slider[0].set_value(0.7).run()
    at.slider[1].set_value(0.75).run()
    at.button("Simulate Pathway Impact").click().run()

    assert at.markdown[3].value.startswith(f"Current AI-R Score: **{mock_df_employees['current_ai_r_score'].iloc[1]:.2f}**")
    assert at.markdown[4].value.startswith("Chosen Pathway: **HR Analytics**")
    assert at.pyplot[0].figure is not None


def test_pathway_optimization_simulation():
    at = AppTest.from_file("app.py").run()
    at.button(key="nav_optimization").click().run()

    # Ensure initial values are set from session state
    assert at.selectbox[0].value == mock_df_employees['employee_id'].iloc[0]
    assert at.slider[0].value == 300  # Max Time
    assert at.slider[1].value == 0.005 # Cost Weight

    at.button("Optimize Pathways").click().run()

    # Check if results are displayed
    assert at.subheader[0].value == "Optimization Results:"
    assert "Current AI-R Score:" in at.markdown[3].value
    assert "Recommended Pathway Sequence:" in at.markdown[4].value
    assert at.pyplot[0].figure is not None

    # Test changing employee, max time, and cost weight
    at.selectbox[0].set(mock_df_employees['employee_id'].iloc[1]).run() # Select E002
    at.slider[0].set_value(200).run()
    at.slider[1].set_value(0.008).run()
    at.button("Optimize Pathways").click().run()

    assert at.markdown[3].value.startswith(f"Current AI-R Score: **{mock_df_employees['current_ai_r_score'].iloc[1]:.2f}**")
    assert at.pyplot[0].figure is not None


def test_strategic_recommendations_with_optimization_results():
    at = AppTest.from_file("app.py")
    
    # Pre-set session state for optimization results
    at.session_state["optimization_results"] = {
        "current_ai_r": 75.0,
        "selected_employee_id": "E001",
        "recommended_sequence": ["Advanced ML", "Cloud AI Basics"],
        "projected_final_ai_r": 90.5,
        "total_cost": 1750,
        "total_time_hours": 140,
        "ai_r_improvement": 15.5
    }
    
    at.run()
    at.button(key="nav_recommendations").click().run()

    assert at.session_state["current_page"] == "Strategic Recommendations"
    assert "Recommended Pathway Sequence: **Advanced ML, Cloud AI Basics**" in at.markdown[11].value
    assert "Projected AI-R Improvement: **15.50**" in at.markdown[12].value

