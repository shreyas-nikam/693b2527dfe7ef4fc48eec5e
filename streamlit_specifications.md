
# Streamlit Application Specification: Workforce AI-Readiness & Upskilling Strategizer

## 1. Application Overview

### Purpose
The "Workforce AI-Readiness & Upskilling Strategizer" Streamlit application provides AI Workforce leaders and HR executives with a data-driven tool to assess, simulate, and optimize their workforce's preparedness for AI-enabled careers. It implements the AI-Readiness Score (AI-R) framework to quantify individual capabilities and market opportunities, enabling strategic talent development and upskilling initiatives.

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

## 2. Code Requirements

### Import Statement
The Streamlit application (`app.py`) will begin with the following import statements:

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from source import * # Imports all functions and global variables like df_employees, PARAMS etc.
```

### `st.session_state` Design

`st.session_state` will be extensively used to maintain the application's state across user interactions and page navigations. All dataframes and parameters derived from `source.py` will be copied into session state upon initial load. This ensures that any modifications or selections made by the user within the app are preserved and don't affect the original imported objects from `source.py`.

**Initialization (at the beginning of `app.py`, after imports):**

```python
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

```

### Application Structure and Flow

The application will feature a prominent sidebar for primary navigation, enabling a multi-page user experience through conditional rendering based on the `st.session_state.current_page` variable.

**Sidebar Navigation:**

```python
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
```

**Main Content Area (Conditional Rendering Logic):**

```python
if st.session_state.current_page == "Dashboard":
    # Dashboard Page Content
elif st.session_state.current_page == "What-If Scenario":
    # What-If Scenario Page Content
elif st.session_state.current_page == "Pathway Optimization":
    # Pathway Optimization Page Content
elif st.session_state.current_page == "Strategic Recommendations":
    # Strategic Recommendations Page Content
elif st.session_state.current_page == "AI-R Overview":
    # AI-R Overview Page Content
elif st.session_state.current_page == "Systematic Opportunity (HR^R)":
    # Systematic Opportunity (HR^R) Page Content
elif st.session_state.current_page == "Idiosyncratic Readiness (V^R)":
    # Idiosyncratic Readiness (V^R) Page Content
elif st.session_state.current_page == "Synergy Function":
    # Synergy Function Page Content
```

---

#### **Page: Dashboard**

*   **Application Flow & Persona Focus:** This page serves as the primary entry point for AI Workforce leaders and HR executives. It allows them to quickly grasp the collective AI-readiness of their workforce, identify high-level strengths and weaknesses across departments and job roles, and pinpoint areas that may require strategic attention.
*   **Markdown:**
    ```python
    st.title("Workforce AI-Readiness Dashboard")
    st.markdown(f"Gain a high-level overview of your workforce's AI-Readiness, broken down by key organizational groups.")
    st.markdown(f"---")
    st.header("Aggregated AI-Readiness Report")
    st.markdown(f"The 'Workforce AI-Readiness Report' summarizes the aggregated AI-R scores, providing a high-level overview of the organization's AI-readiness across different segments.")
    ```
*   **Streamlit Widgets & Interaction:**
    *   **Group By Selector:**
        ```python
        st.session_state.report_group_by = st.selectbox(
            "Group AI-Readiness Report by:",
            ['job_role', 'department'],
            index=0 if st.session_state.report_group_by == 'job_role' else 1,
            key='dashboard_group_by_select',
            on_change=lambda: st.session_state.update({'report_group_by': st.session_state.dashboard_group_by_select})
        )
        ```
    *   **Summary Table Display:**
        ```python
        ai_r_summary_report = generate_ai_r_report_summary(st.session_state.df_employees)
        st.dataframe(ai_r_summary_report)
        st.markdown(f"Average AI-R score for the entire workforce: **{st.session_state.df_employees['current_ai_r_score'].mean():.2f}**")
        ```
    *   **Skills Gap Heatmap:**
        ```python
        st.header("Skills Gap Analysis Heatmap")
        st.markdown(f"This heatmap visualizes the average scores for Idiosyncratic Readiness ($V^R$) sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity) across different employee groups.")
        st.markdown(f"The heatmap offers a granular view, clearly highlighting which $V^R$ sub-components are strong or weak within specific job roles/departments, thereby pinpointing areas for targeted upskilling efforts.")
        
        # Adaptation: plot_skills_gap_heatmap needs to return a matplotlib figure.
        # Original: plt.show() -> Modified: return plt.gcf()
        fig_heatmap, ax_heatmap = plt.subplots(figsize=(10, 6))
        vr_sub_components = ['ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score']
        heatmap_data = st.session_state.df_employees.groupby(st.session_state.report_group_by)[vr_sub_components].mean()
        sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt=".1f", linewidths=.5, ax=ax_heatmap)
        ax_heatmap.set_title(f'Average $V^R$ Sub-Component Scores by {st.session_state.report_group_by}')
        ax_heatmap.set_ylabel(st.session_state.report_group_by)
        ax_heatmap.set_xlabel('$V^R$ Sub-Component')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig_heatmap)
        ```
*   **Function Invocation Points:**
    *   `generate_ai_r_report_summary(df_employees_data)`: Called to generate the summary table for aggregated AI-R scores. (Reads `st.session_state.df_employees`).
    *   `plot_skills_gap_heatmap(df_employees_data, group_by_column)`: (Adapted from `source.py` to return a `matplotlib` figure for `st.pyplot`) Called to generate the skills gap heatmap. (Reads `st.session_state.df_employees`).
*   **`st.session_state` Usage:**
    *   **Reads**: `st.session_state.df_employees`, `st.session_state.report_group_by`.
    *   **Updates**: `st.session_state.report_group_by` (via selectbox interaction).

---

#### **Page: What-If Scenario Engine**

*   **Application Flow & Persona Focus:** This page is designed for Human Resources executives and AI Workforce leaders to simulate the potential impact of specific training programs on individual employees. By adjusting completion rates and mastery scores, they can assess the effectiveness of learning pathways and make data-driven decisions about talent investment.
*   **Markdown:**
    ```python
    st.title("What-If Scenario Engine")
    st.markdown(f"Simulate the impact of learning pathways on individual employee AI-Readiness scores.")
    st.markdown(f"---")
    st.header("Simulating Learning Pathway Impact")
    st.markdown(f"The 'What-If' scenario engine allows HR leaders to simulate the impact of various training programs and learning pathways on an individual's AI-Readiness. This dynamic tool helps assess potential improvements to $V^R$ sub-components and the overall AI-R score.")
    st.markdown(f"The update formula for AI-R is conceptually:")
    st.markdown(r"$$AI-R_{i,t+1} = AI-R_{i,t} + \sum_{p \in P} \Delta_p \cdot Completion_p \cdot Mastery_p$$")
    st.markdown(f"where $\\Delta_p$ is the pre-calibrated impact coefficient for pathway $p$ (from `df_pathways`), $Completion_p \\in [0,1]$ is the fraction completed, and $Mastery_p \\in [0,1]$ is the assessment performance score.")
    st.markdown(f"The pathway impact ($\\Delta_p$) will directly affect the AI-Fluency, Domain-Expertise, or Adaptive-Capacity scores, which then propagate to $V^R$ and subsequently AI-R.")
    st.markdown(f"This simulation demonstrates the predictive power of the framework, allowing leaders to evaluate the effectiveness of different training programs. By adjusting completion and mastery rates, they can gain insights into the potential ROI of various learning investments and tailor programs to maximize workforce AI-readiness.")
    ```
*   **Streamlit Widgets & Interaction:**
    *   **Employee Selector:**
        ```python
        employee_ids = st.session_state.df_employees['employee_id'].tolist()
        selected_employee_id = st.selectbox(
            "Select Employee:",
            employee_ids,
            index=employee_ids.index(st.session_state.selected_employee_id_whatif) if st.session_state.selected_employee_id_whatif in employee_ids else 0,
            key='whatif_employee_select'
        )
        st.session_state.selected_employee_id_whatif = selected_employee_id
        ```
    *   **Pathway Selector:**
        ```python
        pathway_names = st.session_state.df_pathways['pathway_name'].tolist()
        pathway_map = st.session_state.df_pathways.set_index('pathway_name')['pathway_id'].to_dict()
        default_pathway_name_whatif = st.session_state.df_pathways[st.session_state.df_pathways['pathway_id'] == st.session_state.selected_pathway_id_whatif]['pathway_name'].iloc[0] if st.session_state.selected_pathway_id_whatif != "N/A" and st.session_state.selected_pathway_id_whatif in pathway_map.values() else pathway_names[0]
        selected_pathway_name = st.selectbox(
            "Select Learning Pathway:",
            pathway_names,
            index=pathway_names.index(default_pathway_name_whatif),
            key='whatif_pathway_select'
        )
        selected_pathway_id = pathway_map.get(selected_pathway_name, "N/A")
        st.session_state.selected_pathway_id_whatif = selected_pathway_id
        ```
    *   **Completion Rate Slider:**
        ```python
        completion_rate = st.slider("Completion Rate", 0.0, 1.0, st.session_state.completion_rate_whatif, 0.05, key='whatif_completion_rate')
        st.session_state.completion_rate_whatif = completion_rate
        ```
    *   **Mastery Score Slider:**
        ```python
        mastery_score = st.slider("Mastery Score", 0.0, 1.0, st.session_state.mastery_score_whatif, 0.05, key='whatif_mastery_score')
        st.session_state.mastery_score_whatif = mastery_score
        ```
    *   **Simulate Button:**
        ```python
        if st.button("Simulate Pathway Impact"):
            if st.session_state.selected_employee_id_whatif != "N/A" and st.session_state.selected_pathway_id_whatif != "N/A":
                current_ai_r_val = st.session_state.df_employees[st.session_state.df_employees['employee_id'] == st.session_state.selected_employee_id_whatif]['current_ai_r_score'].iloc[0]
                projected_ai_r, delta_ai_r, pathway_name_res = simulate_pathway_impact(
                    st.session_state.selected_employee_id_whatif,
                    st.session_state.selected_pathway_id_whatif,
                    st.session_state.completion_rate_whatif,
                    st.session_state.mastery_score_whatif,
                    st.session_state.df_employees,
                    st.session_state.df_occupations,
                    st.session_state.df_pathways,
                    st.session_state.PARAMS
                )
                st.session_state.whatif_results = {
                    "current_ai_r": current_ai_r_val,
                    "projected_ai_r": projected_ai_r,
                    "delta_ai_r": delta_ai_r,
                    "pathway_name": pathway_name_res,
                    "selected_employee_id": st.session_state.selected_employee_id_whatif # Store selected employee ID for results display
                }
            else:
                st.warning("Please ensure an employee and a pathway are selected for simulation.")
        ```
    *   **Display Results (if simulation completed):**
        ```python
        if st.session_state.whatif_results and st.session_state.whatif_results["selected_employee_id"] == st.session_state.selected_employee_id_whatif:
            res = st.session_state.whatif_results
            st.subheader("Simulation Results:")
            st.markdown(f"Employee ID: **{res['selected_employee_id']}**")
            st.markdown(f"Current AI-R Score: **{res['current_ai_r']:.2f}**")
            st.markdown(f"Chosen Pathway: **{res['pathway_name']}**")
            st.markdown(f"Projected AI-R Score: **{res['projected_ai_r']:.2f}**")
            st.markdown(f"Change in AI-R ($\\Delta$AI-R): **{res['delta_ai_r']:.2f}**")

            # Adaptation: plot_current_vs_projected_ai_r needs to return a matplotlib figure.
            # Original: plt.show() -> Modified: return plt.gcf()
            fig_whatif, ax_whatif = plt.subplots(figsize=(8, 5))
            plot_current_vs_projected_ai_r(res['current_ai_r'], [res['projected_ai_r']], [res['pathway_name']])
            st.pyplot(fig_whatif)
        ```
*   **Function Invocation Points:**
    *   `simulate_pathway_impact(...)`: Main logic for calculating projected AI-R. (Reads `st.session_state.df_employees`, `st.session_state.df_occupations`, `st.session_state.df_pathways`, `st.session_state.PARAMS`).
    *   `plot_current_vs_projected_ai_r(...)`: (Adapted from `source.py` to return a `matplotlib` figure for `st.pyplot`) Visualizes the current vs. projected AI-R scores.
*   **`st.session_state` Usage:**
    *   **Reads**: `st.session_state.df_employees`, `st.session_state.df_occupations`, `st.session_state.df_pathways`, `st.session_state.PARAMS`, `st.session_state.selected_employee_id_whatif`, `st.session_state.selected_pathway_id_whatif`, `st.session_state.completion_rate_whatif`, `st.session_state.mastery_score_whatif`, `st.session_state.whatif_results`.
    *   **Updates**: `st.session_state.selected_employee_id_whatif`, `st.session_state.selected_pathway_id_whatif`, `st.session_state.completion_rate_whatif`, `st.session_state.mastery_score_whatif`, `st.session_state.whatif_results`.

---

#### **Page: Multi-Step Pathway Optimization**

*   **Application Flow & Persona Focus:** This page empowers AI Workforce leaders and Data Analysts to identify an optimal sequence of learning pathways for a selected employee. It's crucial for designing strategic roadmaps for talent development, especially for complex skill transitions, by balancing AI-R improvement with budget and time constraints.
*   **Markdown:**
    ```python
    st.title("Multi-Step Pathway Optimization")
    st.markdown(f"Generate an optimized sequence of learning pathways to maximize AI-Readiness within defined constraints.")
    st.markdown(f"---")
    st.header("Multi-Step Pathway Optimization")
    st.markdown(f"For complex skill transitions or broader workforce development, identifying an optimal sequence of learning pathways is crucial. This involves balancing AI-R improvement with constraints like total cost and time. The multi-step pathway optimization problem can be formulated as:")
    st.markdown(r"$$\max_{P_1,...,P_K} AI-R(P_1,..., P_K) - \lambda_{\text{cost}} \cdot \sum_{k=1}^K Cost(P_k)$$")
    st.markdown(f"subject to:")
    st.markdown(r"$$ \sum_{k=1}^K Time(P_k) \leq T_{\text{max}} $$")
    st.markdown(r"$$ P_k \in P_{\text{feasible}} $$")
    st.markdown(r"$$ Prerequisites(P_k) \subseteq \{P_1,...,P_{k-1}\} $$")
    st.markdown(f"For this application, we implement a simplified greedy optimization strategy to identify a sequence of pathways that maximizes AI-R improvement within a given time budget, considering the cost.")
    st.markdown(f"The pathway optimization function provides a strategic roadmap for investing in talent development. By considering multiple pathways, their costs, and time commitments, organizations can make data-driven decisions to maximize the AI-Readiness of their workforce efficiently, identifying high-ROI learning initiatives.")
    ```
*   **Streamlit Widgets & Interaction:**
    *   **Employee Selector:**
        ```python
        employee_ids_opt = st.session_state.df_employees['employee_id'].tolist()
        selected_employee_id_opt = st.selectbox(
            "Select Employee for Optimization:",
            employee_ids_opt,
            index=employee_ids_opt.index(st.session_state.selected_employee_id_opt) if st.session_state.selected_employee_id_opt in employee_ids_opt else 0,
            key='opt_employee_select'
        )
        st.session_state.selected_employee_id_opt = selected_employee_id_opt
        ```
    *   **Max Time Hours Slider:**
        ```python
        T_max_hours = st.slider("Maximum Time (hours)", 50, 500, st.session_state.T_max_hours_opt, 10, key='opt_max_time')
        st.session_state.T_max_hours_opt = T_max_hours
        ```
    *   **Cost Weight Lambda Slider:**
        ```python
        cost_weight_lambda = st.slider("Cost Weight ($\\lambda_{\\text{cost}}$)", 0.001, 0.01, st.session_state.cost_weight_lambda_opt, 0.001, key='opt_cost_weight', format="%.3f")
        st.session_state.cost_weight_lambda_opt = cost_weight_lambda
        ```
    *   **Optimize Button:**
        ```python
        if st.button("Optimize Pathways"):
            if st.session_state.selected_employee_id_opt != "N/A":
                current_ai_r_opt_val = st.session_state.df_employees[st.session_state.df_employees['employee_id'] == st.session_state.selected_employee_id_opt]['current_ai_r_score'].iloc[0]
                optimization_results = optimize_pathway_sequence(
                    st.session_state.selected_employee_id_opt,
                    current_ai_r_opt_val,
                    st.session_state.df_pathways,
                    st.session_state.T_max_hours_opt,
                    st.session_state.cost_weight_lambda_opt,
                    st.session_state.df_employees,
                    st.session_state.df_occupations, # Not directly used in this `optimize_pathway_sequence` but kept for consistency with source.py signature
                    st.session_state.PARAMS
                )
                st.session_state.optimization_results = {
                    "current_ai_r": current_ai_r_opt_val,
                    "selected_employee_id": st.session_state.selected_employee_id_opt, # Store selected employee ID for results display
                    **optimization_results # Unpack results from the function
                }
            else:
                st.warning("Please select an employee for optimization.")
        ```
    *   **Display Results (if optimization completed):**
        ```python
        if st.session_state.optimization_results and st.session_state.optimization_results["selected_employee_id"] == st.session_state.selected_employee_id_opt:
            opt_res = st.session_state.optimization_results
            st.subheader("Optimization Results:")
            st.markdown(f"Employee ID: **{opt_res['selected_employee_id']}**")
            st.markdown(f"Current AI-R Score: **{opt_res['current_ai_r']:.2f}**")
            st.markdown(f"Recommended Pathway Sequence: **{', '.join(opt_res['recommended_sequence']) if opt_res['recommended_sequence'] else 'No pathways recommended within constraints'}**")
            st.markdown(f"Projected Final AI-R: **{opt_res['projected_final_ai_r']:.2f}**")
            st.markdown(f"Total Cost: **${opt_res['total_cost']:.2f}**")
            st.markdown(f"Total Time (hours): **{opt_res['total_time_hours']:.2f}**")
            st.markdown(f"AI-R Improvement: **{opt_res['ai_r_improvement']:.2f}**")

            # Adaptation: plot_current_vs_projected_ai_r needs to return a matplotlib figure.
            # Original: plt.show() -> Modified: return plt.gcf()
            fig_opt, ax_opt = plt.subplots(figsize=(8, 5))
            plot_current_vs_projected_ai_r(
                opt_res['current_ai_r'],
                [opt_res['projected_final_ai_r']],
                ['Optimized Pathway Sequence']
            )
            st.pyplot(fig_opt)
        ```
*   **Function Invocation Points:**
    *   `optimize_pathway_sequence(...)`: Main logic for multi-step optimization. (Reads `st.session_state.df_employees`, `st.session_state.df_pathways`, `st.session_state.df_occupations`, `st.session_state.PARAMS`).
    *   `plot_current_vs_projected_ai_r(...)`: (Adapted from `source.py` to return a `matplotlib` figure for `st.pyplot`) Visualizes the current vs. projected AI-R scores.
*   **`st.session_state` Usage:**
    *   **Reads**: `st.session_state.df_employees`, `st.session_state.df_occupations`, `st.session_state.df_pathways`, `st.session_state.PARAMS`, `st.session_state.selected_employee_id_opt`, `st.session_state.T_max_hours_opt`, `st.session_state.cost_weight_lambda_opt`, `st.session_state.optimization_results`.
    *   **Updates**: `st.session_state.selected_employee_id_opt`, `st.session_state.T_max_hours_opt`, `st.session_state.cost_weight_lambda_opt`, `st.session_state.optimization_results`.

---

#### **Page: Strategic Recommendations**

*   **Application Flow & Persona Focus:** This page consolidates all insights for AI Workforce leaders and HR executives, offering actionable recommendations based on the comprehensive AI-Readiness assessment, skills gap analysis, and training simulations. It provides a strategic roadmap for continuous workforce adaptation.
*   **Markdown:**
    ```python
    st.title("Strategic Recommendations & Conclusion")
    st.markdown(f"Leverage data-driven insights to formulate actionable strategies for AI workforce development.")
    st.markdown(f"---")
    st.header("Strategic Recommendations for AI Workforce Development")
    st.markdown(f"Based on the AI-Readiness assessment, skills gap analysis, and 'What-If' scenario simulations, we can formulate strategic recommendations for workforce development. These insights move beyond static skill inventories, providing a dynamic framework for continuous adaptation in an AI-transformed landscape.")
    st.markdown(f"**Summary of Insights:**")

    # Insight 1: Identify low AI-R cohorts and their drivers
    st.subheader("1. Target Low AI-R Cohorts with Driver-Specific Interventions")
    st.markdown(f"Identify employees with significantly lower AI-R scores and analyze whether their low score is primarily driven by low Idiosyncratic Readiness ($V^R$) or insufficient Systematic Opportunity ($H^R$) in their current role. Tailor interventions accordingly.")
    low_ai_r_cohorts = st.session_state.df_employees.sort_values(by='current_ai_r_score').head(5)
    st.markdown(f"**Example: Top 5 Employees with Lowest AI-R Scores**")
    st.dataframe(low_ai_r_cohorts[['employee_id', 'job_role', 'department', 'current_ai_r_score', 'vr_score', 'hr_r_score']].set_index('employee_id'))
    st.markdown(f"*   **Action:** For employees with low $V^R$, recommend AI-Fluency focused training. For those with low $H^R$, consider internal mobility options or upskilling for roles with higher market opportunity.")

    # Insight 2: Pinpoint critical skills gaps (references Dashboard insights)
    st.subheader("2. Address Critical Skills Gaps via Targeted Upskilling")
    st.markdown(f"Based on the Skills Gap Heatmap (from the Dashboard), common weaknesses can be identified. For instance, if 'Business Analyst' roles show lower 'Adaptive-Capacity' scores, a targeted training program focusing on 'Strategic Career Management' or 'Cognitive Flexibility' would be beneficial.")
    st.markdown(f"*   **Example:** If 'Data Scientist' roles generally excel in 'AI-Fluency' but show gaps in 'Domain-Expertise', prioritize advanced domain-specific AI applications and certifications.")

    # Insight 3: Recommend specific learning pathways (references Optimization results)
    st.subheader("3. Implement Optimized Multi-Step Learning Pathways")
    if st.session_state.optimization_results:
        opt_res = st.session_state.optimization_results
        st.markdown(f"For employee **{opt_res['selected_employee_id']}** (current AI-R: **{opt_res['current_ai_r']:.2f}**), the optimization identified the following sequence to maximize AI-R improvement within budget and time constraints:")
        st.markdown(f"*   **Recommended Pathway Sequence:** {', '.join(opt_res['recommended_sequence']) if opt_res['recommended_sequence'] else 'No pathways recommended'}")
        st.markdown(f"*   **Projected AI-R Improvement:** {opt_res['ai_r_improvement']:.2f}")
        st.markdown(f"*   **Total Cost:** ${opt_res['total_cost']:.2f}, **Total Time (hours):** {opt_res['total_time_hours']:.2f}")
    else:
        st.markdown(f"No pathway optimization has been run yet. Please use the 'Pathway Optimization' page to generate recommendations.")
    st.markdown(f"*   **Action:** Leverage such optimized pathways to guide individual career development plans, balancing cost, time, and impact.")

    # Insight 4: Highlight roles with high HR^R but low V^R
    st.subheader("4. Invest Strategically in High Opportunity, Low Readiness Roles")
    high_hr_low_vr_roles = st.session_state.df_employees[(st.session_state.df_employees['hr_r_score'] > 70) & (st.session_state.df_employees['vr_score'] < 60)]
    if not high_hr_low_vr_roles.empty:
        st.markdown(f"Identify job roles that have high Systematic Opportunity ($H^R$) but where the current workforce has lower Idiosyncratic Readiness ($V^R$). These are prime candidates for strategic investment.")
        st.markdown(f"**Example: Employees in High $H^R$ / Low $V^R$ Roles**")
        st.dataframe(high_hr_low_vr_roles[['employee_id', 'job_role', 'hr_r_score', 'vr_score', 'current_ai_r_score']].head().set_index('employee_id'))
        st.markdown(f"*   **Action:** For these roles, focused upskilling on AI-Fluency and Domain-Expertise (specific to the high $H^R$ area) will yield high returns.")
    else:
        st.markdown(f"All employees in this simulation appear to have a balanced $H^R$ and $V^R$, or no explicit high opportunity/low readiness roles were identified.")

    # Insight 5: Emphasize adaptive capacities
    st.subheader("5. Foster Continuous Learning and Adaptive Capacity")
    st.markdown(f"The rapid pace of AI evolution necessitates a workforce with strong adaptive capacities. Emphasize training that builds cognitive flexibility, social-emotional intelligence for human-AI collaboration, and strategic career management skills across all employee levels.")
    st.markdown(f"*   **Action:** Integrate 'Adaptive-Capacity' boosting modules into all major learning initiatives and promote a culture of continuous learning and experimentation.")

    st.markdown("---")
    st.markdown(f"This application provides a robust, quantitative framework for proactive workforce planning. By dynamically assessing AI-Readiness, analyzing skill gaps, and simulating training impacts, organizations can make informed investments in their human capital, ensuring competitiveness and adaptability in the evolving AI landscape. The framework's flexibility allows for continuous recalibration and adaptation as market demands and individual capabilities evolve.")
    ```
*   **Function Invocation Points:** None directly, but the insights displayed rely on `st.session_state.df_employees` (which has all calculated scores) and `st.session_state.optimization_results`.
*   **`st.session_state` Usage:**
    *   **Reads**: `st.session_state.df_employees`, `st.session_state.optimization_results`.
    *   **Updates**: None.

---

#### **Page: AI-R Overview**

*   **Application Flow & Persona Focus:** This page is for any persona interested in understanding the foundational concepts. It provides a detailed, formula-driven introduction to the AI-Readiness Framework, ensuring transparency and theoretical grounding for the metrics used throughout the application.
*   **Markdown:**
    ```python
    st.title("The AI-Readiness Framework: Core Concepts")
    st.header("Introduction to the AI-Readiness Framework")
    st.markdown(f"The AI-Readiness Score (AI-R) is a novel parametric framework designed to quantify an individual's preparedness for success in AI-enabled careers. It decomposes career opportunity into two orthogonal components: Systematic Opportunity ($H^R$), representing macro-level job growth and demand, and Idiosyncratic Readiness ($V^R$), representing individual-specific capabilities. A Synergy factor captures the multiplicative benefits when individual readiness aligns with market opportunity.")
    st.markdown(f"The core formula for the AI-Readiness Score for individual $i$ at time $t$ is defined as:")
    st.markdown(r"$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$")
    st.markdown(f"where:")
    st.markdown(f"*   $V^R_{i}(t)$: Idiosyncratic Readiness (individual capability).")
    st.markdown(f"*   $H^R(t)$: Systematic Opportunity (market demand).")
    st.markdown(f"*   $\\alpha \\in [0,1]$: Weight on individual vs. market factors. For this notebook, we'll use $\\alpha = 0.6$.")
    st.markdown(f"*   $\\beta > 0$: Synergy coefficient. For this notebook, we'll use $\\beta = 0.15$.")
    st.markdown(f"*   Both $V^R$ and $H^R$ are normalized to $[0, 100]$.")
    st.markdown(f"*   $Synergy\\% \\in [0,100]$ (percentage units).")
    st.markdown(f"This framework allows for dynamic 'what-if' scenario planning, helping to guide targeted upskilling initiatives and talent development.")
    st.markdown(f"This section demonstrates how the final AI-R score is computed by combining the Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and Synergy components, weighted by the parameters $\\alpha$ and $\\beta$. The example reflects a scenario where an individual has strong readiness in a high-opportunity field with good alignment, resulting in a high AI-R score.")
    ```
*   **Function Invocation Points:** None.
*   **`st.session_state` Usage:** None directly.

---

#### **Page: Systematic Opportunity ($H^R$)**

*   **Application Flow & Persona Focus:** This page provides in-depth information for economists, data scientists, and leaders interested in the macro-level factors influencing career opportunities. It explains how external market forces contribute to an individual's AI-Readiness score.
*   **Markdown:**
    ```python
    st.title("Systematic Opportunity ($H^R$) Component")
    st.header("Conceptual Definition")
    st.markdown(f"Systematic Opportunity ($H^R$) represents the macro-level demand and growth potential in AI-enabled occupations. Following portfolio theory, this is analogous to market beta—an individual cannot create these opportunities through their own actions, but they can position themselves to benefit from favorable market conditions.")
    st.markdown(f"For individual $i$ targeting occupation $o_{target}$ at time $t$:")
    st.markdown(r"$$H^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$")
    st.markdown(f"where $H_{\text{base}}$ is the base opportunity score, $M_{\text{growth}}$ captures temporal momentum, and $M_{\text{regional}}$ adjusts for geographic factors.")

    st.subheader("Base Opportunity Score ($H_{\text{base}}$)")
    st.markdown(f"The Base Opportunity Score ($H_{\text{base}}(o)$) aggregates the various dimensions of occupational attractiveness: AI-Enhancement Potential, Job Growth Projections, Wage Premium, and Entry Accessibility. It is calculated as a weighted sum:")
    st.markdown(r"$$H_{\text{base}}(o) = w_1 \cdot AI\text{-}Enhancement_o + w_2 \cdot Growth_{\text{normalized}} + w_3 \cdot Wage_o + w_4 \cdot Access_o$$")
    st.markdown(f"The weights ($w_j$) reflect the relative importance of each factor, as defined in the `PARAMS` dictionary ($w_1 = 0.30$, $w_2 = 0.30$, $w_3 = 0.25$, $w_4 = 0.15$). The final score is then scaled to $[0,100]$.")
    
    st.markdown(f"**1. AI-Enhancement Potential**")
    st.markdown(f"Measures how much AI augments rather than replaces tasks:")
    st.markdown(r"$$AI\text{-}Enhancement_o = \frac{1}{|T_o|} \sum_{t \in T_o} (1 - Automation_t) \cdot AI\text{-}Augmentation_t$$")
    st.markdown(f"where $T_o$ is the set of tasks for occupation $o$, $Automation_t \\in [0,1]$ measures replaceability, and $AI\text{-}Augmentation_t \\in [0,1]$ measures productivity enhancement. For simplicity in our synthetic data, we directly include an aggregated `ai_enhancement_potential` for each occupation.")
    st.markdown(f"This step demonstrates how the AI-Enhancement Potential, a key sub-component of $H^R$, is retrieved for a specific job role. This value reflects the degree to which AI is expected to augment, rather than automate, tasks within that occupation, indicating its future relevance.")
    
    st.markdown(f"**2. Job Growth Projections**")
    st.markdown(f"Quantify the expected increase or decrease in employment for an occupation over a given period (e.g., 10 years). The raw growth rate $g$ is calculated as:")
    st.markdown(r"$$Growth_o = \frac{\text{Projected Jobs}_{o,t+10} - \text{Current Jobs}_{o,t}}{\text{Current Jobs}_{o,t}}$$")
    st.markdown(f"This raw growth rate is then normalized to a scale of $[0, 100]$ using an affine transformation:")
    st.markdown(r"$$Growth_{\text{normalized}} = \frac{g + 0.5}{2.0} \times 100$$")
    st.markdown(f"This transformation maps a growth rate range of $g \\in [-0.5, 1.5]$ (representing -50% to +150% change) to $[0,100]$.")
    st.markdown(f"The normalized job growth score provides a standardized measure of an occupation's future demand, directly contributing to its Systematic Opportunity. A higher normalized score indicates a greater projected increase in job availability, making the occupation more attractive in the AI-transformed labor market.")

    st.markdown(f"**3. Wage Premium & Entry Accessibility**")
    st.markdown(f"Two other critical factors contributing to Systematic Opportunity are Wage Premium and Entry Accessibility.")
    st.markdown(f"**Wage Premium** ($Wage_o$) measures the compensation potential for AI-skilled roles relative to the median wage in that occupation:")
    st.markdown(r"$$Wage_o = \frac{\text{AI-skilled wage}_o - \text{median wage}_o}{\text{median wage}_o}$$")
    st.markdown(f"This provides an indication of the economic value placed on AI-related skills within a role.")
    st.markdown(f"**Entry Accessibility** ($Access_o$) quantifies the ease of transitioning into a role, based on typical educational and experience requirements:")
    st.markdown(r"$$Access_o = 1 - \frac{\text{Education Years Required} + \text{Experience Years Required}}{10}$$")
    st.markdown(f"This linear formula provides a simplified measure, where a higher score indicates easier entry.")
    st.markdown(f"These calculations complete the primary sub-components of the Base Opportunity Score. Wage Premium highlights the financial attractiveness of an AI-enabled role, while Entry Accessibility provides insight into the practical barriers for individuals considering a transition, both being crucial for assessing Systematic Opportunity.")

    st.subheader("Dynamic Multipliers: Growth & Regional")
    st.markdown(f"Beyond the static Base Opportunity Score, Systematic Opportunity is modulated by dynamic, time-varying market factors:")
    st.markdown(f"**1. Growth Multiplier ($M_{\text{growth}}(t)$):** Captures market momentum based on recent changes in job postings.")
    st.markdown(r"$$M_{\text{growth}}(t) = 1 + \lambda \cdot \left( \frac{\text{Job Postings}_{o,t}}{\text{Job Postings}_{o,t-1}} - 1 \right)$$")
    st.markdown(f"where $\\lambda = 0.3$ dampens volatility, keeping the multiplier typically between $0.7$ and $1.3$.")
    st.markdown(f"**2. Regional Multiplier ($M_{\text{regional}}(t)$):** Adjusts for local labor market conditions and remote work suitability.")
    st.markdown(r"$$M_{\text{regional}}(t) = \frac{\text{Local Demand}_{i,t}}{\text{National Avg Demand}} \times (1 + \gamma \cdot \text{Remote Work Factor}_o)$$")
    st.markdown(f"where $\\gamma = 0.2$ and $Remote Work Factor \\in [0,1]$ measures the occupation's suitability for remote work. For simplicity, we assume `Local Demand` equals `National Avg Demand` for the primary calculation and focus on the `Remote Work Factor` contribution.")
    st.markdown(f"The dynamic multipliers introduce responsiveness to market fluctuations. The Growth Multiplier reflects current hiring trends, while the Regional Multiplier accounts for geographical demand and the increasing prevalence of remote work. These factors ensure that the Systematic Opportunity score remains relevant to contemporary market conditions.")
    st.markdown(f"The final Systematic Opportunity score ($H^R(t)$) for an individual $i$ targeting occupation $o_{\text{target}}$ at time $t$ is calculated by combining the Base Opportunity Score with the dynamic multipliers.")
    st.markdown(f"This step completes the calculation of the Systematic Opportunity component for each employee, linking their current job role to market conditions. This score highlights external career potential that individuals can position themselves to capture.")
    ```
*   **Function Invocation Points:** None.
*   **`st.session_state` Usage:** None directly.

---

#### **Page: Idiosyncratic Readiness ($V^R$)**

*   **Application Flow & Persona Focus:** This page targets HR professionals and individuals focused on personal development. It breaks down the individual capabilities that contribute to AI-readiness, explaining how skills can be actively developed through learning and experience.
*   **Markdown:**
    ```python
    st.title("Idiosyncratic Readiness ($V^R$) Component")
    st.header("Conceptual Definition")
    st.markdown(f"Idiosyncratic Readiness ($V^R$) measures an individual's specific preparation to succeed in AI-enabled careers. Unlike systematic opportunity, these factors can be directly improved through deliberate learning and skill development.")
    st.markdown(f"The final Idiosyncratic Readiness score ($V^R(t)$) aggregates AI-Fluency, Domain-Expertise, and Adaptive-Capacity. This score quantifies an individual's personal preparation to succeed in AI-enabled careers, factors that can be directly improved through deliberate learning and skill development. It is a weighted sum:")
    st.markdown(r"$$V^R(t) = w_{\text{VR1}} \cdot AI\text{-}Fluency_i(t) + w_{\text{VR2}} \cdot Domain\text{-}Expertise_i(t) + w_{\text{VR3}} \cdot Adaptive\text{-}Capacity_i(t)$$")
    st.markdown(f"The weights ($w_{\text{VR1}} = 0.45$, $w_{\text{VR2}} = 0.35$, $w_{\text{VR3}} = 0.20$) reflect the assessment that AI-Fluency is the most critical factor, followed by Domain-Expertise, with Adaptive-Capacity playing a supporting role (weights are from `PARAMS`). The final $V^R$ score is normalized to $[0, 100]$.")
    st.markdown(f"This completes the calculation of the individual-specific readiness component. The $V^R$ score provides a holistic view of an individual's intrinsic capabilities and potential for growth in AI-driven roles, serving as a critical counterpart to the market-driven $H^R$.")

    st.subheader("AI-Fluency Factor")
    st.markdown(f"The AI-Fluency factor is a key sub-component, representing the ability to effectively use, understand, and collaborate with AI systems. It is calculated as a weighted sum of four sub-components:")
    st.markdown(r"$$AI\text{-}Fluency_i = \sum_{k=1}^4 \theta_k \cdot S_{i,k}$$")
    st.markdown(f"The sub-components ($S_{i,k}$) and their weights ($\\theta_k$ from `PARAMS`) are:")
    st.markdown(f"**1. Technical AI Skills** ($S_{i,1}$, $\\theta_1 = 0.30$): Based on Prompting, Tools, Understanding, and Data Literacy scores.")
    st.markdown(r"$$S_{i,1} = \frac{1}{4} (\text{Prompting}_i + \text{Tools}_i + \text{Understanding}_i + \text{DataLit}_i)$$")
    st.markdown(f"**2. AI-Augmented Productivity** ($S_{i,2}$, $\\theta_2 = 0.35$): Measures productivity gains with AI assistance.")
    st.markdown(r"$$S_{i,2} = \frac{\text{Output Quality}_{i,\text{with AI}}}{\text{Output Quality}_{i,\text{without AI}}} \cdot \frac{\text{Time}_{i,\text{without AI}}}{\text{Time}_{i,\text{with AI}}}$$")
    st.markdown(f"For simplicity, our synthetic data has `ai_augmented_productivity_norm` pre-calculated based on this concept.")
    st.markdown(f"**3. Critical AI Judgment** ($S_{i,3}$, $\\theta_3 = 0.20$): Assesses error detection and appropriate trust decisions with AI outputs.")
    st.markdown(r"$$S_{i,3} = \frac{\text{Errors Caught}_i}{\text{Total AI Errors}} + \frac{\text{Appropriate Trust Decisions}_i}{\text{Total Decisions}}$$")
    st.markdown(f"For simplicity, our synthetic data provides `errors_caught_norm` and `trust_decisions_norm` which we'll combine and re-normalize.")
    st.markdown(f"**4. AI Learning Velocity** ($S_{i,4}$, $\\theta_4 = 0.15$): Measures improvement rate per unit time investment.")
    st.markdown(r"$$S_{i,4} = \frac{\Delta Proficiency_i}{\Delta t} \cdot \frac{1}{\text{Hours Invested}}$$")
    st.markdown(f"For simplicity in this notebook, $\\Delta Proficiency_i / \\Delta t$ can be approximated as a 'learning_rate' for simulation purposes and then scaled with `hours_invested`.")
    st.markdown(f"The AI-Fluency score provides a detailed individual assessment of an employee's ability to interact with and leverage AI technologies. This multi-faceted measure highlights specific areas where an individual might excel or need further development in their AI-related capabilities.")

    st.subheader("Domain-Expertise Factor")
    st.markdown(f"Domain-Expertise captures an individual's depth of knowledge in specific application areas, complementing their AI-Fluency. It is a multiplicative combination of Educational Foundation, Practical Experience, and Specialization Depth:")
    st.markdown(r"$$Domain\text{-}Expertise_i = E_{\text{education}} \cdot E_{\text{experience}} \cdot E_{\text{specialization}}$$")
    st.markdown(f"**1. Educational Foundation ($E_{\text{education}}$):** Discrete values based on education level (e.g., PhD=1.0, Master's=0.85, Bachelor's=0.70, Associate's/Certificate=0.60, HS+Coursework=0.50).")
    st.markdown(f"**2. Practical Experience ($E_{\text{experience}}$):** Measured by years of experience with diminishing returns:")
    st.markdown(r"$$E_{\text{experience}} = 1 - e^{-\gamma_{\text{exp}} \cdot Years}$$")
    st.markdown(f"where $\\gamma_{\text{exp}} = 0.15$.")
    st.markdown(f"**3. Specialization Depth ($E_{\text{specialization}}$):** Reflects specific achievements and recognition in their field:")
    st.markdown(r"$$E_{\text{specialization}} = w_{\text{port}} \cdot \text{Portfolio}_i + w_{\text{recog}} \cdot \text{Recognition}_i + w_{\text{cred}} \cdot \text{Credentials}_i$$")
    st.markdown(f"where $w_{\text{port}} = 0.4$, $w_{\text{recog}} = 0.3$, $w_{\text{cred}} = 0.3$.")
    st.markdown(f"Domain-Expertise underscores the importance of deep, specialized knowledge in specific fields, which AI tools are designed to augment. This score provides a quantitative measure of an individual's subject matter mastery, a crucial complement to their AI-Fluency.")

    st.subheader("Adaptive-Capacity Factor")
    st.markdown(f"Adaptive-Capacity measures the meta-skills that enable successful navigation of AI-driven transitions, focusing on an individual's ability to learn, adapt, and interact effectively in new environments. It is an equally weighted sum of three meta-skills:")
    st.markdown(r"$$Adaptive\text{-}Capacity_i = \frac{1}{3} (C_{\text{cognitive}} + C_{\text{social}} + C_{\text{strategic}})$$")
    st.markdown(f"where each $C$ component is scored on a scale of $[0, 100]$:")
    st.markdown(f"*   **Cognitive Flexibility ($C_{\text{cognitive}}$):** Problem-solving in novel contexts, transfer learning, creative application of AI tools.")
    st.markdown(f"*   **Social-Emotional Intelligence ($C_{\text{social}}$):** Empathy, negotiation, leadership, human-AI collaboration.")
    st.markdown(f"*   **Strategic Career Management ($C_{\text{strategic}}$):** Awareness of AI trends, proactive skill development, network building.")
    st.markdown(f"Adaptive-Capacity highlights an individual's inherent ability to thrive in a rapidly changing AI landscape. These meta-skills are increasingly vital for sustained career success, as they enable individuals to continuously learn, adapt, and collaborate effectively with both humans and AI.")
    ```
*   **Function Invocation Points:** None.
*   **`st.session_state` Usage:** None directly.

---

#### **Page: Synergy Function**

*   **Application Flow & Persona Focus:** This page explains to economists and data scientists how the framework captures the multiplicative benefits of aligning individual capabilities with market opportunities, moving beyond simple additive models.
*   **Markdown:**
    ```python
    st.title("Synergy Function")
    st.header("Conceptual Basis")
    st.markdown(f"The Synergy function captures the multiplicative benefits when individual readiness ($V^R$) aligns with market opportunity ($H^R$). It is defined as:")
    st.markdown(r"$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$")
    st.markdown(f"where both $V^R$ and $H^R$ are on $[0,100]$ scale, and $Alignment_i \\in [0,1]$ ensures $Synergy\\% \\in [0,100]$.")
    st.markdown(f"The Synergy score formalizes the idea that career success is more than just individual capability plus market demand; it also depends on how well these two factors align. A high synergy score indicates a 'sweet spot' where an individual's unique skills and career stage perfectly intersect with market opportunities.")

    st.subheader("Alignment Factor: Skills Match & Timing Factor")
    st.markdown(f"The $Alignment_i$ factor measures how well individual skills match occupation requirements and career stage:")
    st.markdown(r"$$Alignment_i = \frac{\text{Skills Match Score}_i}{\text{Maximum Possible Match}} \times \text{Timing Factor}_i$$")
    st.markdown(f"**1. Skills Match Score:** Using O*NET-like task-skill mappings (simulated through `skill_a` to `skill_j` in our synthetic data), we compute:")
    st.markdown(r"$$Match_i = \sum_{s \in S} \min(\text{Individual Skill}_{i,s}, \text{Required Skill}_{o,s}) \cdot \text{Importance}_s$$")
    st.markdown(f"where $S$ is the set of all skills, and the minimum operator ensures that excess skill in one area doesn't compensate for deficiency in critical areas. For `Maximum Possible Match`, we assume a perfect match of 1.0 (after normalization of individual and required skills to 0-1).")
    st.markdown(f"**2. Timing Factor:** Career stage affects transition ease:")
    st.markdown(r"$$Timing(y) = \begin{cases} 1.0 & \text{if } y \in [0,5] \text{ (early career)} \\ 1.0 & \text{if } y \in (5,15] \text{ (mid-career)} \\ 0.8 & \text{if } y > 15 \text{ (late career, transition friction)} \end{cases}$$")
    st.markdown(f"where $y$ is years of experience. Note that all timing values are $\\leq 1.0$ to ensure Alignment remains bounded at $[0, 1]$.")
    st.markdown(f"The Alignment Factor provides a nuanced measure of how well an individual's skills and career stage align with a specific occupational target. This factor is critical for determining the true 'fit' and the potential for synergy between an individual's readiness and market opportunity.")
    ```
*   **Function Invocation Points:** None.
*   **`st.session_state` Usage:** None directly.
