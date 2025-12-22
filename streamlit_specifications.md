
# Streamlit Application Specification: AI-Readiness & Upskilling Strategizer

## 1. Application Overview

The AI-Readiness & Upskilling Strategizer is a Streamlit application designed for AI Workforce leaders and Human Resources executives. It provides an intuitive interface to assess and enhance the AI-readiness of an organization's workforce. The application implements a novel parametric framework to quantify an individual's preparedness for AI-enabled careers, allowing for data-driven strategic workforce planning.

**Learning Goals:**
*   Understand the components and calculation of the AI-Readiness Score (AI-R), which decomposes into Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and Synergy.
*   Perform skills gap analysis to identify collective strengths and weaknesses across $V^R$ sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
*   Simulate the impact of various training programs and learning pathways on individual and cohort AI-R scores using a "What-If" scenario engine.
*   Optimize multi-step learning pathway sequences considering constraints like cost and time.
*   Generate comprehensive workforce AI-Readiness reports and strategic recommendations for upskilling initiatives.

## 2. User Interface Requirements

The application will simulate a multi-page structure within a single `app.py` file, navigated via a sidebar.

### Layout and Navigation Structure

*   **Sidebar (`st.sidebar`):**
    *   A `st.sidebar.radio` widget will enable navigation between the main sections (simulated pages):
        *   "Introduction"
        *   "Data Configuration"
        *   "AI-Readiness Calculation Walkthrough"
        *   "AI-R Report & Skills Gap Analysis"
        *   "What-If Scenario Engine"
        *   "Multi-Step Pathway Optimization"
        *   "Strategic Recommendations"
*   **Main Content Area:** (`st.container` or direct `st.markdown`/`st.pyplot`):
    *   Each selected page will render its specific content, inputs, outputs, and visualizations in the main area.

### Input Widgets and Controls

*   **Global Parameters (on "Data Configuration" page):**
    *   `st.slider` for $\alpha$ (weight on individual vs. market factors) and $\beta$ (synergy coefficient).
    *   `st.slider` or `st.number_input` for $\lambda_{\text{growth}}$ (growth multiplier damping) and $\gamma_{\text{regional}}$ (regional multiplier weight).
    *   `st.number_input` for $\gamma_{\text{exp}}$ (experience decay rate).
    *   `st.expander` sections for weight dictionaries (`hr_base_weights`, `theta_ai_fluency_weights`, `domain_specialization_weights`, `vr_component_weights`) with individual `st.number_input` widgets for each weight.
*   **Data Management (on "Data Configuration" page):**
    *   `st.button` to "Generate/Reset Synthetic Data" for `df_employees`, `df_occupations`, `df_pathways`.
    *   `st.dataframe` to display `head()` of generated/loaded dataframes.
*   **Employee/Pathway Selection (on "AI-Readiness Calculation Walkthrough", "What-If Scenario Engine", "Multi-Step Pathway Optimization" pages):**
    *   `st.selectbox` for `employee_id` to select a specific employee for detailed analysis or simulation.
    *   `st.selectbox` for `pathway_id` to select a learning pathway.
*   **"What-If" Scenario Inputs:**
    *   `st.slider` for `completion_rate` (range: $0.0$ to $1.0$).
    *   `st.slider` for `mastery_score` (range: $0.0$ to $1.0$).
    *   `st.button` to "Run What-If Simulation".
*   **"Multi-Step Pathway Optimization" Inputs:**
    *   `st.number_input` for `T_max_hours` (maximum time budget in hours).
    *   `st.number_input` for `cost_weight_lambda` (parameter for AI-R improvement vs. cost trade-off).
    *   `st.button` to "Run Optimization".
*   **Report Grouping (on "AI-R Report & Skills Gap Analysis" page):**
    *   `st.selectbox` for `group_by_column` (e.g., 'job_role', 'department') to aggregate report data.

### Visualization Components (charts, graphs, tables)

*   **Data Display:** `st.dataframe` for raw data, summary tables, and calculation results (e.g., `df_employees.head()`, `ai_r_summary_report`).
*   **Skills Gap Analysis:** `st.pyplot` to render a Seaborn heatmap from `plot_skills_gap_heatmap`, visualizing average $V^R$ sub-component scores.
*   **Scenario Comparison:** `st.pyplot` to render a Matplotlib bar chart from `plot_current_vs_projected_ai_r`, comparing current and projected AI-R scores.
*   **Key Metrics:** `st.metric` for displaying overall average AI-R, individual scores, and changes ($\Delta AI-R$).

### Interactive Elements and Feedback Mechanisms

*   **Action Buttons:** `st.button` widgets will trigger calculations, simulations, and report generation.
*   **Loading Indicators:** `st.spinner("Calculating...")` will be used for longer computational tasks.
*   **Status Messages:** `st.success("Success!")`, `st.error("An error occurred.")`, `st.info("Information message.")` will provide user feedback.

## 3. Additional Requirements

### Annotation and Tooltip Specifications

*   **Mathematical Formulas:** All display equations using `st.latex(r"$$...$$")` will be accompanied by `st.expander` or `st.info` providing a plain-language explanation of the formula and definitions for each variable.
*   **Key Terms:** Important concepts like "$V^R$", "$H^R$", "Synergy%", "AI-Fluency", "Domain-Expertise", "Adaptive-Capacity" will be explained via `st.info` or `st.help` when first introduced or when their values are displayed.
*   **Parameters:** Each parameter ($\alpha$, $\beta$, $w_j$, $\theta_k$, $\lambda_{\text{growth}}$, $\gamma_{\text{regional}}$, $\gamma_{\text{exp}}$, `T_max_hours`, `cost_weight_lambda`) presented via `st.slider` or `st.number_input` will have an accompanying `st.info` tooltip explaining its purpose and impact on the model.

### Save the States of the Fields Properly

*   **Session State:** All dynamic dataframes (`df_employees`, `df_occupations`, `df_pathways`) and the `PARAMS` dictionary will be initialized and stored in `st.session_state`. This ensures that data and user-modified parameters persist across page navigation and rerun events.
*   **Input Preservation:** User inputs for selections (`employee_id`, `pathway_id`, `group_by_column`) and numerical values (`completion_rate`, `mastery_score`, `T_max_hours`, `cost_weight_lambda`, and all weights in `PARAMS`) will be bound to `st.session_state` keys to maintain their values.
*   **Dynamic Updates:** Any calculations or simulations will update the relevant data stored in `st.session_state` to reflect the current state of the application.

## 4. Notebook Content and Code Requirements

This section outlines how specific content from the Jupyter Notebook will be integrated into the Streamlit application. All Python functions will be defined globally at the top of the `app.py` file.

### Page: "Introduction"

*   **Markdown Content:**
    *   The notebook's main title "# Workforce AI-Readiness & Upskilling Strategizer" will be rendered using `st.title()`.
    *   The "Section 1: Introduction to the AI-Readiness Framework" markdown and subsequent text blocks explaining the AI-Readiness Score, its decomposition, and the dynamic "what-if" scenario planning will be rendered using `st.markdown()`.
*   **Mathematical Formulae:**
    *   The core AI-Readiness formula:
        `st.latex(r"$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$")`
        will be displayed, accompanied by explanations for $V^R_{i}(t)$, $H^R(t)$, $\alpha$, $\beta$, and $Synergy\%$.
*   **Code Stub:**
    *   The `calculate_ai_r` function will be defined globally.
    *   The `PARAMS` dictionary will be initialized in `st.session_state` if not already present.
    *   A sample calculation using placeholder values will be displayed with `st.metric()`.

### Page: "Data Configuration"

*   **Markdown Content:**
    *   "Section 2: Synthetic Data Generation and Setup" and its introductory text will be rendered with `st.header()` and `st.markdown()`.
*   **Code Stubs:**
    *   The `generate_synthetic_employees`, `generate_synthetic_occupations`, and `generate_synthetic_pathways` functions will be defined globally.
    *   A `st.button("Generate/Reset Synthetic Data")` will trigger these functions, storing their outputs (`df_employees`, `df_occupations`, `df_pathways`) into `st.session_state`.
*   **Display:**
    *   `st.dataframe(df_employees.head())`, `st.dataframe(df_occupations.head())`, `st.dataframe(df_pathways.head())` will display the initial data.
    *   The `PARAMS` dictionary will be displayed using `st.json` or formatted `st.dataframe`, and made editable via input widgets as described in Section 2.

### Page: "AI-Readiness Calculation Walkthrough"

This page will provide an interactive step-by-step display of the AI-R calculation for a user-selected employee.

#### Subsection: Systematic Opportunity ($H^R$) Components

*   **Section 3: AI-Enhancement Potential**
    *   Markdown and formula: `st.markdown()`, `st.latex(r"$$AI\text{-}Enhancement_o = \frac{1}{|T_o|} \sum_{t \in T_o} (1 - Automation_t) \cdot AI\text{-}Augmentation_t$$")`
    *   Code: `calculate_ai_enhancement`. Result displayed with `st.metric()`.
*   **Section 4: Job Growth Projections**
    *   Markdown and formulae: `st.markdown()`, `st.latex(r"$$Growth_o = \frac{\text{Projected Jobs}_{o,t+10} - \text{Current Jobs}_{o,t}}{\text{Current Jobs}_{o,t}}$$")`, `st.latex(r"$$Growth_{\text{normalized}} = \frac{g + 0.5}{2.0} \times 100$$")`
    *   Code: `calculate_job_growth_normalized`. Results displayed.
*   **Section 5: Wage Premium & Entry Accessibility**
    *   Markdown and formulae: `st.markdown()`, `st.latex(r"$$Wage_o = \frac{\text{AI-skilled wage}_o - \text{median wage}_o}{\text{median wage}_o}$$")`, `st.latex(r"$$Access_o = 1 - \frac{\text{Education Years Required} + \text{Experience Years Required}}{10}$$")`
    *   Code: `calculate_wage_premium`, `calculate_entry_accessibility`. Results displayed.
*   **Section 6: Calculate Base Opportunity Score ($H_{\text{base}}$)**
    *   Markdown and formula: `st.markdown()`, `st.latex(r"$$H_{\text{base}}(o) = w_1 \cdot AI\text{-}Enhancement_o + w_2 \cdot Growth_{\text{normalized}} + w_3 \cdot Wage_o + w_4 \cdot Access_o$$")`
    *   Code: `calculate_base_opportunity_score`. Result displayed. `df_occupations` in `st.session_state` will be updated with this score for all occupations.
*   **Section 7: Dynamic Multipliers: Growth & Regional**
    *   Markdown and formulae: `st.markdown()`, `st.latex(r"$$M_{\text{growth}}(t) = 1 + \lambda \cdot \left( \frac{\text{Job Postings}_{o,t}}{\text{Job Postings}_{o,t-1}} - 1 \right)$$")`, `st.latex(r"$$M_{\text{regional}}(t) = \frac{\text{Local Demand}_{i,t}}{\text{National Avg Demand}} \times (1 + \gamma \cdot \text{Remote Work Factor}_o)$$")`
    *   Code: `calculate_growth_multiplier`, `calculate_regional_multiplier`. Results displayed. `df_occupations` in `st.session_state` will be updated with these multipliers.
*   **Section 8: Calculate Final Systematic Opportunity ($H^R$)**
    *   Markdown and formula: `st.markdown()`, `st.latex(r"$$HR^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$")`
    *   Code: `calculate_systematic_opportunity`. Result displayed. `df_employees` in `st.session_state` will be updated with `hr_r_score`.

#### Subsection: Idiosyncratic Readiness ($V^R$) Components

*   **Section 9: AI-Fluency Factor**
    *   Markdown and formula: `st.markdown()`, `st.latex(r"$$AI\text{-}Fluency_i = \sum_{k=1}^4 \theta_k \cdot S_{i,k}$$")`
    *   Sub-component formulae:
        *   `st.latex(r"$$S_{i,1} = \frac{1}{4} (\text{Prompting}_i + \text{Tools}_i + \text{Understanding}_i + \text{DataLit}_i)$$")`
        *   `st.latex(r"$$S_{i,2} = \frac{\text{Output Quality}_{i,\text{with AI}}}{\text{Output Quality}_{i,\text{without AI}}} \cdot \frac{\text{Time}_{i,\text{without AI}}}{\text{Time}_{i,\text{with AI}}}$$")`
        *   `st.latex(r"$$S_{i,3} = \frac{\text{Errors Caught}_i}{\text{Total AI Errors}} + \frac{\text{Appropriate Trust Decisions}_i}{\text{Total Decisions}}$$")`
        *   `st.latex(r"$$S_{i,4} = \frac{\Delta Proficiency_i}{\Delta t} \cdot \frac{1}{\text{Hours Invested}}$$")`
    *   Code: `calculate_technical_ai_skills`, `calculate_ai_augmented_productivity`, `calculate_critical_ai_judgment`, `calculate_ai_learning_velocity`, `calculate_ai_fluency`. Results displayed. `df_employees` in `st.session_state` will be updated with `ai_fluency_score`.
*   **Section 10: Domain-Expertise Factor**
    *   Markdown and formula: `st.markdown()`, `st.latex(r"$$Domain\text{-}Expertise_i = E_{\text{education}} \cdot E_{\text{experience}} \cdot E_{\text{specialization}}$$")`
    *   Sub-component formulae: `st.markdown()` for `E_education` rules, `st.latex(r"$$E_{\text{experience}} = 1 - e^{-\gamma_{\text{exp}} \cdot Years}$$")`, `st.latex(r"$$E_{\text{specialization}} = w_{\text{port}} \cdot \text{Portfolio}_i + w_{\text{recog}} \cdot \text{Recognition}_i + w_{\text{cred}} \cdot \text{Credentials}_i$$")`
    *   Code: `calculate_educational_foundation`, `calculate_practical_experience`, `calculate_specialization_depth`, `calculate_domain_expertise`. Results displayed. `df_employees` in `st.session_state` will be updated with `domain_expertise_score`.
*   **Section 11: Adaptive-Capacity Factor**
    *   Markdown and formula: `st.markdown()`, `st.latex(r"$$Adaptive\text{-}Capacity_i = \frac{1}{3} (C_{\text{cognitive}} + C_{\text{social}} + C_{\text{strategic}})$$")`
    *   Code: `calculate_adaptive_capacity`. Result displayed. `df_employees` in `st.session_state` will be updated with `adaptive_capacity_score`.
*   **Section 12: Calculate Final Idiosyncratic Readiness ($V^R$)**
    *   Markdown and formula: `st.markdown()`, `st.latex(r"$$V^R(t) = w_{\text{VR1}} \cdot AI\text{-}Fluency_i(t) + w_{\text{VR2}} \cdot Domain\text{-}Expertise_i(t) + w_{\text{VR3}} \cdot Adaptive\text{-}Capacity_i(t)$$")`
    *   Code: `calculate_idiosyncratic_readiness`. Result displayed. `df_employees` in `st.session_state` will be updated with `vr_score`.

#### Subsection: Synergy Function & Overall AI-R

*   **Section 13: Synergy Function: Skills Match & Timing Factor**
    *   Markdown and formulae: `st.markdown()`, `st.latex(r"$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$")`, `st.latex(r"$$Alignment_i = \frac{\text{Skills Match Score}_i}{\text{Maximum Possible Match}} \times \text{Timing Factor}_i$$")`, `st.latex(r"$$Match_i = \sum_{s \in S} \min(\text{Individual Skill}_{i,s}, \text{Required Skill}_{o,s}) \cdot \text{Importance}_s$$")`, `st.markdown()` for Timing Factor rules.
    *   Code: `calculate_skills_match_score`, `calculate_timing_factor`, `calculate_alignment_factor`. Results displayed. `df_employees` in `st.session_state` will be updated with `alignment_factor`.
*   **Section 14: Calculate Final Synergy Score**
    *   Markdown: `st.markdown()`.
    *   Code: `calculate_synergy`. Result displayed. `df_employees` in `st.session_state` will be updated with `synergy_score`.
*   **Section 15: Calculate Overall AI-Readiness Score (AI-R)**
    *   Markdown: `st.markdown()`.
    *   Code: Apply `calculate_ai_r` to all employees. Display `df_employees[['employee_id', 'job_role', 'department', 'vr_score', 'hr_r_score', 'synergy_score', 'current_ai_r_score']].head()` using `st.dataframe()`. Display `df_employees['current_ai_r_score'].mean()` using `st.metric()`.

### Page: "AI-R Report & Skills Gap Analysis"

*   **Markdown Content:**
    *   "Section 16: AI-Readiness Report & Skills Gap Analysis" and introductory text.
*   **Code Stubs:**
    *   `generate_ai_r_report_summary` function. Call this function, display results using `st.dataframe()`.
    *   `plot_skills_gap_heatmap` function. User selects `group_by_column` (e.g., 'job_role', 'department') via `st.selectbox()`, then `st.pyplot()` displays the heatmap.

### Page: "What-If Scenario Engine"

*   **Markdown Content:**
    *   "Section 17: What-If Scenario Engine: Simulating Learning Pathway Impact" and introductory text.
*   **Mathematical Formula:**
    *   `st.latex(r"$$AI-R_{i,t+1} = AI-R_{i,t} + \sum_{p \in P} \Delta_p \cdot Completion_p \cdot Mastery_p$$")`
*   **Code Stub:**
    *   `simulate_pathway_impact` function. User inputs `employee_id`, `pathway_id`, `completion_rate`, `mastery_score` via `st.selectbox()` and `st.slider()`.
    *   A `st.button("Run What-If Simulation")` will trigger the function.
    *   Display `current_ai_r`, `projected_ai_r`, `delta_ai_r` using `st.metric()`.
    *   `plot_current_vs_projected_ai_r` function will be called and displayed using `st.pyplot()`.

### Page: "Multi-Step Pathway Optimization"

*   **Markdown Content:**
    *   "Section 18: Multi-Step Pathway Optimization" and introductory text.
*   **Mathematical Formulae:**
    *   Optimization objective: `st.latex(r"$$\max_{P_1,...,P_K} AI-R(P_1,..., P_K) - \lambda_{\text{cost}} \cdot \sum_{k=1}^K Cost(P_k)$$")`
    *   Constraints:
        `st.latex(r"$$ \sum_{k=1}^K Time(P_k) \leq T_{\text{max}} $$")`
        `st.latex(r"$$ P_k \in P_{\text{feasible}} $$")`
        `st.latex(r"$$ Prerequisites(P_k) \subseteq \{P_1,...,P_{k-1}\} $$")`
*   **Code Stub:**
    *   `optimize_pathway_sequence` function. User inputs `employee_id`, `T_max_hours`, `cost_weight_lambda` via `st.selectbox()` and `st.number_input()`.
    *   A `st.button("Run Optimization")` will trigger the function.
    *   Display `recommended_sequence`, `projected_final_ai_r`, `total_cost`, `total_time_hours`, `ai_r_improvement` from the optimization results using `st.markdown()` and `st.metric()`.
    *   `plot_current_vs_projected_ai_r` function will be called and displayed using `st.pyplot()`.

### Page: "Strategic Recommendations"

*   **Markdown Content:**
    *   "Section 19: Strategic Recommendations & Conclusion" and its detailed insights will be rendered directly using `st.markdown()`. This section will leverage the results and insights from the previous analytical steps to provide actionable advice.

