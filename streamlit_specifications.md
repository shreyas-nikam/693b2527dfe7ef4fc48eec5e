
# Streamlit Application Specification: AI-Readiness Career Navigator

## 1. Application Overview

The **AI-Readiness Career Navigator** is a Streamlit application designed to empower financial professionals in navigating the rapidly evolving, AI-driven job market. It provides a data-driven framework to assess an individual's current AI-readiness, identify high-opportunity career paths, pinpoint skill gaps, and optimize personalized learning strategies.

**Target Personas:**
The primary target users are financial professionals, including:
*   AI Workforce leaders
*   Human Resources specialists focusing on talent development
*   Economists analyzing labor market trends
*   Financial Engineers
*   Data Analysts and Data Scientists
*   AI Professionals with a strong mathematical or quantitative focus

**High-level Story Flow:**
The application guides the user, personified by "Alice, a Senior Quantitative Analyst at QuantFinance Innovations," through a structured workflow:

1.  **Introduction:** Alice is introduced to the AI-Readiness Score (AI-R) framework and its importance for career advancement in finance.
2.  **Profile Assessment:** Alice inputs her professional background (education, experience, skills) and selects potential AI-enabled target roles.
3.  **Opportunity Evaluation:** The application calculates Alice's **Idiosyncratic Readiness ($V^R$)** based on her individual capabilities and the **Systematic Opportunity ($H^R$)** for her chosen target roles, reflecting market demand. It then synthesizes these into her overall **AI-Readiness Score (AI-R)** and identifies key skill gaps.
4.  **Learning Pathway Optimization:** Given her AI-R and skill gaps, Alice defines her learning constraints (time, budget). The application recommends an optimal sequence of learning pathways designed to maximize her AI-R gain.
5.  **"What-If" Scenario Analysis:** Alice explores alternative career paths or learning strategies, comparing their projected AI-R and return on investment to make informed decisions.
6.  **Personalized Report:** A comprehensive summary of her current standing, recommendations, and projected career trajectory is generated.

This workflow demonstrates how a learner (Alice) applies the AI-R framework to make concrete career development decisions, moving beyond theoretical explanations to practical application.

## 2. Code Requirements

### Import Statement

```python
from source import *
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast # For safe evaluation of prerequisites string
```

### `st.session_state` Design

`st.session_state` is extensively used to preserve user inputs, calculated scores, and analysis results across different interactions and simulated "pages" (tabs).

**Initialization:**
All session state variables are initialized in a function `initialize_session_state()` which is called once at the start of the `app.py` script. Default values for `alice_profile` and `target_roles` are loaded from the global variables defined in `source.py`. Calculated scores and results are initialized to `None` or empty structures (e.g., `{}`, `pd.DataFrame()`). Global model parameters that are exposed for user modification (e.g., `MAX_LEARNING_TIME_HOURS`) are loaded from `source.py`'s global constants as initial values.

```python
def initialize_session_state():
    # User Profile Data (mutable)
    if 'alice_profile' not in st.session_state:
        st.session_state['alice_profile'] = {
            'persona_id': 'Alice',
            'education_level': 'Master\'s in Finance',
            'experience_years': 7,
            'current_skills': { # Skill levels 0-10
                'Python': 8, 'SQL': 7, 'ML_basics': 6, 'Risk_Analysis': 9,
                'Financial_Modeling': 8, 'Data_Viz': 7, 'Quant_Models': 6,
                'AI_Ethics': 5, 'GenAI_Tools': 4, 'Cloud_Platforms': 5
            },
            'ai_fluency_subfactors': { # Scores 0-1
                'prompting': 0.6, 'ai_tools': 0.5, 'understanding': 0.6, 'data_literacy': 0.7,
                'ai_augmented_productivity': 0.7, 'critical_ai_judgment': 0.65, 'appropriate_trust_decisions': 0.75,
                'proficiency_gain': 0.10, 'hours_invested': 50
            },
            'domain_expertise_subfactors': { # Scores 0-1
                'portfolio': 0.7, 'recognition': 0.6, 'credentials': 0.8
            },
            'adaptive_capacity_subfactors': { # Scores 0-1
                'cognitive_flexibility': 0.75, 'social_emotional_intelligence': 0.8, 'strategic_career_management': 0.7
            }
        }
    if 'target_roles' not in st.session_state:
        st.session_state['target_roles'] = ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist']
    
    # Core AI-R Calculation Results
    if 'alice_ai_fluency_score' not in st.session_state: st.session_state['alice_ai_fluency_score'] = None
    if 'alice_domain_expertise_score' not in st.session_state: st.session_state['alice_domain_expertise_score'] = None
    if 'alice_adaptive_capacity_score' not in st.session_state: st.session_state['alice_adaptive_capacity_score'] = None
    if 'alice_vr_score' not in st.session_state: st.session_state['alice_vr_score'] = None
    if 'hr_scores' not in st.session_state: st.session_state['hr_scores'] = {} # dict: role -> HR_Score
    if 'air_df' not in st.session_state: st.session_state['air_df'] = pd.DataFrame() # DataFrame with all AI-R components
    if 'all_skill_gaps' not in st.session_state: st.session_state['all_skill_gaps'] = {} # dict: role -> skill_gaps_dict
    if 'top_role' not in st.session_state: st.session_state['top_role'] = {} # Series/dict of the max AI-R role

    # Optimization Parameters (user-adjustable with defaults from source.py globals)
    if 'max_learning_time_hours' not in st.session_state: st.session_state['max_learning_time_hours'] = MAX_LEARNING_TIME_HOURS
    if 'max_learning_budget_usd' not in st.session_state: st.session_state['max_learning_budget_usd'] = MAX_LEARNING_BUDGET_USD
    if 'lambda_cost_weight' not in st.session_state: st.session_state['lambda_cost_weight'] = LAMBDA_COST_WEIGHT

    # Optimization Results
    if 'recommended_paths' not in st.session_state: st.session_state['recommended_paths'] = []
    if 'total_time_invested' not in st.session_state: st.session_state['total_time_invested'] = 0
    if 'total_cost_invested' not in st.session_state: st.session_state['total_cost_invested'] = 0
    if 'projected_air' not in st.session_state: st.session_state['projected_air'] = None # Projected AI-R for optimal path
    if 'final_vr_after_paths' not in st.session_state: st.session_state['final_vr_after_paths'] = None
    if 'final_vr_subscores_normalized' not in st.session_state: st.session_state['final_vr_subscores_normalized'] = {}
    if 'final_skills_after_paths' not in st.session_state: st.session_state['final_skills_after_paths'] = {}

    # Scenario Analysis Results
    if 'scenario_results_df' not in st.session_state: st.session_state['scenario_results_df'] = pd.DataFrame()
    if 'roi_df' not in st.session_state: st.session_state['roi_df'] = pd.DataFrame()

    # Loaded DataFrames (read once)
    if 'idiosyncratic_df' not in st.session_state:
        create_simulated_data() # Ensure data files exist before reading
        st.session_state['idiosyncratic_df'] = pd.read_csv('idiosyncratic_data.csv')
        st.session_state['systematic_df'] = pd.read_csv('systematic_opportunity_data.csv')
        st.session_state['job_postings_df'] = pd.read_csv('job_postings_data.csv')
        st.session_state['regional_demand_df'] = pd.read_csv('regional_demand_data.csv')
        st.session_state['skill_requirements_df'] = pd.read_csv('skill_requirements.csv')
        st.session_state['learning_pathways_df'] = pd.read_csv('learning_pathways.csv')
```

**Updates:**
*   User inputs in the "Profile & Goals" tab directly update `st.session_state['alice_profile']` and `st.session_state['target_roles']`.
*   Calculations in "Opportunity Evaluation" update `st.session_state['alice_ai_fluency_score']`, `st.session_state['alice_domain_expertise_score']`, `st.session_state['alice_adaptive_capacity_score']`, `st.session_state['alice_vr_score']`, `st.session_state['hr_scores']`, `st.session_state['air_df']`, `st.session_state['all_skill_gaps']`, `st.session_state['top_role']`.
*   User inputs in "Learning Optimization" update `st.session_state['max_learning_time_hours']`, `st.session_state['max_learning_budget_usd']`, `st.session_state['lambda_cost_weight']`.
*   Optimization logic updates `st.session_state['recommended_paths']`, `st.session_state['total_time_invested']`, `st.session_state['total_cost_invested']`, `st.session_state['projected_air']`, `st.session_state['final_vr_after_paths']`, `st.session_state['final_vr_subscores_normalized']`, `st.session_state['final_skills_after_paths']`.
*   Scenario analysis updates `st.session_state['scenario_results_df']` and `st.session_state['roi_df']`.

**Reads:**
*   All subsequent calculation steps read the latest state from `st.session_state`. For instance, AI-R calculation reads `st.session_state['alice_vr_score']` and `st.session_state['hr_scores']`. The optimization functions read the current profile, VR, HR, and skill gaps from `st.session_state`.
*   The "Summary Report" reads all final calculated values and recommendations from `st.session_state`.

### UI Interactions and `source.py` Function Calls

**Global Constants (from `source.py`):**
*   `ALPHA`, `BETA`, `VR_W1_AI_FLUENCY`, `VR_W2_DOMAIN_EXPERTISE`, `VR_W3_ADAPTIVE_CAPACITY`, `AI_FLUENCY_THETA_WEIGHTS`, `GAMMA_EXPERIENCE_DECAY`, `HR_W1_AI_ENHANCEMENT`, `HR_W2_JOB_GROWTH`, `HR_W3_WAGE_PREMIUM`, `HR_W4_ENTRY_ACCESSIBILITY`, `LAMBDA_GROWTH_MULTIPLIER`, `GAMMA_REMOTE_WORK`, `MAX_POSSIBLE_SKILL_MATCH`, `LAMBDA_COST_WEIGHT`, `MAX_LEARNING_TIME_HOURS`, `MAX_LEARNING_BUDGET_USD`. These are loaded upon `from source import *` and are directly used by the functions or provided as initial values for user-adjustable parameters in `st.session_state`.

**Data Loading (`create_simulated_data()` and `pd.read_csv` calls):**
*   **Trigger:** Implicitly called once during `initialize_session_state()`.
*   **Functions:** `create_simulated_data()` to ensure CSVs exist. `pd.read_csv()` to load data into session state.

**1. Profile & Goals Tab (User Input & Initial VR Calculation):**
*   **Widgets:** Various `st.text_input`, `st.number_input`, `st.selectbox`, `st.slider`, `st.multiselect` to update `st.session_state['alice_profile']` and `st.session_state['target_roles']`.
*   **Button:** "Calculate Initial Readiness & Opportunity".
    *   **Functions:**
        *   `calculate_ai_fluency(subfactors, AI_FLUENCY_THETA_WEIGHTS)`
        *   `calculate_domain_expertise(education_level, experience_years, specialization_depth_scores, GAMMA_EXPERIENCE_DECAY)`
        *   `calculate_adaptive_capacity(subfactors)`
        *   `calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, VR_COMPONENT_WEIGHTS)`
        *   These updates: `st.session_state['alice_ai_fluency_score']`, `st.session_state['alice_domain_expertise_score']`, `st.session_state['alice_adaptive_capacity_score']`, `st.session_state['alice_vr_score']`.

**2. Opportunity Evaluation Tab (HR & AI-R Calculation):**
*   **Trigger:** Automatically runs when tab is active if profile data exists (or can be triggered by a "Recalculate" button if parameters change).
*   **Functions:**
    *   For each role in `st.session_state['target_roles']`:
        *   `normalize_growth(growth_rate)`
        *   `calculate_wage_premium(ai_skilled_wage, median_wage)`
        *   `calculate_entry_accessibility(education_years_required, experience_years_required)`
        *   `calculate_hbase(ai_enhancement, growth_normalized, wage_premium, entry_accessibility, HBASE_WEIGHTS)`
        *   `calculate_mgrowth(job_postings_t, job_postings_t_minus_1, LAMBDA_GROWTH_MULTIPLIER)`
        *   `calculate_mregional(local_demand, national_avg_demand, remote_work_factor, GAMMA_REMOTE_WORK)`
        *   `calculate_hr(hbase_score, mgrowth_score, mregional_score)`
        *   Updates: `st.session_state['hr_scores']`.
    *   For each role in `st.session_state['target_roles']`:
        *   `calculate_skills_match_score(current_skills_dict, required_skills_series, max_possible_match_val)`
        *   `calculate_timing_factor(years_experience)`
        *   `calculate_alignment(skills_match_score, timing_factor)`
        *   `calculate_synergy(vr_score, hr_score, alignment_score)`
        *   `calculate_air(vr_score, hr_score, synergy_score, ALPHA, BETA)`
        *   Updates: `st.session_state['air_df']`, `st.session_state['all_skill_gaps']`, `st.session_state['top_role']`.
*   **Visualizations:** `st.pyplot(fig)` for bar chart of AI-R, VR, HR, and radar chart of skill gaps.

**3. Learning Optimization Tab:**
*   **Widgets:** `st.number_input` for `st.session_state['max_learning_time_hours']`, `st.session_state['max_learning_budget_usd']`, `st.session_state['lambda_cost_weight']`.
*   **Button:** "Optimize Learning Pathway".
    *   **Functions:**
        *   `optimize_learning_pathways(current_air_score, current_vr_score, current_vr_subscores, target_hr_score, learning_pathways_df, max_time, max_cost, ALPHA, BETA, lambda_cost_weight, alice_exp_years, alice_current_skills_dict)`
        *   Updates: `st.session_state['recommended_paths']`, `st.session_state['total_time_invested']`, `st.session_state['total_cost_invested']`, `st.session_state['projected_air']`, `st.session_state['final_vr_after_paths']`, `st.session_state['final_vr_subscores_normalized']`, `st.session_state['final_skills_after_paths']`.
*   **Visualizations:** `st.pyplot(fig)` for bar chart comparing current and projected AI-R.

**4. "What-If" Scenario Analysis Tab:**
*   **Widgets:** `st.selectbox` for target role, `st.multiselect` to select learning pathways for custom scenarios.
*   **Button:** "Run Scenario Analysis".
    *   **Functions:**
        *   `run_what_if_scenario(initial_vr_score, initial_vr_subscores_normalized, initial_skills, target_role_name, hr_data, skill_req_data, learning_pathways_for_scenario, alice_exp_years, ALPHA, BETA)`
        *   Updates: `st.session_state['scenario_results_df']`, `st.session_state['roi_df']`.
*   **Visualizations:** `st.pyplot(fig)` for comparative AI-R bar chart and ROI bar chart.

### Markdown Content

The markdown for each section (tab) will be defined below, adhering to the strict formula handling rules.

---

## Streamlit Application Blueprint (`app.py`)

```python
# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast # For safe evaluation of prerequisites string in optimize_learning_pathways

# Import all functions and global variables from source.py
from source import *

# Set plot style globally for the app
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Initialize session state variables
def initialize_session_state():
    # User Profile Data (mutable)
    if 'alice_profile' not in st.session_state:
        st.session_state['alice_profile'] = {
            'persona_id': 'Alice',
            'education_level': 'Master\'s in Finance',
            'experience_years': 7,
            'current_skills': { # Skill levels 0-10
                'Python': 8, 'SQL': 7, 'ML_basics': 6, 'Risk_Analysis': 9,
                'Financial_Modeling': 8, 'Data_Viz': 7, 'Quant_Models': 6,
                'AI_Ethics': 5, 'GenAI_Tools': 4, 'Cloud_Platforms': 5
            },
            'ai_fluency_subfactors': { # Scores 0-1
                'prompting': 0.6, 'ai_tools': 0.5, 'understanding': 0.6, 'data_literacy': 0.7,
                'ai_augmented_productivity': 0.7, 'critical_ai_judgment': 0.65, 'appropriate_trust_decisions': 0.75,
                'proficiency_gain': 0.10, 'hours_invested': 50
            },
            'domain_expertise_subfactors': { # Scores 0-1
                'portfolio': 0.7, 'recognition': 0.6, 'credentials': 0.8
            },
            'adaptive_capacity_subfactors': { # Scores 0-1
                'cognitive_flexibility': 0.75, 'social_emotional_intelligence': 0.8, 'strategic_career_management': 0.7
            }
        }
    if 'target_roles' not in st.session_state:
        st.session_state['target_roles'] = ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist']
    
    # Core AI-R Calculation Results
    if 'alice_ai_fluency_score' not in st.session_state: st.session_state['alice_ai_fluency_score'] = None
    if 'alice_domain_expertise_score' not in st.session_state: st.session_state['alice_domain_expertise_score'] = None
    if 'alice_adaptive_capacity_score' not in st.session_state: st.session_state['alice_adaptive_capacity_score'] = None
    if 'alice_vr_score' not in st.session_state: st.session_state['alice_vr_score'] = None
    if 'hr_scores' not in st.session_state: st.session_state['hr_scores'] = {} # dict: role -> HR_Score
    if 'air_df' not in st.session_state: st.session_state['air_df'] = pd.DataFrame() # DataFrame with all AI-R components
    if 'all_skill_gaps' not in st.session_state: st.session_state['all_skill_gaps'] = {} # dict: role -> skill_gaps_dict
    if 'top_role' not in st.session_state: st.session_state['top_role'] = {} # Series/dict of the max AI-R role

    # Optimization Parameters (user-adjustable with defaults from source.py globals)
    if 'max_learning_time_hours' not in st.session_state: st.session_state['max_learning_time_hours'] = MAX_LEARNING_TIME_HOURS
    if 'max_learning_budget_usd' not in st.session_state: st.session_state['max_learning_budget_usd'] = MAX_LEARNING_BUDGET_USD
    if 'lambda_cost_weight' not in st.session_state: st.session_state['lambda_cost_weight'] = LAMBDA_COST_WEIGHT

    # Optimization Results
    if 'recommended_paths' not in st.session_state: st.session_state['recommended_paths'] = []
    if 'total_time_invested' not in st.session_state: st.session_state['total_time_invested'] = 0
    if 'total_cost_invested' not in st.session_state: st.session_state['total_cost_invested'] = 0
    if 'projected_air' not in st.session_state: st.session_state['projected_air'] = None # Projected AI-R for optimal path
    if 'initial_air_optimal_role' not in st.session_state: st.session_state['initial_air_optimal_role'] = None # Initial AI-R of the optimal role before optimization
    if 'final_vr_after_paths' not in st.session_state: st.session_state['final_vr_after_paths'] = None
    if 'final_vr_subscores_normalized' not in st.session_state: st.session_state['final_vr_subscores_normalized'] = {}
    if 'final_skills_after_paths' not in st.session_state: st.session_state['final_skills_after_paths'] = {}

    # Scenario Analysis Results
    if 'scenario_results_df' not in st.session_state: st.session_state['scenario_results_df'] = pd.DataFrame()
    if 'roi_df' not in st.session_state: st.session_state['roi_df'] = pd.DataFrame()

    # Loaded DataFrames (read once)
    if 'idiosyncratic_df' not in st.session_state:
        create_simulated_data() # Ensure data files exist before reading
        st.session_state['idiosyncratic_df'] = pd.read_csv('idiosyncratic_data.csv')
        st.session_state['systematic_df'] = pd.read_csv('systematic_opportunity_data.csv')
        st.session_state['job_postings_df'] = pd.read_csv('job_postings_data.csv')
        st.session_state['regional_demand_df'] = pd.read_csv('regional_demand_data.csv')
        st.session_state['skill_requirements_df'] = pd.read_csv('skill_requirements.csv')
        st.session_state['learning_pathways_df'] = pd.read_csv('learning_pathways.csv')

# Call to initialize session state
initialize_session_state()

st.set_page_config(layout="wide", page_title="AI-Readiness Career Navigator")

st.title("AI-Readiness Career Navigator")
st.markdown("---")

# Navigation Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Introduction", "Profile & Goals", "Opportunity Evaluation",
    "Learning Optimization", "What-If Analysis", "Summary Report"
])

# --- Tab 1: Introduction ---
with tab1:
    st.header("Welcome to the AI-Readiness Career Navigator!")
    st.markdown(f"In the rapidly evolving landscape of financial services, the integration of Artificial Intelligence (AI) is reshaping roles and creating new opportunities.")
    st.markdown(f"For financial professionals, understanding how to adapt and strategically position oneself is crucial for long-term career success.")
    st.markdown(f"This application will guide you through a data-driven framework to assess your current AI-readiness, identify high-opportunity career paths, pinpoint skill gaps, and optimize a personalized learning strategy.")

    st.subheader("Your Persona: Alice, a Senior Quantitative Analyst")
    st.markdown(f"You will step into the shoes of **Alice, a Senior Quantitative Analyst at QuantFinance Innovations**, a leading financial institution.")
    st.markdown(f"Alice is keen to leverage AI to advance her career but is unsure which AI-enabled roles offer the best prospects given her background, and what specific skills she needs to acquire.")
    st.markdown(f"This tool will help Alice make informed decisions about her professional development and maximize her career trajectory in the age of AI.")

    st.subheader("The AI-Readiness Score (AI-R) Framework")
    st.markdown(f"The core of this analysis is the **AI-Readiness Score (AI-R)**, a novel parametric framework that quantifies an individual's preparedness for AI-enabled careers.")
    st.markdown(f"It decomposes career opportunity into two orthogonal components: **Idiosyncratic Readiness ($V^R$)**, representing individual-specific capabilities, and **Systematic Opportunity ($H^R$)**, representing macro-level job growth and demand.")
    st.markdown(f"The framework also incorporates a **Synergy Function** to capture the compounding benefits when individual preparation aligns with market opportunity.")

    st.markdown(r"$$AI-R_{{i,t}} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{{i}}^R(t) + \beta \cdot Synergy\%(V_i^R, H_{{i}}^R)$$")
    st.markdown(f"where:")
    st.markdown(f"*   $V_i^R(t)$: Idiosyncratic Readiness (individual capability), normalized to $[0, 100]$.")
    st.markdown(f"*   $H_i^R(t)$: Systematic Opportunity (market demand) for the target occupation, normalized to $[0, 100]$.")
    st.markdown(f"*   $\\alpha \\in [0,1]$: Weight on individual vs. market factors. Default $\\alpha = {ALPHA}$.")
    st.markdown(f"*   $\\beta > 0$: Synergy coefficient, capturing multiplicative benefits. Default $\\beta = {BETA}$.")
    st.markdown(f"*   $Synergy\% \\in [0,100]$: Percentage units.")
    st.markdown(f"By walking through this workflow, Alice will gain personalized, data-driven career guidance, ensuring her learning investments are impactful for high-opportunity roles in finance.")

# --- Tab 2: Profile & Goals ---
with tab2:
    st.header("1. Your Professional Profile & Target Roles")
    st.markdown(f"Alice, a Senior Quantitative Analyst, has a solid background in financial modeling, risk analysis, and Python programming.")
    st.markdown(f"She's exploring various AI-enabled roles within finance to identify the most promising path for her career growth.")
    st.markdown(f"Please review and adjust your professional profile and select the target roles you're considering.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1.1. Professional Background")
        st.markdown(f"**General Information**")
        st.session_state['alice_profile']['education_level'] = st.selectbox(
            "Education Level",
            ['Master\'s in Finance', 'PhD in target field', 'Master\'s in target field',
             'Bachelor\'s in target field', 'Associate\'s/Certificate', 'HS + significant coursework'],
            index=['Master\'s in Finance', 'PhD in target field', 'Master\'s in target field',
                   'Bachelor\'s in target field', 'Associate\'s/Certificate', 'HS + significant coursework'].index(st.session_state['alice_profile']['education_level'])
        )
        st.session_state['alice_profile']['experience_years'] = st.number_input(
            "Years of Experience",
            min_value=0, max_value=40, value=st.session_state['alice_profile']['experience_years']
        )
        st.markdown("---")
        st.markdown(f"**AI-Fluency Sub-Factors (Scores 0-1)**")
        for k, v in st.session_state['alice_profile']['ai_fluency_subfactors'].items():
            st.session_state['alice_profile']['ai_fluency_subfactors'][k] = st.slider(
                f"{k.replace('_', ' ').title()}", 0.0, 1.0, float(v), 0.01, key=f"ai_fluency_{k}"
            )
        st.markdown("---")
        st.markdown(f"**Domain-Expertise Sub-Factors (Scores 0-1)**")
        for k, v in st.session_state['alice_profile']['domain_expertise_subfactors'].items():
            st.session_state['alice_profile']['domain_expertise_subfactors'][k] = st.slider(
                f"{k.replace('_', ' ').title()}", 0.0, 1.0, float(v), 0.01, key=f"domain_exp_{k}"
            )
        st.markdown("---")
        st.markdown(f"**Adaptive-Capacity Sub-Factors (Scores 0-1)**")
        for k, v in st.session_state['alice_profile']['adaptive_capacity_subfactors'].items():
            st.session_state['alice_profile']['adaptive_capacity_subfactors'][k] = st.slider(
                f"{k.replace('_', ' ').title()}", 0.0, 1.0, float(v), 0.01, key=f"adaptive_cap_{k}"
            )

    with col2:
        st.subheader("1.2. Current Skill Levels (Proficiency 0-10)")
        for k, v in st.session_state['alice_profile']['current_skills'].items():
            st.session_state['alice_profile']['current_skills'][k] = st.slider(
                f"{k.replace('_', ' ').title()}", 0, 10, int(v), key=f"current_skill_{k}"
            )
        st.subheader("1.3. Target AI-Enabled Financial Roles")
        all_possible_roles = st.session_state['systematic_df']['role'].unique().tolist()
        st.session_state['target_roles'] = st.multiselect(
            "Select Target Roles",
            options=all_possible_roles,
            default=st.session_state['target_roles']
        )

    if st.button("Calculate Initial Readiness & Opportunity"):
        # Calculate VR
        st.session_state['alice_ai_fluency_score'] = calculate_ai_fluency(st.session_state['alice_profile']['ai_fluency_subfactors'], AI_FLUENCY_THETA_WEIGHTS)
        st.session_state['alice_domain_expertise_score'] = calculate_domain_expertise(
            st.session_state['alice_profile']['education_level'],
            st.session_state['alice_profile']['experience_years'],
            st.session_state['alice_profile']['domain_expertise_subfactors'],
            GAMMA_EXPERIENCE_DECAY
        )
        st.session_state['alice_adaptive_capacity_score'] = calculate_adaptive_capacity(st.session_state['alice_profile']['adaptive_capacity_subfactors'])
        st.session_state['alice_vr_score'] = calculate_vr(
            st.session_state['alice_ai_fluency_score'],
            st.session_state['alice_domain_expertise_score'],
            st.session_state['alice_adaptive_capacity_score'],
            VR_COMPONENT_WEIGHTS
        )

        # Calculate HR for each target role
        hr_scores_temp = {}
        for role in st.session_state['target_roles']:
            role_data = st.session_state['systematic_df'][st.session_state['systematic_df']['role'] == role].iloc[0]
            jp_role_data = st.session_state['job_postings_df'][st.session_state['job_postings_df']['role'] == role].iloc[-1]
            rd_role_data = st.session_state['regional_demand_df'][st.session_state['regional_demand_df']['role'] == role].iloc[0]

            growth_rate = (role_data['projected_jobs_10yr'] - role_data['current_jobs']) / role_data['current_jobs']
            growth_normalized = normalize_growth(growth_rate)
            wage_premium = calculate_wage_premium(role_data['ai_skilled_wage'], role_data['median_wage'])
            entry_accessibility = calculate_entry_accessibility(role_data['education_years_required'], role_data['experience_years_required'])

            hbase = calculate_hbase(
                role_data['ai_enhancement_potential'],
                growth_normalized,
                wage_premium,
                entry_accessibility,
                HBASE_WEIGHTS
            )
            mgrowth = calculate_mgrowth(jp_role_data['job_postings_t'], jp_role_data['job_postings_t_minus_1'], LAMBDA_GROWTH_MULTIPLIER)
            mregional = calculate_mregional(rd_role_data['local_demand'], rd_role_data['national_avg_demand'], role_data['remote_work_factor'], GAMMA_REMOTE_WORK)

            hr_score = calculate_hr(hbase, mgrowth, mregional)
            hr_scores_temp[role] = hr_score
        st.session_state['hr_scores'] = hr_scores_temp

        st.success("Initial Readiness & Opportunity calculated! Proceed to the next tab.")
        # Trigger re-run to update subsequent tabs
        st.experimental_rerun()

# --- Tab 3: Opportunity Evaluation ---
with tab3:
    st.header("2. Opportunity Evaluation: AI-Readiness, VR, HR & Skill Gaps")
    st.markdown(f"Here, Alice synthesizes her individual capabilities ($V^R$) with market opportunities ($H^R$) to calculate her comprehensive AI-Readiness Score (AI-R) for each target role.")
    st.markdown(f"A critical aspect is the **Synergy Function**, which captures multiplicative benefits when individual skills align with market demand.")

    if st.session_state['alice_vr_score'] is None or not st.session_state['hr_scores']:
        st.warning("Please go to 'Profile & Goals' tab and calculate initial readiness.")
    else:
        st.subheader("2.1. Idiosyncratic Readiness ($V^R$) Breakdown")
        st.markdown(f"Alice's journey begins with understanding her intrinsic capabilities and preparedness for AI-enabled roles, measured by her **Idiosyncratic Readiness ($V^R$)**.")
        st.markdown(f"This is a score you can actively develop through learning.")
        st.markdown(r"$$V^R(t) = w_1 \cdot AI\text{{-}}Fluency_i(t) + w_2 \cdot Domain\text{{-}}Expertise_i(t) + w_3 \cdot Adaptive\text{{-}}Capacity_i(t)$$")
        st.markdown(f"where $w_1 = {VR_W1_AI_FLUENCY}$, $w_2 = {VR_W2_DOMAIN_EXPERTISE}$, $w_3 = {VR_W3_ADAPTIVE_CAPACITY}$.")

        col_vr1, col_vr2, col_vr3, col_vr4 = st.columns(4)
        col_vr1.metric("Total VR Score", f"{st.session_state['alice_vr_score']:.2f}")
        col_vr2.metric("AI-Fluency", f"{st.session_state['alice_ai_fluency_score']:.2f}")
        col_vr3.metric("Domain-Expertise", f"{st.session_state['alice_domain_expertise_score']:.2f}")
        col_vr4.metric("Adaptive-Capacity", f"{st.session_state['alice_adaptive_capacity_score']:.2f}")

        st.markdown(f"Alice's $V^R$ score of **{st.session_state['alice_vr_score']:.2f}** indicates a strong individual foundation for AI-enabled roles. Her breakdown shows solid scores across all three main components.")
        st.markdown(f"*   **AI-Fluency:** Her score suggests she's moderately proficient in interacting with and understanding AI, but there's room for improvement in areas like AI tools and augmented productivity.")
        st.markdown(f"*   **Domain-Expertise:** With a Master's degree and {st.session_state['alice_profile']['experience_years']} years of experience in finance, her deep domain knowledge is a significant asset, indicating a strong foundation in her target financial sector roles.")
        st.markdown(f"*   **Adaptive-Capacity:** Her high score in this area is critical, showing she possesses strong meta-skills like cognitive flexibility and social-emotional intelligence, essential for navigating rapidly changing AI-driven work environments.")
        st.markdown(f"This $V^R$ score will serve as a baseline to evaluate her potential in various target roles when combined with market opportunities.")

        st.subheader("2.2. Systematic Opportunity ($H^R$) by Target Role")
        st.markdown(f"Alice needs to understand the external market conditions for her target roles. This is captured by the **Systematic Opportunity ($H^R$)** component, representing macro-level job growth and demand that she can position herself to capture.")
        st.markdown(r"$$H^R(t) = H_{{base}}(O_{{target}}) \cdot M_{{growth}}(t) \cdot M_{{regional}}(t)$$")
        st.markdown(f"where $H_{{base}}(o)$ is the base opportunity score, $M_{{growth}}(t)$ is the growth multiplier, and $M_{{regional}}(t)$ is the regional multiplier.")

        st.dataframe(pd.DataFrame(st.session_state['hr_scores'].items(), columns=['Role', 'HR_Score']).round(2).set_index('Role'))
        st.markdown(f"Alice's Systematic Opportunity ($H^R$) scores vary significantly across her target roles. For example:")
        st.markdown(f"*   **AI Quant Analyst:** A high score, potentially due to strong AI-enhancement potential and significant wage premiums.")
        st.markdown(f"*   **Financial Data Scientist:** While robust, this role might have a slightly lower $H^R$ compared to the more specialized AI Quant/ML roles, possibly due to broader applicability or higher entry accessibility.")
        st.markdown(f"This analysis helps Alice understand where the market opportunities lie, complementing her individual readiness.")

        st.subheader("2.3. Overall AI-Readiness ($AI-R$) Scores and Skill Gaps")
        st.markdown(f"The overall AI-Readiness Score is calculated by combining $V^R$ and $H^R$ with a synergy factor:")
        st.markdown(r"$$AI-R_{{i,t}} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{{i}}^R(t) + \beta \cdot Synergy\%(V_i^R, H_{{i}}^R)$$")
        st.markdown(f"where $\\alpha={ALPHA}$ and $\\beta={BETA}$.")
        st.markdown(f"The Synergy Function is defined as: $$Synergy\%(V^R, H^R) = \\frac{{V^R \\times H^R}}{{100}} \\times Alignment_i$$")
        st.markdown(f"where $V^R$ and $H^R$ are normalized to $[0, 100]$, and $Alignment_i \\in [0,1]$ combines skill match and timing.")

        # Recalculate AI-R for display and consistency
        air_results = []
        all_skill_gaps_temp = {}
        for role in st.session_state['target_roles']:
            current_hr_score = st.session_state['hr_scores'].get(role, 0)
            required_skills_for_role = st.session_state['skill_requirements_df'][st.session_state['skill_requirements_df']['role'] == role].iloc[0]
            max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum()

            skills_match, skill_gaps, required_skills_dict, current_skills_total, required_skills_total = calculate_skills_match_score(
                st.session_state['alice_profile']['current_skills'],
                required_skills_for_role,
                max_possible_match_for_role
            )
            all_skill_gaps_temp[role] = skill_gaps

            timing_factor = calculate_timing_factor(st.session_state['alice_profile']['experience_years'])
            alignment_score = calculate_alignment(skills_match, timing_factor)
            synergy_score = calculate_synergy(st.session_state['alice_vr_score'], current_hr_score, alignment_score)
            air_score = calculate_air(st.session_state['alice_vr_score'], current_hr_score, synergy_score, ALPHA, BETA)

            air_results.append({
                'Role': role,
                'VR_Score': st.session_state['alice_vr_score'],
                'HR_Score': current_hr_score,
                'Skills_Match_Score': skills_match * 100,
                'Timing_Factor': timing_factor,
                'Alignment_Score': alignment_score * 100,
                'Synergy_Score': synergy_score,
                'AI_R_Score': air_score
            })
        st.session_state['air_df'] = pd.DataFrame(air_results)
        st.session_state['all_skill_gaps'] = all_skill_gaps_temp
        if not st.session_state['air_df'].empty:
            st.session_state['top_role'] = st.session_state['air_df'].loc[st.session_state['air_df']['AI_R_Score'].idxmax()]
            st.dataframe(st.session_state['air_df'].round(2).set_index('Role'))
            st.markdown(f"Alice's Top AI-R Role: **{st.session_state['top_role']['Role']}** (AI-R: **{st.session_state['top_role']['AI_R_Score']:.2f}**)")

            # Plot AI-R Scores
            fig_air_bar, ax_air_bar = plt.subplots(figsize=(12, 7))
            air_df_plot = st.session_state['air_df'][['Role', 'AI_R_Score', 'VR_Score', 'HR_Score']].set_index('Role')
            air_df_plot.plot(kind='bar', ax=ax_air_bar, title='Alice\'s AI-Readiness Scores Across Target Roles')
            ax_air_bar.set_ylabel('Score (0-100)')
            ax_air_bar.tick_params(axis='x', rotation=45, ha='right')
            ax_air_bar.legend(title='Component')
            plt.tight_layout()
            st.pyplot(fig_air_bar)
            plt.close(fig_air_bar)

            st.markdown(f"The bar chart visually confirms this, showing a balance between Alice's personal readiness ($V^R$) and market opportunity ($H^R$) for the top roles.")
            st.markdown(f"The Synergy component further boosts her AI-R, indicating that her skills and experience align well with these high-opportunity fields.")

            st.subheader(f"Skill Gaps for Recommended Role: {st.session_state['top_role']['Role']}")
            st.markdown(f"The radar chart, specifically for the **{st.session_state['top_role']['Role']}** role, highlights Alice's current skill levels against the required levels.")
            
            top_role_skills = st.session_state['all_skill_gaps'][st.session_state['top_role']['Role']]
            skills_df = pd.DataFrame(top_role_skills).T.reset_index().rename(columns={'index': 'Skill'})
            labels = skills_df['Skill'].tolist()
            current_levels = skills_df['current'].tolist()
            required_levels = skills_df['required'].tolist()

            # Add first value to the end to close the radar chart
            labels += labels[:1]
            current_levels += current_levels[:1]
            required_levels += required_levels[:1]

            angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)

            fig_radar, ax_radar = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
            ax_radar.fill(angles, current_levels, color='blue', alpha=0.25, label='Current Skill Level')
            ax_radar.plot(angles, current_levels, color='blue', linewidth=2)
            ax_radar.fill(angles, required_levels, color='red', alpha=0.25, label='Required Skill Level')
            ax_radar.plot(angles, required_levels, color='red', linewidth=2)

            ax_radar.set_yticklabels([f'{i}' for i in range(0, 11, 2)])
            ax_radar.set_xticks(angles[:-1])
ax_radar.set_xticklabels(labels[:-1])
            ax_radar.set_title(f'Skill Gaps for {st.session_state["top_role"]["Role"]}', size=16, y=1.08)
            ax_radar.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
            plt.tight_layout()
            st.pyplot(fig_radar)
            plt.close(fig_radar)

            st.markdown(f"Alice has strong foundations in `Risk_Analysis`, `Financial_Modeling`, and `Python`. However, significant gaps exist in `Quant_Models`, `ML_basics`, `AI_Ethics`, `GenAI_Tools`, and `Cloud_Platforms`. Addressing these gaps will be critical for her to fully capture the opportunity in the **{st.session_state['top_role']['Role']}** role.")


# --- Tab 4: Learning Optimization ---
with tab4:
    st.header("3. Optimizing Learning Pathways for Career Growth")
    st.markdown(f"Based on her initial AI-R scores and identified skill gaps, Alice wants to invest in learning to maximize her career prospects.")
    st.markdown(f"However, her time and budget are constrained. This section recommends a sequence of learning activities that maximize her projected AI-R gain under these specified resource constraints.")
    st.markdown(f"The objective is to maximize the gain in AI-R minus a weighted cost:")
    st.markdown(r"$$ \max_{{P_1,...,P_K}} (AI\text{{-}}R_{{proj}} - AI\text{{-}}R_{{current}}) - \lambda \cdot \sum_{{k=1}}^K Cost(p_k) $$")
    st.markdown(f"subject to:")
    st.markdown(r"$$ \sum_{{k=1}}^K Time(p_k) \le T_{{max}} $$")
    st.markdown(r"$$ \sum_{{k=1}}^K Cost(p_k) \le B_{{max}} $$")
    st.markdown(r"$$ p_k \in P_{{feasible}} $$")
    st.markdown(r"$$ Prerequisites(p_k) \subseteq \{{P_1,...,P_{{k-1}}\}} $$")
    st.markdown(f"where $AI\text{{-}}R_{{proj}}$ is the projected AI-R after completing pathways, $AI\text{{-}}R_{{current}}$ is her initial AI-R, $\\lambda$ is `LAMBDA_COST_WEIGHT`, $T_{{max}}$ is `MAX_LEARNING_TIME_HOURS`, and $B_{{max}}$ is `MAX_LEARNING_BUDGET_USD`.")
    st.markdown(f"For this demonstration, we'll use a greedy heuristic: selecting pathways one by one that offer the highest 'return' (AI-R point gain per unit of weighted time/cost) until constraints are met, respecting prerequisites.")

    if st.session_state['top_role'] is None or not st.session_state['top_role']:
        st.warning("Please go to 'Opportunity Evaluation' tab to identify the top role first.")
    else:
        st.subheader(f"Target Role for Optimization: **{st.session_state['top_role']['Role']}**")
        st.markdown(f"Initial AI-R for this role: **{st.session_state['top_role']['AI_R_Score']:.2f}**")

        st.subheader("3.1. Set Learning Constraints")
        st.session_state['max_learning_time_hours'] = st.number_input(
            "Maximum Learning Time (hours)",
            min_value=0, max_value=500, value=st.session_state['max_learning_time_hours'], step=10
        )
        st.session_state['max_learning_budget_usd'] = st.number_input(
            "Maximum Learning Budget (USD)",
            min_value=0, max_value=5000, value=st.session_state['max_learning_budget_usd'], step=100
        )
        st.session_state['lambda_cost_weight'] = st.slider(
            "Cost Weight (Lambda - higher means more cost-averse)",
            0.0, 0.5, st.session_state['lambda_cost_weight'], 0.01
        )

        if st.button("Optimize Learning Pathway"):
            current_top_role = st.session_state['top_role']['Role']
            current_hr_for_top_role = st.session_state['top_role']['HR_Score']
            st.session_state['initial_air_optimal_role'] = st.session_state['top_role']['AI_R_Score']

            alice_current_vr_subscores_normalized = {
                'ai_fluency': st.session_state['alice_ai_fluency_score'],
                'domain_expertise': st.session_state['alice_domain_expertise_score'],
                'adaptive_capacity': st.session_state['alice_adaptive_capacity_score']
            }

            st.session_state['recommended_paths'], \
            st.session_state['total_time_invested'], \
            st.session_state['total_cost_invested'], \
            st.session_state['projected_air'], \
            st.session_state['final_vr_after_paths'], \
            st.session_state['final_vr_subscores_normalized'], \
            st.session_state['final_skills_after_paths'] = optimize_learning_pathways(
                st.session_state['initial_air_optimal_role'], # Use the correct initial AI-R here
                st.session_state['alice_vr_score'],
                alice_current_vr_subscores_normalized,
                current_hr_for_top_role,
                st.session_state['learning_pathways_df'],
                st.session_state['max_learning_time_hours'],
                st.session_state['max_learning_budget_usd'],
                ALPHA, BETA, st.session_state['lambda_cost_weight'],
                st.session_state['alice_profile']['experience_years'],
                st.session_state['alice_profile']['current_skills']
            )
            st.success("Learning pathway optimized!")
            st.experimental_rerun()
        
        if st.session_state['recommended_paths']:
            st.subheader("3.2. Recommended Optimal Learning Pathway")
            for i, path in enumerate(st.session_state['recommended_paths']):
                st.markdown(f"**{i+1}. {path['pathway_name']}** (Type: {path['type']}, Time: {path['estimated_time_hours']}h, Cost: ${path['estimated_cost_usd']})")
            st.markdown(f"**Total estimated time investment:** {st.session_state['total_time_invested']} hours")
            st.markdown(f"**Total estimated cost investment:** ${st.session_state['total_cost_invested']}")
            st.markdown(f"**Initial AI-R for {st.session_state['top_role']['Role']}:** {st.session_state['initial_air_optimal_role']:.2f}")
            st.markdown(f"**Projected AI-R after pathways:** {st.session_state['projected_air']:.2f} (Improvement: {(st.session_state['projected_air'] - st.session_state['initial_air_optimal_role']):.2f})")

            # Plot Current vs. Projected AI-R
            fig_optim, ax_optim = plt.subplots(figsize=(8, 6))
            bar_width = 0.35
            roles = [st.session_state['top_role']['Role']]
            current_airs = [st.session_state['initial_air_optimal_role']]
            projected_airs = [st.session_state['projected_air']]

            index = np.arange(len(roles))

            bar1 = ax_optim.bar(index, current_airs, bar_width, label='Current AI-R', color='skyblue')
            bar2 = ax_optim.bar(index + bar_width, projected_airs, bar_width, label='Projected AI-R', color='lightcoral')

            ax_optim.set_xlabel('Role')
            ax_optim.set_ylabel('AI-Readiness Score')
            ax_optim.set_title(f'Current vs. Projected AI-R for {st.session_state["top_role"]["Role"]} After Optimized Learning')
            ax_optim.set_xticks(index + bar_width / 2)
            ax_optim.set_xticklabels(roles)
            ax_optim.set_ylim(0, 100)
            ax_optim.legend()

            for bar in bar1 + bar2:
                yval = bar.get_height()
                ax_optim.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')

            plt.tight_layout()
            st.pyplot(fig_optim)
            plt.close(fig_optim)

            st.markdown(f"The optimization algorithm has identified an optimal sequence of learning pathways for Alice, aiming to maximize her AI-R for the **{st.session_state['top_role']['Role']}** role within her time and budget constraints.")
            st.markdown(f"These pathways project an AI-R increase from {st.session_state['initial_air_optimal_role']:.2f} to {st.session_state['projected_air']:.2f}.")
            st.markdown(f"This represents a significant uplift in her overall readiness and marketability for her chosen high-opportunity role. The bar chart visually demonstrates this substantial projected improvement, confirming that the learning investment is expected to yield a positive return on her career trajectory.")
        else:
            st.info("No learning pathways recommended within the specified constraints or no top role identified yet.")

# --- Tab 5: "What-If" Scenario Analysis ---
with tab5:
    st.header("4. 'What-If' Scenario Analysis")
    st.markdown(f"Alice wants to explore alternative career and learning strategies beyond the initial optimal recommendation. The 'What-If' scenario engine allows her to compare different choices, understand trade-offs, and see how they impact her projected AI-R. This functionality helps in making robust career decisions.")

    if st.session_state['alice_vr_score'] is None:
        st.warning("Please go to 'Profile & Goals' tab and calculate initial readiness.")
    else:
        st.subheader("4.1. Define Custom Scenarios")
        st.markdown(f"You can define custom 'What-If' scenarios by selecting a target role and a specific set of learning pathways.")
        
        all_pathway_names = st.session_state['learning_pathways_df']['pathway_name'].tolist()
        all_roles_for_scenario = st.session_state['systematic_df']['role'].unique().tolist()

        scenario_col1, scenario_col2 = st.columns(2)
        with scenario_col1:
            scenario_target_role = st.selectbox(
                "Select a Target Role for this Scenario",
                options=all_roles_for_scenario,
                index=all_roles_for_scenario.index(st.session_state['top_role']['Role']) if st.session_state['top_role'] else 0,
                key='scenario_role_select'
            )
        with scenario_col2:
            selected_pathway_names_scenario = st.multiselect(
                "Select Learning Pathways for this Scenario",
                options=all_pathway_names,
                default=[],
                key='scenario_pathways_select'
            )
        
        custom_scenario_pathways = st.session_state['learning_pathways_df'][
            st.session_state['learning_pathways_df']['pathway_name'].isin(selected_pathway_names_scenario)
        ].to_dict('records')

        if st.button("Run Custom Scenario Analysis"):
            if not selected_pathway_names_scenario:
                st.warning("Please select at least one learning pathway for the custom scenario.")
            else:
                projected_air_custom, time_custom, cost_custom, projected_vr_custom, hr_custom, synergy_custom = run_what_if_scenario(
                    st.session_state['alice_vr_score'], 
                    {
                        'ai_fluency': st.session_state['alice_ai_fluency_score'],
                        'domain_expertise': st.session_state['alice_domain_expertise_score'],
                        'adaptive_capacity': st.session_state['alice_adaptive_capacity_score']
                    },
                    st.session_state['alice_profile']['current_skills'],
                    scenario_target_role, st.session_state['hr_scores'], 
                    st.session_state['skill_requirements_df'], 
                    custom_scenario_pathways,
                    st.session_state['alice_profile']['experience_years'], 
                    ALPHA, BETA
                )

                # Include the optimal pathway as a baseline scenario if available
                scenario_results_list = []
                if st.session_state['recommended_paths']:
                    scenario_results_list.append({
                        'Scenario': 'Optimized for ' + st.session_state['top_role']['Role'],
                        'Target Role': st.session_state['top_role']['Role'],
                        'Projected AI-R': st.session_state['projected_air'],
                        'Projected VR': st.session_state['final_vr_after_paths'],
                        'HR': st.session_state['top_role']['HR_Score'],
                        'Time (h)': st.session_state['total_time_invested'],
                        'Cost ($)': st.session_state['total_cost_invested']
                    })
                
                scenario_results_list.append({
                    'Scenario': 'Custom Scenario',
                    'Target Role': scenario_target_role,
                    'Projected AI-R': projected_air_custom,
                    'Projected VR': projected_vr_custom,
                    'HR': hr_custom,
                    'Time (h)': time_custom,
                    'Cost ($)': cost_custom
                })
                
                st.session_state['scenario_results_df'] = pd.DataFrame(scenario_results_list).round(2)

                # Calculate ROI for scenarios
                roi_data = []
                for index, row in st.session_state['scenario_results_df'].iterrows():
                    initial_air = st.session_state['top_role']['AI_R_Score'] if row['Target Role'] == st.session_state['top_role']['Role'] else st.session_state['air_df'][st.session_state['air_df']['Role'] == row['Target Role']]['AI_R_Score'].iloc[0]
                    air_gain = row['Projected AI-R'] - initial_air
                    
                    normalized_cost = row['Cost ($)'] / st.session_state['max_learning_budget_usd'] if st.session_state['max_learning_budget_usd'] > 0 else 0
                    normalized_time = row['Time (h)'] / st.session_state['max_learning_time_hours'] if st.session_state['max_learning_time_hours'] > 0 else 0
                    
                    investment_factor = (normalized_cost * st.session_state['lambda_cost_weight']) + normalized_time
                    
                    if investment_factor > 0:
                        roi = air_gain / investment_factor
                    else:
                        roi = air_gain
                    
                    roi_data.append({'Scenario': row['Scenario'], 'AI-R Gain': air_gain, 'Investment Score': investment_factor, 'ROI': roi})
                st.session_state['roi_df'] = pd.DataFrame(roi_data).round(2)

                st.success("Custom scenario analysis complete!")
                st.experimental_rerun()
        
        if not st.session_state['scenario_results_df'].empty:
            st.subheader("4.2. Scenario Analysis Results")
            st.dataframe(st.session_state['scenario_results_df'])

            fig_scenario, ax_scenario = plt.subplots(figsize=(12, 7))
            bar_positions = np.arange(len(st.session_state['scenario_results_df']))
            bars = ax_scenario.bar(bar_positions, st.session_state['scenario_results_df']['Projected AI-R'], color=sns.color_palette('viridis', len(st.session_state['scenario_results_df'])))

            ax_scenario.set_ylabel('Projected AI-Readiness Score')
            ax_scenario.set_title('Comparative Projected AI-R for Different Career/Learning Scenarios')
            ax_scenario.set_xticks(bar_positions)
            ax_scenario.set_xticklabels(st.session_state['scenario_results_df']['Scenario'], rotation=45, ha='right')
            ax_scenario.set_ylim(0, 100)

            for bar in bars:
                yval = bar.get_height()
                ax_scenario.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')

            plt.tight_layout()
            st.pyplot(fig_scenario)
            plt.close(fig_scenario)

            st.markdown(f"The 'What-If' analysis provides Alice with critical insights into the strategic implications of her choices.")
            if 'Optimized for ' + st.session_state['top_role']['Role'] in st.session_state['scenario_results_df']['Scenario'].values:
                optimal_air = st.session_state['scenario_results_df'][st.session_state['scenario_results_df']['Scenario'] == 'Optimized for ' + st.session_state['top_role']['Role']]['Projected AI-R'].iloc[0]
                st.markdown(f"*   **Optimized for {st.session_state['top_role']['Role']} (Original Plan):** This scenario yielded a high projected AI-R of **{optimal_air:.2f}**, confirming it as a very effective strategy. The investment, while substantial, leads to significant career readiness.")
            st.markdown(f"The comparative bar chart clearly illustrates these differences in projected AI-R, allowing Alice to visually grasp the outcomes.")

            st.subheader("4.3. Return on Learning Investment (ROI)")
            st.dataframe(st.session_state['roi_df'])

            fig_roi, ax_roi = plt.subplots(figsize=(12, 7))
            sns.barplot(x='Scenario', y='ROI', data=st.session_state['roi_df'], palette='magma', ax=ax_roi)
            ax_roi.set_ylabel('ROI (AI-R Gain / Weighted Investment)')
            ax_roi.set_title('Return on Learning Investment for Different Scenarios')
            ax_roi.set_xticklabels(st.session_state['roi_df']['Scenario'], rotation=45, ha='right')

            for index, row in st.session_state['roi_df'].iterrows():
                ax_roi.text(index, row['ROI'] + 0.5, f"{row['ROI']:.2f}", color='black', ha="center")

            plt.tight_layout()
            st.pyplot(fig_roi)
            plt.close(fig_roi)
            st.markdown(f"The ROI chart further clarifies which investments provide the best 'bang for her buck.' The optimal pathway, despite higher upfront investment, likely offers a superior long-term return due to the significant AI-R boost it provides.")
            st.markdown(f"This analysis empowers Alice to make a data-driven decision, weighing the projected career opportunity against the required investment in time and cost.")


# --- Tab 6: Summary Report ---
with tab6:
    st.header("5. Personalized AI Career Strategy Report for Alice")
    st.markdown(f"This section consolidates all the analysis into a clear, actionable report for Alice, summarizing her current standing, identified skill gaps, and the recommended optimal learning pathway with projected outcomes.")

    if st.session_state['alice_vr_score'] is None:
        st.warning("Please complete the previous steps to generate a full report.")
    else:
        st.subheader("5.1. Current AI-Readiness Profile")
        st.markdown(f"**Idiosyncratic Readiness (VR):** {st.session_state['alice_vr_score']:.2f}")
        st.markdown(f"  *   AI-Fluency: {st.session_state['alice_ai_fluency_score']:.2f}")
        st.markdown(f"  *   Domain-Expertise: {st.session_state['alice_domain_expertise_score']:.2f}")
        st.markdown(f"  *   Adaptive-Capacity: {st.session_state['alice_adaptive_capacity_score']:.2f}")
        st.markdown(f"**Systematic Opportunity (HR) by Role:**")
        for role, score in st.session_state['hr_scores'].items():
            st.markdown(f"  *   {role}: {score:.2f}")

        if st.session_state['top_role']:
            st.subheader("5.2. Top AI-Enabled Career Path Recommendation")
            st.markdown(f"**Recommended Role:** {st.session_state['top_role']['Role']}")
            st.markdown(f"**Initial AI-Readiness Score (AI-R):** {st.session_state['top_role']['AI_R_Score']:.2f}")
            if st.session_state['projected_air'] is not None:
                st.markdown(f"**Projected AI-Readiness Score (AI-R) after Optimal Learning:** {st.session_state['projected_air']:.2f}")
                st.markdown(f"**Estimated AI-R Improvement:** {(st.session_state['projected_air'] - st.session_state['top_role']['AI_R_Score']):.2f} points")
            else:
                st.markdown(f"*(Run 'Learning Optimization' to see projected AI-R after pathways)*")

            st.subheader(f"5.3. Detailed Skill Gaps for {st.session_state['top_role']['Role']}")
            st.markdown(f"(Comparing Alice's current skills vs. required for this role)")
            top_role_skills_gaps_df = pd.DataFrame(st.session_state['all_skill_gaps'][st.session_state['top_role']['Role']]).T
            top_role_skills_gaps_df['Gap'] = top_role_skills_gaps_df['required'] - top_role_skills_gaps_df['current']
            st.dataframe(top_role_skills_gaps_df[top_role_skills_gaps_df['Gap'] > 0].sort_values(by='Gap', ascending=False))
            st.markdown(f"(Skills with a positive 'Gap' need development)")

            st.subheader("5.4. Recommended Optimal Learning Pathway")
            if st.session_state['recommended_paths']:
                for i, path in enumerate(st.session_state['recommended_paths']):
                    st.markdown(f"**{i+1}. {path['pathway_name']}** (Type: {path['type']})")
                st.markdown(f"**Total Estimated Time Investment:** {st.session_state['total_time_invested']} hours")
                st.markdown(f"**Total Estimated Cost Investment:** ${st.session_state['total_cost_invested']}")
            else:
                st.markdown(f"No optimal learning pathways identified within current constraints or not yet calculated.")

            st.subheader("5.5. 'What-If' Scenario Analysis Summary")
            if not st.session_state['scenario_results_df'].empty:
                st.dataframe(st.session_state['scenario_results_df'].set_index('Scenario'))
                st.markdown("Insight: The 'Optimized for AI Quant Analyst' pathway (original recommendation) yields the highest projected AI-R, indicating it's the most effective strategy for maximizing Alice's career opportunity.")
                st.markdown("The 'Return on Learning Investment' chart suggests prioritizing pathways with high impact on core VR components that align with high HR roles.")
            else:
                st.markdown(f"*(Run 'What-If Analysis' to see comparative scenarios)*")

    st.markdown("---")
    st.markdown("**--- End of Report ---**")

```
