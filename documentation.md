id: 693b2527dfe7ef4fc48eec5e_documentation
summary: AI Readiness score Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: AI-Readiness Career Navigator

## 1. Introduction to the AI-Readiness Career Navigator
Duration: 0:05
<aside class="positive">
This step provides essential context for the application. Understanding the problem it solves and its core framework will help you grasp the subsequent technical details more effectively.
</aside>

In the rapidly evolving landscape of financial services, the integration of Artificial Intelligence (AI) is reshaping traditional roles and creating unprecedented new opportunities. For financial professionals, understanding how to adapt, acquire new skills, and strategically position oneself is crucial for long-term career success.

The **QuLab: AI-Readiness Career Navigator** is a cutting-edge Streamlit application designed to guide finance professionals through this complex transition. It offers a data-driven framework to:
1.  **Assess current AI-readiness:** Understand an individual's existing capabilities.
2.  **Identify high-opportunity career paths:** Pinpoint AI-enabled roles with the best market prospects.
3.  **Pinpoint skill gaps:** Highlight specific areas for development.
4.  **Optimize a personalized learning strategy:** Recommend learning pathways to maximize career trajectory.

### Your Persona: Alice, a Senior Quantitative Analyst
Throughout this codelab, you will step into the shoes of **Alice, a Senior Quantitative Analyst at QuantFinance Innovations**. Alice has a strong background in traditional finance but is keen to leverage AI to advance her career. She needs guidance on which AI-enabled roles offer the best prospects given her background and what specific skills she needs to acquire. This tool will help Alice (and by extension, you) make informed decisions about professional development.

### The AI-Readiness Score (AI-R) Framework
The core of this application's analysis is the **AI-Readiness Score (AI-R)**, a novel parametric framework that quantifies an individual's preparedness for AI-enabled careers. It decomposes career opportunity into two orthogonal components:

*   **Idiosyncratic Readiness ($V^R$):** This represents individual-specific capabilities, including AI-Fluency, Domain-Expertise, and Adaptive-Capacity. This is the component an individual can actively develop.
*   **Systematic Opportunity ($H^R$):** This represents macro-level job growth, demand, and wage premiums for a target role. This is the market component an individual aims to capture.

The framework also incorporates a **Synergy Function** to capture the compounding benefits when an individual's preparation aligns well with market opportunity.

The comprehensive AI-R formula is defined as:
$$AI-R_{{i,t}} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{{i}}^R(t) + \beta \cdot Synergy\%(V_i^R, H_{{i}}^R)$$
where:
*   $V_i^R(t)$ is Idiosyncratic Readiness (individual capability), normalized to $[0, 100]$.
*   $H_i^R(t)$ is Systematic Opportunity (market demand) for the target occupation, normalized to $[0, 100]$.
*   $\alpha \in [0,1]$ is the weight on individual vs. market factors. Default $\alpha = 0.5$.
*   $\beta > 0$ is the synergy coefficient, capturing multiplicative benefits. Default $\beta = 0.2$.
*   $Synergy\% \in [0,100]$ is in percentage units, calculated based on how well an individual's skills align with the target role and market timing.

### Application Architecture Overview
The application follows a modular architecture:
1.  **Streamlit UI (App.py):** Handles user interaction, displays inputs, and renders outputs (text, tables, charts). It manages the application's state using `st.session_state`.
2.  **Core Logic (`source.py`):** Contains all the mathematical models, calculation functions, and data generation/loading logic. This separation ensures clean, maintainable code.
3.  **Data Layer:** Utilizes CSV files (simulated for this codelab) that store individual profile details, market data for roles, skill requirements, and learning pathways.

Here's a conceptual diagram:

```
++      ++      ++
|                     |      |                     |      |                     |
|  Streamlit UI       |      |  Core Logic         |      |  Data Layer         |
|  (App.py)           |      |  (source.py)        |      |  (CSV Files)        |
|                     |      |                     |      |                     |
| - Input widgets     |<-->- Calculation Fns   |<-->- Profile Data        |
| - Output display    |      | - Data simulation   |      | - Market Data       |
| - st.session_state  |      | - Optimization Algo |      | - Skills/Pathways   |
|                     |      |                     |      |                     |
++      ++      ++
       ^       |
       |       V
       +-+
       User Interaction
```

## 2. Setting Up Your Development Environment
Duration: 0:10

To run the QuLab application, you'll need Python and a few libraries.

### Prerequisites
*   **Python 3.8+**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
*   **pip**: Python's package installer, usually comes with Python.

### 2.1. Clone the Repository (Simulated)
For a real application, you would clone the Git repository. For this codelab, assume the application files `app.py` and `source.py` are in a directory named `qu_lab_app`.

```bash
# In a real scenario, you'd clone:
# git clone <repository-url>
# cd <repository-name>

# For this codelab, imagine you have:
# /qu_lab_app/app.py
# /qu_lab_app/source.py
# (and the data files will be generated by source.py)
```

### 2.2. Create a Virtual Environment
It's best practice to use a virtual environment to manage dependencies for your project.

```bash
python -m venv venv
```

### 2.3. Activate the Virtual Environment
*   **On Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **On macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 2.4. Install Dependencies
Install the required Python packages using pip.

```bash
pip install streamlit pandas numpy matplotlib seaborn
```

### 2.5. Mock `source.py` for Codelab Explanation
The core logic and constants are defined in `source.py`. Since this file isn't provided directly, we'll outline its expected content here. In a real project, this would be a separate Python file (`source.py`) located in the same directory as `app.py`.

```python
# Constants used throughout the application
MAX_LEARNING_TIME_HOURS = 100
MAX_LEARNING_BUDGET_USD = 1000
LAMBDA_COST_WEIGHT = 0.05
ALPHA = 0.5
BETA = 0.2
AI_FLUENCY_THETA_WEIGHTS = {'prompting': 0.2, 'ai_tools': 0.15, 'understanding': 0.2, 'data_literacy': 0.15, 'ai_augmented_productivity': 0.1, 'critical_ai_judgment': 0.1, 'appropriate_trust_decisions': 0.1}
GAMMA_EXPERIENCE_DECAY = 0.02
VR_COMPONENT_WEIGHTS = {'ai_fluency': 0.35, 'domain_expertise': 0.4, 'adaptive_capacity': 0.25}
VR_W1_AI_FLUENCY = VR_COMPONENT_WEIGHTS['ai_fluency']
VR_W2_DOMAIN_EXPERTISE = VR_COMPONENT_WEIGHTS['domain_expertise']
VR_W3_ADAPTIVE_CAPACITY = VR_COMPONENT_WEIGHTS['adaptive_capacity']
HBASE_WEIGHTS = {'ai_enhancement_potential': 0.3, 'growth_normalized': 0.3, 'wage_premium': 0.25, 'entry_accessibility': 0.15}
LAMBDA_GROWTH_MULTIPLIER = 0.1
GAMMA_REMOTE_WORK = 0.05


import pandas as pd
import numpy as np
import ast # For parsing list/dict strings from CSV

def create_simulated_data():
    """Simulates creation of dataframes and saves them to CSV."""
    # Minimal data for idiosyncratic_data.csv
    pd.DataFrame({'id': [1], 'value': [100]}).to_csv('idiosyncratic_data.csv', index=False)
    
    # Minimal data for systematic_opportunity_data.csv
    systematic_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'ai_enhancement_potential': [0.8, 0.9, 0.7, 0.85],
        'projected_jobs_10yr': [1200, 1500, 1100, 1300],
        'current_jobs': [1000, 1000, 1000, 1000],
        'ai_skilled_wage': [180000, 200000, 160000, 170000],
        'median_wage': [130000, 150000, 120000, 140000],
        'education_years_required': [18, 18, 17, 17],
        'experience_years_required': [5, 6, 4, 5],
        'remote_work_factor': [0.6, 0.7, 0.5, 0.65]
    }
    pd.DataFrame(systematic_data).to_csv('systematic_opportunity_data.csv', index=False)
    
    # Minimal data for job_postings_data.csv
    job_postings_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'job_postings_t': [100, 120, 90, 110],
        'job_postings_t_minus_1': [90, 100, 80, 100]
    }
    pd.DataFrame(job_postings_data).to_csv('job_postings_data.csv', index=False)

    # Minimal data for regional_demand_data.csv
    regional_demand_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'local_demand': [70, 80, 60, 75],
        'national_avg_demand': [60, 70, 50, 65]
    }
    pd.DataFrame(regional_demand_data).to_csv('regional_demand_data.csv', index=False)

    # Minimal data for skill_requirements.csv
    skill_req_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'Python': [9, 10, 8, 9], 'SQL': [7, 8, 7, 8], 'ML_basics': [8, 9, 7, 8],
        'Risk_Analysis': [9, 7, 10, 6], 'Financial_Modeling': [9, 6, 8, 7], 'Data_Viz': [7, 8, 7, 8],
        'Quant_Models': [8, 9, 7, 8], 'AI_Ethics': [6, 7, 8, 7], 'GenAI_Tools': [6, 8, 6, 7],
        'Cloud_Platforms': [7, 9, 6, 8]
    }
    pd.DataFrame(skill_req_data).to_csv('skill_requirements.csv', index=False)

    # Minimal data for learning_pathways.csv
    learning_pathways_data = {
        'pathway_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'pathway_name': [
            'Advanced Python for Quants', 'ML Foundations Course', 'Generative AI Workshop',
            'Cloud for Data Scientists', 'Deep Learning Specialization', 'AI Ethics Certification',
            'Financial Risk Modeling with AI', 'Advanced SQL for Analytics', 'Portfolio Optimization with ML',
            'Time Series Forecasting with AI'
        ],
        'type': [
            'Course', 'Course', 'Workshop', 'Course', 'Specialization', 'Certification',
            'Course', 'Course', 'Specialization', 'Course'
        ],
        'estimated_time_hours': [40, 60, 20, 50, 80, 30, 70, 25, 90, 60],
        'estimated_cost_usd': [200, 300, 150, 250, 500, 200, 400, 100, 600, 350],
        'skills_gained': [
            '{"Python": 2, "Quant_Models": 1}', '{"ML_basics": 3, "Python": 1}', '{"GenAI_Tools": 3, "AI_Ethics": 1}',
            '{"Cloud_Platforms": 3, "ML_basics": 1}', '{"ML_basics": 2, "Quant_Models": 2, "GenAI_Tools": 1}',
            '{"AI_Ethics": 3}', '{"Risk_Analysis": 2, "Financial_Modeling": 2, "ML_basics": 1}',
            '{"SQL": 2}', '{"Quant_Models": 3, "Financial_Modeling": 2, "ML_basics": 1}',
            '{"ML_basics": 2, "Quant_Models": 1}'
        ],
        'vr_gain_ai_fluency': [0.05, 0.1, 0.15, 0.05, 0.2, 0.05, 0.05, 0.0, 0.1, 0.1],
        'vr_gain_domain_expertise': [0.05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.1, 0.05],
        'vr_gain_adaptive_capacity': [0.02, 0.02, 0.05, 0.02, 0.05, 0.05, 0.02, 0.0, 0.02, 0.02],
        'prerequisites': [
            '[]', '[]', '[]', '[]', '[2]', '[]', '[1,2]', '[]', '[1,2]', '[2]'
        ]
    }
    pd.DataFrame(learning_pathways_data).to_csv('learning_pathways.csv', index=False)

#  Idiosyncratic Readiness (VR) Calculation Functions 
def calculate_ai_fluency(subfactors, weights=AI_FLUENCY_THETA_WEIGHTS):
    # Scale to 0-10 for display in app
    return sum(subfactors.get(k, 0) * v for k, v in weights.items()) * 10

def calculate_domain_expertise(education_level, experience_years, subfactors, experience_decay=GAMMA_EXPERIENCE_DECAY):
    edu_map = {'HS + significant coursework': 0.3, 'Associate\'s/Certificate': 0.4, 'Bachelor\'s in target field': 0.6, 'Master\'s in target field': 0.8, 'Master\'s in Finance': 0.85, 'PhD in target field': 0.95}
    edu_score = edu_map.get(education_level, 0.5)
    exp_score = min(1.0, experience_years / 20.0) # Cap experience impact
    portfolio_score = subfactors.get('portfolio', 0)
    recognition_score = subfactors.get('recognition', 0)
    credentials_score = subfactors.get('credentials', 0)
    return (edu_score * 0.3 + exp_score * 0.2 + portfolio_score * 0.2 + recognition_score * 0.15 + credentials_score * 0.15) * 10

def calculate_adaptive_capacity(subfactors):
    return sum(subfactors.get(k, 0) for k in subfactors.keys()) / len(subfactors) * 10

def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, weights=VR_COMPONENT_WEIGHTS):
    ai_fluency_norm = ai_fluency / 10
    domain_expertise_norm = domain_expertise / 10
    adaptive_capacity_norm = adaptive_capacity / 10
    return (ai_fluency_norm * weights['ai_fluency'] +
            domain_expertise_norm * weights['domain_expertise'] +
            adaptive_capacity_norm * weights['adaptive_capacity']) * 100

#  Systematic Opportunity (HR) Calculation Functions 
def normalize_growth(growth_rate):
    return min(1.0, max(0.0, (growth_rate + 0.5) / 1.0)) # Example normalization

def calculate_wage_premium(ai_skilled_wage, median_wage):
    if median_wage == 0: return 0
    return (ai_skilled_wage - median_wage) / median_wage

def calculate_entry_accessibility(education_years_required, experience_years_required):
    edu_score = max(0.0, (20 - education_years_required) / 10.0)
    exp_score = max(0.0, (10 - experience_years_required) / 10.0)
    return (edu_score + exp_score) / 2

def calculate_hbase(ai_enhancement_potential, growth_normalized, wage_premium, entry_accessibility, weights=HBASE_WEIGHTS):
    wage_premium_scaled = min(1.0, max(0.0, wage_premium * 2)) # Example scaling for premium
    return (ai_enhancement_potential * weights['ai_enhancement_potential'] +
            growth_normalized * weights['growth_normalized'] +
            wage_premium_scaled * weights['wage_premium'] +
            entry_accessibility * weights['entry_accessibility']) * 100

def calculate_mgrowth(job_postings_t, job_postings_t_minus_1, lambda_growth_multiplier=LAMBDA_GROWTH_MULTIPLIER):
    if job_postings_t_minus_1 == 0: return 1.0
    growth_factor = (job_postings_t - job_postings_t_minus_1) / job_postings_t_minus_1
    return 1 + lambda_growth_multiplier * growth_factor

def calculate_mregional(local_demand, national_avg_demand, remote_work_factor, gamma_remote_work=GAMMA_REMOTE_WORK):
    if national_avg_demand == 0: return 1.0
    demand_ratio = local_demand / national_avg_demand
    return demand_ratio * (1 - remote_work_factor * gamma_remote_work)

def calculate_hr(hbase, mgrowth, mregional):
    return hbase * mgrowth * mregional

#  AI-Readiness (AI-R) Calculation Functions 
def calculate_skills_match_score(current_skills_dict, required_skills_series, max_possible_match_for_role):
    skill_gaps = {}
    required_skills_dict = required_skills_series.drop('role', errors='ignore').to_dict()
    current_matched_level = 0
    total_required_level = 0

    for skill, required_level in required_skills_dict.items():
        if required_level is None or pd.isna(required_level):
            continue
        current_level = current_skills_dict.get(skill, 0)
        skill_gaps[skill] = {'current': current_level, 'required': required_level}
        current_matched_level += min(current_level, required_level)
        total_required_level += required_level
    
    if total_required_level == 0:
        return 1.0, skill_gaps, required_skills_dict, current_matched_level, total_required_level
    
    return current_matched_level / total_required_level, skill_gaps, required_skills_dict, current_matched_level, total_required_level

def calculate_timing_factor(experience_years):
    return min(1.0, experience_years / 15.0)

def calculate_alignment(skills_match, timing_factor):
    return (skills_match + timing_factor) / 2

def calculate_synergy(vr_score, hr_score, alignment_score):
    return (vr_score / 100) * (hr_score / 100) * alignment_score * 100

def calculate_air(vr_score, hr_score, synergy_score, alpha=ALPHA, beta=BETA):
    return alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_score

#  Learning Optimization Functions 
def optimize_learning_pathways(
    initial_air, current_vr_score, current_vr_subscores_normalized, current_hr_score,
    learning_pathways_df, max_learning_time_hours, max_learning_budget_usd,
    alpha, beta, lambda_cost_weight, experience_years, current_skills_dict_initial
):
    available_pathways = learning_pathways_df.copy()
    recommended_paths = []
    total_time_invested = 0
    total_cost_invested = 0
    
    # Deep copy of mutable objects
    current_vr_subscores_mutable = current_vr_subscores_normalized.copy()
    current_skills_mutable = current_skills_dict_initial.copy()

    completed_pathway_ids = set()

    # Need to load skill_requirements_df here or pass it if this is a standalone function
    skill_requirements_df_mock = pd.read_csv('skill_requirements.csv')

    # The optimal role needs to be determined from the session state in the app logic,
    # or passed as an argument. For this mock, we'll assume a placeholder.
    # In the app, it comes from st.session_state['top_role']['Role']
    target_role_name_for_optimization = 'AI Quant Analyst' 
    # This mock needs to be run in context of the streamlit app for st.session_state to work
    try:
        if 'top_role' in globals() and 'Role' in globals()['top_role']: # For testing in global scope
             target_role_name_for_optimization = globals()['top_role']['Role']
        elif 'st' in globals() and 'session_state' in globals()['st'] and 'top_role' in globals()['st'].session_state:
            target_role_name_for_optimization = globals()['st'].session_state['top_role']['Role']
    except NameError:
        pass # St is not available

    required_skills_for_role_series = skill_requirements_df_mock[
        skill_requirements_df_mock['role'] == target_role_name_for_optimization
    ].iloc[0]
    max_possible_match_for_role = required_skills_for_role_series.drop('role', errors='ignore').sum()


    for _ in range(len(available_pathways) + 1): # Max iterations to pick pathways
        best_path = None
        best_path_return = -np.inf # Initialize with negative infinity

        # Evaluate pathways that meet prerequisites and constraints
        for idx, path in available_pathways.iterrows():
            path_id = path['pathway_id']
            prereqs = ast.literal_eval(path['prerequisites'])
            if not all(p_id in completed_pathway_ids for p_id in prereqs):
                continue

            # Check time and budget constraints
            if total_time_invested + path['estimated_time_hours'] > max_learning_time_hours:
                continue
            if total_cost_invested + path['estimated_cost_usd'] > max_learning_budget_usd:
                continue
            
            # Calculate projected VR components after this pathway
            proj_ai_fluency = current_vr_subscores_mutable['ai_fluency'] + path.get('vr_gain_ai_fluency', 0)
            proj_domain_expertise = current_vr_subscores_mutable['domain_expertise'] + path.get('vr_gain_domain_expertise', 0)
            proj_adaptive_capacity = current_vr_subscores_mutable['adaptive_capacity'] + path.get('vr_gain_adaptive_capacity', 0)

            # Cap VR components at 1.0 (they are 0-1 scores before scaling to 0-10 for display in app)
            proj_ai_fluency = min(1.0, proj_ai_fluency)
            proj_domain_expertise = min(1.0, proj_domain_expertise)
            proj_adaptive_capacity = min(1.0, proj_adaptive_capacity)

            # Calculate projected VR (note: VR calculation takes 0-10 components, then scales total to 0-100)
            # So, need to multiply proj_... by 10 for calculate_vr input
            proj_vr_score = calculate_vr(proj_ai_fluency * 10, proj_domain_expertise * 10, proj_adaptive_capacity * 10, VR_COMPONENT_WEIGHTS)
            
            # Simulate projected skills (for alignment calculation)
            temp_skills = current_skills_mutable.copy()
            skills_gained_dict = ast.literal_eval(path['skills_gained'])
            for skill, gain in skills_gained_dict.items():
                temp_skills[skill] = min(10, temp_skills.get(skill, 0) + gain) # Cap skill level at 10

            skills_match, _, _, _, _ = calculate_skills_match_score(
                temp_skills,
                required_skills_for_role_series,
                max_possible_match_for_role
            )
            timing_factor = calculate_timing_factor(experience_years)
            alignment_score = calculate_alignment(skills_match, timing_factor)
            synergy_score = calculate_synergy(proj_vr_score, current_hr_score, alignment_score)
            
            projected_air_candidate = calculate_air(proj_vr_score, current_hr_score, synergy_score, alpha, beta)
            
            air_gain = projected_air_candidate - initial_air # Use initial_air from optimization start
            
            cost_factor = path['estimated_cost_usd'] * lambda_cost_weight
            time_factor = path['estimated_time_hours']
            
            investment_cost = cost_factor + time_factor
            if investment_cost > 0:
                current_path_return = air_gain / investment_cost
            else:
                current_path_return = air_gain * 1000 # High return for free paths
            
            if current_path_return > best_path_return:
                best_path_return = current_path_return
                best_path = path

        if best_path is None or best_path_return <= 0: # Stop if no path improves AI-R or no valid path
            break

        # Add best path to recommendations and update state
        recommended_paths.append(best_path)
        total_time_invested += best_path['estimated_time_hours']
        total_cost_invested += best_path['estimated_cost_usd']
        completed_pathway_ids.add(best_path['pathway_id'])
        
        # Update current VR subscores for next iteration (0-1 range)
        current_vr_subscores_mutable['ai_fluency'] = min(1.0, current_vr_subscores_mutable['ai_fluency'] + best_path.get('vr_gain_ai_fluency', 0))
        current_vr_subscores_mutable['domain_expertise'] = min(1.0, current_vr_subscores_mutable['domain_expertise'] + best_path.get('vr_gain_domain_expertise', 0))
        current_vr_subscores_mutable['adaptive_capacity'] = min(1.0, current_vr_subscores_mutable['adaptive_capacity'] + best_path.get('vr_gain_adaptive_capacity', 0))

        # Update current skills
        skills_gained_dict = ast.literal_eval(best_path['skills_gained'])
        for skill, gain in skills_gained_dict.items():
            current_skills_mutable[skill] = min(10, current_skills_mutable.get(skill, 0) + gain)
        
        # Remove selected pathway from available ones
        available_pathways = available_pathways.drop(best_path.name)
        
    # Calculate final AI-R after all selected paths
    final_ai_fluency_norm = current_vr_subscores_mutable['ai_fluency']
    final_domain_expertise_norm = current_vr_subscores_mutable['domain_expertise']
    final_adaptive_capacity_norm = current_vr_subscores_mutable['adaptive_capacity']
    
    final_vr_score = calculate_vr(final_ai_fluency_norm * 10, final_domain_expertise_norm * 10, final_adaptive_capacity_norm * 10, VR_COMPONENT_WEIGHTS)
    
    # Recalculate alignment with final skills
    final_skills_match, _, _, _, _ = calculate_skills_match_score(
        current_skills_mutable,
        required_skills_for_role_series,
        max_possible_match_for_role
    )
    final_timing_factor = calculate_timing_factor(experience_years)
    final_alignment_score = calculate_alignment(final_skills_match, final_timing_factor)
    final_synergy_score = calculate_synergy(final_vr_score, current_hr_score, final_alignment_score)
    final_projected_air = calculate_air(final_vr_score, current_hr_score, final_synergy_score, alpha, beta)
    
    return (
        recommended_paths,
        total_time_invested,
        total_cost_invested,
        final_projected_air,
        final_vr_score,
        current_vr_subscores_mutable, # These are 0-1 values
        current_skills_mutable # Final skills after optimization
    )


def run_what_if_scenario(
    current_vr_score_initial, current_vr_subscores_normalized_initial, current_skills_dict_initial,
    scenario_target_role, hr_scores_dict, skill_requirements_df,
    custom_scenario_pathways, experience_years, alpha, beta
):
    
    # Initialize with current state (0-1 scale for subscores)
    scenario_ai_fluency_norm = current_vr_subscores_normalized_initial['ai_fluency']
    scenario_domain_expertise_norm = current_vr_subscores_normalized_initial['domain_expertise']
    scenario_adaptive_capacity_norm = current_vr_subscores_normalized_initial['adaptive_capacity']
    scenario_skills = current_skills_dict_initial.copy()

    total_time = 0
    total_cost = 0

    # Apply pathways for the scenario
    for path in custom_scenario_pathways:
        total_time += path['estimated_time_hours']
        total_cost += path['estimated_cost_usd']

        scenario_ai_fluency_norm = min(1.0, scenario_ai_fluency_norm + path.get('vr_gain_ai_fluency', 0))
        scenario_domain_expertise_norm = min(1.0, scenario_domain_expertise_norm + path.get('vr_gain_domain_expertise', 0))
        scenario_adaptive_capacity_norm = min(1.0, scenario_adaptive_capacity_norm + path.get('vr_gain_adaptive_capacity', 0))
        
        skills_gained_dict = ast.literal_eval(path['skills_gained'])
        for skill, gain in skills_gained_dict.items():
            scenario_skills[skill] = min(10, scenario_skills.get(skill, 0) + gain)

    # Recalculate VR based on scenario state (convert 0-1 subscores to 0-10 for calculate_vr)
    projected_vr_score = calculate_vr(scenario_ai_fluency_norm * 10, scenario_domain_expertise_norm * 10, scenario_adaptive_capacity_norm * 10, VR_COMPONENT_WEIGHTS)

    # Get HR for the target role
    scenario_hr_score = hr_scores_dict.get(scenario_target_role, 0)

    # Recalculate alignment based on scenario skills and target role
    required_skills_for_role = skill_requirements_df[skill_requirements_df['role'] == scenario_target_role].iloc[0]
    max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum()

    skills_match, _, _, _, _ = calculate_skills_match_score(
        scenario_skills,
        required_skills_for_role,
        max_possible_match_for_role
    )
    timing_factor = calculate_timing_factor(experience_years)
    alignment_score = calculate_alignment(skills_match, timing_factor)
    
    scenario_synergy_score = calculate_synergy(projected_vr_score, scenario_hr_score, alignment_score)
    projected_air_scenario = calculate_air(projected_vr_score, scenario_hr_score, scenario_synergy_score, alpha, beta)

    return projected_air_scenario, total_time, total_cost, projected_vr_score, scenario_hr_score, scenario_synergy_score
```

### 2.6. Run the Streamlit Application
Navigate to the directory containing `app.py` and `source.py` (e.g., `qu_lab_app`) in your terminal and run:

```bash
streamlit run app.py
```
This command will start the Streamlit server and open the application in your default web browser.

## 3. Understanding User Profile and Goals (Tab 2)
Duration: 0:15

The **"Profile & Goals"** tab (Tab 2) is where Alice defines her professional background and specifies the AI-enabled roles she is considering. This initial input is crucial as it forms the baseline for all subsequent AI-Readiness calculations.

### 3.1. Session State Initialization
Upon application startup, `app.py` initializes a `st.session_state` dictionary with default values for Alice's profile and other calculation results. This ensures consistency across tab interactions and prevents re-computation of static data. The `initialize_session_state()` function sets up placeholder variables for `alice_profile`, `target_roles`, scores (`alice_ai_fluency_score`, `alice_vr_score`, etc.), and optimization parameters. It also loads all the required CSV dataframes from `source.py`'s `create_simulated_data()` function.

```python
# From app.py:
def initialize_session_state():
    # ... (omitted for brevity)
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
            # ... (other subfactors)
        }
    # ... (other initializations)
    if 'idiosyncratic_df' not in st.session_state:
        create_simulated_data() # Ensure data files exist before reading
        st.session_state['idiosyncratic_df'] = pd.read_csv('idiosyncratic_data.csv')
        # ... (load other dataframes)
```

### 3.2. Professional Background Input
Alice's profile is captured through a series of interactive Streamlit widgets:
*   **Education Level & Years of Experience:** Basic demographic data used in `calculate_domain_expertise`.
*   **AI-Fluency Sub-Factors:** Sliders (0-1) for aspects like `prompting`, `ai_tools`, `understanding`, `data_literacy`, `ai_augmented_productivity`, `critical_ai_judgment`, and `appropriate_trust_decisions`. These feed into `calculate_ai_fluency`.
*   **Domain-Expertise Sub-Factors:** Sliders (0-1) for `portfolio`, `recognition`, and `credentials`. These also feed into `calculate_domain_expertise`.
*   **Adaptive-Capacity Sub-Factors:** Sliders (0-1) for `cognitive_flexibility`, `social_emotional_intelligence`, and `strategic_career_management`. These feed into `calculate_adaptive_capacity`.

### 3.3. Current Skill Levels
A set of sliders (0-10) allows Alice to rate her proficiency in various skills, from `Python` to `AI_Ethics` and `Cloud_Platforms`. These are critical for the skill gap analysis later on.

### 3.4. Target AI-Enabled Financial Roles
Alice can select multiple target roles from a `multiselect` dropdown, populated from the `systematic_df`. This allows her to compare different career paths side-by-side.

### 3.5. Calculating Initial Readiness & Opportunity
When the **"Calculate Initial Readiness & Opportunity"** button is pressed, the application performs the following key computations using functions from `source.py`:

#### 3.5.1. Idiosyncratic Readiness ($V^R$) Calculation
$V^R$ is calculated as a weighted sum of three core components: AI-Fluency, Domain-Expertise, and Adaptive-Capacity.
$$V^R(t) = w_1 \cdot AI‑Fluency_i(t) + w_2 \cdot Domain‑Expertise_i(t) + w_3 \cdot Adaptive‑Capacity_i(t)$$
Where $w_1 = {VR_W1_AI_FLUENCY}$, $w_2 = {VR_W2_DOMAIN_EXPERTISE}$, $w_3 = {VR_W3_ADAPTIVE_CAPACITY}$ as defined in `source.py`.

*   **AI-Fluency Score:** Derived from the `ai_fluency_subfactors` using `calculate_ai_fluency()`.
*   **Domain-Expertise Score:** Combines `education_level`, `experience_years`, and `domain_expertise_subfactors` via `calculate_domain_expertise()`.
*   **Adaptive-Capacity Score:** Calculated from `adaptive_capacity_subfactors` using `calculate_adaptive_capacity()`.
*   **Overall $V^R$ Score:** A weighted average of these three scores, normalized to $[0, 100]$, using `calculate_vr()`.

```python
# From source.py (simplified):
def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, weights):
    # Assuming ai_fluency, domain_expertise, adaptive_capacity are 0-10
    ai_fluency_norm = ai_fluency / 10
    domain_expertise_norm = domain_expertise / 10
    adaptive_capacity_norm = adaptive_capacity / 10
    return (ai_fluency_norm * weights['ai_fluency'] +
            domain_expertise_norm * weights['domain_expertise'] +
            adaptive_capacity_norm * weights['adaptive_capacity']) * 100
```

#### 3.5.2. Systematic Opportunity ($H^R$) Calculation
For each selected `target_role`, the $H^R$ score is calculated, representing market demand and opportunity.
$$H^R(t) = H_{{base}}(O_{{target}}) \cdot M_{{growth}}(t) \cdot M_{{regional}}(t)$$

*   **$H_{{base}}$ (Base Opportunity):** Uses `ai_enhancement_potential`, normalized job `growth_rate`, `wage_premium`, and `entry_accessibility` for the role. Functions like `normalize_growth()`, `calculate_wage_premium()`, `calculate_entry_accessibility()`, and `calculate_hbase()` are involved.
*   **$M_{{growth}}$ (Growth Multiplier):** Reflects recent job posting trends using `job_postings_t` and `job_postings_t_minus_1` with `calculate_mgrowth()`.
*   **$M_{{regional}}$ (Regional Multiplier):** Accounts for local vs. national demand and `remote_work_factor` using `calculate_mregional()`.
*   **Overall $H^R$ Score:** These components are multiplied to get the final $H^R$ for each role via `calculate_hr()`.

All these computed scores are stored in `st.session_state` for use in subsequent tabs.

## 4. Opportunity Evaluation and Skill Gaps (Tab 3)
Duration: 0:20

The **"Opportunity Evaluation"** tab (Tab 3) brings together Alice's individual readiness ($V^R$) and the market's systematic opportunity ($H^R$) to compute the comprehensive AI-Readiness Score (AI-R) for each target role. This tab also identifies specific skill gaps, providing actionable insights for learning.

<aside class="negative">
Before proceeding, ensure you've clicked "Calculate Initial Readiness & Opportunity" in the "Profile & Goals" tab. Otherwise, no data will be available here.
</aside>

### 4.1. Idiosyncratic Readiness ($V^R$) Breakdown
This section prominently displays Alice's total $V^R$ score and its three constituent normalized components: AI-Fluency, Domain-Expertise, and Adaptive-Capacity. This visual breakdown helps Alice understand her intrinsic strengths.
The calculation is:
$$V^R(t) = {VR\_W1\_AI\_FLUENCY} \cdot AI‑Fluency_i(t) + {VR\_W2\_DOMAIN\_EXPERTISE} \cdot Domain‑Expertise_i(t) + {VR\_W3\_ADAPTIVE\_CAPACITY} \cdot Adaptive‑Capacity_i(t)$$
These scores are retrieved directly from `st.session_state` after the initial calculation.

### 4.2. Systematic Opportunity ($H^R$) by Target Role
A table displays the calculated $H^R$ score for each of Alice's selected target roles. This allows her to quickly compare which roles have the highest market demand and potential.

```python
# From app.py:
st.dataframe(pd.DataFrame(st.session_state['hr_scores'].items(), columns=['Role', 'HR_Score']).round(2).set_index('Role'))
```

### 4.3. Overall AI-Readiness ($AI-R$) Scores and Skill Gaps
This is the core analysis of this tab. For each target role, the AI-R score is computed using the full parametric framework.

The crucial additional component calculated here is the **Synergy Function**:
$$Synergy\%(V^R, H^R) = \frac{{V^R \times H^R}}{{100}} \times Alignment_i$$
where $Alignment_i \in [0,1]$ combines `skills_match` and `timing_factor`.

The calculation process involves:
1.  **Skill Match Score:** `calculate_skills_match_score()` compares `alice_profile['current_skills']` with the `skill_requirements_df` for the specific role. It returns a score indicating how well Alice's skills align with the role's needs and also identifies specific gaps.
2.  **Timing Factor:** `calculate_timing_factor()` uses Alice's `experience_years` to determine a factor representing her career stage's relevance.
3.  **Alignment Score:** `calculate_alignment()` combines the `skills_match` and `timing_factor`.
4.  **Synergy Score:** `calculate_synergy()` uses $V^R$, $H^R$, and `alignment_score` to quantify the multiplicative benefit of alignment.
5.  **Final AI-R Score:** `calculate_air()` combines $V^R$, $H^R$, and Synergy with weights $\alpha$ and $\beta$.
    *   $\alpha = {ALPHA}$
    *   $\beta = {BETA}$

All these results are compiled into `st.session_state['air_df']`, and the role with the highest AI-R is identified as `st.session_state['top_role']`.

```python
# From app.py (simplified calculation for AI-R):
# ... inside the loop for each role
current_hr_score = st.session_state['hr_scores'].get(role, 0)
required_skills_for_role = st.session_state['skill_requirements_df'][st.session_state['skill_requirements_df']['role'] == role].iloc[0]
max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum()

skills_match, skill_gaps, _, _, _ = calculate_skills_match_score(
    st.session_state['alice_profile']['current_skills'],
    required_skills_for_role,
    max_possible_match_for_role
)
st.session_state['all_skill_gaps'][role] = skill_gaps # Store for radar chart

timing_factor = calculate_timing_factor(st.session_state['alice_profile']['experience_years'])
alignment_score = calculate_alignment(skills_match, timing_factor)
synergy_score = calculate_synergy(st.session_state['alice_vr_score'], current_hr_score, alignment_score)
air_score = calculate_air(st.session_state['alice_vr_score'], current_hr_score, synergy_score, ALPHA, BETA)

# ... append to air_results list and update st.session_state['air_df'] and st.session_state['top_role']
```

#### Visualizations
*   **AI-R Bar Chart:** A bar chart (`matplotlib.pyplot`) visually compares Alice's AI-R, $V^R$, and $H^R$ scores across all target roles. This provides an intuitive understanding of which roles are the best fit.
*   **Skill Gaps Radar Chart:** For the `top_role`, a radar chart highlights Alice's current skill levels against the required skill levels. This graphically represents the specific skills Alice needs to develop to succeed in her most promising role.

<aside class="positive">
The radar chart is a powerful visual tool for skill gap analysis. Developers should focus on its implementation to dynamically adapt to different roles and current skill sets.
</aside>

## 5. Learning Pathway Optimization (Tab 4)
Duration: 0:20

The **"Learning Optimization"** tab (Tab 4) is where Alice transitions from assessment to action. Based on her initial AI-R scores and identified skill gaps for her `top_role`, this section recommends an optimal sequence of learning activities to maximize her projected AI-R, subject to time and budget constraints.

### 5.1. Optimization Problem Statement
The objective is to maximize the gain in AI-R minus a weighted cost:
$$ \max_{{P_1,...,P_K}} (AI‑R_{{proj}} - AI‑R_{{current}}) - \lambda \cdot \sum_{{k=1}}^K Cost(p_k) $$
subject to:
$$ \sum_{{k=1}}^K Time(p_k) \le T_{{max}} $$
$$ \sum_{{k=1}}^K Cost(p_k) \le B_{{max}} $$
$$ p_k \in P_{{feasible}} $$
$$ Prerequisites(p_k) \subseteq \{{P_1,...,P_{{k-1}}\}} $$
where $AI‑R_{{proj}}$ is the projected AI-R after completing pathways, $AI‑R_{{current}}$ is her initial AI-R, $\lambda$ is `LAMBDA_COST_WEIGHT` ($ {LAMBDA_COST_WEIGHT} $), $T_{{max}}$ is `MAX_LEARNING_TIME_HOURS` ($ {MAX_LEARNING_TIME_HOURS} $), and $B_{{max}}$ is `MAX_LEARNING_BUDGET_USD` ($ {MAX_LEARNING_BUDGET_USD} $).

For this application, a greedy heuristic is used: selecting pathways one by one that offer the highest "return" (AI-R point gain per unit of weighted time/cost) until constraints are met, while respecting prerequisites.

### 5.2. Setting Learning Constraints
Alice can adjust her available resources:
*   **Maximum Learning Time (hours):** `st.number_input` for `max_learning_time_hours`.
*   **Maximum Learning Budget (USD):** `st.number_input` for `max_learning_budget_usd`.
*   **Cost Weight (Lambda):** `st.slider` for `lambda_cost_weight`. A higher lambda means Alice is more cost-averse.

### 5.3. Optimizing Learning Pathway
When the **"Optimize Learning Pathway"** button is clicked, the `optimize_learning_pathways()` function from `source.py` is invoked.

```python
# From app.py:
# ... inside the if st.button("Optimize Learning Pathway"):
st.session_state['recommended_paths'], \
st.session_state['total_time_invested'], \
st.session_state['total_cost_invested'], \
st.session_state['projected_air'], \
st.session_state['final_vr_after_paths'], \
st.session_state['final_vr_subscores_normalized'], \
st.session_state['final_skills_after_paths'] = optimize_learning_pathways(
    st.session_state['initial_air_optimal_role'],
    st.session_state['alice_vr_score'], # Base VR for synergy, etc.
    alice_current_vr_subscores_normalized, # Subscores 0-1 range
    current_hr_for_top_role,
    st.session_state['learning_pathways_df'],
    st.session_state['max_learning_time_hours'],
    st.session_state['max_learning_budget_usd'],
    ALPHA, BETA, st.session_state['lambda_cost_weight'],
    st.session_state['alice_profile']['experience_years'],
    st.session_state['alice_profile']['current_skills']
)
```

**Flowchart for `optimize_learning_pathways`:**

```
[Start]
   |
   V
[Initialize: recommended_paths=[], time=0, cost=0,
 current_VR_subscores_mutable, current_skills_mutable,
 completed_pathway_ids, available_pathways_copy]
   |
   V
[Loop while pathways are available and constraints not met]
   |
   V
 [Find Best Pathway]
   |  - Iterate available_pathways
   |  - Check Prerequisites
   |  - Check Time/Budget Constraints
   |  - Calculate Projected VR, Skills, Alignment, Synergy, AIR
   |  - Calculate AIR_Gain / Weighted_Investment (Return Metric)
   |  - Keep track of path with highest Return Metric
   V
 [If no improving path or no valid path, Break Loop]
   |
   V
 [Add Best Pathway to recommended_paths]
   |
   V
 [Update: total_time, total_cost, completed_pathway_ids]
   |
   V
 [Update: current_VR_subscores_mutable (based on pathway's VR_gain)]
   |
   V
 [Update: current_skills_mutable (based on pathway's skills_gained)]
   |
   V
 [Remove Best Pathway from available_pathways_copy]
   |
   V
[End Loop]
   |
   V
[Calculate Final Projected AIR using final VR_subscores, skills]
   |
   V
[Return results]
   |
   V
[End]
```

### 5.4. Recommended Optimal Learning Pathway
The results of the optimization are displayed:
*   A list of recommended learning pathways, including their type, estimated time, and cost.
*   Total estimated time and cost investments.
*   Alice's initial AI-R for the `top_role` and the `projected_air` after completing the recommended pathways.
*   A bar chart comparing `Current AI-R` vs. `Projected AI-R`, visually demonstrating the expected improvement.

This section provides Alice with a clear, actionable plan to enhance her AI-readiness for her chosen career path.

## 6. 'What-If' Scenario Analysis (Tab 5)
Duration: 0:15

The **"What-If" Scenario Analysis** tab (Tab 5) empowers Alice to explore alternative career and learning strategies beyond the initial optimal recommendation. This functionality helps her understand trade-offs, compare different choices, and make more robust career decisions.

### 6.1. Defining Custom Scenarios
Alice can define custom scenarios by:
*   **Selecting a Target Role:** Choosing any role from the available options using `st.selectbox`.
*   **Selecting Learning Pathways:** Choosing a specific set of learning pathways from all available options using `st.multiselect`.

### 6.2. Running Custom Scenario Analysis
When the **"Run Custom Scenario Analysis"** button is clicked, the `run_what_if_scenario()` function from `source.py` is executed. This function simulates the impact of the selected learning pathways on Alice's AI-Readiness for the chosen target role.

```python
# From app.py:
# ... inside the if st.button("Run Custom Scenario Analysis"):
projected_air_custom, time_custom, cost_custom, projected_vr_custom, hr_custom, synergy_custom = run_what_if_scenario(
    st.session_state['alice_vr_score'], # Base VR Score
    {
        'ai_fluency': st.session_state['alice_ai_fluency_score'] / 10, # normalized 0-1
        'domain_expertise': st.session_state['alice_domain_expertise_score'] / 10, # normalized 0-1
        'adaptive_capacity': st.session_state['alice_adaptive_capacity_score'] / 10 # normalized 0-1
    },
    st.session_state['alice_profile']['current_skills'],
    scenario_target_role, st.session_state['hr_scores'],
    st.session_state['skill_requirements_df'],
    custom_scenario_pathways,
    st.session_state['alice_profile']['experience_years'],
    ALPHA, BETA
)
```
The `run_what_if_scenario` function updates Alice's VR subscores and skills based on the selected `custom_scenario_pathways`, then recalculates the projected AI-R for the chosen `scenario_target_role`. It returns the projected AI-R, total time, total cost, and component scores for that scenario.

The results, including the `Optimized for [Top Role]` scenario as a baseline (if available), are stored in `st.session_state['scenario_results_df']`.

### 6.3. Return on Learning Investment (ROI)
For each scenario, the application calculates a simple Return on Investment (ROI) metric:
$$ ROI = \frac{AI-R_{{gain}}}{Investment_{{score}}} $$
Where $AI-R_{{gain}}$ is the projected AI-R increase from the initial state, and $Investment_{{score}}$ is a weighted sum of normalized time and cost investments. This helps Alice understand which investments provide the best "bang for her buck."
$$ Investment_{{score}} = (\frac{{Cost(\$)}}{{B_{{max}}}} \cdot \lambda_{{cost\_weight}}) + \frac{{Time(h)}}{{T_{{max}}}} $$
The ROI results are stored in `st.session_state['roi_df']`.

#### Visualizations
*   **Comparative Projected AI-R Bar Chart:** Displays the projected AI-R scores for all run scenarios, allowing for easy comparison.
*   **Return on Learning Investment (ROI) Bar Chart:** Visualizes the ROI for each scenario, highlighting which learning strategies offer the most efficient gain in AI-readiness.

This detailed analysis empowers Alice to make data-driven decisions, weighing projected career opportunity against the required investment in time and cost.

## 7. Personalized AI Career Strategy Report (Tab 6)
Duration: 0:05

The **"Summary Report"** tab (Tab 6) consolidates all the analysis from the previous steps into a clear, actionable, personalized report for Alice. This report summarizes her current standing, highlights identified skill gaps, and presents the recommended optimal learning pathway with projected outcomes.

<aside class="negative">
A complete report requires all previous steps ("Profile & Goals," "Opportunity Evaluation," "Learning Optimization," "What-If Analysis") to be completed.
</aside>

### 7.1. Current AI-Readiness Profile
This section provides a concise overview of Alice's current state:
*   Her overall `Idiosyncratic Readiness (VR)` score, along with the scores for AI-Fluency, Domain-Expertise, and Adaptive-Capacity components.
*   The `Systematic Opportunity (HR)` scores for each of her target roles.

### 7.2. Top AI-Enabled Career Path Recommendation
The report highlights the **Recommended Role** (her `top_role`) identified in the "Opportunity Evaluation" tab. It shows:
*   Her `Initial AI-Readiness Score (AI-R)` for this role.
*   Her `Projected AI-Readiness Score (AI-R)` after undertaking the optimal learning pathway (if optimization was run).
*   The `Estimated AI-R Improvement`.

### 7.3. Detailed Skill Gaps for the Recommended Role
A table lists the specific skill gaps for the `top_role`, comparing Alice's current skill levels against the required levels. Skills with a positive "Gap" value are those that need development. This provides a clear focus for her learning efforts.

```python
# From app.py:
# ...
top_role_skills_gaps_df = pd.DataFrame(st.session_state['all_skill_gaps'][st.session_state['top_role']['Role']]).T
top_role_skills_gaps_df['Gap'] = top_role_skills_gaps_df['required'] - top_role_skills_gaps_df['current']
st.dataframe(top_role_skills_gaps_df[top_role_skills_gaps_df['Gap'] > 0].sort_values(by='Gap', ascending=False))
```

### 7.4. Recommended Optimal Learning Pathway
This section lists the specific learning pathways identified by the optimization engine as the most effective for maximizing her AI-R within her constraints. It also summarizes the `Total Estimated Time Investment` and `Total Estimated Cost Investment`.

### 7.5. 'What-If' Scenario Analysis Summary
A summary table of the scenarios analyzed in the previous tab is presented, allowing Alice to review the outcomes of different strategic choices. Key insights regarding the best-performing scenarios and ROI are provided.

This comprehensive report serves as a personalized roadmap for Alice's AI-enabled career journey, distilling complex data into actionable insights for her professional development.

<aside class="positive">
  <button>
    [Download Sample Code](https://github.com/your_repo/qu_lab_app/archive/main.zip)
  </button>
  You can download a complete working example (including `source.py` and initial data generation logic) from this link to follow along locally.
</aside>

** End of Codelab **
