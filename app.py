
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import ast
# Removed 'from source import *' as it's causing the ModuleNotFoundError.
# All functions and constants previously in 'source.py' are defined below.

# --- Define constants that were likely in source.py ---
# General AI-R Framework weights
ALPHA = 0.5  # Weight for VR in AI-R calculation
BETA = 20.0  # Synergy coefficient

# VR Component Weights
AI_FLUENCY_THETA_WEIGHTS = {  # Weights for AI Fluency sub-factors
    'prompting': 0.2, 'ai_tools': 0.2, 'understanding': 0.15, 'data_literacy': 0.15,
    'ai_augmented_productivity': 0.15, 'critical_ai_judgment': 0.1, 'appropriate_trust_decisions': 0.05
}
GAMMA_EXPERIENCE_DECAY = 0.02  # Decay factor for experience in domain expertise
VR_COMPONENT_WEIGHTS = {  # Weights for VR components (AI-Fluency, Domain-Expertise, Adaptive-Capacity)
    'ai_fluency': 0.4,
    'domain_expertise': 0.4,
    'adaptive_capacity': 0.2
}
# For display purposes in markdown (should ideally be derived from VR_COMPONENT_WEIGHTS)
VR_W1_AI_FLUENCY = VR_COMPONENT_WEIGHTS['ai_fluency']
VR_W2_DOMAIN_EXPERTISE = VR_COMPONENT_WEIGHTS['domain_expertise']
VR_W3_ADAPTIVE_CAPACITY = VR_COMPONENT_WEIGHTS['adaptive_capacity']

# HR Component Weights
HBASE_WEIGHTS = {  # Weights for Hbase components
    'ai_enhancement_potential': 0.4,
    'growth_normalized': 0.3,
    'wage_premium': 0.2,
    'entry_accessibility': 0.1
}
LAMBDA_GROWTH_MULTIPLIER = 1.2  # Multiplier for job growth
GAMMA_REMOTE_WORK = 0.5  # Factor for remote work in regional demand

# Learning Optimization Parameters
MAX_LEARNING_TIME_HOURS = 160  # Default max learning time in hours
MAX_LEARNING_BUDGET_USD = 1500  # Default max learning budget in USD
LAMBDA_COST_WEIGHT = 0.05  # Default cost weight for optimization

# --- Dummy functions that were likely in source.py ---

# Data Generation
def create_simulated_data():
    """Generates dummy CSV files for the application."""
    # Idiosyncratic data (not heavily used in the app directly, but good to have)
    idiosyncratic_df = pd.DataFrame({
        'persona_id': ['Alice'],
        'education_level': ["Master's in Finance"],
        'experience_years': [7],
        'current_skills': [{'Python': 8, 'SQL': 7}], # simplified for dummy
        'ai_fluency_subfactors': [{'prompting': 0.6}], # simplified
        'domain_expertise_subfactors': [{'portfolio': 0.7}], # simplified
        'adaptive_capacity_subfactors': [{'cognitive_flexibility': 0.75}] # simplified
    })
    idiosyncratic_df.to_csv('idiosyncratic_data.csv', index=False)

    # Systematic Opportunity Data
    roles = ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist']
    systematic_data = {
        'role': roles,
        'current_jobs': [1000, 800, 900, 1200],
        'projected_jobs_10yr': [1500, 1300, 1350, 1600],
        'ai_skilled_wage': [180000, 190000, 170000, 165000],
        'median_wage': [120000, 130000, 110000, 100000],
        'education_years_required': [18, 18, 16, 16], # Master's is usually 18 years
        'experience_years_required': [5, 5, 4, 3],
        'ai_enhancement_potential': [0.9, 0.95, 0.85, 0.8]
    }
    systematic_df = pd.DataFrame(systematic_data)
    systematic_df.to_csv('systematic_opportunity_data.csv', index=False)

    # Job Postings Data
    job_postings_data = {
        'role': roles,
        'job_postings_t': [200, 180, 150, 220],
        'job_postings_t_minus_1': [180, 160, 140, 200]
    }
    job_postings_df = pd.DataFrame(job_postings_data)
    job_postings_df.to_csv('job_postings_data.csv', index=False)

    # Regional Demand Data
    regional_demand_data = {
        'role': roles,
        'local_demand': [0.8, 0.9, 0.75, 0.85],
        'national_avg_demand': [0.7, 0.8, 0.7, 0.75],
        'remote_work_factor': [0.6, 0.7, 0.5, 0.65]
    }
    regional_demand_df = pd.DataFrame(regional_demand_data)
    regional_demand_df.to_csv('regional_demand_data.csv', index=False)

    # Skill Requirements
    skill_columns = ['Python', 'SQL', 'ML_basics', 'Risk_Analysis', 'Financial_Modeling',
                     'Data_Viz', 'Quant_Models', 'AI_Ethics', 'GenAI_Tools', 'Cloud_Platforms']
    skill_requirements_data = {
        'role': roles,
        'Python': [9, 9, 8, 8],
        'SQL': [7, 8, 7, 7],
        'ML_basics': [8, 9, 7, 7],
        'Risk_Analysis': [8, 6, 9, 6],
        'Financial_Modeling': [8, 6, 7, 7],
        'Data_Viz': [7, 7, 6, 8],
        'Quant_Models': [9, 8, 7, 7],
        'AI_Ethics': [7, 8, 8, 6],
        'GenAI_Tools': [7, 8, 7, 7],
        'Cloud_Platforms': [7, 8, 7, 7]
    }
    skill_requirements_df = pd.DataFrame(skill_requirements_data)
    skill_requirements_df.to_csv('skill_requirements.csv', index=False)

    # Learning Pathways
    learning_pathways_data = [
        {'pathway_name': 'Advanced Python for Quant Finance', 'type': 'Course', 'estimated_time_hours': 40, 'estimated_cost_usd': 300,
         'skills_gained': {'Python': 2, 'Quant_Models': 1}, 'prerequisites': [],
         'vr_ai_fluency_gain': 0.02, 'vr_domain_expertise_gain': 0.01, 'vr_adaptive_capacity_gain': 0.01},
        {'pathway_name': 'Machine Learning in Finance', 'type': 'Certification', 'estimated_time_hours': 80, 'estimated_cost_usd': 800,
         'skills_gained': {'ML_basics': 3, 'Data_Viz': 1}, 'prerequisites': ['Advanced Python for Quant Finance'],
         'vr_ai_fluency_gain': 0.05, 'vr_domain_expertise_gain': 0.03, 'vr_adaptive_capacity_gain': 0.02},
        {'pathway_name': 'Generative AI Tools for Financial Analysts', 'type': 'Workshop', 'estimated_time_hours': 20, 'estimated_cost_usd': 200,
         'skills_gained': {'GenAI_Tools': 3, 'AI_Ethics': 1}, 'prerequisites': [],
         'vr_ai_fluency_gain': 0.03, 'vr_domain_expertise_gain': 0.01, 'vr_adaptive_capacity_gain': 0.01},
        {'pathway_name': 'Cloud Platforms for Data Science', 'type': 'Course', 'estimated_time_hours': 60, 'estimated_cost_usd': 500,
         'skills_gained': {'Cloud_Platforms': 3}, 'prerequisites': ['Machine Learning in Finance'],
         'vr_ai_fluency_gain': 0.04, 'vr_domain_expertise_gain': 0.01, 'vr_adaptive_capacity_gain': 0.02},
        {'pathway_name': 'AI Ethics and Governance in Finance', 'type': 'Seminar', 'estimated_time_hours': 15, 'estimated_cost_usd': 150,
         'skills_gained': {'AI_Ethics': 2}, 'prerequisites': [],
         'vr_ai_fluency_gain': 0.02, 'vr_domain_expertise_gain': 0.01, 'vr_adaptive_capacity_gain': 0.01},
        {'pathway_name': 'Advanced Quantitative Models for AI', 'type': 'Course', 'estimated_time_hours': 60, 'estimated_cost_usd': 400,
         'skills_gained': {'Quant_Models': 3, 'ML_basics': 1}, 'prerequisites': ['Advanced Python for Quant Finance'],
         'vr_ai_fluency_gain': 0.04, 'vr_domain_expertise_gain': 0.02, 'vr_adaptive_capacity_gain': 0.01},
    ]
    learning_pathways_df = pd.DataFrame(learning_pathways_data)
    # Convert dicts to string representations for CSV, they'll be parsed back with ast.literal_eval
    learning_pathways_df['skills_gained'] = learning_pathways_df['skills_gained'].apply(str)
    learning_pathways_df['prerequisites'] = learning_pathways_df['prerequisites'].apply(str)

    learning_pathways_df.to_csv('learning_pathways.csv', index=False)


# VR Calculation Functions
def calculate_ai_fluency(subfactors, weights):
    """Calculates AI Fluency score from sub-factors."""
    score = sum(subfactors.get(k, 0) * weights.get(k, 0) for k in weights)
    # Normalize to 0-100, assuming max possible score for subfactors (0-1) and weights sum to 1.0
    # If weights sum to 1, then score is already 0-1 range. Convert to 0-100.
    total_weight = sum(weights.values())
    return (score / total_weight) * 100 if total_weight > 0 else 0

def calculate_domain_expertise(education_level, experience_years, subfactors, gamma_decay):
    """Calculates Domain Expertise score."""
    edu_scores = {
        "Master's in Finance": 0.9,
        "PhD in target field": 1.0,
        "Master's in target field": 0.95,
        "Bachelor's in target field": 0.75,
        "Associate's/Certificate": 0.5,
        "HS + significant coursework": 0.3
    }
    edu_score = edu_scores.get(education_level, 0.5)

    exp_score = min(1.0, experience_years / 10.0 + gamma_decay * experience_years) # Simplified
    
    # Subfactors 'portfolio', 'recognition', 'credentials' are already 0-1
    subfactor_score = np.mean(list(subfactors.values())) if subfactors else 0.0

    score = (edu_score * 0.4 + exp_score * 0.3 + subfactor_score * 0.3) * 100
    return min(score, 100.0)

def calculate_adaptive_capacity(subfactors):
    """Calculates Adaptive Capacity score."""
    score = np.mean(list(subfactors.values())) if subfactors else 0.0
    return score * 100

def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, weights):
    """Calculates overall VR score."""
    score = (ai_fluency * weights.get('ai_fluency', 0) +
             domain_expertise * weights.get('domain_expertise', 0) +
             adaptive_capacity * weights.get('adaptive_capacity', 0))
    return score

# HR Calculation Functions
def normalize_growth(growth_rate):
    """Normalizes growth rate to a 0-1 scale."""
    # A simple example: map -0.5 to 0, 1.0 to 1, anything in between linearly
    return max(0, min(1, (growth_rate + 0.5) / 1.5))

def calculate_wage_premium(ai_wage, median_wage):
    """Calculates wage premium."""
    if median_wage > 0:
        premium_ratio = (ai_wage - median_wage) / median_wage
        # Normalize: e.g., 0 premium_ratio -> 0.5, 100% premium_ratio -> 1.0
        return max(0, min(1, premium_ratio * 0.5 + 0.5))
    return 0.5 # Default if median_wage is zero or invalid

def calculate_entry_accessibility(education_years, experience_years):
    """Calculates entry accessibility (higher score for lower requirements)."""
    # Assuming lower years means easier access, normalize inversely
    total_years_required = education_years + experience_years
    # Example: 15 years required might be 1.0 (easy), 30 years might be 0.0 (hard)
    return max(0, min(1, (30 - total_years_required) / 15))

def calculate_hbase(ai_enhancement, growth_normalized, wage_premium, entry_accessibility, weights):
    """Calculates Hbase score."""
    score = (ai_enhancement * weights.get('ai_enhancement_potential', 0) +
             growth_normalized * weights.get('growth_normalized', 0) +
             wage_premium * weights.get('wage_premium', 0) +
             entry_accessibility * weights.get('entry_accessibility', 0))
    # Assuming input factors are 0-1 and weights sum to 1, score is 0-1. Convert to 0-100.
    return score * 100

def calculate_mgrowth(jp_t, jp_t_minus_1, lambda_multiplier):
    """Calculates market growth multiplier."""
    if jp_t_minus_1 > 0:
        growth_ratio = jp_t / jp_t_minus_1
        return 1 + (growth_ratio - 1) * lambda_multiplier
    return 1.0 # No growth or previous data

def calculate_mregional(local_demand, national_avg_demand, remote_work_factor, gamma_remote):
    """Calculates regional market multiplier."""
    demand_ratio = local_demand / national_avg_demand if national_avg_demand > 0 else 1.0
    return demand_ratio * (1 + remote_work_factor * gamma_remote)

def calculate_hr(hbase, mgrowth, mregional):
    """Calculates overall HR score."""
    # HR is assumed to be 0-100. hbase is 0-100. multipliers adjust it.
    return min(100, hbase * mgrowth * mregional)

# Synergy and AI-R Calculation Functions
def calculate_skills_match_score(current_skills, required_skills_row, max_possible_match):
    """Calculates skill match score and identifies gaps.
       Note: max_possible_match is a vestigial parameter in this implementation.
    """
    current_skills_total = 0
    required_skills_total = 0
    skill_gaps = {}
    required_skills_dict = required_skills_row.drop('role', errors='ignore').to_dict()

    for skill, required_level in required_skills_dict.items():
        # The line 'if skill not in current_skills: current_skills[skill] = 0' was removed
        # as current_skills.get(skill, 0) correctly handles missing skills without modifying
        # the original dictionary passed from session state.
        current_level = current_skills.get(skill, 0)
        
        current_skills_total += min(current_level, required_level) # Only count matching part
        required_skills_total += required_level

        if current_level < required_level:
            skill_gaps[skill] = {'current': current_level, 'required': required_level, 'gap': required_level - current_level}
        else:
            skill_gaps[skill] = {'current': current_level, 'required': required_level, 'gap': 0}

    if required_skills_total > 0:
        match_score = current_skills_total / required_skills_total
    else:
        match_score = 0.0 # No skills required

    return match_score, skill_gaps, required_skills_dict, current_skills_total, required_skills_total


def calculate_timing_factor(experience_years):
    """Calculates timing factor based on experience."""
    return max(0.5, min(1.0, experience_years / 15.0)) # Example: up to 15 years gives max 1.0, starts at 0.5

def calculate_alignment(skills_match_score, timing_factor):
    """Calculates alignment score."""
    return (skills_match_score * 0.7 + timing_factor * 0.3) # Simple weighted average, score 0-1

def calculate_synergy(vr_score, hr_score, alignment_score):
    """Calculates synergy score."""
    # VR and HR are assumed 0-100. Alignment 0-1.
    # Synergy is often a bonus. Let's assume it should contribute proportional to alignment and product of VR, HR.
    # The formula (VR * HR / 100) * Alignment / 100 will give a value between 0 and 1,
    # which when multiplied by beta will fit into the AI-R equation (assuming beta scales it to 0-100 range)
    return (vr_score / 100) * (hr_score / 100) * alignment_score * 100 # Normalize VR/HR to 0-1, then multiply by alignment. Result 0-100.

def calculate_air(vr_score, hr_score, synergy_score, alpha, beta):
    """Calculates overall AI-Readiness score."""
    return (alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_score)

# Learning Optimization Functions
def optimize_learning_pathways(
    initial_air_optimal_role, # This is the initial AI-R score for the chosen optimal role
    initial_vr_score, # This is the initial VR score
    current_vr_subscores_normalized, # Current values of AI-Fluency, Domain-Expertise, Adaptive-Capacity
    initial_hr_for_role, # HR score for the chosen optimal role
    learning_pathways_df, max_learning_time_hours, max_learning_budget_usd,
    alpha, beta, lambda_cost_weight, experience_years, current_skills
):
    """
    Optimizes learning pathways based on constraints and AI-R gain.
    Uses a greedy heuristic.
    """
    current_time = 0
    current_cost = 0
    
    # Make copies of mutable objects
    current_skills_after_paths = current_skills.copy()
    
    # Track projected VR sub-scores (0-100)
    projected_ai_fluency = current_vr_subscores_normalized['ai_fluency']
    projected_domain_expertise = current_vr_subscores_normalized['domain_expertise']
    projected_adaptive_capacity = current_vr_subscores_normalized['adaptive_capacity']

    # Need to parse skills_gained and prerequisites from string to dict/list
    learning_pathways_df_copy = learning_pathways_df.copy()
    if learning_pathways_df_copy.shape[0] > 0: # Check if dataframe is not empty
        if isinstance(learning_pathways_df_copy['skills_gained'].iloc[0], str):
            learning_pathways_df_copy['skills_gained'] = learning_pathways_df_copy['skills_gained'].apply(ast.literal_eval)
        if isinstance(learning_pathways_df_copy['prerequisites'].iloc[0], str):
            learning_pathways_df_copy['prerequisites'] = learning_pathways_df_copy['prerequisites'].apply(ast.literal_eval)

    available_paths = learning_pathways_df_copy.to_dict('records')
    recommended_paths = []
    completed_path_names = set()

    # Retrieve target role details from session state for calculations within the loop
    # This block assumes st.session_state['top_role'] is NOT empty, which is checked in the calling function (Tab 4)
    target_role_name = st.session_state['top_role']['Role']
    required_skills_for_role_data = st.session_state['skill_requirements_df'][st.session_state['skill_requirements_df']['role'] == target_role_name]

    if required_skills_for_role_data.empty:
        # If no skill requirements for the target role, no optimization is possible based on skill alignment.
        # This case should ideally be handled before calling this function, but for robustness:
        return ([], 0, 0, initial_air_optimal_role, initial_vr_score, current_vr_subscores_normalized, current_skills_after_paths)

    required_skills_for_role = required_skills_for_role_data.iloc[0]
    max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum()


    for _ in range(len(available_paths) + 1): # Iterate up to the number of available paths to find a best_path
        best_path = None
        best_return = -1e9 # Initialize with a very small number

        for path in available_paths:
            if path['pathway_name'] in completed_path_names:
                continue

            # Check prerequisites
            prereqs_met = all(p in completed_path_names for p in path['prerequisites'])
            if not prereqs_met:
                continue

            # Check if this path can be afforded
            if current_time + path['estimated_time_hours'] > max_learning_time_hours or \
               current_cost + path['estimated_cost_usd'] > max_learning_budget_usd:
                continue

            # Calculate potential VR sub-score gains from this pathway
            temp_ai_fluency = min(100, projected_ai_fluency + path.get('vr_ai_fluency_gain', 0) * 100)
            temp_domain_expertise = min(100, projected_domain_expertise + path.get('vr_domain_expertise_gain', 0) * 100)
            temp_adaptive_capacity = min(100, projected_adaptive_capacity + path.get('vr_adaptive_capacity_gain', 0) * 100)

            # Recalculate VR with potential gains
            temp_vr = calculate_vr(
                temp_ai_fluency, temp_domain_expertise, temp_adaptive_capacity, VR_COMPONENT_WEIGHTS
            )

            # Simulate skills gained for alignment calculation
            temp_skills = current_skills_after_paths.copy() # Start from current accumulated skills
            for skill, gain in path['skills_gained'].items():
                temp_skills[skill] = min(10, temp_skills.get(skill, 0) + gain)

            # Calculate alignment and synergy based on improved skills & VR
            
            skills_match_post_path, _, _, _, _ = calculate_skills_match_score(
                temp_skills,
                required_skills_for_role,
                max_possible_match_for_role
            )
            timing_factor_post_path = calculate_timing_factor(experience_years)
            alignment_post_path = calculate_alignment(skills_match_post_path, timing_factor_post_path)
            synergy_post_path = calculate_synergy(temp_vr, initial_hr_for_role, alignment_post_path)
            projected_air_candidate = calculate_air(temp_vr, initial_hr_for_role, synergy_post_path, alpha, beta)
            
            # Calculate return (AI-R gain per unit of weighted time/cost)
            air_gain = projected_air_candidate - initial_air_optimal_role
            weighted_cost_time = (path['estimated_cost_usd'] * lambda_cost_weight) + path['estimated_time_hours']
            
            if weighted_cost_time > 0:
                current_return = air_gain / weighted_cost_time
            else:
                current_return = air_gain * 1000 if air_gain > 0 else air_gain # Assign a high return if cost/time is zero and gain is positive

            if current_return > best_return:
                best_return = current_return
                best_path = path

        if best_path:
            recommended_paths.append(best_path)
            completed_path_names.add(best_path['pathway_name'])
            current_time += best_path['estimated_time_hours']
            current_cost += best_path['estimated_cost_usd']

            # Update actual projected VR subfactors and skills for next iteration
            projected_ai_fluency = min(100, projected_ai_fluency + best_path.get('vr_ai_fluency_gain', 0) * 100)
            projected_domain_expertise = min(100, projected_domain_expertise + best_path.get('vr_domain_expertise_gain', 0) * 100)
            projected_adaptive_capacity = min(100, projected_adaptive_capacity + best_path.get('vr_adaptive_capacity_gain', 0) * 100)

            for skill, gain in best_path['skills_gained'].items():
                current_skills_after_paths[skill] = min(10, current_skills_after_paths.get(skill, 0) + gain)
            
            # Remove chosen path from available to avoid re-selecting it in the same iteration
            available_paths = [p for p in available_paths if p['pathway_name'] != best_path['pathway_name']]
        else:
            break # No more paths can be added within constraints or no more beneficial paths

    # Final VR calculation after all paths
    final_vr_subscores_normalized = {
        'ai_fluency': projected_ai_fluency,
        'domain_expertise': projected_domain_expertise,
        'adaptive_capacity': projected_adaptive_capacity
    }
    final_vr = calculate_vr(
        projected_ai_fluency, projected_domain_expertise, projected_adaptive_capacity, VR_COMPONENT_WEIGHTS
    )

    # Final AI-R calculation
    # required_skills_for_role_data and max_possible_match_for_role are already defined above
    
    final_skills_match, _, _, _, _ = calculate_skills_match_score(
        current_skills_after_paths,
        required_skills_for_role,
        max_possible_match_for_role
    )
    final_timing_factor = calculate_timing_factor(experience_years)
    final_alignment = calculate_alignment(final_skills_match, final_timing_factor)
    
    final_synergy = calculate_synergy(final_vr, initial_hr_for_role, final_alignment)
    projected_air = calculate_air(final_vr, initial_hr_for_role, final_synergy, alpha, beta)

    return (recommended_paths, current_time, current_cost, projected_air,
            final_vr, final_vr_subscores_normalized, current_skills_after_paths)


def run_what_if_scenario(
    initial_vr_score, current_vr_subscores_normalized, current_skills,
    target_role_name, hr_scores, skill_requirements_df,
    scenario_pathways, experience_years, alpha, beta
):
    """
    Runs a "what-if" scenario for a given role and learning pathways.
    Returns projected AI-R, total time, total cost, and projected VR components.
    """
    projected_ai_fluency = current_vr_subscores_normalized['ai_fluency']
    projected_domain_expertise = current_vr_subscores_normalized['domain_expertise']
    projected_adaptive_capacity = current_vr_subscores_normalized['adaptive_capacity']
    
    current_skills_after_paths = current_skills.copy()
    total_time = 0
    total_cost = 0

    # Ensure skills_gained and prerequisites are parsed if they are strings
    for path in scenario_pathways:
        if isinstance(path['skills_gained'], str):
            path['skills_gained'] = ast.literal_eval(path['skills_gained'])
        if isinstance(path['prerequisites'], str):
            path['prerequisites'] = ast.literal_eval(path['prerequisites'])

    for path in scenario_pathways:
        total_time += path['estimated_time_hours']
        total_cost += path['estimated_cost_usd']

        projected_ai_fluency = min(100, projected_ai_fluency + path.get('vr_ai_fluency_gain', 0) * 100)
        projected_domain_expertise = min(100, projected_domain_expertise + path.get('vr_domain_expertise_gain', 0) * 100)
        projected_adaptive_capacity = min(100, projected_adaptive_capacity + path.get('vr_adaptive_capacity_gain', 0) * 100)

        for skill, gain in path['skills_gained'].items():
            current_skills_after_paths[skill] = min(10, current_skills_after_paths.get(skill, 0) + gain)

    # Final VR calculation after all paths
    final_vr_subscores_normalized = {
        'ai_fluency': projected_ai_fluency,
        'domain_expertise': projected_domain_expertise,
        'adaptive_capacity': projected_adaptive_capacity
    }
    final_vr = calculate_vr(
        projected_ai_fluency, projected_domain_expertise, projected_adaptive_capacity, VR_COMPONENT_WEIGHTS
    )

    # HR for the target role
    hr_for_target_role = hr_scores.get(target_role_name, 0)

    # Final AI-R calculation
    required_skills_for_role_data = skill_requirements_df[skill_requirements_df['role'] == target_role_name]
    
    if required_skills_for_role_data.empty:
        # Fallback if no skill requirements found for the target role
        final_skills_match = 0
        final_timing_factor = 0
        final_alignment = 0
    else:
        required_skills_for_role = required_skills_for_role_data.iloc[0]
        max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum()

        final_skills_match, _, _, _, _ = calculate_skills_match_score(
            current_skills_after_paths,
            required_skills_for_role,
            max_possible_match_for_role
        )
        final_timing_factor = calculate_timing_factor(experience_years)
        final_alignment = calculate_alignment(final_skills_match, final_timing_factor)
    
    final_synergy = calculate_synergy(final_vr, hr_for_target_role, final_alignment)
    projected_air = calculate_air(final_vr, hr_for_target_role, final_synergy, alpha, beta)

    return projected_air, total_time, total_cost, final_vr, hr_for_target_role, final_synergy


# Set page config first
st.set_page_config(page_title="QuLab: AI Readiness score", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: AI Readiness score")
st.divider()

# Set plot style globally for the app
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

def initialize_session_state():
    # Create simulated data if not exists (function from source.py)
    if 'idiosyncratic_df' not in st.session_state:
        create_simulated_data() # Ensure data files exist
        st.session_state['idiosyncratic_df'] = pd.read_csv('idiosyncratic_data.csv')
        st.session_state['systematic_df'] = pd.read_csv('systematic_opportunity_data.csv')
        st.session_state['job_postings_df'] = pd.read_csv('job_postings_data.csv')
        st.session_state['regional_demand_df'] = pd.read_csv('regional_demand_data.csv')
        
        # Read skill requirements and parse skills_gained/prerequisites which might be stored as string dict/list
        skill_req_df = pd.read_csv('skill_requirements.csv')
        st.session_state['skill_requirements_df'] = skill_req_df

        learning_paths_df = pd.read_csv('learning_pathways.csv')
        # Ensure skills_gained and prerequisites are parsed from string to dict/list
        # Apply ast.literal_eval only if the column contains string representations of lists/dicts
        if learning_paths_df.shape[0] > 0 and isinstance(learning_paths_df['skills_gained'].iloc[0], str):
             learning_paths_df['skills_gained'] = learning_paths_df['skills_gained'].apply(ast.literal_eval)
        if learning_paths_df.shape[0] > 0 and isinstance(learning_paths_df['prerequisites'].iloc[0], str):
            learning_paths_df['prerequisites'] = learning_paths_df['prerequisites'].apply(ast.literal_eval)

        st.session_state['learning_pathways_df'] = learning_paths_df

    # User Profile Data (mutable)
    if 'alice_profile' not in st.session_state:
        st.session_state['alice_profile'] = {
            'persona_id': 'Alice',
            'education_level': "Master's in Finance",
            'experience_years': 7,
            'current_skills': {
                'Python': 8, 'SQL': 7, 'ML_basics': 6, 'Risk_Analysis': 9,
                'Financial_Modeling': 8, 'Data_Viz': 7, 'Quant_Models': 6,
                'AI_Ethics': 5, 'GenAI_Tools': 4, 'Cloud_Platforms': 5
            },
            'ai_fluency_subfactors': {
                'prompting': 0.6, 'ai_tools': 0.5, 'understanding': 0.6, 'data_literacy': 0.7,
                'ai_augmented_productivity': 0.7, 'critical_ai_judgment': 0.65, 'appropriate_trust_decisions': 0.75,
                'proficiency_gain': 0.10, 'hours_invested': 50
            },
            'domain_expertise_subfactors': {
                'portfolio': 0.7, 'recognition': 0.6, 'credentials': 0.8
            },
            'adaptive_capacity_subfactors': {
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
    if 'hr_scores' not in st.session_state: st.session_state['hr_scores'] = {}
    if 'air_df' not in st.session_state: st.session_state['air_df'] = pd.DataFrame()
    if 'all_skill_gaps' not in st.session_state: st.session_state['all_skill_gaps'] = {}
    # Changed type of 'top_role' to pd.Series for consistency with .loc[idxmax()] result
    if 'top_role' not in st.session_state: st.session_state['top_role'] = pd.Series(dtype='object') 

    # Optimization Parameters
    if 'max_learning_time_hours' not in st.session_state: st.session_state['max_learning_time_hours'] = MAX_LEARNING_TIME_HOURS
    if 'max_learning_budget_usd' not in st.session_state: st.session_state['max_learning_budget_usd'] = MAX_LEARNING_BUDGET_USD
    if 'lambda_cost_weight' not in st.session_state: st.session_state['lambda_cost_weight'] = LAMBDA_COST_WEIGHT

    # Optimization Results
    if 'recommended_paths' not in st.session_state: st.session_state['recommended_paths'] = []
    if 'total_time_invested' not in st.session_state: st.session_state['total_time_invested'] = 0
    if 'total_cost_invested' not in st.session_state: st.session_state['total_cost_invested'] = 0
    if 'projected_air' not in st.session_state: st.session_state['projected_air'] = None
    if 'initial_air_optimal_role' not in st.session_state: st.session_state['initial_air_optimal_role'] = None
    if 'final_vr_after_paths' not in st.session_state: st.session_state['final_vr_after_paths'] = None
    if 'final_vr_subscores_normalized' not in st.session_state: st.session_state['final_vr_subscores_normalized'] = {}
    if 'final_skills_after_paths' not in st.session_state: st.session_state['final_skills_after_paths'] = {}

    # Scenario Analysis Results
    if 'scenario_results_df' not in st.session_state: st.session_state['scenario_results_df'] = pd.DataFrame()
    if 'roi_df' not in st.session_state: st.session_state['roi_df'] = pd.DataFrame()

# Call to initialize session state
initialize_session_state()

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

    # Fixed syntax warnings with raw strings (r"")
    st.markdown(r"$$AI-R_{i,t} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{i}^R(t) + \beta \cdot \text{Synergy}\%(V_i^R, H_{i}^R)$$")
    st.markdown(f"where:")
    st.markdown(r"$$V_i^R(t)$$: Idiosyncratic Readiness (individual capability), normalized to $$[0, 100]$$.")
    st.markdown(r"$$H_i^R(t)$$: Systematic Opportunity (market demand) for the target occupation, normalized to $$[0, 100]$$.")
    st.markdown(r"$$\alpha \in [0,1]$$: Weight on individual vs. market factors. Default $$\alpha = {ALPHA}$$.")
    st.markdown(r"$$\beta > 0$$: Synergy coefficient, capturing multiplicative benefits. Default $$\beta = {BETA}$$.")
    st.markdown(r"$$\text{Synergy}\% \in [0,100]$$: Percentage units.")
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
        edu_options = ['Master\'s in Finance', 'PhD in target field', 'Master\'s in target field', 'Bachelor\'s in target field', 'Associate\'s/Certificate', 'HS + significant coursework']
        st.session_state['alice_profile']['education_level'] = st.selectbox(
            "Education Level",
            edu_options,
            index=edu_options.index(st.session_state['alice_profile']['education_level'])
        )
        st.session_state['alice_profile']['experience_years'] = st.number_input(
            "Years of Experience",
            min_value=0, max_value=40, value=st.session_state['alice_profile']['experience_years']
        )
        st.markdown("---")
        st.markdown(f"**AI-Fluency Sub-Factors (Scores 0-1)**")
        # Ensure all expected AI fluency subfactors from AI_FLUENCY_THETA_WEIGHTS are present in the profile
        for k in AI_FLUENCY_THETA_WEIGHTS.keys():
            if k not in st.session_state['alice_profile']['ai_fluency_subfactors']:
                st.session_state['alice_profile']['ai_fluency_subfactors'][k] = 0.0 # Default missing subfactor

        # Filter out 'proficiency_gain' and 'hours_invested' if they are present but not part of calculation
        for k, v in list(st.session_state['alice_profile']['ai_fluency_subfactors'].items()): # Iterate over copy if modifying dict
            if k not in AI_FLUENCY_THETA_WEIGHTS: # Only show sliders for actual AI_FLUENCY_THETA_WEIGHTS
                continue # Skip extra items
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
        # Ensure all skill requirements are present in current_skills, add if missing
        # This assumes 'skill_requirements_df' is populated by create_simulated_data()
        if not st.session_state['skill_requirements_df'].empty:
            all_required_skills = st.session_state['skill_requirements_df'].columns.drop('role').tolist()
            for skill in all_required_skills:
                if skill not in st.session_state['alice_profile']['current_skills']:
                    st.session_state['alice_profile']['current_skills'][skill] = 0 # Default missing skill to 0
        
        # Sort skills for consistent display
        sorted_skills = dict(sorted(st.session_state['alice_profile']['current_skills'].items()))
        for k, v in sorted_skills.items():
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
        # Filter out non-subfactor keys before passing to calculate_ai_fluency
        ai_fluency_calc_subfactors = {k: v for k, v in st.session_state['alice_profile']['ai_fluency_subfactors'].items() if k in AI_FLUENCY_THETA_WEIGHTS}
        st.session_state['alice_ai_fluency_score'] = calculate_ai_fluency(ai_fluency_calc_subfactors, AI_FLUENCY_THETA_WEIGHTS)
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
            role_data_df = st.session_state['systematic_df'][st.session_state['systematic_df']['role'] == role]
            if role_data_df.empty:
                st.warning(f"No systematic data found for role: {role}. Skipping HR calculation for this role.")
                continue
            role_data = role_data_df.iloc[0]

            jp_role_data_df = st.session_state['job_postings_df'][st.session_state['job_postings_df']['role'] == role]
            if jp_role_data_df.empty:
                st.warning(f"No job posting data found for role: {role}. Skipping HR calculation for this role.")
                continue
            jp_role_data = jp_role_data_df.iloc[-1] # take latest

            rd_role_data_df = st.session_state['regional_demand_df'][st.session_state['regional_demand_df']['role'] == role]
            if rd_role_data_df.empty:
                st.warning(f"No regional demand data found for role: {role}. Skipping HR calculation for this role.")
                continue
            rd_role_data = rd_role_data_df.iloc[0]

            growth_rate = (role_data['projected_jobs_10yr'] - role_data['current_jobs']) / role_data['current_jobs'] if role_data['current_jobs'] > 0 else 0
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
            mregional = calculate_mregional(rd_role_data['local_demand'], rd_role_data['national_avg_demand'], rd_role_data['remote_work_factor'], GAMMA_REMOTE_WORK)

            hr_score = calculate_hr(hbase, mgrowth, mregional)
            hr_scores_temp[role] = hr_score
        st.session_state['hr_scores'] = hr_scores_temp

        st.success("Initial Readiness & Opportunity calculated! Proceed to the next tab.")
        st.rerun()

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
        # Fixed syntax warning with raw string
        st.markdown(r"$$V^R(t) = w_1 \cdot \text{AI‑Fluency}_i(t) + w_2 \cdot \text{Domain‑Expertise}_i(t) + w_3 \cdot \text{Adaptive‑Capacity}_i(t)$$")
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
        # Fixed syntax warning with raw string
        st.markdown(r"$$H^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$")
        st.markdown(r"where $H_{\text{base}}(o)$ is the base opportunity score, $M_{\text{growth}}(t)$ is the growth multiplier, and $M_{\text{regional}}(t)$ is the regional multiplier.")

        st.dataframe(pd.DataFrame(st.session_state['hr_scores'].items(), columns=['Role', 'HR_Score']).round(2).set_index('Role'))
        st.markdown(f"Alice's Systematic Opportunity ($H^R$) scores vary significantly across her target roles. For example:")
        st.markdown(f"*   **AI Quant Analyst:** A high score, potentially due to strong AI-enhancement potential and significant wage premiums.")
        st.markdown(f"*   **Financial Data Scientist:** While robust, this role might have a slightly lower $H^R$ compared to the more specialized AI Quant/ML roles, possibly due to broader applicability or higher entry accessibility.")
        st.markdown(f"This analysis helps Alice understand where the market opportunities lie, complementing her individual readiness.")

        st.subheader("2.3. Overall AI-Readiness ($AI-R$) Scores and Skill Gaps")
        st.markdown(f"The overall AI-Readiness Score is calculated by combining $V^R$ and $H^R$ with a synergy factor:")
        # Fixed syntax warning with raw string
        st.markdown(r"$$AI-R_{i,t} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{i}^R(t) + \beta \cdot \text{Synergy}\%(V_i^R, H_{i}^R)$$")
        st.markdown(f"where $\alpha={ALPHA}$ and $\beta={BETA}$.")
        st.markdown(f"The Synergy Function is defined as:")
        # Fixed syntax warning with raw string
        st.markdown(r"$$\text{Synergy}\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times \text{Alignment}_i$$")
        st.markdown(r"where $V^R$ and $H^R$ are normalized to $[0, 100]$, and $\text{Alignment}_i \in [0,1]$ combines skill match and timing.")

        # Recalculate AI-R for display and consistency
        air_results = []
        all_skill_gaps_temp = {}
        for role in st.session_state['target_roles']:
            current_hr_score = st.session_state['hr_scores'].get(role, 0)
            
            # Check if skill requirements exist for the role
            required_skills_data_df = st.session_state['skill_requirements_df'][st.session_state['skill_requirements_df']['role'] == role]
            if required_skills_data_df.empty:
                st.warning(f"No skill requirements found for role: {role}. Cannot calculate skill gaps or AI-R for this role.")
                continue

            required_skills_for_role = required_skills_data_df.iloc[0]
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
            
            top_role_skills_gaps = st.session_state['all_skill_gaps'].get(st.session_state['top_role']['Role'], {})
            skills_df = pd.DataFrame(top_role_skills_gaps).T.reset_index().rename(columns={'index': 'Skill'})
            
            # Filter skills that have a non-zero gap for more relevant visualization
            skills_with_gaps_df = skills_df[skills_df['gap'] > 0]
            if not skills_with_gaps_df.empty:
                labels = skills_with_gaps_df['Skill'].tolist()
                current_levels = skills_with_gaps_df['current'].tolist()
                required_levels = skills_with_gaps_df['required'].tolist()
            else:
                # If no gaps, plot all skills just to show something, or show a message
                if not skills_df.empty:
                    labels = skills_df['Skill'].tolist()
                    current_levels = skills_df['current'].tolist()
                    required_levels = skills_df['required'].tolist()
                    st.info(f"No significant skill gaps identified for {st.session_state['top_role']['Role']}.")
                else:
                    labels = [] # No skills to plot
                    current_levels = []
                    required_levels = []
                    st.info(f"No skill data available for {st.session_state['top_role']['Role']}.")


            # Add first value to the end to close the radar chart, only if there are skills
            if labels: # FIX: Added 'if labels:' to prevent IndexError on empty list
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
            else:
                st.info("No skills to display for radar chart.")


# --- Tab 4: Learning Optimization ---
with tab4:
    st.header("3. Optimizing Learning Pathways for Career Growth")
    st.markdown(f"Based on her initial AI-R scores and identified skill gaps, Alice wants to invest in learning to maximize her career prospects.")
    st.markdown(f"However, her time and budget are constrained. This section recommends a sequence of learning activities that maximize her projected AI-R gain under these specified resource constraints.")
    # Fixed syntax warnings with raw strings
    st.markdown(r"$$ \max_{P_1,...,P_K} (AI‑R_{\text{proj}} - AI‑R_{\text{current}}) - \lambda \cdot \sum_{k=1}^K \text{Cost}(p_k) $$")
    st.markdown(f"subject to:")
    st.markdown(r"$$ \sum_{k=1}^K \text{Time}(p_k) \le T_{\text{max}} $$")
    st.markdown(r"$$ \sum_{k=1}^K \text{Cost}(p_k) \le B_{\text{max}} $$")
    st.markdown(r"$$ p_k \in P_{\text{feasible}} $$")
    st.markdown(r"$$ \text{Prerequisites}(p_k) \subseteq \{P_1,...,P_{k-1}\} $$")
    # Fixed syntax warning with raw string
    st.markdown(r"where $AI‑R_{\text{proj}}$ is the projected AI-R after completing pathways, $AI‑R_{\text{current}}$ is her initial AI-R, $\lambda$ is `LAMBDA_COST_WEIGHT`, $T_{\text{max}}$ is `MAX_LEARNING_TIME_HOURS`, and $B_{\text{max}}$ is `MAX_LEARNING_BUDGET_USD`.")
    st.markdown(f"For this demonstration, we'll use a greedy heuristic: selecting pathways one by one that offer the highest 'return' (AI-R point gain per unit of weighted time/cost) until constraints are met, respecting prerequisites.")

    if st.session_state['top_role'].empty or st.session_state['air_df'].empty: # Also check if air_df is empty to ensure top_role is valid
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
            # Ensure top_role is valid before proceeding
            if st.session_state['top_role'].empty:
                 st.error("Top role not identified or invalid. Please ensure 'Opportunity Evaluation' tab is completed and a top role is identified.") # Clarified error message
                 st.stop() # Stop execution to prevent further errors

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
                st.session_state['initial_air_optimal_role'],
                st.session_state['alice_vr_score'], # Pass initial VR score for baseline
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
            st.rerun()
        
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

        # Safely determine default index for scenario_target_role
        default_role_index = 0
        if not st.session_state['top_role'].empty and st.session_state['top_role']['Role'] in all_roles_for_scenario:
            try:
                default_role_index = all_roles_for_scenario.index(st.session_state['top_role']['Role'])
            except ValueError:
                default_role_index = 0 # Fallback if top_role not in list
        elif not all_roles_for_scenario: # if list of all roles is empty
            default_role_index = None # indicate no roles to select, though create_simulated_data ensures it's not empty
        
        scenario_col1, scenario_col2 = st.columns(2)
        with scenario_col1:
            scenario_target_role = st.selectbox(
                "Select a Target Role for this Scenario",
                options=all_roles_for_scenario,
                index=default_role_index,
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
            elif not scenario_target_role:
                 st.warning("Please select a target role for the custom scenario.")
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

                # Initialize scenario_results_list for this run
                scenario_results_list = []
                
                # Retrieve current scenario_results_df to prevent adding duplicates on rerun
                current_scenario_names = st.session_state['scenario_results_df']['Scenario'].values.tolist() if not st.session_state['scenario_results_df'].empty else []

                # Include the optimal pathway as a baseline scenario if available and not already added
                if st.session_state['recommended_paths'] and not st.session_state['top_role'].empty:
                    optimal_scenario_name = 'Optimized for ' + st.session_state['top_role']['Role']
                    if optimal_scenario_name not in current_scenario_names:
                        scenario_results_list.append({
                            'Scenario': optimal_scenario_name,
                            'Target Role': st.session_state['top_role']['Role'],
                            'Projected AI-R': st.session_state['projected_air'],
                            'Projected VR': st.session_state['final_vr_after_paths'],
                            'HR': st.session_state['top_role']['HR_Score'],
                            'Time (h)': st.session_state['total_time_invested'],
                            'Cost ($)': st.session_state['total_cost_invested']
                        })
                
                # Add the custom scenario, ensuring it's not a duplicate if run multiple times without changing name
                custom_scenario_name = 'Custom Scenario'
                if custom_scenario_name in current_scenario_names:
                    # If custom scenario already exists, create a new one with a distinct name
                    custom_scenario_name = f'Custom Scenario ({pd.Timestamp.now().strftime("%H%M%S")})'

                scenario_results_list.append({
                    'Scenario': custom_scenario_name,
                    'Target Role': scenario_target_role,
                    'Projected AI-R': projected_air_custom,
                    'Projected VR': projected_vr_custom,
                    'HR': hr_custom,
                    'Time (h)': time_custom,
                    'Cost ($)': cost_custom
                })
                
                st.session_state['scenario_results_df'] = pd.concat([st.session_state['scenario_results_df'], pd.DataFrame(scenario_results_list)], ignore_index=True).drop_duplicates(subset=['Scenario', 'Target Role']).round(2)


                # Calculate ROI for scenarios
                roi_data = []
                for index, row in st.session_state['scenario_results_df'].iterrows():
                    initial_air = 0 # Default fallback
                    # Try to get initial AI-R from air_df for the specific target role
                    if not st.session_state['air_df'].empty and row['Target Role'] in st.session_state['air_df']['Role'].values:
                         initial_air = st.session_state['air_df'][st.session_state['air_df']['Role'] == row['Target Role']]['AI_R_Score'].iloc[0]
                    
                    air_gain = row['Projected AI-R'] - initial_air
                    
                    # Ensure denominators are not zero
                    # Use a small epsilon to prevent division by zero for investment factor if time/cost are 0
                    investment_factor = (row['Cost ($)'] * st.session_state['lambda_cost_weight']) + row['Time (h)']
                    
                    if investment_factor > 0:
                        roi = air_gain / investment_factor
                    else:
                        roi = air_gain # If no investment, gain is pure ROI, or 0 if gain is 0
                    
                    roi_data.append({'Scenario': row['Scenario'], 'AI-R Gain': air_gain, 'Investment Score': investment_factor, 'ROI': roi})
                
                # Update ROI dataframe, dropping duplicates if they arise from scenario management
                st.session_state['roi_df'] = pd.DataFrame(roi_data).drop_duplicates(subset=['Scenario']).round(2)

                st.success("Custom scenario analysis complete!")
                st.rerun()
        
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
            # Ensure top_role is valid before accessing its elements
            if not st.session_state['top_role'].empty and ('Optimized for ' + st.session_state['top_role']['Role']) in st.session_state['scenario_results_df']['Scenario'].values:
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
        if st.session_state['hr_scores']:
            for role, score in st.session_state['hr_scores'].items():
                st.markdown(f"  *   {role}: {score:.2f}")
        else:
            st.markdown("  *   No HR scores calculated yet.")

        if not st.session_state['top_role'].empty:
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
            if st.session_state['top_role']['Role'] in st.session_state['all_skill_gaps']:
                top_role_skills_gaps_df = pd.DataFrame(st.session_state['all_skill_gaps'][st.session_state['top_role']['Role']]).T
                top_role_skills_gaps_df['Gap'] = top_role_skills_gaps_df['required'] - top_role_skills_gaps_df['current']
                st.dataframe(top_role_skills_gaps_df[top_role_skills_gaps_df['Gap'] > 0].sort_values(by='Gap', ascending=False))
                st.markdown(f"(Skills with a positive 'Gap' need development)")
            else:
                st.markdown(f"No skill gaps calculated for {st.session_state['top_role']['Role']}.")

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
                # Dynamically set insight based on top_role
                optimal_role_name = st.session_state['top_role']['Role']
                st.markdown(f"Insight: The 'Optimized for {optimal_role_name}' pathway (original recommendation) yields the highest projected AI-R, indicating it's the most effective strategy for maximizing Alice's career opportunity.")
                st.markdown("The 'Return on Learning Investment' chart suggests prioritizing pathways with high impact on core VR components that align with high HR roles.")
            else:
                st.markdown(f"*(Run 'What-If Analysis' to see comparative scenarios)*")

    st.markdown("---")
    st.markdown("**--- End of Report ---**")
