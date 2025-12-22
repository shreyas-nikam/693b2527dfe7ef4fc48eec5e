
import streamlit as st
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import networkx as nx

st.set_page_config(page_title="QuLab: AI Readiness score", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: AI Readiness score")
st.divider()

# Your code starts here
st.markdown("""
In this lab, we embark on a journey to understand and quantify "AI Readiness" within an organization's workforce.
The **AI-Readiness & Upskilling Strategizer** is a powerful Streamlit application designed for AI Workforce leaders and Human Resources executives.
It offers an intuitive interface to assess and enhance the AI-readiness of an organization's workforce by implementing a novel parametric framework.
This framework quantifies an individual's preparedness for AI-enabled careers, enabling data-driven strategic workforce planning.

**Through this application, you will:**
*   **Understand the AI-Readiness Score (AI-R):** Discover how AI-R decomposes into Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and Synergy, and how these components are calculated.
*   **Perform Skills Gap Analysis:** Identify collective strengths and weaknesses across $V^R$ sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity) at various organizational levels.
*   **Simulate Impact with "What-If" Scenarios:** Model the effect of different training programs and learning pathways on individual and cohort AI-R scores.
*   **Optimize Learning Pathways:** Explore strategies for sequencing multi-step learning pathways while considering real-world constraints like cost and time.
*   **Generate Strategic Recommendations:** Access comprehensive workforce AI-Readiness reports and actionable recommendations for targeted upskilling initiatives.
""")

# --- Global Parameters and Session State Initialization ---
if 'PARAMS' not in st.session_state:
    st.session_state.PARAMS = {
        # Global AI-R weights
        'alpha': 0.6,
        'beta': 0.1,

        # HR_Base_Weights
        'hr_base_weights': {
            'w_ai_enhancement': 0.3,
            'w_growth_normalized': 0.3,
            'w_wage_premium': 0.2,
            'w_entry_accessibility': 0.2
        },

        # Dynamic Multipliers
        'lambda_growth': 0.5,
        'gamma_regional': 0.4, # Regional multiplier weight

        # AI-Fluency Sub-component Weights (theta_ai_fluency_weights)
        'theta_ai_fluency_weights': {
            't_technical_ai_skills': 0.3,
            't_ai_augmented_productivity': 0.3,
            't_critical_ai_judgment': 0.2,
            't_ai_learning_velocity': 0.2
        },

        # Domain Specialization Weights (domain_specialization_weights)
        'domain_specialization_weights': {
            'w_portfolio': 0.4,
            'w_recognition': 0.3,
            'w_credentials': 0.3
        },
        'gamma_exp': 0.1, # Experience decay rate

        # VR Component Weights (vr_component_weights)
        'vr_component_weights': {
            'w_ai_fluency': 0.4,
            'w_domain_expertise': 0.4,
            'w_adaptive_capacity': 0.2
        }
    }

if 'df_employees' not in st.session_state:
    st.session_state.df_employees = pd.DataFrame()
if 'df_occupations' not in st.session_state:
    st.session_state.df_occupations = pd.DataFrame()
if 'df_pathways' not in st.session_state:
    st.session_state.df_pathways = pd.DataFrame()

# --- Global Functions ---

@st.cache_data(ttl="2h")
def generate_synthetic_employees(num_employees=100):
    np.random.seed(42)
    random.seed(42)

    employee_data = []
    job_roles = ['Data Scientist', 'Software Engineer', 'Marketing Specialist', 'HR Business Partner', 'Financial Analyst', 'Project Manager']
    departments = ['R&D', 'Engineering', 'Marketing', 'Human Resources', 'Finance', 'Operations']
    education_levels = ['High School', 'Bachelor\'s', 'Master\'s', 'PhD']
    # Skills for 'Alignment' calculation
    skill_set = ['Python', 'SQL', 'Machine Learning', 'Deep Learning', 'Data Analysis', 'Communication', 'Project Management', 'Cloud Computing', 'Marketing Strategy', 'Recruitment', 'Financial Modeling', 'Risk Management']

    for i in range(num_employees):
        job_role = random.choice(job_roles)
        department = random.choice(departments)
        education = random.choice(education_levels)
        years_experience = np.random.randint(1, 20)
        
        # VR sub-components (0-100 scale)
        prompting = np.random.uniform(50, 95)
        ai_tools = np.random.uniform(40, 90)
        ai_understanding = np.random.uniform(45, 90)
        data_literacy = np.random.uniform(50, 95)

        output_quality_with_ai = np.random.uniform(0.7, 1.2) # multiplier
        output_quality_without_ai = np.random.uniform(0.5, 1.0)
        time_without_ai = np.random.uniform(1.0, 2.0)
        time_with_ai = np.random.uniform(0.4, 1.0)

        errors_caught = np.random.randint(1, 10)
        total_ai_errors = np.random.randint(5, 15)
        appropriate_trust_decisions = np.random.randint(5, 15)
        total_decisions = np.random.randint(10, 20)

        delta_proficiency = np.random.uniform(5, 20)
        delta_t = np.random.uniform(0.5, 3)
        hours_invested = np.random.uniform(10, 100)
        
        cognitive_capacity = np.random.uniform(0.6, 0.95)
        social_capacity = np.random.uniform(0.6, 0.95)
        strategic_capacity = np.random.uniform(0.6, 0.95)

        portfolio_score = np.random.uniform(0.3, 0.9) # for specialization_depth
        recognition_score = np.random.uniform(0.3, 0.9)
        credentials_score = np.random.uniform(0.3, 0.9)

        # Skills for 'Alignment' calculation
        individual_skills = {skill: np.random.uniform(0.1, 1.0) if random.random() < 0.7 else 0 for skill in skill_set}


        employee_data.append({
            'employee_id': f'EMP{i:03d}',
            'job_role': job_role,
            'department': department,
            'education_level': education,
            'years_experience': years_experience,
            'salary': np.random.randint(50000, 150000),
            'current_occupation_id': f'OCC{job_roles.index(job_role):03d}', # Link to occupation
            'target_occupation_id': f'OCC{random.randint(0, len(job_roles)-1):03d}',

            # AI-Fluency sub-components
            'prompting_score': prompting,
            'ai_tools_score': ai_tools,
            'ai_understanding_score': ai_understanding,
            'data_literacy_score': data_literacy,

            'output_quality_with_ai': output_quality_with_ai,
            'output_quality_without_ai': output_quality_without_ai,
            'time_without_ai': time_without_ai,
            'time_with_ai': time_with_ai,

            'errors_caught': errors_caught,
            'total_ai_errors': total_ai_errors,
            'appropriate_trust_decisions': appropriate_trust_decisions,
            'total_decisions': total_decisions,

            'delta_proficiency': delta_proficiency,
            'delta_t': delta_t,
            'hours_invested': hours_invested,
            
            # Adaptive Capacity
            'cognitive_capacity': cognitive_capacity,
            'social_capacity': social_capacity,
            'strategic_capacity': strategic_capacity,

            # Domain Specialization
            'portfolio_score': portfolio_score,
            'recognition_score': recognition_score,
            'credentials_score': credentials_score,

            # Skills for Synergy (Alignment)
            **{f'skill_{k}': v for k, v in individual_skills.items()},

            # Placeholder for calculated scores
            'ai_fluency_score': 0.0,
            'domain_expertise_score': 0.0,
            'adaptive_capacity_score': 0.0,
            'vr_score': 0.0,
            'hr_r_score': 0.0,
            'synergy_score': 0.0,
            'current_ai_r_score': 0.0,
            'projected_ai_r_score': 0.0,
            'alignment_factor': 0.0,
            'skills_match_score': 0.0,
            'timing_factor': 0.0,
        })
    return pd.DataFrame(employee_data)

@st.cache_data(ttl="2h")
def generate_synthetic_occupations(num_occupations=len(['Data Scientist', 'Software Engineer', 'Marketing Specialist', 'HR Business Partner', 'Financial Analyst', 'Project Manager'])):
    np.random.seed(42)
    random.seed(42)

    occupation_data = []
    job_roles = ['Data Scientist', 'Software Engineer', 'Marketing Specialist', 'HR Business Partner', 'Financial Analyst', 'Project Manager']
    skill_set = ['Python', 'SQL', 'Machine Learning', 'Deep Learning', 'Data Analysis', 'Communication', 'Project Management', 'Cloud Computing', 'Marketing Strategy', 'Recruitment', 'Financial Modeling', 'Risk Management']

    for i, role in enumerate(job_roles[:num_occupations]):
        automation_t = np.random.uniform(0.1, 0.6)
        ai_augmentation_t = np.random.uniform(0.3, 0.9)
        projected_jobs_t_plus_10 = np.random.randint(50000, 200000)
        current_jobs_t = np.random.randint(30000, 150000)
        
        # Ensure projected > current for positive growth bias
        if projected_jobs_t_plus_10 < current_jobs_t:
            projected_jobs_t_plus_10 = current_jobs_t + np.random.randint(5000, 50000)

        ai_skilled_wage = np.random.randint(80000, 180000)
        median_wage = np.random.randint(60000, 120000)
        education_years_required = np.random.randint(4, 8) # Bachelor's to PhD
        experience_years_required = np.random.randint(0, 10)
        
        job_postings_t = np.random.randint(100, 1000)
        job_postings_t_minus_1 = np.random.randint(50, 800)
        local_demand_t = np.random.uniform(0.8, 1.5)
        national_avg_demand = np.random.uniform(0.9, 1.1)
        remote_work_factor = np.random.uniform(0.1, 0.9)

        # Required skills for alignment (occupation_skills)
        occupation_skills = {skill: np.random.uniform(0.3, 1.0) if random.random() < 0.6 else 0 for skill in skill_set}
        # Ensure some core skills are always present for specific roles
        if "Data Scientist" in role:
            occupation_skills['Python'] = max(occupation_skills['Python'], 0.8)
            occupation_skills['Machine Learning'] = max(occupation_skills['Machine Learning'], 0.9)
            occupation_skills['SQL'] = max(occupation_skills['SQL'], 0.7)
        if "Software Engineer" in role:
            occupation_skills['Python'] = max(occupation_skills['Python'], 0.7)
            occupation_skills['Cloud Computing'] = max(occupation_skills['Cloud Computing'], 0.8)
        if "Marketing Specialist" in role:
            occupation_skills['Marketing Strategy'] = max(occupation_skills['Marketing Strategy'], 0.9)
            occupation_skills['Communication'] = max(occupation_skills['Communication'], 0.8)
        
        # Skill importance
        skill_importance = {skill: np.random.uniform(0.5, 1.0) for skill in skill_set}


        occupation_data.append({
            'occupation_id': f'OCC{i:03d}',
            'job_role': role,
            'automation_t': automation_t,
            'ai_augmentation_t': ai_augmentation_t,
            'projected_jobs_t_plus_10': projected_jobs_t_plus_10,
            'current_jobs_t': current_jobs_t,
            'ai_skilled_wage': ai_skilled_wage,
            'median_wage': median_wage,
            'education_years_required': education_years_required,
            'experience_years_required': experience_years_required,
            'job_postings_t': job_postings_t,
            'job_postings_t_minus_1': job_postings_t_minus_1,
            'local_demand_t': local_demand_t,
            'national_avg_demand': national_avg_demand,
            'remote_work_factor': remote_work_factor,
            
            # Required skills for Synergy (Alignment)
            **{f'req_skill_{k}': v for k, v in occupation_skills.items()},
            **{f'skill_importance_{k}': v for k, v in skill_importance.items()},

            # Placeholder for calculated scores
            'ai_enhancement': 0.0,
            'growth_normalized': 0.0,
            'wage_premium': 0.0,
            'entry_accessibility': 0.0,
            'h_base_score': 0.0,
            'growth_multiplier': 1.0,
            'regional_multiplier': 1.0,
            'hr_r_score': 0.0,
        })
    return pd.DataFrame(occupation_data)

@st.cache_data(ttl="2h")
def generate_synthetic_pathways(num_pathways=20):
    np.random.seed(42)
    random.seed(42)

    pathway_data = []
    pathway_types = ['AI Fundamentals', 'Advanced ML', 'Data Science Toolkit', 'AI Ethics', 'Prompt Engineering', 'Cloud AI Services', 'Domain Specific AI']
    skill_impact_areas = ['ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score'] # Which VR component it primarily impacts
    
    # Define a set of skills that pathways can enhance
    all_possible_skills = ['Python', 'SQL', 'Machine Learning', 'Deep Learning', 'Data Analysis', 'Communication', 'Project Management', 'Cloud Computing', 'Marketing Strategy', 'Recruitment', 'Financial Modeling', 'Risk Management']


    for i in range(num_pathways):
        pathway_type = random.choice(pathway_types)
        cost = np.random.randint(100, 2000)
        time_hours = np.random.randint(10, 100)
        
        # Delta AI-R is the potential improvement an employee could get
        delta_ai_r_potential = np.random.uniform(5, 25)
        
        # Primary impact on one VR sub-component (for simulation purposes)
        impact_area = random.choice(skill_impact_areas)
        impact_magnitude = np.random.uniform(0.1, 0.4) # As a percentage of the remaining gap to 100

        # Prerequisites: A pathway might require another pathway.
        prerequisites = []
        if i > 0 and random.random() < 0.3: # 30% chance of a prerequisite
            prereq_id = f'PW{random.randint(0, i-1):03d}'
            prerequisites.append(prereq_id)

        # Skills enhanced by this pathway (for multi-step optimization)
        enhanced_skills = random.sample(all_possible_skills, k=random.randint(1, 3))
        
        pathway_data.append({
            'pathway_id': f'PW{i:03d}',
            'pathway_name': f'{pathway_type} - Level {random.randint(1, 3)}',
            'cost': cost,
            'time_hours': time_hours,
            'delta_ai_r_potential': delta_ai_r_potential,
            'impact_area': impact_area, # Which VR component it primarily impacts
            'impact_magnitude': impact_magnitude, # How much it improves the impact_area score
            'prerequisites': prerequisites, # List of pathway_ids
            'enhanced_skills': enhanced_skills # List of skills the pathway enhances
        })
    return pd.DataFrame(pathway_data)

# --- Calculation Functions (as per notebook spec) ---
# HR Components
def calculate_ai_enhancement(df_occupations, params):
    df_occupations['ai_enhancement'] = df_occupations.apply(
        lambda row: (1 - row['automation_t']) * row['ai_augmentation_t'],
        axis=1
    )
    return df_occupations

def calculate_job_growth_normalized(df_occupations, params):
    df_occupations['growth'] = (df_occupations['projected_jobs_t_plus_10'] - df_occupations['current_jobs_t']) / df_occupations['current_jobs_t']
    df_occupations['growth_normalized'] = (df_occupations['growth'] + 0.5) / 2.0 * 100 # Normalize to roughly 0-100 range, assuming growth can be -0.5 to 1.5
    df_occupations['growth_normalized'] = df_occupations['growth_normalized'].clip(0, 100) # Clip to ensure it's within 0-100
    return df_occupations

def calculate_wage_premium(df_occupations, params):
    df_occupations['wage_premium'] = (df_occupations['ai_skilled_wage'] - df_occupations['median_wage']) / df_occupations['median_wage']
    df_occupations['wage_premium'] = df_occupations['wage_premium'].clip(0, 1.0) # Clip for reasonable range for scoring
    df_occupations['wage_premium'] = df_occupations['wage_premium'] * 100 # Scale to 0-100
    return df_occupations

def calculate_entry_accessibility(df_occupations, params):
    df_occupations['entry_accessibility'] = 1 - (df_occupations['education_years_required'] + df_occupations['experience_years_required']) / 10
    df_occupations['entry_accessibility'] = df_occupations['entry_accessibility'].clip(0, 1.0) # Clip for reasonable range
    df_occupations['entry_accessibility'] = df_occupations['entry_accessibility'] * 100 # Scale to 0-100
    return df_occupations

def calculate_base_opportunity_score(df_occupations, params):
    weights = params['hr_base_weights']
    df_occupations['h_base_score'] = (
        weights['w_ai_enhancement'] * df_occupations['ai_enhancement'] +
        weights['w_growth_normalized'] * df_occupations['growth_normalized'] +
        weights['w_wage_premium'] * df_occupations['wage_premium'] +
        weights['w_entry_accessibility'] * df_occupations['entry_accessibility']
    )
    df_occupations['h_base_score'] = df_occupations['h_base_score'].clip(0, 100)
    return df_occupations

def calculate_growth_multiplier(df_occupations, params):
    lambda_growth = params['lambda_growth']
    df_occupations['job_posting_change'] = (df_occupations['job_postings_t'] / df_occupations['job_postings_t_minus_1']) - 1
    df_occupations['growth_multiplier'] = 1 + lambda_growth * df_occupations['job_posting_change']
    df_occupations['growth_multiplier'] = df_occupations['growth_multiplier'].clip(0.5, 2.0) # Keep within reasonable bounds
    return df_occupations

def calculate_regional_multiplier(df_occupations, params):
    gamma_regional = params['gamma_regional']
    df_occupations['regional_multiplier'] = (
        df_occupations['local_demand_t'] / df_occupations['national_avg_demand']
    ) * (1 + gamma_regional * df_occupations['remote_work_factor'])
    df_occupations['regional_multiplier'] = df_occupations['regional_multiplier'].clip(0.5, 2.0) # Keep within reasonable bounds
    return df_occupations

def calculate_systematic_opportunity(df_employees, df_occupations, params):
    # Merge occupation data into employee data based on target_occupation_id
    df_merged = pd.merge(
        df_employees,
        df_occupations[['occupation_id', 'h_base_score', 'growth_multiplier', 'regional_multiplier']],
        left_on='target_occupation_id',
        right_on='occupation_id',
        how='left',
        suffixes=('', '_occ')
    )
    df_merged['hr_r_score'] = (
        df_merged['h_base_score'] *
        df_merged['growth_multiplier'] *
        df_merged['regional_multiplier']
    )
    df_merged['hr_r_score'] = df_merged['hr_r_score'].clip(0, 100)
    df_employees = df_merged.drop(columns=['occupation_id_occ', 'h_base_score', 'growth_multiplier', 'regional_multiplier'])
    return df_employees

# VR Components
def calculate_technical_ai_skills(employee_row):
    return (employee_row['prompting_score'] + employee_row['ai_tools_score'] +
            employee_row['ai_understanding_score'] + employee_row['data_literacy_score']) / 4

def calculate_ai_augmented_productivity(employee_row):
    try:
        quality_ratio = employee_row['output_quality_with_ai'] / employee_row['output_quality_without_ai']
        time_ratio = employee_row['time_without_ai'] / employee_row['time_with_ai']
        return quality_ratio * time_ratio * 10 # Scale for 0-100, assuming ratios are around 1-2
    except ZeroDivisionError:
        return 0.0

def calculate_critical_ai_judgment(employee_row):
    error_detection = employee_row['errors_caught'] / max(1, employee_row['total_ai_errors'])
    trust_decisions = employee_row['appropriate_trust_decisions'] / max(1, employee_row['total_decisions'])
    return (error_detection + trust_decisions) / 2 * 100 # Scale to 0-100

def calculate_ai_learning_velocity(employee_row):
    try:
        return (employee_row['delta_proficiency'] / employee_row['delta_t']) / (employee_row['hours_invested'] / 100) * 10 # Scale to 0-100
    except ZeroDivisionError:
        return 0.0

def calculate_ai_fluency(df_employees, params):
    weights = params['theta_ai_fluency_weights']
    df_employees['s1_technical_ai_skills'] = df_employees.apply(calculate_technical_ai_skills, axis=1)
    df_employees['s2_ai_augmented_productivity'] = df_employees.apply(calculate_ai_augmented_productivity, axis=1)
    df_employees['s3_critical_ai_judgment'] = df_employees.apply(calculate_critical_ai_judgment, axis=1)
    df_employees['s4_ai_learning_velocity'] = df_employees.apply(calculate_ai_learning_velocity, axis=1)

    df_employees['ai_fluency_score'] = (
        weights['t_technical_ai_skills'] * df_employees['s1_technical_ai_skills'] +
        weights['t_ai_augmented_productivity'] * df_employees['s2_ai_augmented_productivity'] +
        weights['t_critical_ai_judgment'] * df_employees['s3_critical_ai_judgment'] +
        weights['t_ai_learning_velocity'] * df_employees['s4_ai_learning_velocity']
    )
    df_employees['ai_fluency_score'] = df_employees['ai_fluency_score'].clip(0, 100)
    return df_employees

def calculate_educational_foundation(employee_row):
    if employee_row['education_level'] == 'PhD': return 100
    elif employee_row['education_level'] == 'Master\'s': return 80
    elif employee_row['education_level'] == 'Bachelor\'s': return 60
    else: return 30 # High School or less
    
def calculate_practical_experience(employee_row, params):
    gamma_exp = params['gamma_exp']
    return (1 - np.exp(-gamma_exp * employee_row['years_experience'])) * 100

def calculate_specialization_depth(employee_row, params):
    weights = params['domain_specialization_weights']
    return (
        weights['w_portfolio'] * employee_row['portfolio_score'] +
        weights['w_recognition'] * employee_row['recognition_score'] +
        weights['w_credentials'] * employee_row['credentials_score']
    ) * 100 # Scale to 0-100

def calculate_domain_expertise(df_employees, params):
    df_employees['e_education'] = df_employees.apply(calculate_educational_foundation, axis=1)
    df_employees['e_experience'] = df_employees.apply(lambda row: calculate_practical_experience(row, params), axis=1)
    df_employees['e_specialization'] = df_employees.apply(lambda row: calculate_specialization_depth(row, params), axis=1)
    
    # A simple multiplicative model for demonstration
    df_employees['domain_expertise_score'] = (
        df_employees['e_education'] / 100 * # Normalize to 0-1 for multiplication
        df_employees['e_experience'] / 100 *
        df_employees['e_specialization'] / 100
    ) * 100 # Scale back to 0-100
    df_employees['domain_expertise_score'] = df_employees['domain_expertise_score'].clip(0, 100)
    return df_employees

def calculate_adaptive_capacity(df_employees, params):
    df_employees['adaptive_capacity_score'] = (
        df_employees['cognitive_capacity'] +
        df_employees['social_capacity'] +
        df_employees['strategic_capacity']
    ) / 3 * 100
    df_employees['adaptive_capacity_score'] = df_employees['adaptive_capacity_score'].clip(0, 100)
    return df_employees

def calculate_idiosyncratic_readiness(df_employees, params):
    weights = params['vr_component_weights']
    df_employees['vr_score'] = (
        weights['w_ai_fluency'] * df_employees['ai_fluency_score'] +
        weights['w_domain_expertise'] * df_employees['domain_expertise_score'] +
        weights['w_adaptive_capacity'] * df_employees['adaptive_capacity_score']
    )
    df_employees['vr_score'] = df_employees['vr_score'].clip(0, 100)
    return df_employees

# Synergy Components
def calculate_skills_match_score(employee_row, df_occupations):
    target_occ_id = employee_row['target_occupation_id']
    occupation_row = df_occupations[df_occupations['occupation_id'] == target_occ_id].iloc[0]
    
    match_score = 0
    max_possible_match = 0
    
    for skill in [col.replace('skill_', '') for col in employee_row.index if col.startswith('skill_')]:
        individual_skill_val = employee_row[f'skill_{skill}']
        required_skill_val = occupation_row.get(f'req_skill_{skill}', 0)
        importance = occupation_row.get(f'skill_importance_{skill}', 1) # Default importance 1

        match_score += min(individual_skill_val, required_skill_val) * importance
        max_possible_match += required_skill_val * importance # Max possible if individual has all required skills perfectly

    if max_possible_match == 0:
        return 0, 1 # No skills required, consider it a perfect match
    return match_score, max_possible_match

def calculate_timing_factor(employee_row):
    # Simplified timing factor based on current AI-R compared to average
    avg_ai_r = st.session_state.df_employees['current_ai_r_score'].mean() if 'current_ai_r_score' in st.session_state.df_employees.columns else 50
    if employee_row['current_ai_r_score'] > avg_ai_r * 1.2: return 1.1 # Early adopter bonus
    elif employee_row['current_ai_r_score'] < avg_ai_r * 0.8: return 0.9 # Needs more time/catch-up
    else: return 1.0

def calculate_alignment_factor(df_employees, df_occupations):
    df_employees['skills_match_score'] = 0.0
    df_employees['timing_factor'] = 1.0 # Initialize

    max_possible_match_global = 1.0 # To normalize skills match score

    # First, calculate all skills matches and determine global max_possible_match
    temp_skills_data = []
    for idx, row in df_employees.iterrows():
        match, max_match = calculate_skills_match_score(row, df_occupations)
        temp_skills_data.append({'employee_id': row['employee_id'], 'match_score': match, 'max_match_score': max_match})

    temp_df = pd.DataFrame(temp_skills_data)
    if not temp_df.empty:
        max_possible_match_global = temp_df['max_match_score'].max()
        
    df_employees['skills_match_score'] = temp_df['match_score'] # Assign directly
    
    if max_possible_match_global > 0:
        df_employees['normalized_skills_match_score'] = df_employees['skills_match_score'] / max_possible_match_global
    else:
        df_employees['normalized_skills_match_score'] = 0.0 # No skills required in any occupation

    df_employees['timing_factor'] = df_employees.apply(calculate_timing_factor, axis=1)
    
    df_employees['alignment_factor'] = df_employees['normalized_skills_match_score'] * df_employees['timing_factor']
    df_employees['alignment_factor'] = df_employees['alignment_factor'].clip(0, 1.5) # Clip to reasonable range
    return df_employees

def calculate_synergy(df_employees, params):
    df_employees['synergy_score'] = (
        (df_employees['vr_score'] * df_employees['hr_r_score']) / 10000 * # Normalize VR*HR product to roughly 0-100
        df_employees['alignment_factor']
    ) * 100
    df_employees['synergy_score'] = df_employees['synergy_score'].clip(0, 100) # Keep within 0-100
    return df_employees

def calculate_ai_r(df_employees, params):
    alpha = params['alpha']
    beta = params['beta']
    df_employees['current_ai_r_score'] = (
        alpha * df_employees['vr_score'] +
        (1 - alpha) * df_employees['hr_r_score'] +
        beta * df_employees['synergy_score']
    )
    df_employees['current_ai_r_score'] = df_employees['current_ai_r_score'].clip(0, 100)
    return df_employees

# Report Functions
def generate_ai_r_report_summary(df_employees, group_by_column='department'):
    if group_by_column not in df_employees.columns:
        st.warning(f"Column '{group_by_column}' not found for grouping. Grouping by 'department' instead.")
        group_by_column = 'department'
    
    # Calculate average scores by group
    summary = df_employees.groupby(group_by_column).agg(
        Average_AI_R=('current_ai_r_score', 'mean'),
        Average_VR=('vr_score', 'mean'),
        Average_HR=('hr_r_score', 'mean'),
        Average_Synergy=('synergy_score', 'mean'),
        Average_AI_Fluency=('ai_fluency_score', 'mean'),
        Average_Domain_Expertise=('domain_expertise_score', 'mean'),
        Average_Adaptive_Capacity=('adaptive_capacity_score', 'mean'),
        Employee_Count=('employee_id', 'count')
    ).round(2)
    return summary

def plot_skills_gap_heatmap(df_employees, group_by_column='department'):
    if group_by_column not in df_employees.columns:
        st.warning(f"Column '{group_by_column}' not found for grouping. Using 'department' for heatmap.")
        group_by_column = 'department'

    sub_components = ['ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score']
    
    avg_scores = df_employees.groupby(group_by_column)[sub_components].mean()

    fig, ax = plt.subplots(figsize=(10, len(avg_scores) * 0.8))
    sns.heatmap(avg_scores, annot=True, cmap='viridis', fmt=".1f", linewidths=.5, ax=ax)
    ax.set_title(f'Average $V^R$ Sub-Component Scores by {group_by_column}', fontsize=16)
    ax.set_ylabel(group_by_column, fontsize=12)
    ax.set_xlabel('VR Sub-Components', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    return fig

# Scenario Engine Functions
def simulate_pathway_impact(employee_id, pathway_id, completion_rate, mastery_score, df_employees, df_pathways, params):
    if df_employees.empty or df_pathways.empty:
        st.error("Employee or pathway data is not loaded.")
        return None, None, None

    employee_df = df_employees[df_employees['employee_id'] == employee_id].copy()
    if employee_df.empty:
        st.error(f"Employee {employee_id} not found.")
        return None, None, None
    employee_row = employee_df.iloc[0]

    pathway_df = df_pathways[df_pathways['pathway_id'] == pathway_id].copy()
    if pathway_df.empty:
        st.error(f"Pathway {pathway_id} not found.")
        return None, None, None
    pathway_row = pathway_df.iloc[0]

    current_ai_r = employee_row['current_ai_r_score']
    projected_employee_row = employee_row.copy()

    # Impact on VR sub-component directly
    impact_area = pathway_row['impact_area']
    impact_magnitude = pathway_row['impact_magnitude']
    
    # Calculate potential improvement for the specific impact area
    current_impact_score = projected_employee_row[impact_area]
    remaining_gap = 100 - current_impact_score
    
    # Apply impact based on completion and mastery
    improvement = remaining_gap * impact_magnitude * completion_rate * mastery_score
    projected_employee_row[impact_area] = min(100, current_impact_score + improvement)

    # Recalculate VR based on updated sub-component
    projected_employee_row = calculate_idiosyncratic_readiness(pd.DataFrame([projected_employee_row]), params).iloc[0]
    
    # Recalculate Synergy based on new VR
    # Assuming HR and Alignment are relatively stable in short-term pathway simulation
    # For a full recalculation, you'd re-run calculate_synergy and then calculate_ai_r
    # We will simplify here and just use the change in VR for the overall AI-R change
    alpha = params['alpha']
    beta = params['beta']
    
    # Placeholder for full recalculation if desired
    # projected_employee_row = calculate_synergy(pd.DataFrame([projected_employee_row]), params).iloc[0]
    # projected_employee_row = calculate_ai_r(pd.DataFrame([projected_employee_row]), params).iloc[0]

    # For now, a simpler update based on delta VR directly affecting AI-R
    delta_vr = projected_employee_row['vr_score'] - employee_row['vr_score']
    
    projected_ai_r = current_ai_r + (alpha * delta_vr * completion_rate * mastery_score) * (pathway_row['delta_ai_r_potential'] / 100.0)
    projected_ai_r = min(100, projected_ai_r) # Cap at 100
    
    delta_ai_r = projected_ai_r - current_ai_r
    
    # Update df_employees in session state for the selected employee's projected score
    st.session_state.df_employees.loc[st.session_state.df_employees['employee_id'] == employee_id, 'projected_ai_r_score'] = projected_ai_r

    return current_ai_r, projected_ai_r, delta_ai_r

def plot_current_vs_projected_ai_r(employee_id, df_employees):
    employee_row = df_employees[df_employees['employee_id'] == employee_id].iloc[0]
    current_ai_r = employee_row['current_ai_r_score']
    projected_ai_r = employee_row['projected_ai_r_score'] if 'projected_ai_r_score' in employee_row.index else current_ai_r

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(['Current AI-R', 'Projected AI-R'], [current_ai_r, projected_ai_r], color=['skyblue', 'lightcoral'])
    ax.set_ylabel('AI-Readiness Score')
    ax.set_title(f'AI-R Comparison for {employee_id}')
    ax.set_ylim(0, 100)

    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2, round(yval, 2), ha='center', va='bottom') # Add text labels

    plt.tight_layout()
    return fig

# Multi-Step Optimization Functions
def optimize_pathway_sequence(employee_id, T_max_hours, cost_weight_lambda, df_employees, df_pathways, params):
    if df_employees.empty or df_pathways.empty:
        st.error("Employee or pathway data is not loaded.")
        return None, None, None, None, None

    employee_row = df_employees[df_employees['employee_id'] == employee_id].iloc[0].copy()
    current_ai_r = employee_row['current_ai_r_score']
    
    # Simple Greedy approach for demonstration purposes
    # A real optimization would involve more complex algorithms (e.g., dynamic programming, A* search)
    
    available_pathways = df_pathways.copy()
    
    recommended_sequence = []
    total_cost = 0
    total_time_hours = 0
    
    # Track current VR scores for employee to simulate improvement
    temp_employee_vr_scores = {
        'ai_fluency_score': employee_row['ai_fluency_score'],
        'domain_expertise_score': employee_row['domain_expertise_score'],
        'adaptive_capacity_score': employee_row['adaptive_capacity_score'],
        'vr_score': employee_row['vr_score']
    }
    
    # To track which pathways have been "completed" for prerequisite checks
    completed_pathways_ids = set()

    max_iterations = 5 # Limit for greedy algorithm to prevent infinite loops or excessive computation

    for _ in range(max_iterations):
        best_pathway = None
        max_score_improvement = -np.inf

        for idx, pathway_row in available_pathways.iterrows():
            # Check prerequisites
            prereqs_met = True
            for prereq_id in pathway_row['prerequisites']:
                if prereq_id not in completed_pathways_ids:
                    prereqs_met = False
                    break
            if not prereqs_met:
                continue

            # Check time constraint
            if total_time_hours + pathway_row['time_hours'] > T_max_hours:
                continue
            
            # Simulate impact of this pathway
            current_impact_score = temp_employee_vr_scores[pathway_row['impact_area']]
            remaining_gap = 100 - current_impact_score
            
            # A rough estimate of AI-R improvement without full recalculation for each step
            # We'll assume a fixed completion/mastery rate for optimization (e.g., 0.8, 0.8)
            estimated_vr_improvement_for_impact_area = remaining_gap * pathway_row['impact_magnitude'] * 0.8 * 0.8
            
            # Calculate an approximate total AI-R improvement based on VR's weight
            approx_ai_r_improvement = params['alpha'] * params['vr_component_weights'][pathway_row['impact_area']] * (estimated_vr_improvement_for_impact_area / 100.0) * (pathway_row['delta_ai_r_potential'] / 100.0) * 100
            
            # Objective: Maximize AI-R improvement - lambda * cost
            score_improvement = approx_ai_r_improvement - cost_weight_lambda * pathway_row['cost']

            if score_improvement > max_score_improvement:
                max_score_improvement = score_improvement
                best_pathway = pathway_row
        
        if best_pathway is not None and max_score_improvement > 0: # Only add if it improves the score
            recommended_sequence.append(best_pathway['pathway_name'])
            total_cost += best_pathway['cost']
            total_time_hours += best_pathway['time_hours']
            completed_pathways_ids.add(best_pathway['pathway_id'])
            
            # Update temporary employee VR scores for next iteration
            current_impact_score = temp_employee_vr_scores[best_pathway['impact_area']]
            remaining_gap = 100 - current_impact_score
            temp_employee_vr_scores[best_pathway['impact_area']] = min(100, current_impact_score + remaining_gap * best_pathway['impact_magnitude'] * 0.8 * 0.8)
            
            # Re-calculate overall VR score based on the updated component
            # This is a bit of a hack for the greedy algorithm, ideally you'd recalculate VR components properly
            temp_vr_score = (
                params['vr_component_weights']['w_ai_fluency'] * temp_employee_vr_scores['ai_fluency_score'] +
                params['vr_component_weights']['w_domain_expertise'] * temp_employee_vr_scores['domain_expertise_score'] +
                params['vr_component_weights']['w_adaptive_capacity'] * temp_employee_vr_scores['adaptive_capacity_score']
            )
            temp_employee_vr_scores['vr_score'] = temp_vr_score

            # Remove pathway from available options
            available_pathways = available_pathways[available_pathways['pathway_id'] != best_pathway['pathway_id']]
        else:
            break # No more beneficial pathways or no pathways fit constraints

    # Calculate final projected AI-R based on aggregated improvements
    # This is a simplification; a full model would recalculate VR, HR, Synergy, AI-R.
    # For a direct estimate, sum up the delta_ai_r_potential from recommended pathways, weighted by a factor
    
    projected_final_ai_r_improvement_estimate = sum(
        df_pathways[df_pathways['pathway_name'] == name]['delta_ai_r_potential'].iloc[0] * 0.8 * 0.8 / 100 # Adjust by completion/mastery
        for name in recommended_sequence
    )
    projected_final_ai_r = current_ai_r + projected_final_ai_r_improvement_estimate * 100 * params['alpha'] # Scale back and apply alpha
    projected_final_ai_r = min(100, projected_final_ai_r)
    
    ai_r_improvement = projected_final_ai_r - current_ai_r

    # Update df_employees in session state for the selected employee's projected score
    st.session_state.df_employees.loc[st.session_state.df_employees['employee_id'] == employee_id, 'projected_ai_r_score'] = projected_final_ai_r

    return recommended_sequence, projected_final_ai_r, total_cost, total_time_hours, ai_r_improvement

# --- Streamlit UI Logic ---
PAGES = {
    "Introduction": "introduction",
    "Data Configuration": "data_configuration",
    "AI-Readiness Calculation Walkthrough": "ai_r_walkthrough",
    "AI-R Report & Skills Gap Analysis": "ai_r_report",
    "What-If Scenario Engine": "what_if_scenario",
    "Multi-Step Pathway Optimization": "pathway_optimization",
    "Strategic Recommendations": "strategic_recommendations"
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# --- Page: Introduction ---
if selection == "Introduction":
    st.header("1. Introduction to the AI-Readiness Framework")
    st.markdown("""
    The AI-Readiness Score (AI-R) provides a comprehensive assessment of an individual's or organization's preparedness for an AI-centric future.
    It synthesizes individual capabilities, market opportunities, and the strategic alignment between the two.
    """)

    st.subheader("The Core AI-Readiness Formula")
    st.markdown(r"$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$")
    st.markdown("""
    where:
    *   $AI-R_{i,t}$: The overall AI-Readiness Score for individual $i$ at time $t$.
    *   $V^R_{i}(t)$: **Idiosyncratic Readiness** – Reflects individual-specific attributes, skills, and adaptive capacities. This is essentially "what the employee brings to the table."
    *   $H^R(t)$: **Systematic Opportunity** – Represents external market factors, job growth, wage premiums, and the AI-enhancement potential of an occupation. This is "what the market demands."
    *   $Synergy\%(V^R, H^R)$: **Synergy** – Quantifies the alignment and match between an individual's skills ($V^R$) and market opportunities ($H^R$), considering factors like timing and skill importance.
    *   $\alpha$: A weighting parameter (0 to 1) that balances the importance of individual readiness ($V^R$) versus systematic opportunity ($H^R$).
    *   $\beta$: A coefficient that determines the impact of Synergy on the overall AI-R score.
    """)

    st.info("The `PARAMS` dictionary in `st.session_state` stores the current values for alpha, beta, and all other weights used in the calculations. You can configure these on the 'Data Configuration' page.")

    # Sample calculation stub
    st.subheader("Sample AI-R Calculation (Illustrative)")
    params = st.session_state.PARAMS
    sample_vr = 75.0
    sample_hr = 80.0
    sample_synergy = 60.0 # Assumed synergy %

    sample_ai_r = (
        params['alpha'] * sample_vr +
        (1 - params['alpha']) * sample_hr +
        params['beta'] * sample_synergy
    )
    st.markdown(f"Using current global parameters ($\\alpha={params['alpha']}, \\beta={params['beta']}$):")
    st.metric(label="Sample Idiosyncratic Readiness ($V^R$)", value=f"{sample_vr:.1f}")
    st.metric(label="Sample Systematic Opportunity ($H^R$)", value=f"{sample_hr:.1f}")
    st.metric(label="Sample Synergy%", value=f"{sample_synergy:.1f}")
    st.metric(label="Calculated Sample AI-Readiness Score (AI-R)", value=f"{sample_ai_r:.2f}")

# --- Page: Data Configuration ---
elif selection == "Data Configuration":
    st.header("2. Data Configuration")
    st.markdown("""
    This section allows you to generate synthetic data for employees, occupations, and learning pathways,
    and configure the various parameters and weights used in the AI-Readiness calculations.
    All data and parameters are stored in `st.session_state` for persistence.
    """)

    if st.button("Generate/Reset Synthetic Data"):
        with st.spinner("Generating data..."):
            st.session_state.df_employees = generate_synthetic_employees()
            st.session_state.df_occupations = generate_synthetic_occupations()
            st.session_state.df_pathways = generate_synthetic_pathways()
        st.success("Synthetic data generated successfully!")

    st.subheader("Employee Data (df_employees.head())")
    if not st.session_state.df_employees.empty:
        st.dataframe(st.session_state.df_employees.head())
    else:
        st.info("No employee data available. Please generate synthetic data.")

    st.subheader("Occupation Data (df_occupations.head())")
    if not st.session_state.df_occupations.empty:
        st.dataframe(st.session_state.df_occupations.head())
    else:
        st.info("No occupation data available. Please generate synthetic data.")

    st.subheader("Learning Pathways Data (df_pathways.head())")
    if not st.session_state.df_pathways.empty:
        st.dataframe(st.session_state.df_pathways.head())
    else:
        st.info("No pathway data available. Please generate synthetic data.")

    st.subheader("Global Parameters & Weights Configuration")
    st.markdown("Adjust these parameters to see their impact on the AI-Readiness scores.")

    # Global AI-R weights
    st.session_state.PARAMS['alpha'] = st.slider(
        "α (Weight on Individual Readiness $V^R$ vs. Systematic Opportunity $H^R$)",
        min_value=0.0, max_value=1.0, value=st.session_state.PARAMS['alpha'], step=0.01,
        help="A higher alpha means individual skills and readiness are weighted more heavily."
    )
    st.session_state.PARAMS['beta'] = st.slider(
        "β (Synergy Coefficient)",
        min_value=0.0, max_value=1.0, value=st.session_state.PARAMS['beta'], step=0.01,
        help="Determines the impact of the Synergy score on the overall AI-R."
    )

    # Dynamic Multipliers
    st.session_state.PARAMS['lambda_growth'] = st.number_input(
        "λ_growth (Growth Multiplier Damping)",
        min_value=0.0, max_value=2.0, value=st.session_state.PARAMS['lambda_growth'], step=0.1,
        help="Controls how strongly job posting changes influence the growth multiplier for HR."
    )
    st.session_state.PARAMS['gamma_regional'] = st.number_input(
        "γ_regional (Regional Multiplier Weight)",
        min_value=0.0, max_value=1.0, value=st.session_state.PARAMS['gamma_regional'], step=0.1,
        help="Determines the influence of remote work factor on the regional multiplier for HR."
    )
    st.session_state.PARAMS['gamma_exp'] = st.number_input(
        "γ_exp (Experience Decay Rate for Domain Expertise)",
        min_value=0.0, max_value=0.5, value=st.session_state.PARAMS['gamma_exp'], step=0.01,
        help="Higher values mean practical experience contributes more rapidly to Domain Expertise but also saturates faster."
    )

    # Weights in expanders
    with st.expander("HR Base Weights (H_base(o))"):
        for key, value in st.session_state.PARAMS['hr_base_weights'].items():
            st.session_state.PARAMS['hr_base_weights'][key] = st.number_input(
                f"Weight for {key.replace('w_', '').replace('_', ' ').title()}",
                min_value=0.0, max_value=1.0, value=value, step=0.01, key=f"hr_w_{key}"
            )
        if sum(st.session_state.PARAMS['hr_base_weights'].values()) > 1.01:
            st.warning("Sum of HR Base Weights exceeds 1.0. Consider normalizing.")

    with st.expander("AI-Fluency Sub-component Weights (θ_k)"):
        for key, value in st.session_state.PARAMS['theta_ai_fluency_weights'].items():
            st.session_state.PARAMS['theta_ai_fluency_weights'][key] = st.number_input(
                f"Weight for {key.replace('t_', '').replace('_', ' ').title()}",
                min_value=0.0, max_value=1.0, value=value, step=0.01, key=f"ai_fluency_w_{key}"
            )
        if sum(st.session_state.PARAMS['theta_ai_fluency_weights'].values()) > 1.01:
            st.warning("Sum of AI-Fluency Sub-component Weights exceeds 1.0. Consider normalizing.")

    with st.expander("Domain Specialization Weights"):
        for key, value in st.session_state.PARAMS['domain_specialization_weights'].items():
            st.session_state.PARAMS['domain_specialization_weights'][key] = st.number_input(
                f"Weight for {key.replace('w_', '').replace('_', ' ').title()}",
                min_value=0.0, max_value=1.0, value=value, step=0.01, key=f"domain_spec_w_{key}"
            )
        if sum(st.session_state.PARAMS['domain_specialization_weights'].values()) > 1.01:
            st.warning("Sum of Domain Specialization Weights exceeds 1.0. Consider normalizing.")

    with st.expander("VR Component Weights (Idiosyncratic Readiness)"):
        for key, value in st.session_state.PARAMS['vr_component_weights'].items():
            st.session_state.PARAMS['vr_component_weights'][key] = st.number_input(
                f"Weight for {key.replace('w_','').replace('_',' ').title()}",
                min_value=0.0, max_value=1.0, value=value, step=0.01, key=f"vr_comp_w_{key}"
            )
        if sum(st.session_state.PARAMS['vr_component_weights'].values()) > 1.01:
            st.warning("Sum of VR Component Weights exceeds 1.0. Consider normalizing.")

    st.subheader("Current `PARAMS` Dictionary")
    st.json(st.session_state.PARAMS)

# --- Page: AI-Readiness Calculation Walkthrough ---
elif selection == "AI-Readiness Calculation Walkthrough":
    st.header("3. AI-Readiness Calculation Walkthrough")
    st.markdown("""
    This section provides a step-by-step demonstration of how the AI-Readiness score is calculated
    for a selected employee, breaking down each component and sub-component.
    """)

    if st.session_state.df_employees.empty or st.session_state.df_occupations.empty:
        st.warning("Please generate synthetic data on the 'Data Configuration' page first.")
    else:
        employee_ids = st.session_state.df_employees['employee_id'].tolist()
        selected_employee_id = st.selectbox("Select an Employee ID:", employee_ids, key='walkthrough_employee_id')
        
        selected_employee_data = st.session_state.df_employees[
            st.session_state.df_employees['employee_id'] == selected_employee_id
        ].iloc[0]
        st.markdown(f"**Employee:** {selected_employee_id} | **Job Role:** {selected_employee_data['job_role']} | **Department:** {selected_employee_data['department']}")
        st.markdown(f"**Target Occupation:** {selected_employee_data['target_occupation_id']}")
        
        # --- Run all calculations for selected employee and all occupations ---
        # This is done to ensure all HR components are pre-calculated for the merge
        
        with st.spinner("Running all calculations..."):
            df_occupations_calc = st.session_state.df_occupations.copy()
            df_employees_calc = st.session_state.df_employees.copy()
            params = st.session_state.PARAMS

            # HR Components
            df_occupations_calc = calculate_ai_enhancement(df_occupations_calc, params)
            df_occupations_calc = calculate_job_growth_normalized(df_occupations_calc, params)
            df_occupations_calc = calculate_wage_premium(df_occupations_calc, params)
            df_occupations_calc = calculate_entry_accessibility(df_occupations_calc, params)
            df_occupations_calc = calculate_base_opportunity_score(df_occupations_calc, params)
            df_occupations_calc = calculate_growth_multiplier(df_occupations_calc, params)
            df_occupations_calc = calculate_regional_multiplier(df_occupations_calc, params)
            st.session_state.df_occupations = df_occupations_calc # Update in session state
            
            df_employees_calc = calculate_systematic_opportunity(df_employees_calc, df_occupations_calc, params)

            # VR Components
            df_employees_calc = calculate_ai_fluency(df_employees_calc, params)
            df_employees_calc = calculate_domain_expertise(df_employees_calc, params)
            df_employees_calc = calculate_adaptive_capacity(df_employees_calc, params)
            df_employees_calc = calculate_idiosyncratic_readiness(df_employees_calc, params)

            # Synergy & Overall AI-R
            df_employees_calc = calculate_alignment_factor(df_employees_calc, df_occupations_calc)
            df_employees_calc = calculate_synergy(df_employees_calc, params)
            df_employees_calc = calculate_ai_r(df_employees_calc, params)
            
            st.session_state.df_employees = df_employees_calc # Update in session state

        # Retrieve the updated data for the selected employee
        employee_row = st.session_state.df_employees[st.session_state.df_employees['employee_id'] == selected_employee_id].iloc[0]
        occupation_row = st.session_state.df_occupations[st.session_state.df_occupations['occupation_id'] == employee_row['target_occupation_id']].iloc[0]

        st.subheader("Systematic Opportunity ($H^R$) Components")

        with st.expander("3. AI-Enhancement Potential"):
            st.markdown(r"$$AI\text{-}Enhancement_o = (1 - Automation_t) \cdot AI\text{-}Augmentation_t$$")
            st.markdown("""
            where:
            *   $Automation_t$: The percentage of tasks in occupation $o$ that can be automated by AI at time $t$.
            *   $AI\text{-}Augmentation_t$: The potential productivity gain from AI tools in occupation $o$ at time $t$.
            """)
            st.metric(label="AI-Enhancement Score", value=f"{occupation_row['ai_enhancement']:.2f}")

        with st.expander("4. Job Growth Projections"):
            st.markdown(r"$$Growth_o = \frac{\text{Projected Jobs}_{o,t+10} - \text{Current Jobs}_{o,t}}{\text{Current Jobs}_{o,t}}$$")
            st.markdown(r"$$Growth_{\text{normalized}} = \frac{g + 0.5}{2.0} \times 100$$")
            st.markdown("""
            where:
            *   $Growth_o$: The projected growth rate for occupation $o$.
            *   $Growth_{\text{normalized}}$: The growth rate normalized to a 0-100 scale.
            """)
            st.metric(label="Raw Job Growth ($g$)", value=f"{occupation_row['growth']:.2%}")
            st.metric(label="Normalized Job Growth", value=f"{occupation_row['growth_normalized']:.2f}")

        with st.expander("5. Wage Premium & Entry Accessibility"):
            st.markdown(r"$$Wage_o = \frac{\text{AI-skilled wage}_o - \text{median wage}_o}{\text{median wage}_o}$$")
            st.markdown(r"$$Access_o = 1 - \frac{\text{Education Years Required} + \text{Experience Years Required}}{10}$$")
            st.markdown("""
            where:
            *   $Wage_o$: The premium offered for AI-skilled roles in occupation $o$.
            *   $Access_o$: The ease of entry into occupation $o$ based on educational and experiential requirements.
            """)
            st.metric(label="Wage Premium", value=f"{occupation_row['wage_premium']:.2f}")
            st.metric(label="Entry Accessibility", value=f"{occupation_row['entry_accessibility']:.2f}")

        with st.expander("6. Calculate Base Opportunity Score ($H_{\text{base}}$)"):
            st.markdown(r"$$H_{\text{base}}(o) = w_1 \cdot AI\text{-}Enhancement_o + w_2 \cdot Growth_{\text{normalized}} + w_3 \cdot Wage_o + w_4 \cdot Access_o$$")
            st.markdown("""
            where $w_1, w_2, w_3, w_4$ are the configurable weights for each sub-component (see Data Configuration).
            """)
            st.metric(label="Base Opportunity Score ($H_{\text{base}}$)", value=f"{occupation_row['h_base_score']:.2f}")

        with st.expander("7. Dynamic Multipliers: Growth & Regional"):
            st.markdown(r"$$M_{\text{growth}}(t) = 1 + \lambda_{\text{growth}} \cdot \left( \frac{\text{Job Postings}_{o,t}}{\text{Job Postings}_{o,t-1}} - 1 \right)$$")
            st.markdown(r"$$M_{\text{regional}}(t) = \frac{\text{Local Demand}_{i,t}}{\text{National Avg Demand}} \times (1 + \gamma_{\text{regional}} \cdot \text{Remote Work Factor}_o)$$")
            st.markdown("""
            where:
            *   $M_{\text{growth}}(t)$: Multiplier based on recent job posting trends, damped by $\lambda_{\text{growth}}$.
            *   $M_{\text{regional}}(t)$: Multiplier reflecting local demand and remote work potential, influenced by $\gamma_{\text{regional}}$.
            """)
            st.metric(label="Growth Multiplier ($M_{\text{growth}}$)", value=f"{occupation_row['growth_multiplier']:.2f}")
            st.metric(label="Regional Multiplier ($M_{\text{regional}}$)", value=f"{occupation_row['regional_multiplier']:.2f}")

        with st.expander("8. Calculate Final Systematic Opportunity ($H^R$)"):
            st.markdown(r"$$H^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$")
            st.markdown("""
            The final Systematic Opportunity score is the product of the base score and the dynamic multipliers.
            """)
            st.metric(label="Final Systematic Opportunity Score ($H^R$)", value=f"{employee_row['hr_r_score']:.2f}")

        st.subheader("Idiosyncratic Readiness ($V^R$) Components")

        with st.expander("9. AI-Fluency Factor"):
            st.markdown(r"$$AI\text{-}Fluency_i = \sum_{k=1}^4 \theta_k \cdot S_{i,k}$$")
            st.markdown("""
            The AI-Fluency score is a weighted sum of four sub-components ($S_{i,k}$), with weights $\theta_k$ (see Data Configuration).
            """)
            st.markdown(r"$$S_{i,1} = \frac{1}{4} (\text{Prompting}_i + \text{Tools}_i + \text{Understanding}_i + \text{DataLit}_i)$$")
            st.markdown(f"""
            $S_{i,1}$: **Technical AI Skills** - Average of scores in prompting, AI tool usage, AI understanding, and data literacy.
            *   Current Value: {employee_row['s1_technical_ai_skills']:.2f}
            """)
            st.markdown(r"$$S_{i,2} = \frac{\text{Output Quality}_{i,\text{with AI}}}{\text{Output Quality}_{i,\text{without AI}}} \cdot \frac{\text{Time}_{i,\text{without AI}}}{\text{Time}_{i,\text{with AI}}}$$")
            st.markdown(f"""
            $S_{i,2}$: **AI-Augmented Productivity** - Ratio of productivity with AI vs. without AI.
            *   Current Value: {employee_row['s2_ai_augmented_productivity']:.2f}
            """)
            st.markdown(r"$$S_{i,3} = \frac{\text{Errors Caught}_i}{\text{Total AI Errors}} + \frac{\text{Appropriate Trust Decisions}_i}{\text{Total Decisions}}$$")
            st.markdown(f"""
            $S_{i,3}$: **Critical AI Judgment** - Ability to identify and correct AI errors, and make sound decisions regarding AI outputs.
            *   Current Value: {employee_row['s3_critical_ai_judgment']:.2f}
            """)
            st.markdown(r"$$S_{i,4} = \frac{\Delta Proficiency_i}{\Delta t} \cdot \frac{1}{\text{Hours Invested}}$$")
            st.markdown(f"""
            $S_{i,4}$: **AI Learning Velocity** - How quickly an individual improves AI proficiency per unit of effort.
            *   Current Value: {employee_row['s4_ai_learning_velocity']:.2f}
            """)
            st.metric(label="Final AI-Fluency Score", value=f"{employee_row['ai_fluency_score']:.2f}")

        with st.expander("10. Domain-Expertise Factor"):
            st.markdown(r"$$Domain\text{-}Expertise_i = E_{\text{education}} \cdot E_{\text{experience}} \cdot E_{\text{specialization}}$$")
            st.markdown("""
            The Domain-Expertise score is a composite of educational foundation, practical experience, and specialization depth.
            """)
            # Fix applied here: separated descriptive markdown from f-string for current value
            st.markdown(r"""
            $E_{\text{education}}$: **Educational Foundation** - Score based on highest education level (e.g., PhD=100, Master\'s=80, Bachelor\'s=60, High School=30).
            """)
            st.markdown(f"""
            *   Current Value: {employee_row['e_education']:.2f}
            """)
            st.markdown(r"$$E_{\text{experience}} = 1 - e^{-\gamma_{\text{exp}} \cdot Years}$$")
            # Fix applied here: separated descriptive markdown from f-string for current value
            st.markdown(r"""
            $E_{\text{experience}}$: **Practical Experience** - Exponentially increasing score based on years of experience, with decay rate $\gamma_{\text{exp}}$.
            """)
            st.markdown(f"""
            *   Current Value: {employee_row['e_experience']:.2f}
            """)
            st.markdown(r"$$E_{\text{specialization}} = w_{\text{port}} \cdot \text{Portfolio}_i + w_{\text{recog}} \cdot \text{Recognition}_i + w_{\text{cred}} \cdot \text{Credentials}_i$$")
            # Fix applied here: separated descriptive markdown from f-string for current value
            st.markdown(r"""
            $E_{\text{specialization}}$: **Specialization Depth** - Weighted sum of portfolio, industry recognition, and credentials (weights $w$ configurable).
            """)
            st.markdown(f"""
            *   Current Value: {employee_row['e_specialization']:.2f}
            """)
            st.metric(label="Final Domain-Expertise Score", value=f"{employee_row['domain_expertise_score']:.2f}")

        with st.expander("11. Adaptive-Capacity Factor"):
            st.markdown(r"$$Adaptive\text{-}Capacity_i = \frac{1}{3} (C_{\text{cognitive}} + C_{\text{social}} + C_{\text{strategic}})$$")
            st.markdown("""
            The Adaptive-Capacity score is the average of cognitive, social, and strategic adaptive capacities.
            """)
            st.metric(label="Final Adaptive-Capacity Score", value=f"{employee_row['adaptive_capacity_score']:.2f}")

        with st.expander("12. Calculate Final Idiosyncratic Readiness ($V^R$)"):
            st.markdown(r"$$V^R(t) = w_{\text{VR1}} \cdot AI\text{-}Fluency_i(t) + w_{\text{VR2}} \cdot Domain\text{-}Expertise_i(t) + w_{\text{VR3}} \cdot Adaptive\text{-}Capacity_i(t)$$")
            st.markdown("""
            The final Idiosyncratic Readiness score is a weighted sum of the three main $V^R$ components, with weights $w_{VR}$ (see Data Configuration).
            """)
            st.metric(label="Final Idiosyncratic Readiness Score ($V^R$)", value=f"{employee_row['vr_score']:.2f}")

        st.subheader("Synergy Function & Overall AI-R")

        with st.expander("13. Synergy Function: Skills Match & Timing Factor"):
            st.markdown(r"$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$")
            st.markdown(r"$$Alignment_i = \frac{\text{Skills Match Score}_i}{\text{Maximum Possible Match}} \times \text{Timing Factor}_i$$")
            st.markdown(r"$$Match_i = \sum_{s \in S} \min(\text{Individual Skill}_{i,s}, \text{Required Skill}_{o,s}) \cdot \text{Importance}_s$$")
            st.markdown(f"""
            **Skills Match Score** ($Match_i$): A weighted sum of the minimum of individual skill proficiency and required skill proficiency for each skill $s$.
            *   Current Value: {employee_row['skills_match_score']:.2f}
            
            **Timing Factor** ($Timing Factor_i$): A dynamic multiplier based on current AI-R compared to the average.
            *   If employee AI-R is significantly above average, Timing Factor may be > 1 (early adopter bonus).
            *   If employee AI-R is significantly below average, Timing Factor may be < 1 (needs to catch up).
            *   Current Value: {employee_row['timing_factor']:.2f}

            **Alignment Factor** ($Alignment_i$): The overall alignment between an individual's skills and the market's requirements.
            *   Current Value: {employee_row['alignment_factor']:.2f}
            """)

        with st.expander("14. Calculate Final Synergy Score"):
            st.markdown("The final Synergy Score quantifies how well the individual's readiness aligns with and leverages market opportunities.")
            st.metric(label="Final Synergy Score", value=f"{employee_row['synergy_score']:.2f}")

        with st.expander("15. Calculate Overall AI-Readiness Score (AI-R)"):
            st.markdown(r"$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$")
            st.markdown("The final AI-Readiness Score is calculated using the global $\\alpha$ and $\\beta$ parameters applied to the $V^R$, $H^R$, and Synergy scores.")
            
            st.dataframe(st.session_state.df_employees[['employee_id', 'job_role', 'department', 'vr_score', 'hr_r_score', 'synergy_score', 'current_ai_r_score']].head())
            st.metric(label="Average AI-Readiness Score Across All Employees", value=f"{st.session_state.df_employees['current_ai_r_score'].mean():.2f}")
            st.metric(label=f"Overall AI-Readiness Score for {selected_employee_id}", value=f"{employee_row['current_ai_r_score']:.2f}")

# --- Page: AI-R Report & Skills Gap Analysis ---
elif selection == "AI-R Report & Skills Gap Analysis":
    st.header("16. AI-Readiness Report & Skills Gap Analysis")
    st.markdown("""
    This section provides aggregated insights into the workforce's AI-Readiness, allowing leaders
    to identify collective strengths and weaknesses and inform strategic planning.
    """)

    if st.session_state.df_employees.empty:
        st.warning("Please generate synthetic data and run calculations on previous pages first.")
    else:
        st.subheader("AI-Readiness Summary Report")
        group_by_options = ['department', 'job_role', 'education_level']
        selected_group_by = st.selectbox(
            "Group report by:",
            group_by_options,
            key='report_group_by_column'
        )

        ai_r_summary = generate_ai_r_report_summary(st.session_state.df_employees, selected_group_by)
        st.dataframe(ai_r_summary)
        st.info("This table summarizes average AI-R and its components across different groups.")

        st.subheader("Skills Gap Analysis Heatmap ($V^R$ Sub-Components)")
        st.markdown("""
        The heatmap below visualizes the average scores for the three main Idiosyncratic Readiness ($V^R$)
        sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity) grouped by your selection.
        Lower scores (darker colors) indicate potential areas for upskilling initiatives.
        """)
        
        fig = plot_skills_gap_heatmap(st.session_state.df_employees, selected_group_by)
        st.pyplot(fig)
        st.info("Identify departments or job roles with lower scores in specific $V^R$ sub-components to target training.")

# --- Page: What-If Scenario Engine ---
elif selection == "What-If Scenario Engine":
    st.header("17. What-If Scenario Engine: Simulating Learning Pathway Impact")
    st.markdown("""
    Use this engine to simulate the potential impact of a single learning pathway on an individual's
    AI-Readiness score. Adjust completion and mastery rates to see different outcomes.
    """)

    if st.session_state.df_employees.empty or st.session_state.df_pathways.empty:
        st.warning("Please generate synthetic data and run calculations on previous pages first.")
    else:
        employee_ids = st.session_state.df_employees['employee_id'].tolist()
        pathway_ids = st.session_state.df_pathways['pathway_id'].tolist()

        selected_employee_id = st.selectbox("Select Employee:", employee_ids, key='whatif_employee_id')
        selected_pathway_id = st.selectbox("Select Learning Pathway:", pathway_ids, key='whatif_pathway_id')

        completion_rate = st.slider("Pathway Completion Rate", min_value=0.0, max_value=1.0, value=0.7, step=0.05,
                                    help="The percentage of the pathway successfully completed.")
        mastery_score = st.slider("Achieved Mastery Score", min_value=0.0, max_value=1.0, value=0.8, step=0.05,
                                  help="The level of skill mastery achieved after completing the pathway.")

        st.markdown(r"$$AI-R_{i,t+1} = AI-R_{i,t} + \sum_{p \in P} \Delta_p \cdot Completion_p \cdot Mastery_p$$")
        st.markdown(f"""
        Where $\Delta_p$ represents the potential AI-R improvement from pathway $p$, adjusted by its completion and mastery rates.
        This simplified formula shows the projected AI-R score after the intervention.
        """)

        if st.button("Run What-If Simulation"):
            with st.spinner("Running simulation..."):
                current_ai_r, projected_ai_r, delta_ai_r = simulate_pathway_impact(
                    selected_employee_id, selected_pathway_id, completion_rate, mastery_score,
                    st.session_state.df_employees, st.session_state.df_pathways, st.session_state.PARAMS
                )

            if current_ai_r is not None:
                st.success("Simulation complete!")
                st.metric(label="Current AI-Readiness Score", value=f"{current_ai_r:.2f}")
                st.metric(label="Projected AI-Readiness Score", value=f"{projected_ai_r:.2f}")
                st.metric(label="Change in AI-Readiness ($\Delta AI-R$)", value=f"{delta_ai_r:.2f}")

                st.subheader("AI-R Comparison Chart")
                fig = plot_current_vs_projected_ai_r(selected_employee_id, st.session_state.df_employees)
                st.pyplot(fig)
            else:
                st.error("Failed to run simulation. Please check inputs and data.")

# --- Page: Multi-Step Pathway Optimization ---
elif selection == "Multi-Step Pathway Optimization":
    st.header("18. Multi-Step Pathway Optimization")
    st.markdown("""
    This section helps identify an optimal sequence of learning pathways for a selected employee,
    considering a maximum time budget and a trade-off between AI-R improvement and cost.
    """)

    if st.session_state.df_employees.empty or st.session_state.df_pathways.empty:
        st.warning("Please generate synthetic data and run calculations on previous pages first.")
    else:
        employee_ids = st.session_state.df_employees['employee_id'].tolist()
        selected_employee_id = st.selectbox("Select Employee for Optimization:", employee_ids, key='optimize_employee_id')

        T_max_hours = st.number_input("Maximum Time Budget (hours)", min_value=10, max_value=500, value=100, step=10,
                                     help="Total hours the employee can spend on learning pathways.")
        cost_weight_lambda = st.number_input("Cost Weight (λ_cost)", min_value=0.0, max_value=1.0, value=0.01, step=0.005,
                                           help="Higher values prioritize cost-effectiveness over raw AI-R improvement. This is a trade-off parameter.")

        st.subheader("Optimization Objective and Constraints")
        st.markdown(r"$$\max_{P_1,...,P_K} AI-R(P_1,..., P_K) - \lambda_{\text{cost}} \cdot \sum_{k=1}^K Cost(P_k)$$")
        # FIX: Changed f-string to raw string for LaTeX expression to avoid SyntaxError
        st.markdown(r"""
        This objective function aims to maximize the projected AI-R score while penalizing the total cost of the pathways.
        A higher $\lambda_{\text{cost}}$ makes the optimizer more sensitive to pathway costs.
        """)

        st.markdown(r"$$ \sum_{k=1}^K Time(P_k) \leq T_{\text{max}} $$")
        st.markdown(r"$$ P_k \in P_{\text{feasible}} $$")
        st.markdown(r"$$ Prerequisites(P_k) \subseteq \{P_1,...,P_{k-1}\} $$")
        st.markdown(f"""
        **Constraints:**
        *   **Time Budget:** The total time spent on selected pathways cannot exceed $T_{\text{max}}$ hours.
        *   **Feasible Pathways:** Only available pathways can be selected.
        *   **Prerequisites:** Any pathway with prerequisites must have its prerequisites completed in earlier steps of the sequence.
        """)
        
        if st.button("Run Optimization"):
            with st.spinner("Running pathway optimization..."):
                recommended_sequence, projected_final_ai_r, total_cost, total_time_hours, ai_r_improvement = optimize_pathway_sequence(
                    selected_employee_id, T_max_hours, cost_weight_lambda,
                    st.session_state.df_employees, st.session_state.df_pathways, st.session_state.PARAMS
                )

            if recommended_sequence is not None:
                st.success("Optimization complete!")
                st.subheader("Optimization Results")
                
                employee_current_ai_r = st.session_state.df_employees[
                    st.session_state.df_employees['employee_id'] == selected_employee_id
                ].iloc[0]['current_ai_r_score']

                st.metric(label="Current AI-Readiness Score", value=f"{employee_current_ai_r:.2f}")
                st.metric(label="Projected Final AI-Readiness Score", value=f"{projected_final_ai_r:.2f}")
                st.metric(label="AI-R Improvement", value=f"{ai_r_improvement:.2f}")
                st.metric(label="Total Estimated Cost", value=f"${total_cost:.2f}")
                st.metric(label="Total Estimated Time (hours)", value=f"{total_time_hours:.2f} hrs")

                st.markdown("### Recommended Learning Pathway Sequence:")
                if recommended_sequence:
                    for i, pathway_name in enumerate(recommended_sequence):
                        st.markdown(f"{i+1}. {pathway_name}")
                else:
                    st.info("No optimal pathways found within the given constraints or no beneficial pathways identified.")

                st.subheader("AI-R Comparison Chart (Before vs. After Optimization)")
                fig = plot_current_vs_projected_ai_r(selected_employee_id, st.session_state.df_employees)
                st.pyplot(fig)
            else:
                st.error("Failed to run optimization. Please check inputs and data.")

# --- Page: Strategic Recommendations ---
elif selection == "Strategic Recommendations":
    st.header("19. Strategic Recommendations & Conclusion")
    st.markdown("""
    Based on the AI-Readiness framework and the insights gained from the application's analysis and simulations,
    here are key strategic recommendations for AI Workforce leaders and HR executives.
    """)

    st.subheader("1. Data-Driven Upskilling Initiatives")
    st.markdown("""
    Leverage the **AI-R Report & Skills Gap Analysis** to identify specific departments, job roles, or even individuals
    with lower scores in critical $V^R$ sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
    This granular insight enables highly targeted training programs, maximizing the return on learning investments.
    For instance, if 'Marketing Specialists' show low 'AI-Fluency', prioritize prompt engineering and AI tool workshops for that group.
    """)

    st.subheader("2. Personalized Learning Pathways")
    st.markdown("""
    Utilize the **What-If Scenario Engine** and **Multi-Step Pathway Optimization** to create personalized learning
    roadmaps for employees. Instead of one-size-fits-all training, tailor pathways based on individual
    current AI-R scores, career aspirations (target occupations), and learning styles.
    The optimization engine helps find cost-effective and time-efficient sequences to achieve desired AI-R uplift.
    """)

    st.subheader("3. Dynamic Workforce Planning")
    st.markdown("""
    The `Systematic Opportunity ($H^R$)` component provides a dynamic view of market demands.
    Regularly review $H^R$ trends (job growth, wage premiums, AI-enhancement potential) for key occupations.
    This foresight allows HR to proactively invest in skills development for roles poised for AI-driven growth
    and to strategically re-skill employees in roles facing higher automation risks.
    """)

    st.subheader("4. Cultivating Synergy and Alignment")
    st.markdown("""
    The **Synergy** component highlights the importance of aligning individual skills with market needs.
    Focus on initiatives that enhance "Skills Match" and "Timing Factor". This includes:
    *   **Skill Mapping:** Continuously update individual skill profiles and job role skill requirements.
    *   **Internal Mobility:** Facilitate movement of employees to roles where their developing AI skills have higher market synergy.
    *   **Proactive Engagement:** Identify early adopters (high timing factor) for leadership roles in AI transformation, and provide targeted support for those needing to catch up.
    """)

    st.subheader("5. Fostering an Adaptive Culture")
    st.markdown("""
    The **Adaptive-Capacity** factor is crucial for long-term AI readiness. Implement programs that enhance:
    *   **Cognitive Agility:** Problem-solving, critical thinking in ambiguous AI contexts.
    *   **Social Intelligence:** Collaboration with AI systems and diverse human teams.
    *   **Strategic Foresight:** Understanding the broader implications of AI and anticipating future skill needs.
    This creates a resilient workforce capable of continuous learning and adaptation.
    """)

    st.subheader("Conclusion")
    st.markdown("""
    The AI-Readiness & Upskilling Strategizer provides a robust, data-driven framework to navigate the complexities
    of the AI-driven workforce transformation. By continuously assessing, simulating, and optimizing,
    organizations can build a future-proof workforce that thrives in the age of AI.
    """)

# Your code ends here
