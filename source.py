import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Global DataFrames (Dummy Data for Demonstration) ---
# In a real application, these would be loaded from a database or external files.

df_employees = pd.DataFrame({
    'employee_id': ['E001', 'E002', 'E003', 'E004', 'E005', 'E006', 'E007', 'E008', 'E009', 'E010'],
    'job_role': ['Data Scientist', 'Business Analyst', 'Software Engineer', 'HR Specialist', 'Marketing Manager',
                 'Data Scientist', 'Software Engineer', 'Business Analyst', 'Marketing Manager', 'HR Specialist'],
    'department': ['AI/ML', 'Strategy', 'Engineering', 'HR', 'Marketing',
                   'AI/ML', 'Engineering', 'Strategy', 'Marketing', 'HR'],
    'years_experience': [5, 8, 3, 10, 6, 4, 7, 2, 9, 1],
    'education_level': ['PhD', 'Master's', 'Bachelor's', 'Master's', 'Bachelor's',
                        'Master's', 'PhD', 'Bachelor's', 'Master's', 'Associate's/Certificate'],
    'portfolio_score': [0.9, 0.6, 0.7, 0.3, 0.5, 0.8, 0.95, 0.4, 0.65, 0.2],
    'recognition_score': [0.8, 0.7, 0.6, 0.4, 0.5, 0.75, 0.85, 0.3, 0.7, 0.3],
    'credentials_score': [0.85, 0.65, 0.75, 0.5, 0.45, 0.8, 0.9, 0.35, 0.6, 0.25],
    'prompting_score': [85, 70, 80, 50, 60, 90, 75, 55, 65, 45],
    'tools_score': [80, 65, 75, 45, 55, 85, 70, 50, 60, 40],
    'understanding_score': [88, 72, 82, 52, 62, 92, 77, 57, 67, 47],
    'data_literacy_score': [90, 75, 85, 55, 65, 95, 80, 60, 70, 50],
    'ai_augmented_productivity_norm': [0.9, 0.7, 0.8, 0.6, 0.65, 0.95, 0.85, 0.55, 0.7, 0.4],
    'errors_caught_norm': [0.85, 0.6, 0.7, 0.4, 0.5, 0.9, 0.75, 0.35, 0.65, 0.25],
    'trust_decisions_norm': [0.9, 0.7, 0.8, 0.5, 0.6, 0.95, 0.8, 0.4, 0.7, 0.3],
    'learning_rate_score': [0.8, 0.6, 0.7, 0.5, 0.55, 0.85, 0.75, 0.45, 0.6, 0.35],
    'cognitive_flexibility_score': [80, 70, 75, 60, 65, 85, 90, 55, 70, 50],
    'social_emotional_intelligence_score': [75, 80, 65, 70, 75, 80, 70, 60, 85, 55],
    'strategic_career_management_score': [85, 75, 70, 65, 80, 90, 80, 50, 75, 60],
    # Dummy skills for alignment factor
    'skill_a': [0.8, 0.6, 0.7, 0.5, 0.5, 0.85, 0.75, 0.4, 0.6, 0.3],
    'skill_b': [0.9, 0.7, 0.8, 0.6, 0.6, 0.9, 0.8, 0.5, 0.7, 0.4],
    'skill_c': [0.7, 0.8, 0.6, 0.7, 0.7, 0.65, 0.7, 0.6, 0.8, 0.5],
    'skill_d': [0.8, 0.6, 0.7, 0.5, 0.5, 0.8, 0.7, 0.4, 0.6, 0.3],
    'skill_e': [0.9, 0.7, 0.8, 0.6, 0.6, 0.9, 0.8, 0.5, 0.7, 0.4],
    'skill_f': [0.7, 0.8, 0.6, 0.7, 0.7, 0.65, 0.7, 0.6, 0.8, 0.5],
    'skill_g': [0.8, 0.6, 0.7, 0.5, 0.5, 0.8, 0.7, 0.4, 0.6, 0.3],
    'skill_h': [0.9, 0.7, 0.8, 0.6, 0.6, 0.9, 0.8, 0.5, 0.7, 0.4],
    'skill_i': [0.7, 0.8, 0.6, 0.7, 0.7, 0.65, 0.7, 0.6, 0.8, 0.5],
    'skill_j': [0.8, 0.6, 0.7, 0.5, 0.5, 0.8, 0.7, 0.4, 0.6, 0.3],
})

df_occupations = pd.DataFrame({
    'job_role': ['Data Scientist', 'Business Analyst', 'Software Engineer', 'HR Specialist', 'Marketing Manager'],
    'ai_enhancement_potential': [0.9, 0.7, 0.8, 0.6, 0.65],
    'growth_rate': [0.25, 0.15, 0.20, 0.05, 0.10], # Normalized growth rate
    'wage_premium': [0.30, 0.10, 0.20, 0.05, 0.08],
    'entry_accessibility': [0.7, 0.8, 0.75, 0.9, 0.85],
    'remote_work_factor': [0.8, 0.6, 0.7, 0.5, 0.6],
    # Required skills for alignment factor
    'req_skill_a': [0.9, 0.6, 0.8, 0.4, 0.5],
    'req_skill_b': [0.9, 0.7, 0.8, 0.5, 0.6],
    'req_skill_c': [0.7, 0.8, 0.6, 0.7, 0.7],
    'req_skill_d': [0.8, 0.6, 0.7, 0.5, 0.5],
    'req_skill_e': [0.9, 0.7, 0.8, 0.6, 0.6],
    'req_skill_f': [0.7, 0.8, 0.6, 0.7, 0.7],
    'req_skill_g': [0.8, 0.6, 0.7, 0.5, 0.5],
    'req_skill_h': [0.9, 0.7, 0.8, 0.6, 0.6],
    'req_skill_i': [0.7, 0.8, 0.6, 0.7, 0.7],
    'req_skill_j': [0.8, 0.6, 0.7, 0.5, 0.5],
})

df_pathways = pd.DataFrame({
    'pathway_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
    'pathway_name': ['Advanced Python for AI', 'Cloud AI Platforms', 'Data Storytelling', 'Leadership in AI', 'Machine Learning Fundamentals', 'Ethics in AI'],
    'impact_on_ai_fluency': [10, 12, 5, 3, 15, 2], # Points increase
    'impact_on_domain_expertise': [5, 8, 10, 4, 7, 1],
    'impact_on_adaptive_capacity': [3, 7, 8, 10, 5, 3],
    'cost': [500, 750, 300, 1000, 600, 200],
    'time_hours': [40, 60, 20, 80, 50, 15],
    'prerequisites': ['None', 'P001', 'None', 'None', 'None', 'None'], # Simplified for now
})

# --- Parameters ---
PARAMS = {
    'ALPHA': 0.6,
    'BETA': 0.15,
    'VR_WEIGHTS': {
        'ai_fluency': 0.45,
        'domain_expertise': 0.35,
        'adaptive_capacity': 0.20
    },
    'HR_BASE_WEIGHTS': {
        'ai_enhancement_potential': 0.30,
        'growth_rate': 0.30,
        'wage_premium': 0.25,
        'entry_accessibility': 0.15
    },
    'AI_FLUENCY_WEIGHTS': {
        'technical_ai_skills': 0.30,
        'ai_augmented_productivity': 0.35,
        'critical_ai_judgment': 0.20,
        'ai_learning_velocity': 0.15
    },
    'DOMAIN_EXPERTISE_GAMMA_EXP': 0.15,
    'EDUCATION_MAP': {
        'PhD': 1.0,
        'Master\'s': 0.85,
        'Bachelor\'s': 0.70,
        'Associate\'s/Certificate': 0.60,
        'HS+Coursework': 0.50
    },
    'DOMAIN_SPECIALIZATION_WEIGHTS': {
        'portfolio_score': 0.4,
        'recognition_score': 0.3,
        'credentials_score': 0.3
    },
    'ADAPTIVE_CAPACITY_WEIGHT': 1/3, # Equal weight for cognitive, social, strategic
    'SKILL_IMPORTANCE': { # Dummy importance for skills a-j
        'skill_a': 0.1, 'skill_b': 0.1, 'skill_c': 0.1, 'skill_d': 0.1, 'skill_e': 0.1,
        'skill_f': 0.1, 'skill_g': 0.1, 'skill_h': 0.1, 'skill_i': 0.1, 'skill_j': 0.1
    },
    'TIMING_FACTOR_YEARS': {
        (0, 5): 1.0,
        (5, 15): 1.0,
        (15, np.inf): 0.8
    }
}

# --- Helper Functions for AI-R Calculation ---

def _calculate_ai_fluency(employee_row, PARAMS):
    tech_ai_skills_avg = (employee_row['prompting_score'] + employee_row['tools_score'] + \
                          employee_row['understanding_score'] + employee_row['data_literacy_score']) / 4
    tech_ai_skills_norm = tech_ai_skills_avg / 100.0 # Normalize to 0-1
    
    critical_ai_judgment_norm = (employee_row['errors_caught_norm'] + employee_row['trust_decisions_norm']) / 2

    # Simplified AI Learning Velocity: assume learning_rate_score is already normalized
    ai_learning_velocity_norm = employee_row['learning_rate_score']

    ai_fluency = (
        PARAMS['AI_FLUENCY_WEIGHTS']['technical_ai_skills'] * tech_ai_skills_norm +
        PARAMS['AI_FLUENCY_WEIGHTS']['ai_augmented_productivity'] * employee_row['ai_augmented_productivity_norm'] +
        PARAMS['AI_FLUENCY_WEIGHTS']['critical_ai_judgment'] * critical_ai_judgment_norm +
        PARAMS['AI_FLUENCY_WEIGHTS']['ai_learning_velocity'] * ai_learning_velocity_norm
    )
    return ai_fluency * 100 # Scale to 0-100

def _calculate_domain_expertise(employee_row, PARAMS):
    edu_factor = PARAMS['EDUCATION_MAP'].get(employee_row['education_level'], 0.5) # Default to 0.5 if not found
    exp_factor = 1 - np.exp(-PARAMS['DOMAIN_EXPERTISE_GAMMA_EXP'] * employee_row['years_experience'])
    
    specialization_factor = (
        PARAMS['DOMAIN_SPECIALIZATION_WEIGHTS']['portfolio_score'] * employee_row['portfolio_score'] +
        PARAMS['DOMAIN_SPECIALIZATION_WEIGHTS']['recognition_score'] * employee_row['recognition_score'] +
        PARAMS['DOMAIN_SPECIALIZATION_WEIGHTS']['credentials_score'] * employee_row['credentials_score']
    )
    
    # Ensure factors are between 0 and 1 before multiplication
    domain_expertise = np.clip(edu_factor, 0, 1) * np.clip(exp_factor, 0, 1) * np.clip(specialization_factor, 0, 1)
    return domain_expertise * 100 # Scale to 0-100

def _calculate_adaptive_capacity(employee_row, PARAMS):
    # Scores are already 0-100, so normalize to 0-1 for weighted sum, then scale back.
    cognitive_flexibility_norm = employee_row['cognitive_flexibility_score'] / 100.0
    social_emotional_intelligence_norm = employee_row['social_emotional_intelligence_score'] / 100.0
    strategic_career_management_norm = employee_row['strategic_career_management_score'] / 100.0

    adaptive_capacity = PARAMS['ADAPTIVE_CAPACITY_WEIGHT'] * (
        cognitive_flexibility_norm +
        social_emotional_intelligence_norm +
        strategic_career_management_norm
    )
    return adaptive_capacity * 100 # Scale to 0-100

def _calculate_vr_score(employee_row, PARAMS):
    ai_fluency = _calculate_ai_fluency(employee_row, PARAMS)
    domain_expertise = _calculate_domain_expertise(employee_row, PARAMS)
    adaptive_capacity = _calculate_adaptive_capacity(employee_row, PARAMS)

    vr_score = (
        PARAMS['VR_WEIGHTS']['ai_fluency'] * ai_fluency +
        PARAMS['VR_WEIGHTS']['domain_expertise'] * domain_expertise +
        PARAMS['VR_WEIGHTS']['adaptive_capacity'] * adaptive_capacity
    )
    return vr_score, ai_fluency, domain_expertise, adaptive_capacity # Return sub-components too

def _calculate_hr_score(employee_row, df_occupations, PARAMS):
    # Get occupation data for the employee's job role
    job_role = employee_row['job_role']
    occupation_data = df_occupations[df_occupations['job_role'] == job_role].iloc[0]

    # Calculate Base Opportunity Score
    h_base = (
        PARAMS['HR_BASE_WEIGHTS']['ai_enhancement_potential'] * occupation_data['ai_enhancement_potential'] +
        PARAMS['HR_BASE_WEIGHTS']['growth_rate'] * occupation_data['growth_rate'] +
        PARAMS['HR_BASE_WEIGHTS']['wage_premium'] * occupation_data['wage_premium'] +
        PARAMS['HR_BASE_WEIGHTS']['entry_accessibility'] * occupation_data['entry_accessibility']
    )
    h_base_scaled = h_base * 100 # Scale to 0-100 based on these normalized inputs

    # Dynamic Multipliers (simplified for synthetic data)
    # Assume current growth multiplier is 1.0 (no recent change) and remote factor is main contributor
    growth_multiplier = 1.0 # For simplicity, assuming no real-time job posting data
    
    # Regional Multiplier - simplified to only use remote_work_factor contribution
    gamma = 0.2 # From description
    remote_work_factor_contribution = gamma * occupation_data['remote_work_factor']
    regional_multiplier = 1.0 + remote_work_factor_contribution # Assuming local/national demand is equal for simplicity
    
    hr_score = h_base_scaled * growth_multiplier * regional_multiplier
    return np.clip(hr_score, 0, 100) # Ensure it stays within 0-100

def _calculate_alignment_factor(employee_row, occupation_row, PARAMS):
    # Skills Match Score
    match_score = 0
    skill_cols = [f'skill_{chr(97 + i)}' for i in range(10)] # skill_a to skill_j
    req_skill_cols = [f'req_skill_{chr(97 + i)}' for i in range(10)] # req_skill_a to req_skill_j

    for i, skill in enumerate(skill_cols):
        employee_skill = employee_row[skill]
        required_skill = occupation_row[req_skill_cols[i]]
        importance = PARAMS['SKILL_IMPORTANCE'].get(skill, 0.1) # Default importance
        match_score += min(employee_skill, required_skill) * importance
    
    # Max possible match (assuming all skills are 1.0 and summed importance)
    max_possible_match = sum(PARAMS['SKILL_IMPORTANCE'].values())
    
    skills_match_norm = match_score / max_possible_match if max_possible_match > 0 else 0

    # Timing Factor
    years_experience = employee_row['years_experience']
    timing_factor = 1.0
    for (lower, upper), factor in PARAMS['TIMING_FACTOR_YEARS'].items():
        if lower <= years_experience <= upper:
            timing_factor = factor
            break
        elif years_experience > 15: # Handle > 15 years explicitly since upper is np.inf
             timing_factor = PARAMS['TIMING_FACTOR_YEARS'][(15, np.inf)]
             break
    
    alignment_factor = skills_match_norm * timing_factor
    return np.clip(alignment_factor, 0, 1) # Ensure alignment is between 0 and 1

def _calculate_synergy_score(vr_score, hr_score, employee_row, df_occupations, PARAMS):
    job_role = employee_row['job_role']
    occupation_data = df_occupations[df_occupations['job_role'] == job_role].iloc[0]
    alignment_factor = _calculate_alignment_factor(employee_row, occupation_data, PARAMS)
    
    synergy_percent = (vr_score * hr_score / 100) * alignment_factor
    return np.clip(synergy_percent, 0, 100)

def calculate_ai_r_score(employee_row, df_occupations, PARAMS):
    vr_score, ai_fluency, domain_expertise, adaptive_capacity = _calculate_vr_score(employee_row, PARAMS)
    hr_score = _calculate_hr_score(employee_row, df_occupations, PARAMS)
    synergy_score = _calculate_synergy_score(vr_score, hr_score, employee_row, df_occupations, PARAMS)

    ai_r_score = (
        PARAMS['ALPHA'] * vr_score +
        (1 - PARAMS['ALPHA']) * hr_score +
        PARAMS['BETA'] * synergy_score
    )
    return np.clip(ai_r_score, 0, 100), vr_score, hr_score, ai_fluency, domain_expertise, adaptive_capacity

# Calculate initial AI-R scores for all employees
def initialize_ai_r_scores(df_employees, df_occupations, PARAMS):
    results = df_employees.apply(
        lambda row: calculate_ai_r_score(row, df_occupations, PARAMS),
        axis=1, result_type='expand'
    )
    df_employees[['current_ai_r_score', 'vr_score', 'hr_r_score', 'ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score']] = results
    return df_employees

df_employees = initialize_ai_r_scores(df_employees.copy(), df_occupations.copy(), PARAMS.copy())

# --- Dashboard Page Functions ---
def generate_ai_r_report_summary(df_employees_data):
    summary = df_employees_data.groupby(['department', 'job_role'])['current_ai_r_score'].mean().reset_index()
    summary.rename(columns={'current_ai_r_score': 'Average AI-R Score'}, inplace=True)
    return summary.round(2)

def plot_skills_gap_heatmap(df_employees_data, group_by_column):
    vr_sub_components = ['ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score']
    heatmap_data = df_employees_data.groupby(group_by_column)[vr_sub_components].mean()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt=\".1f\", linewidths=.5, ax=ax)
    ax.set_title(f'Average $V^R$ Sub-Component Scores by {group_by_column}')
    ax.set_ylabel(group_by_column)
    ax.set_xlabel('$V^R$ Sub-Component')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig # Return the figure object

# --- What-If Scenario Engine Functions ---
def simulate_pathway_impact(employee_id, pathway_id, completion_rate, mastery_score, df_employees, df_occupations, df_pathways, PARAMS):
    employee_row = df_employees[df_employees['employee_id'] == employee_id].iloc[0].copy()
    pathway_row = df_pathways[df_pathways['pathway_id'] == pathway_id].iloc[0]

    # Calculate impact based on completion and mastery
    impact_factor = completion_rate * mastery_score

    # Update sub-component scores. Ensure they don't exceed 100.
    employee_row['ai_fluency_score'] = min(100, employee_row['ai_fluency_score'] + pathway_row['impact_on_ai_fluency'] * impact_factor)
    employee_row['domain_expertise_score'] = min(100, employee_row['domain_expertise_score'] + pathway_row['impact_on_domain_expertise'] * impact_factor)
    employee_row['adaptive_capacity_score'] = min(100, employee_row['adaptive_capacity_score'] + pathway_row['impact_on_adaptive_capacity'] * impact_factor)

    # Recalculate AI-R with updated scores
    projected_ai_r, _, _, _, _, _ = calculate_ai_r_score(employee_row, df_occupations, PARAMS)
    current_ai_r = df_employees[df_employees['employee_id'] == employee_id]['current_ai_r_score'].iloc[0]
    delta_ai_r = projected_ai_r - current_ai_r
    
    return projected_ai_r, delta_ai_r, pathway_row['pathway_name']

def plot_current_vs_projected_ai_r(current_ai_r, projected_ai_r_list, labels):
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Bars for current AI-R
    ax.bar(['Current AI-R'], [current_ai_r], color='skyblue', label='Current AI-R')
    
    # Bars for projected AI-R
    x_positions = np.arange(len(projected_ai_r_list)) + 1 # Offset for projected bars
    ax.bar([f'Projected ({label})' for label in labels], projected_ai_r_list, color='lightcoral', label='Projected AI-R')
    
    ax.set_ylabel('AI-R Score')
    ax.set_title('Current vs. Projected AI-Readiness Score')
    ax.set_ylim(0, 100)
    ax.legend()
    plt.tight_layout()
    return fig # Return the figure object

# --- Multi-Step Pathway Optimization Functions ---
def optimize_pathway_sequence(employee_id, current_ai_r, df_pathways, T_max_hours, cost_weight_lambda, df_employees, df_occupations, PARAMS):
    employee_data = df_employees[df_employees['employee_id'] == employee_id].iloc[0].copy() # Get a mutable copy
    
    recommended_sequence = []
    total_cost = 0
    total_time_hours = 0
    
    # Use a deep copy for iterative simulations to avoid modifying original df_employees
    temp_employee_state = employee_data.copy()
    temp_ai_r = current_ai_r

    available_pathways = df_pathways.copy()
    completed_pathways = set()

    # Greedy approach: in each step, pick the pathway that gives the best (AI-R_impact - cost_weight*cost) within time limit
    while total_time_hours < T_max_hours and not available_pathways.empty:
        best_pathway = None
        max_score = -np.inf

        for idx, pathway in available_pathways.iterrows():
            # Check prerequisites (simplified: assumes 'None' means no prereq, otherwise check ID)
            prereq = pathway['prerequisites']
            if prereq != 'None' and prereq not in completed_pathways:
                continue # Skip if prerequisites are not met
            
            # Check if adding this pathway exceeds max time
            if total_time_hours + pathway['time_hours'] > T_max_hours:
                continue

            # Simulate impact of this single pathway
            # Create a temporary employee state for this simulation step
            sim_employee_state = temp_employee_state.copy()
            sim_employee_state['ai_fluency_score'] = min(100, sim_employee_state['ai_fluency_score'] + pathway['impact_on_ai_fluency'] * 1.0) # Assume 100% completion/mastery for optimization step
            sim_employee_state['domain_expertise_score'] = min(100, sim_employee_state['domain_expertise_score'] + pathway['impact_on_domain_expertise'] * 1.0)
            sim_employee_state['adaptive_capacity_score'] = min(100, sim_employee_state['adaptive_capacity_score'] + pathway['impact_on_adaptive_capacity'] * 1.0)
            
            projected_ai_r_after_pathway, _, _, _, _, _ = calculate_ai_r_score(sim_employee_state, df_occupations, PARAMS)
            delta_ai_r = projected_ai_r_after_pathway - temp_ai_r

            # Calculate score for this pathway (AI-R improvement minus weighted cost)
            pathway_score = delta_ai_r - cost_weight_lambda * pathway['cost']
            
            if pathway_score > max_score:
                max_score = pathway_score
                best_pathway = pathway
        
        if best_pathway is not None:
            # Add best pathway to sequence and update state
            recommended_sequence.append(best_pathway['pathway_name'])
            completed_pathways.add(best_pathway['pathway_id'])
            total_cost += best_pathway['cost']
            total_time_hours += best_pathway['time_hours']

            # Apply the changes to the temporary employee state for the next iteration
            temp_employee_state['ai_fluency_score'] = min(100, temp_employee_state['ai_fluency_score'] + best_pathway['impact_on_ai_fluency'] * 1.0)
            temp_employee_state['domain_expertise_score'] = min(100, temp_employee_state['domain_expertise_score'] + best_pathway['impact_on_domain_expertise'] * 1.0)
            temp_employee_state['adaptive_capacity_score'] = min(100, temp_employee_state['adaptive_capacity_score'] + best_pathway['impact_on_adaptive_capacity'] * 1.0)
            temp_ai_r, _, _, _, _, _ = calculate_ai_r_score(temp_employee_state, df_occupations, PARAMS)

            # Remove the chosen pathway from available pathways for the next iteration
            available_pathways = available_pathways[available_pathways['pathway_id'] != best_pathway['pathway_id']]
        else:
            # No suitable pathway found in this iteration
            break

    ai_r_improvement = temp_ai_r - current_ai_r

    return {
        "recommended_sequence": recommended_sequence,
        "projected_final_ai_r": temp_ai_r,
        "total_cost": total_cost,
        "total_time_hours": total_time_hours,
        "ai_r_improvement": ai_r_improvement
    }