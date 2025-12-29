
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from source import df_employees, df_occupations, df_pathways, PARAMS, calculate_ai_r_score, generate_ai_r_report_summary, simulate_pathway_impact, optimize_pathway_sequence, plot_current_vs_projected_ai_r, plot_skills_gap_heatmap # Imports all functions and global variables like df_employees, PARAMS etc.

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, the **"Workforce AI-Readiness & Upskilling Strategizer"** Streamlit application provides AI Workforce leaders and HR executives with a data-driven tool to assess, simulate, and optimize their workforce's preparedness for AI-enabled careers. It implements the AI-Readiness Score (AI-R) framework to quantify individual capabilities and market opportunities, enabling strategic talent development and upskilling initiatives.

### Target Personas
*   **AI Workforce Leaders**: To understand the collective AI-readiness, identify strategic skill gaps, and plan large-scale training programs.
*   **Human Resources Executives**: To manage talent development, design learning pathways, and forecast future workforce needs in the context of AI transformation.
*   **Economists & Financial Engineers**: To analyze the economic value of AI skills, assess return on investment for training, and model labor market dynamics.
*   **Data Analysts & Data Scientists**: To drill down into specific metrics, perform ad-hoc analyses, and validate model assumptions.

### High-Level Story Flow
The application guides the user through a structured workflow to analyze and act on workforce AI-readiness:

1.  **Framework Introduction**: The user is first introduced to the core AI-Readiness Score (AI-R) framework, its components, and underlying formulas. (Accessible via sidebar for reference).
2.  **Workforce Dashboard**: The user views an aggregated overview of the workforce's current AI-R scores and broad skill gaps, broken down by departments or job roles. This allows for quick assessment of the current state of the talent pool.
3.  **What-If Scenario Engine**: The user selects an individual employee and a specific learning pathway, then simulates the immediate impact of completing that pathway (with adjustable completion and mastery rates) on their AI-R score. This helps in evaluating program effectiveness at an individual level.
4.  **Multi-Step Pathway Optimization**: For more complex transitions or broader skill development, the user can identify an optimal sequence of learning pathways for a selected employee, balancing AI-R improvement with time and cost constraints. This provides a strategic roadmap for talent investment.
5.  **Strategic Recommendations**: Based on the comprehensive analysis and simulations, the application synthesizes insights and generates strategic recommendations for targeted upskilling initiatives and overall workforce development plans.
""")

# Initialize core dataframes and parameters from source.py
# Using .copy() to ensure modifications within the app do not alter the original imported data
if 'df_employees' not in st.session_state:
    st.session_state.df_employees = df_employees.copy()
if 'df_occupations' not in st.session_state:
    st.session_state.df_occupations = df_occupations.copy()
if 'df_pathways' not in st.session_state:
    st.session_state.df_pathways = df_pathways.copy()
if 'PARAMS' not in st.session_state:
    st.session_state.PARAMS = PARAMS.copy()

# Initialize variables for application navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Dashboard" # Sets the default landing page

# State for Dashboard page (Workforce Assessment & Skills Gap Analysis)
if 'report_group_by' not in st.session_state:
    st.session_state.report_group_by = 'job_role' # Default grouping for reports/heatmaps

# State for What-If Scenario Engine page
if 'selected_employee_id_whatif' not in st.session_state:
    st.session_state.selected_employee_id_whatif = st.session_state.df_employees['employee_id'].iloc[0] if not st.session_state.df_employees.empty else "N/A"
if 'selected_pathway_id_whatif' not in st.session_state:
    st.session_state.selected_pathway_id_whatif = st.session_state.df_pathways['pathway_id'].iloc[0] if not st.session_state.df_pathways.empty else "N/A"
if 'completion_rate_whatif' not in st.session_state:
    st.session_state.completion_rate_whatif = 0.9
if 'mastery_score_whatif' not in st.session_state:
    st.session_state.mastery_score_whatif = 0.85
if 'whatif_results' not in st.session_state:
    st.session_state.whatif_results = None # Stores {current_ai_r, projected_ai_r, delta_ai_r, pathway_name}

# State for Multi-Step Pathway Optimization page
if 'selected_employee_id_opt' not in st.session_state:
    st.session_state.selected_employee_id_opt = st.session_state.df_employees['employee_id'].iloc[0] if not st.session_state.df_employees.empty else "N/A"
if 'T_max_hours_opt' not in st.session_state:
    st.session_state.T_max_hours_opt = 300
if 'cost_weight_lambda_opt' not in st.session_state:
    st.session_state.cost_weight_lambda_opt = 0.005
if 'optimization_results' not in st.session_state:
    st.session_state.optimization_results = None # Stores {current_ai_r, recommended_sequence, projected_final_ai_r, total_cost, total_time_hours, ai_r_improvement}

# Sidebar Navigation:
with st.sidebar:
    st.title("AI-Readiness Strategizer")
    st.markdown("---")
    st.markdown("### Core Workflow")
    if st.button("Dashboard", key="nav_dashboard"):
        st.session_state.current_page = "Dashboard"
    if st.button("What-If Scenario Engine", key="nav_whatif"):
        st.session_state.current_page = "What-If Scenario"
    if st.button("Pathway Optimization", key="nav_optimization"):
        st.session_state.current_page = "Pathway Optimization"
    if st.button("Strategic Recommendations", key="nav_recommendations"):
        st.session_state.current_page = "Strategic Recommendations"
    st.markdown("---")
    st.markdown("### Framework Details")
    if st.button("AI-R Overview", key="nav_air_overview"):
        st.session_state.current_page = "AI-R Overview"
    if st.button("Systematic Opportunity (HR^R)", key="nav_hrr"):
        st.session_state.current_page = "Systematic Opportunity (HR^R)"
    if st.button("Idiosyncratic Readiness (V^R)", key="nav_vr"):
        st.session_state.current_page = "Idiosyncratic Readiness (V^R)"
    if st.button("Synergy Function", key="nav_synergy"):
        st.session_state.current_page = "Synergy Function"


# Main Content Area (Conditional Rendering Logic):
if st.session_state.current_page == "Dashboard":
    from application_pages.dashboard import run_page
    run_page()
elif st.session_state.current_page == "What-If Scenario":
    from application_pages.what_if_scenario import run_page
    run_page()
elif st.session_state.current_page == "Pathway Optimization":
    from application_pages.pathway_optimization import run_page
    run_page()
elif st.session_state.current_page == "Strategic Recommendations":
    from application_pages.strategic_recommendations import run_page
    run_page()
elif st.session_state.current_page == "AI-R Overview":
    from application_pages.air_overview import run_page
    run_page()
elif st.session_state.current_page == "Systematic Opportunity (HR^R)":
    from application_pages.systematic_opportunity_hrr import run_page
    run_page()
elif st.session_state.current_page == "Idiosyncratic Readiness (V^R)":
    from application_pages.idiosyncratic_readiness_vr import run_page
    run_page()
elif st.session_state.current_page == "Synergy Function":
    from application_pages.synergy_function import run_page
    run_page()

