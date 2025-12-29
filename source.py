import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Global Model Parameters (Adjustable by Alice for scenario analysis) ---

# AI-Readiness Score (AI-R) weights
ALPHA = 0.6  # Weight on Idiosyncratic Readiness (VR)
BETA = 0.15  # Synergy coefficient

# Idiosyncratic Readiness (VR) component weights
VR_W1_AI_FLUENCY = 0.45
VR_W2_DOMAIN_EXPERTISE = 0.35
VR_W3_ADAPTIVE_CAPACITY = 0.20
VR_COMPONENT_WEIGHTS = {
    'ai_fluency': VR_W1_AI_FLUENCY,
    'domain_expertise': VR_W2_DOMAIN_EXPERTISE,
    'adaptive_capacity': VR_W3_ADAPTIVE_CAPACITY
}

# AI-Fluency sub-factor weights (theta_k)
THETA1_TECHNICAL_AI_SKILLS = 0.30
THETA2_AI_AUGMENTED_PRODUCTIVITY = 0.35
THETA3_CRITICAL_AI_JUDGMENT = 0.20
THETA4_AI_LEARNING_VELOCITY = 0.15
AI_FLUENCY_THETA_WEIGHTS = {
    'technical_ai_skills': THETA1_TECHNICAL_AI_SKILLS,
    'ai_augmented_productivity': THETA2_AI_AUGMENTED_PRODUCTIVITY,
    'critical_ai_judgment': THETA3_CRITICAL_AI_JUDGMENT,
    'ai_learning_velocity': THETA4_AI_LEARNING_VELOCITY
}

# Domain-Expertise parameters
GAMMA_EXPERIENCE_DECAY = 0.15 # For E_experience = 1 - e^(-gamma_experience * Years)

# Systematic Opportunity (HR) base score weights (w_j)
HR_W1_AI_ENHANCEMENT = 0.30
HR_W2_JOB_GROWTH = 0.30
HR_W3_WAGE_PREMIUM = 0.25
HR_W4_ENTRY_ACCESSIBILITY = 0.15
HBASE_WEIGHTS = {
    'ai_enhancement': HR_W1_AI_ENHANCEMENT,
    'job_growth': HR_W2_JOB_GROWTH,
    'wage_premium': HR_W3_WAGE_PREMIUM,
    'entry_accessibility': HR_W4_ENTRY_ACCESSIBILITY
}

# Systematic Opportunity (HR) multiplier parameters
LAMBDA_GROWTH_MULTIPLIER = 0.3 # Dampens volatility for growth multiplier
GAMMA_REMOTE_WORK = 0.2 # Weight for remote work factor in regional multiplier

# Synergy Function parameters
MAX_POSSIBLE_SKILL_MATCH = 100 # Maximum sum of required skill levels (assuming 0-10 scale for 10 skills)

# Learning Pathway Optimization parameters
LAMBDA_COST_WEIGHT = 0.1 # Weight for cost in the optimization objective (higher means more cost-averse)
MAX_LEARNING_TIME_HOURS = 200 # Max hours Alice can invest
MAX_LEARNING_BUDGET_USD = 1500 # Max budget Alice has for learning

# Set plot style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Libraries imported and global parameters defined.")
# Create simulated data files for the notebook
def create_simulated_data():
    # idiosyncratic_data.csv
    id_data = {
        'persona_id': ['Alice'],
        'prompting': [0.6], 'ai_tools': [0.5], 'understanding': [0.6], 'data_literacy': [0.7],
        'ai_augmented_productivity_ratio': [0.7], 'critical_ai_judgment_accuracy': [0.65],
        'appropriate_trust_decisions_ratio': [0.75],
        'proficiency_gain': [0.10], 'hours_invested': [50],
        'education_level': ['Master\'s in Finance'], 'experience_years': [7],
        'portfolio_score': [0.7], 'recognition_score': [0.6], 'credentials_score': [0.8],
        'cognitive_flexibility': [0.75], 'social_emotional_intelligence': [0.8],
        'strategic_career_management': [0.7]
    }
    pd.DataFrame(id_data).to_csv('idiosyncratic_data.csv', index=False)

    # systematic_opportunity_data.csv
    so_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'ai_enhancement_potential': [0.85, 0.90, 0.80, 0.75],
        'current_jobs': [5000, 4500, 6000, 7000],
        'projected_jobs_10yr': [7500, 7000, 8500, 9000],
        'ai_skilled_wage': [180000, 195000, 160000, 150000],
        'median_wage': [120000, 130000, 110000, 105000],
        'education_years_required': [18, 18, 16, 16],
        'experience_years_required': [5, 6, 4, 3],
        'remote_work_factor': [0.6, 0.5, 0.7, 0.75]
    }
    pd.DataFrame(so_data).to_csv('systematic_opportunity_data.csv', index=False)

    # job_postings_data.csv
    jp_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'] * 2,
        'month': [1,2]*4,
        'job_postings_t': [500, 520, 450, 480, 600, 630, 700, 720],
        'job_postings_t_minus_1': [490, 500, 440, 450, 590, 600, 680, 700]
    }
    pd.DataFrame(jp_data).to_csv('job_postings_data.csv', index=False)

    # regional_demand_data.csv
    rd_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'local_demand': [1.1, 0.9, 1.2, 1.0],
        'national_avg_demand': [1.0, 1.0, 1.0, 1.0]
    }
    pd.DataFrame(rd_data).to_csv('regional_demand_data.csv', index=False)

    # skill_requirements.csv
    sr_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'Python': [9, 10, 8, 9], 'SQL': [7, 8, 9, 8], 'ML_basics': [8, 9, 7, 8],
        'Risk_Analysis': [9, 6, 10, 7], 'Financial_Modeling': [9, 7, 8, 8],
        'Data_Viz': [7, 8, 7, 8], 'Quant_Models': [10, 8, 7, 6], 'AI_Ethics': [7, 8, 9, 7],
        'GenAI_Tools': [6, 7, 6, 7], 'Cloud_Platforms': [7, 9, 7, 8]
    }
    pd.DataFrame(sr_data).to_csv('skill_requirements.csv', index=False)

    # learning_pathways.csv
    lp_data = {
        'pathway_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008'],
        'pathway_name': ['Prompt Engineering for Finance', 'Advanced ML for Trading',
                         'AI Ethics in Risk Management', 'Generative AI for Financial Data',
                         'Deep Learning Fundamentals', 'Human-AI Collaboration Skills',
                         'Financial Domain-Specific AI', 'Strategic Career Planning with AI'],
        'type': ['AI-Fluency', 'Domain+AI', 'Adaptive Capacity', 'AI-Fluency',
                 'Domain+AI', 'Adaptive Capacity', 'Domain+AI', 'Adaptive Capacity'],
        'impact_ai_fluency': [10, 5, 2, 12, 8, 3, 6, 2],
        'impact_domain_expertise': [3, 15, 1, 4, 10, 1, 18, 1],
        'impact_adaptive_capacity': [1, 2, 8, 1, 2, 7, 2, 9],
        'estimated_time_hours': [40, 80, 30, 50, 70, 25, 90, 35],
        'estimated_cost_usd': [300, 800, 200, 450, 700, 180, 950, 250],
        'prerequisites': ['[]', '[P001]', '[]', '[]', '[P001]', '[]', '[P001]', '[]']
    }
    pd.DataFrame(lp_data).to_csv('learning_pathways.csv', index=False)

# Ensure simulated data exists
create_simulated_data()

# Alice's current professional profile
alice_profile = {
    'persona_id': 'Alice',
    'education_level': 'Master\'s in Finance',
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

# Target AI-enabled financial roles Alice is considering
target_roles = ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist']

# Load pre-simulated dataframes
idiosyncratic_df = pd.read_csv('idiosyncratic_data.csv')
systematic_df = pd.read_csv('systematic_opportunity_data.csv')
job_postings_df = pd.read_csv('job_postings_data.csv')
regional_demand_df = pd.read_csv('regional_demand_data.csv')
skill_requirements_df = pd.read_csv('skill_requirements.csv')
learning_pathways_df = pd.read_csv('learning_pathways.csv')

print(f"Alice's Profile:")
for key, value in alice_profile.items():
    if key != 'current_skills' and key != 'ai_fluency_subfactors' and key != 'domain_expertise_subfactors' and key != 'adaptive_capacity_subfactors':
        print(f"- {key.replace('_', ' ').title()}: {value}")
print(f"- Current Skills: {', '.join([f'{s}: {l}' for s,l in alice_profile['current_skills'].items()])}")
print(f"\nTarget AI-enabled Roles: {', '.join(target_roles)}")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Global Model Parameters (Adjustable by Alice for scenario analysis) ---

# AI-Readiness Score (AI-R) weights
ALPHA = 0.6  # Weight on Idiosyncratic Readiness (VR)
BETA = 0.15  # Synergy coefficient

# Idiosyncratic Readiness (VR) component weights
VR_W1_AI_FLUENCY = 0.45
VR_W2_DOMAIN_EXPERTISE = 0.35
VR_W3_ADAPTIVE_CAPACITY = 0.20
VR_COMPONENT_WEIGHTS = {
    'ai_fluency': VR_W1_AI_FLUENCY,
    'domain_expertise': VR_W2_DOMAIN_EXPERTISE,
    'adaptive_capacity': VR_W3_ADAPTIVE_CAPACITY
}

# AI-Fluency sub-factor weights (theta_k)
THETA1_TECHNICAL_AI_SKILLS = 0.30
THETA2_AI_AUGMENTED_PRODUCTIVITY = 0.35
THETA3_CRITICAL_AI_JUDGMENT = 0.20
THETA4_AI_LEARNING_VELOCITY = 0.15
AI_FLUENCY_THETA_WEIGHTS = {
    'technical_ai_skills': THETA1_TECHNICAL_AI_SKILLS,
    'ai_augmented_productivity': THETA2_AI_AUGMENTED_PRODUCTIVITY,
    'critical_ai_judgment': THETA3_CRITICAL_AI_JUDGMENT,
    'ai_learning_velocity': THETA4_AI_LEARNING_VELOCITY
}

# Domain-Expertise parameters
GAMMA_EXPERIENCE_DECAY = 0.15 # For E_experience = 1 - e^(-gamma_experience * Years)

# Systematic Opportunity (HR) base score weights (w_j)
HR_W1_AI_ENHANCEMENT = 0.30
HR_W2_JOB_GROWTH = 0.30
HR_W3_WAGE_PREMIUM = 0.25
HR_W4_ENTRY_ACCESSIBILITY = 0.15
HBASE_WEIGHTS = {
    'ai_enhancement': HR_W1_AI_ENHANCEMENT,
    'job_growth': HR_W2_JOB_GROWTH,
    'wage_premium': HR_W3_WAGE_PREMIUM,
    'entry_accessibility': HR_W4_ENTRY_ACCESSIBILITY
}

# Systematic Opportunity (HR) multiplier parameters
LAMBDA_GROWTH_MULTIPLIER = 0.3 # Dampens volatility for growth multiplier
GAMMA_REMOTE_WORK = 0.2 # Weight for remote work factor in regional multiplier

# Synergy Function parameters
MAX_POSSIBLE_SKILL_MATCH = 100 # Maximum sum of required skill levels (assuming 0-10 scale for 10 skills)

# Learning Pathway Optimization parameters
LAMBDA_COST_WEIGHT = 0.1 # Weight for cost in the optimization objective (higher means more cost-averse)
MAX_LEARNING_TIME_HOURS = 200 # Max hours Alice can invest
MAX_LEARNING_BUDGET_USD = 1500 # Max budget Alice has for learning

# Set plot style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Libraries imported and global parameters defined.")

# Create simulated data files for the notebook
def create_simulated_data():
    # idiosyncratic_data.csv
    id_data = {
        'persona_id': ['Alice'],
        'prompting': [0.6], 'ai_tools': [0.5], 'understanding': [0.6], 'data_literacy': [0.7],
        'ai_augmented_productivity_ratio': [0.7], 'critical_ai_judgment_accuracy': [0.65],
        'appropriate_trust_decisions_ratio': [0.75],
        'proficiency_gain': [0.10], 'hours_invested': [50],
        'education_level': ['Master\'s in Finance'], 'experience_years': [7],
        'portfolio_score': [0.7], 'recognition_score': [0.6], 'credentials_score': [0.8],
        'cognitive_flexibility': [0.75], 'social_emotional_intelligence': [0.8],
        'strategic_career_management': [0.7]
    }
    pd.DataFrame(id_data).to_csv('idiosyncratic_data.csv', index=False)

    # systematic_opportunity_data.csv
    so_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'ai_enhancement_potential': [0.85, 0.90, 0.80, 0.75],
        'current_jobs': [5000, 4500, 6000, 7000],
        'projected_jobs_10yr': [7500, 7000, 8500, 9000],
        'ai_skilled_wage': [180000, 195000, 160000, 150000],
        'median_wage': [120000, 130000, 110000, 105000],
        'education_years_required': [18, 18, 16, 16],
        'experience_years_required': [5, 6, 4, 3],
        'remote_work_factor': [0.6, 0.5, 0.7, 0.75]
    }
    pd.DataFrame(so_data).to_csv('systematic_opportunity_data.csv', index=False)

    # job_postings_data.csv
    jp_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'] * 2,
        'month': [1,2]*4,
        'job_postings_t': [500, 520, 450, 480, 600, 630, 700, 720],
        'job_postings_t_minus_1': [490, 500, 440, 450, 590, 600, 680, 700]
    }
    pd.DataFrame(jp_data).to_csv('job_postings_data.csv', index=False)

    # regional_demand_data.csv
    rd_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'local_demand': [1.1, 0.9, 1.2, 1.0],
        'national_avg_demand': [1.0, 1.0, 1.0, 1.0]
    }
    pd.DataFrame(rd_data).to_csv('regional_demand_data.csv', index=False)

    # skill_requirements.csv
    sr_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'Python': [9, 10, 8, 9], 'SQL': [7, 8, 9, 8], 'ML_basics': [8, 9, 7, 8],
        'Risk_Analysis': [9, 6, 10, 7], 'Financial_Modeling': [9, 7, 8, 8],
        'Data_Viz': [7, 8, 7, 8], 'Quant_Models': [10, 8, 7, 6], 'AI_Ethics': [7, 8, 9, 7],
        'GenAI_Tools': [6, 7, 6, 7], 'Cloud_Platforms': [7, 9, 7, 8]
    }
    pd.DataFrame(sr_data).to_csv('skill_requirements.csv', index=False)

    # learning_pathways.csv
    lp_data = {
        'pathway_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008'],
        'pathway_name': ['Prompt Engineering for Finance', 'Advanced ML for Trading',
                         'AI Ethics in Risk Management', 'Generative AI for Financial Data',
                         'Deep Learning Fundamentals', 'Human-AI Collaboration Skills',
                         'Financial Domain-Specific AI', 'Strategic Career Planning with AI'],
        'type': ['AI-Fluency', 'Domain+AI', 'Adaptive Capacity', 'AI-Fluency',
                 'Domain+AI', 'Adaptive Capacity', 'Domain+AI', 'Adaptive Capacity'],
        'impact_ai_fluency': [10, 5, 2, 12, 8, 3, 6, 2],
        'impact_domain_expertise': [3, 15, 1, 4, 10, 1, 18, 1],
        'impact_adaptive_capacity': [1, 2, 8, 1, 2, 7, 2, 9],
        'estimated_time_hours': [40, 80, 30, 50, 70, 25, 90, 35],
        'estimated_cost_usd': [300, 800, 200, 450, 700, 180, 950, 250],
        'prerequisites': ['[]', '[P001]', '[]', '[]', '[P001]', '[]', '[P001]', '[]']
    }
    pd.DataFrame(lp_data).to_csv('learning_pathways.csv', index=False)

# Ensure simulated data exists
create_simulated_data()

# Alice's current professional profile
alice_profile = {
    'persona_id': 'Alice',
    'education_level': 'Master\'s in Finance',
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

# Target AI-enabled financial roles Alice is considering
target_roles = ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist']

# Load pre-simulated dataframes
idiosyncratic_df = pd.read_csv('idiosyncratic_data.csv')
systematic_df = pd.read_csv('systematic_opportunity_data.csv')
job_postings_df = pd.read_csv('job_postings_data.csv')
regional_demand_df = pd.read_csv('regional_demand_data.csv')
skill_requirements_df = pd.read_csv('skill_requirements.csv')
learning_pathways_df = pd.read_csv('learning_pathways.csv')

print(f"Alice's Profile:")
for key, value in alice_profile.items():
    if key != 'current_skills' and key != 'ai_fluency_subfactors' and key != 'domain_expertise_subfactors' and key != 'adaptive_capacity_subfactors':
        print(f"- {key.replace('_', ' ').title()}: {value}")
print(f"- Current Skills: {', '.join([f'{s}: {l}' for s,l in alice_profile['current_skills'].items()])}")
print(f"\nTarget AI-enabled Roles: {', '.join(target_roles)}")


def calculate_ai_fluency(subfactors, theta_weights):
    """Calculates AI-Fluency score based on sub-factors."""
    s1 = np.mean([subfactors['prompting'], subfactors['ai_tools'], subfactors['understanding'], subfactors['data_literacy']])
    s2 = subfactors['ai_augmented_productivity'] 
    s3 = subfactors['critical_ai_judgment']
    s4 = subfactors['proficiency_gain'] / subfactors['hours_invested'] if subfactors['hours_invested'] > 0 else 0
    s4 = np.clip(s4 * 100, 0, 1)

    ai_fluency_score = (
        theta_weights['technical_ai_skills'] * s1 +
        theta_weights['ai_augmented_productivity'] * s2 +
        theta_weights['critical_ai_judgment'] * s3 +
        theta_weights['ai_learning_velocity'] * s4
    )
    return np.clip(ai_fluency_score, 0, 1)

def calculate_domain_expertise(education_level, experience_years, specialization_depth_scores, gamma_exp):
    """Calculates Domain-Expertise score."""
    edu_map = {
        'PhD in target field': 1.0,
        'Master\'s in Finance': 0.85,
        'Master\'s in target field': 0.85,
        'Bachelor\'s in target field': 0.70,
        'Associate\'s/Certificate': 0.60,
        'HS + significant coursework': 0.50
    }
    e_education = edu_map.get(education_level, 0.50)

    e_experience = 1 - np.exp(-gamma_exp * experience_years)

    e_specialization = (
        0.4 * specialization_depth_scores['portfolio'] +
        0.3 * specialization_depth_scores['recognition'] +
        0.3 * specialization_depth_scores['credentials']
    )
    
    domain_expertise_score = e_education * e_experience * e_specialization
    return np.clip(domain_expertise_score, 0, 1)

def calculate_adaptive_capacity(subfactors):
    """Calculates Adaptive-Capacity score."""
    c_cognitive = subfactors['cognitive_flexibility']
    c_social = subfactors['social_emotional_intelligence']
    c_strategic = subfactors['strategic_career_management']
    
    adaptive_capacity_score = (c_cognitive + c_social + c_strategic) / 3
    return np.clip(adaptive_capacity_score, 0, 1)

def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, vr_weights):
    """Calculates total Idiosyncratic Readiness (VR) score."""
    vr_score = (
        vr_weights['ai_fluency'] * ai_fluency +
        vr_weights['domain_expertise'] * domain_expertise +
        vr_weights['adaptive_capacity'] * adaptive_capacity
    )
    return np.clip(vr_score * 100, 0, 100)

# Execute VR calculation for Alice
alice_id_data = idiosyncratic_df[idiosyncratic_df['persona_id'] == alice_profile['persona_id']].iloc[0]

alice_ai_fluency_subfactors = {
    'prompting': alice_id_data['prompting'],
    'ai_tools': alice_id_data['ai_tools'],
    'understanding': alice_id_data['understanding'],
    'data_literacy': alice_id_data['data_literacy'],
    'ai_augmented_productivity': alice_id_data['ai_augmented_productivity_ratio'],
    'critical_ai_judgment': alice_id_data['critical_ai_judgment_accuracy'],
    'appropriate_trust_decisions': alice_id_data['appropriate_trust_decisions_ratio'],
    'proficiency_gain': alice_id_data['proficiency_gain'],
    'hours_invested': alice_id_data['hours_invested']
}

alice_domain_expertise_subfactors = {
    'portfolio': alice_id_data['portfolio_score'],
    'recognition': alice_id_data['recognition_score'],
    'credentials': alice_id_data['credentials_score']
}

alice_adaptive_capacity_subfactors = {
    'cognitive_flexibility': alice_id_data['cognitive_flexibility'],
    'social_emotional_intelligence': alice_id_data['social_emotional_intelligence'],
    'strategic_career_management': alice_id_data['strategic_career_management']
}

alice_ai_fluency_score = calculate_ai_fluency(alice_ai_fluency_subfactors, AI_FLUENCY_THETA_WEIGHTS)
alice_domain_expertise_score = calculate_domain_expertise(
    alice_id_data['education_level'], 
    alice_id_data['experience_years'], 
    alice_domain_expertise_subfactors, 
    GAMMA_EXPERIENCE_DECAY
)
alice_adaptive_capacity_score = calculate_adaptive_capacity(alice_adaptive_capacity_subfactors)

alice_vr_score = calculate_vr(
    alice_ai_fluency_score, alice_domain_expertise_score, alice_adaptive_capacity_score, VR_COMPONENT_WEIGHTS
)

print(f"--- Alice's Idiosyncratic Readiness (VR) Breakdown ---")
print(f"AI-Fluency Score (normalized): {alice_ai_fluency_score:.2f}")
print(f"Domain-Expertise Score (normalized): {alice_domain_expertise_score:.2f}")
print(f"Adaptive-Capacity Score (normalized): {alice_adaptive_capacity_score:.2f}")
print(f"\nAlice's Total Idiosyncratic Readiness (VR) Score: {alice_vr_score:.2f}")
def normalize_growth(growth_rate):
    """Normalizes job growth rate to a [0, 100] scale."""
    return np.clip(((growth_rate + 0.5) / 2.0) * 100, 0, 100)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    """Calculates wage premium as a ratio."""
    if median_wage == 0:
        return 0
    return np.clip((ai_skilled_wage - median_wage) / median_wage, 0, 1)

def calculate_entry_accessibility(education_years_required, experience_years_required):
    """Calculates entry accessibility."""
    total_requirements = education_years_required + experience_years_required
    return np.clip(1 - (total_requirements / 28), 0, 1)

def calculate_hbase(ai_enhancement, growth_normalized, wage_premium, entry_accessibility, hbase_weights):
    """Calculates the base opportunity score for a role."""
    hbase_score = (
        hbase_weights['ai_enhancement'] * ai_enhancement +
        hbase_weights['job_growth'] * (growth_normalized / 100) +
        hbase_weights['wage_premium'] * wage_premium +
        hbase_weights['entry_accessibility'] * entry_accessibility
    )
    return np.clip(hbase_score, 0, 1)

def calculate_mgrowth(job_postings_t, job_postings_t_minus_1, lambda_param):
    """Calculates the growth multiplier based on job posting momentum."""
    if job_postings_t_minus_1 == 0:
        return 1.0
    momentum = (job_postings_t / job_postings_t_minus_1) - 1
    return 1 + lambda_param * momentum

def calculate_mregional(local_demand, national_avg_demand, remote_work_factor, gamma_param):
    """Calculates the regional multiplier."""
    if national_avg_demand == 0:
        return 1.0
    demand_ratio = local_demand / national_avg_demand
    return demand_ratio * (1 + gamma_param * remote_work_factor)

def calculate_hr(hbase_score, mgrowth_score, mregional_score):
    """Calculates total Systematic Opportunity (HR) score."""
    hr_score = hbase_score * mgrowth_score * mregional_score
    return np.clip(hr_score * 100, 0, 100)

# Execute HR calculation for each target role for Alice
hr_scores = {}
for role in target_roles:
    role_data = systematic_df[systematic_df['role'] == role].iloc[0]
    jp_role_data = job_postings_df[job_postings_df['role'] == role].iloc[-1]
    rd_role_data = regional_demand_df[regional_demand_df['role'] == role].iloc[0]

    # Calculate base components
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
    hr_scores[role] = hr_score

print(f"--- Systematic Opportunity (HR) Scores for Alice's Target Roles ---")
for role, score in hr_scores.items():
    print(f"{role}: {score:.2f}")

alice_hr_df = pd.DataFrame(list(hr_scores.items()), columns=['Role', 'HR_Score'])
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Global Model Parameters (Adjustable by Alice for scenario analysis) ---

# AI-Readiness Score (AI-R) weights
ALPHA = 0.6  # Weight on Idiosyncratic Readiness (VR)
BETA = 0.15  # Synergy coefficient

# Idiosyncratic Readiness (VR) component weights
VR_W1_AI_FLUENCY = 0.45
VR_W2_DOMAIN_EXPERTISE = 0.35
VR_W3_ADAPTIVE_CAPACITY = 0.20
VR_COMPONENT_WEIGHTS = {
    'ai_fluency': VR_W1_AI_FLUENCY,
    'domain_expertise': VR_W2_DOMAIN_EXPERTISE,
    'adaptive_capacity': VR_W3_ADAPTIVE_CAPACITY
}

# AI-Fluency sub-factor weights (theta_k)
THETA1_TECHNICAL_AI_SKILLS = 0.30
THETA2_AI_AUGMENTED_PRODUCTIVITY = 0.35
THETA3_CRITICAL_AI_JUDGMENT = 0.20
THETA4_AI_LEARNING_VELOCITY = 0.15
AI_FLUENCY_THETA_WEIGHTS = {
    'technical_ai_skills': THETA1_TECHNICAL_AI_SKILLS,
    'ai_augmented_productivity': THETA2_AI_AUGMENTED_PRODUCTIVITY,
    'critical_ai_judgment': THETA3_CRITICAL_AI_JUDGMENT,
    'ai_learning_velocity': THETA4_AI_LEARNING_VELOCITY
}

# Domain-Expertise parameters
GAMMA_EXPERIENCE_DECAY = 0.15 # For E_experience = 1 - e^(-gamma_experience * Years)

# Systematic Opportunity (HR) base score weights (w_j)
HR_W1_AI_ENHANCEMENT = 0.30
HR_W2_JOB_GROWTH = 0.30
HR_W3_WAGE_PREMIUM = 0.25
HR_W4_ENTRY_ACCESSIBILITY = 0.15
HBASE_WEIGHTS = {
    'ai_enhancement': HR_W1_AI_ENHANCEMENT,
    'job_growth': HR_W2_JOB_GROWTH,
    'wage_premium': HR_W3_WAGE_PREMIUM,
    'entry_accessibility': HR_W4_ENTRY_ACCESSIBILITY
}

# Systematic Opportunity (HR) multiplier parameters
LAMBDA_GROWTH_MULTIPLIER = 0.3 # Dampens volatility for growth multiplier
GAMMA_REMOTE_WORK = 0.2 # Weight for remote work factor in regional multiplier

# Synergy Function parameters
MAX_POSSIBLE_SKILL_MATCH = 100 # Maximum sum of required skill levels (assuming 0-10 scale for 10 skills)

# Learning Pathway Optimization parameters
LAMBDA_COST_WEIGHT = 0.1 # Weight for cost in the optimization objective (higher means more cost-averse)
MAX_LEARNING_TIME_HOURS = 200 # Max hours Alice can invest
MAX_LEARNING_BUDGET_USD = 1500 # Max budget Alice has for learning

# Set plot style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Libraries imported and global parameters defined.")

# Create simulated data files for the notebook
def create_simulated_data():
    # idiosyncratic_data.csv
    id_data = {
        'persona_id': ['Alice'],
        'prompting': [0.6], 'ai_tools': [0.5], 'understanding': [0.6], 'data_literacy': [0.7],
        'ai_augmented_productivity_ratio': [0.7], 'critical_ai_judgment_accuracy': [0.65],
        'appropriate_trust_decisions_ratio': [0.75],
        'proficiency_gain': [0.10], 'hours_invested': [50],
        'education_level': ['Master\'s in Finance'], 'experience_years': [7],
        'portfolio_score': [0.7], 'recognition_score': [0.6], 'credentials_score': [0.8],
        'cognitive_flexibility': [0.75], 'social_emotional_intelligence': [0.8],
        'strategic_career_management': [0.7]
    }
    pd.DataFrame(id_data).to_csv('idiosyncratic_data.csv', index=False)

    # systematic_opportunity_data.csv
    so_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'ai_enhancement_potential': [0.85, 0.90, 0.80, 0.75],
        'current_jobs': [5000, 4500, 6000, 7000],
        'projected_jobs_10yr': [7500, 7000, 8500, 9000],
        'ai_skilled_wage': [180000, 195000, 160000, 150000],
        'median_wage': [120000, 130000, 110000, 105000],
        'education_years_required': [18, 18, 16, 16],
        'experience_years_required': [5, 6, 4, 3],
        'remote_work_factor': [0.6, 0.5, 0.7, 0.75]
    }
    pd.DataFrame(so_data).to_csv('systematic_opportunity_data.csv', index=False)

    # job_postings_data.csv
    jp_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'] * 2,
        'month': [1,2]*4,
        'job_postings_t': [500, 520, 450, 480, 600, 630, 700, 720],
        'job_postings_t_minus_1': [490, 500, 440, 450, 590, 600, 680, 700]
    }
    pd.DataFrame(jp_data).to_csv('job_postings_data.csv', index=False)

    # regional_demand_data.csv
    rd_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'local_demand': [1.1, 0.9, 1.2, 1.0],
        'national_avg_demand': [1.0, 1.0, 1.0, 1.0]
    }
    pd.DataFrame(rd_data).to_csv('regional_demand_data.csv', index=False)

    # skill_requirements.csv
    sr_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'Python': [9, 10, 8, 9], 'SQL': [7, 8, 9, 8], 'ML_basics': [8, 9, 7, 8],
        'Risk_Analysis': [9, 6, 10, 7], 'Financial_Modeling': [9, 7, 8, 8],
        'Data_Viz': [7, 8, 7, 8], 'Quant_Models': [10, 8, 7, 6], 'AI_Ethics': [7, 8, 9, 7],
        'GenAI_Tools': [6, 7, 6, 7], 'Cloud_Platforms': [7, 9, 7, 8]
    }
    pd.DataFrame(sr_data).to_csv('skill_requirements.csv', index=False)

    # learning_pathways.csv
    lp_data = {
        'pathway_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008'],
        'pathway_name': ['Prompt Engineering for Finance', 'Advanced ML for Trading',
                         'AI Ethics in Risk Management', 'Generative AI for Financial Data',
                         'Deep Learning Fundamentals', 'Human-AI Collaboration Skills',
                         'Financial Domain-Specific AI', 'Strategic Career Planning with AI'],
        'type': ['AI-Fluency', 'Domain+AI', 'Adaptive Capacity', 'AI-Fluency',
                 'Domain+AI', 'Adaptive Capacity', 'Domain+AI', 'Adaptive Capacity'],
        'impact_ai_fluency': [10, 5, 2, 12, 8, 3, 6, 2],
        'impact_domain_expertise': [3, 15, 1, 4, 10, 1, 18, 1],
        'impact_adaptive_capacity': [1, 2, 8, 1, 2, 7, 2, 9],
        'estimated_time_hours': [40, 80, 30, 50, 70, 25, 90, 35],
        'estimated_cost_usd': [300, 800, 200, 450, 700, 180, 950, 250],
        'prerequisites': ['[]', '[P001]', '[]', '[]', '[P001]', '[]', '[P001]', '[]']
    }
    pd.DataFrame(lp_data).to_csv('learning_pathways.csv', index=False)

# Ensure simulated data exists
create_simulated_data()

# Alice's current professional profile
alice_profile = {
    'persona_id': 'Alice',
    'education_level': 'Master\'s in Finance',
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

# Target AI-enabled financial roles Alice is considering
target_roles = ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist']

# Load pre-simulated dataframes
idiosyncratic_df = pd.read_csv('idiosyncratic_data.csv')
systematic_df = pd.read_csv('systematic_opportunity_data.csv')
job_postings_df = pd.read_csv('job_postings_data.csv')
regional_demand_df = pd.read_csv('regional_demand_data.csv')
skill_requirements_df = pd.read_csv('skill_requirements.csv')
learning_pathways_df = pd.read_csv('learning_pathways.csv')

print(f"Alice's Profile:")
for key, value in alice_profile.items():
    if key != 'current_skills' and key != 'ai_fluency_subfactors' and key != 'domain_expertise_subfactors' and key != 'adaptive_capacity_subfactors':
        print(f"- {key.replace('_', ' ').title()}: {value}")
print(f"- Current Skills: {', '.join([f'{s}: {l}' for s,l in alice_profile['current_skills'].items()])}")
print(f"\nTarget AI-enabled Roles: {', '.join(target_roles)}")


def calculate_ai_fluency(subfactors, theta_weights):
    """Calculates AI-Fluency score based on sub-factors."""
    s1 = np.mean([subfactors['prompting'], subfactors['ai_tools'], subfactors['understanding'], subfactors['data_literacy']])
    s2 = subfactors['ai_augmented_productivity'] 
    s3 = subfactors['critical_ai_judgment']
    s4 = subfactors['proficiency_gain'] / subfactors['hours_invested'] if subfactors['hours_invested'] > 0 else 0
    s4 = np.clip(s4 * 100, 0, 1)

    ai_fluency_score = (
        theta_weights['technical_ai_skills'] * s1 +
        theta_weights['ai_augmented_productivity'] * s2 +
        theta_weights['critical_ai_judgment'] * s3 +
        theta_weights['ai_learning_velocity'] * s4
    )
    return np.clip(ai_fluency_score, 0, 1)

def calculate_domain_expertise(education_level, experience_years, specialization_depth_scores, gamma_exp):
    """Calculates Domain-Expertise score."""
    edu_map = {
        'PhD in target field': 1.0,
        'Master\'s in Finance': 0.85,
        'Master\'s in target field': 0.85,
        'Bachelor\'s in target field': 0.70,
        'Associate\'s/Certificate': 0.60,
        'HS + significant coursework': 0.50
    }
    e_education = edu_map.get(education_level, 0.50)

    e_experience = 1 - np.exp(-gamma_exp * experience_years)

    e_specialization = (
        0.4 * specialization_depth_scores['portfolio'] +
        0.3 * specialization_depth_scores['recognition'] +
        0.3 * specialization_depth_scores['credentials']
    )
    
    domain_expertise_score = e_education * e_experience * e_specialization
    return np.clip(domain_expertise_score, 0, 1)

def calculate_adaptive_capacity(subfactors):
    """Calculates Adaptive-Capacity score."""
    c_cognitive = subfactors['cognitive_flexibility']
    c_social = subfactors['social_emotional_intelligence']
    c_strategic = subfactors['strategic_career_management']
    
    adaptive_capacity_score = (c_cognitive + c_social + c_strategic) / 3
    return np.clip(adaptive_capacity_score, 0, 1)

def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, vr_weights):
    """Calculates total Idiosyncratic Readiness (VR) score."""
    vr_score = (
        vr_weights['ai_fluency'] * ai_fluency +
        vr_weights['domain_expertise'] * domain_expertise +
        vr_weights['adaptive_capacity'] * adaptive_capacity
    )
    return np.clip(vr_score * 100, 0, 100)

# Execute VR calculation for Alice
alice_id_data = idiosyncratic_df[idiosyncratic_df['persona_id'] == alice_profile['persona_id']].iloc[0]

alice_ai_fluency_subfactors = {
    'prompting': alice_id_data['prompting'],
    'ai_tools': alice_id_data['ai_tools'],
    'understanding': alice_id_data['understanding'],
    'data_literacy': alice_id_data['data_literacy'],
    'ai_augmented_productivity': alice_id_data['ai_augmented_productivity_ratio'],
    'critical_ai_judgment': alice_id_data['critical_ai_judgment_accuracy'],
    'appropriate_trust_decisions': alice_id_data['appropriate_trust_decisions_ratio'],
    'proficiency_gain': alice_id_data['proficiency_gain'],
    'hours_invested': alice_id_data['hours_invested']
}

alice_domain_expertise_subfactors = {
    'portfolio': alice_id_data['portfolio_score'],
    'recognition': alice_id_data['recognition_score'],
    'credentials': alice_id_data['credentials_score']
}

alice_adaptive_capacity_subfactors = {
    'cognitive_flexibility': alice_id_data['cognitive_flexibility'],
    'social_emotional_intelligence': alice_id_data['social_emotional_intelligence'],
    'strategic_career_management': alice_id_data['strategic_career_management']
}

alice_ai_fluency_score = calculate_ai_fluency(alice_ai_fluency_subfactors, AI_FLUENCY_THETA_WEIGHTS)
alice_domain_expertise_score = calculate_domain_expertise(
    alice_id_data['education_level'], 
    alice_id_data['experience_years'], 
    alice_domain_expertise_subfactors, 
    GAMMA_EXPERIENCE_DECAY
)
alice_adaptive_capacity_score = calculate_adaptive_capacity(alice_adaptive_capacity_subfactors)

alice_vr_score = calculate_vr(
    alice_ai_fluency_score, alice_domain_expertise_score, alice_adaptive_capacity_score, VR_COMPONENT_WEIGHTS
)

print(f"--- Alice's Idiosyncratic Readiness (VR) Breakdown ---")
print(f"AI-Fluency Score (normalized): {alice_ai_fluency_score:.2f}")
print(f"Domain-Expertise Score (normalized): {alice_domain_expertise_score:.2f}")
print(f"Adaptive-Capacity Score (normalized): {alice_adaptive_capacity_score:.2f}")
print(f"\nAlice's Total Idiosyncratic Readiness (VR) Score: {alice_vr_score:.2f}")


def normalize_growth(growth_rate):
    """Normalizes job growth rate to a [0, 100] scale."""
    return np.clip(((growth_rate + 0.5) / 2.0) * 100, 0, 100)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    """Calculates wage premium as a ratio."""
    if median_wage == 0:
        return 0
    return np.clip((ai_skilled_wage - median_wage) / median_wage, 0, 1)

def calculate_entry_accessibility(education_years_required, experience_years_required):
    """Calculates entry accessibility."""
    total_requirements = education_years_required + experience_years_required
    return np.clip(1 - (total_requirements / 28), 0, 1)

def calculate_hbase(ai_enhancement, growth_normalized, wage_premium, entry_accessibility, hbase_weights):
    """Calculates the base opportunity score for a role."""
    hbase_score = (
        hbase_weights['ai_enhancement'] * ai_enhancement +
        hbase_weights['job_growth'] * (growth_normalized / 100) +
        hbase_weights['wage_premium'] * wage_premium +
        hbase_weights['entry_accessibility'] * entry_accessibility
    )
    return np.clip(hbase_score, 0, 1)

def calculate_mgrowth(job_postings_t, job_postings_t_minus_1, lambda_param):
    """Calculates the growth multiplier based on job posting momentum."""
    if job_postings_t_minus_1 == 0:
        return 1.0
    momentum = (job_postings_t / job_postings_t_minus_1) - 1
    return 1 + lambda_param * momentum

def calculate_mregional(local_demand, national_avg_demand, remote_work_factor, gamma_param):
    """Calculates the regional multiplier."""
    if national_avg_demand == 0:
        return 1.0
    demand_ratio = local_demand / national_avg_demand
    return demand_ratio * (1 + gamma_param * remote_work_factor)

def calculate_hr(hbase_score, mgrowth_score, mregional_score):
    """Calculates total Systematic Opportunity (HR) score."""
    hr_score = hbase_score * mgrowth_score * mregional_score
    return np.clip(hr_score * 100, 0, 100)

# Execute HR calculation for each target role for Alice
hr_scores = {}
for role in target_roles:
    role_data = systematic_df[systematic_df['role'] == role].iloc[0]
    jp_role_data = job_postings_df[job_postings_df['role'] == role].iloc[-1]
    rd_role_data = regional_demand_df[regional_demand_df['role'] == role].iloc[0]

    # Calculate base components
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
    hr_scores[role] = hr_score

print(f"--- Systematic Opportunity (HR) Scores for Alice's Target Roles ---")
for role, score in hr_scores.items():
    print(f"{role}: {score:.2f}")

alice_hr_df = pd.DataFrame(list(hr_scores.items()), columns=['Role', 'HR_Score'])


def calculate_skills_match_score(current_skills_dict, required_skills_series, max_possible_match_val):
    """Calculates the skills match score based on current vs. required skills."""
    match_score = 0
    skills_in_common = 0
    current_skills_level = 0
    required_skills_level = 0
    
    req_skills = required_skills_series.drop('role', errors='ignore').to_dict()

    for skill, req_level in req_skills.items():
        if skill in current_skills_dict:
            match_score += min(current_skills_dict[skill], req_level)
            skills_in_common += 1
            current_skills_level += current_skills_dict[skill]
        required_skills_level += req_level
            
    if max_possible_match_val == 0:
        return 0, {}, {}, 0, 0
    
    normalized_match_score = match_score / max_possible_match_val
    
    skill_gaps = {}
    for skill, req_level in req_skills.items():
        current_level = current_skills_dict.get(skill, 0)
        skill_gaps[skill] = {'current': current_level, 'required': req_level}

    return np.clip(normalized_match_score, 0, 1), skill_gaps, req_skills, current_skills_level, required_skills_level


def calculate_timing_factor(years_experience):
    """Calculates the timing factor based on years of experience."""
    if years_experience <= 5:
        return 1.0
    elif 5 < years_experience <= 15:
        return 1.0
    else:
        return 0.8

def calculate_alignment(skills_match_score, timing_factor):
    """Calculates the alignment factor."""
    return np.clip(skills_match_score * timing_factor, 0, 1)

def calculate_synergy(vr_score, hr_score, alignment_score):
    """Calculates the synergy percentage."""
    synergy_base = (vr_score * hr_score) / 100
    return np.clip(synergy_base * alignment_score, 0, 100)

def calculate_air(vr_score, hr_score, synergy_score, alpha, beta):
    """Calculates the total AI-Readiness Score."""
    air_score = alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_score
    return np.clip(air_score, 0, 100)

# Store results
air_results = []
all_skill_gaps = {}

for role in target_roles:
    current_hr_score = hr_scores[role]

    required_skills_for_role = skill_requirements_df[skill_requirements_df['role'] == role].iloc[0]
    
    max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum() # Added errors='ignore' for robustness
    
    skills_match, skill_gaps, required_skills_dict, current_skills_total, required_skills_total = calculate_skills_match_score(
        alice_profile['current_skills'], 
        required_skills_for_role,
        max_possible_match_for_role
    )
    all_skill_gaps[role] = skill_gaps

    timing_factor = calculate_timing_factor(alice_profile['experience_years'])

    alignment_score = calculate_alignment(skills_match, timing_factor)

    synergy_score = calculate_synergy(alice_vr_score, current_hr_score, alignment_score)

    air_score = calculate_air(alice_vr_score, current_hr_score, synergy_score, ALPHA, BETA)
    
    air_results.append({
        'Role': role,
        'VR_Score': alice_vr_score,
        'HR_Score': current_hr_score,
        'Skills_Match_Score': skills_match * 100,
        'Timing_Factor': timing_factor,
        'Alignment_Score': alignment_score * 100,
        'Synergy_Score': synergy_score,
        'AI_R_Score': air_score
    })

air_df = pd.DataFrame(air_results)
print("\n--- Alice's AI-Readiness Scores (AI-R) for Target Roles ---")
print(air_df.round(2))

top_role = air_df.loc[air_df['AI_R_Score'].idxmax()]
print(f"\nAlice's Top AI-R Role: {top_role['Role']} (AI-R: {top_role['AI_R_Score']:.2f})")

air_df_plot = air_df[['Role', 'AI_R_Score', 'VR_Score', 'HR_Score']].set_index('Role')
air_df_plot.plot(kind='bar', figsize=(12, 7), title='Alice\'s AI-Readiness Scores Across Target Roles')
plt.ylabel('Score (0-100)')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Component')
plt.tight_layout()
plt.show()

top_role_skills = all_skill_gaps[top_role['Role']]
skills_df = pd.DataFrame(top_role_skills).T.reset_index().rename(columns={'index': 'Skill'}) # Corrected: Removed extra curly braces
labels = skills_df['Skill'].tolist()
current_levels = skills_df['current'].tolist()
required_levels = skills_df['required'].tolist()

labels += labels[:1]
current_levels += current_levels[:1]
required_levels += required_levels[:1]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
# angles_degrees = np.degrees(angles) # This line is not used, can be removed or kept as is.

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, current_levels, color='blue', alpha=0.25, label='Current Skill Level')
ax.plot(angles, current_levels, color='blue', linewidth=2)
ax.fill(angles, required_levels, color='red', alpha=0.25, label='Required Skill Level')
ax.plot(angles, required_levels, color='red', linewidth=2)

ax.set_yticklabels([f'{i}' for i in range(0, 11, 2)])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels[:-1])
ax.set_title(f'Skill Gaps for {top_role["Role"]}', size=16, y=1.08)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import ast # Import the ast module for safe evaluation of literal structures

# --- Global Model Parameters (Adjustable by Alice for scenario analysis) ---

# AI-Readiness Score (AI-R) weights
ALPHA = 0.6  # Weight on Idiosyncratic Readiness (VR)
BETA = 0.15  # Synergy coefficient

# Idiosyncratic Readiness (VR) component weights
VR_W1_AI_FLUENCY = 0.45
VR_W2_DOMAIN_EXPERTISE = 0.35
VR_W3_ADAPTIVE_CAPACITY = 0.20
VR_COMPONENT_WEIGHTS = {
    'ai_fluency': VR_W1_AI_FLUENCY,
    'domain_expertise': VR_W2_DOMAIN_EXPERTISE,
    'adaptive_capacity': VR_W3_ADAPTIVE_CAPACITY
}

# AI-Fluency sub-factor weights (theta_k)
THETA1_TECHNICAL_AI_SKILLS = 0.30
THETA2_AI_AUGMENTED_PRODUCTIVITY = 0.35
THETA3_CRITICAL_AI_JUDGMENT = 0.20
THETA4_AI_LEARNING_VELOCITY = 0.15
AI_FLUENCY_THETA_WEIGHTS = {
    'technical_ai_skills': THETA1_TECHNICAL_AI_SKILLS,
    'ai_augmented_productivity': THETA2_AI_AUGMENTED_PRODUCTIVITY,
    'critical_ai_judgment': THETA3_CRITICAL_AI_JUDGMENT,
    'ai_learning_velocity': THETA4_AI_LEARNING_VELOCITY
}

# Domain-Expertise parameters
GAMMA_EXPERIENCE_DECAY = 0.15 # For E_experience = 1 - e^(-gamma_experience * Years)

# Systematic Opportunity (HR) base score weights (w_j)
HR_W1_AI_ENHANCEMENT = 0.30
HR_W2_JOB_GROWTH = 0.30
HR_W3_WAGE_PREMIUM = 0.25
HR_W4_ENTRY_ACCESSIBILITY = 0.15
HBASE_WEIGHTS = {
    'ai_enhancement': HR_W1_AI_ENHANCEMENT,
    'job_growth': HR_W2_JOB_GROWTH,
    'wage_premium': HR_W3_WAGE_PREMIUM,
    'entry_accessibility': HR_W4_ENTRY_ACCESSIBILITY
}

# Systematic Opportunity (HR) multiplier parameters
LAMBDA_GROWTH_MULTIPLIER = 0.3 # Dampens volatility for growth multiplier
GAMMA_REMOTE_WORK = 0.2 # Weight for remote work factor in regional multiplier

# Synergy Function parameters
MAX_POSSIBLE_SKILL_MATCH = 100 # Maximum sum of required skill levels (assuming 0-10 scale for 10 skills)

# Learning Pathway Optimization parameters
LAMBDA_COST_WEIGHT = 0.1 # Weight for cost in the optimization objective (higher means more cost-averse)
MAX_LEARNING_TIME_HOURS = 200 # Max hours Alice can invest
MAX_LEARNING_BUDGET_USD = 1500 # Max budget Alice has for learning

# Set plot style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Libraries imported and global parameters defined.")

# Create simulated data files for the notebook
def create_simulated_data():
    # idiosyncratic_data.csv
    id_data = {
        'persona_id': ['Alice'],
        'prompting': [0.6], 'ai_tools': [0.5], 'understanding': [0.6], 'data_literacy': [0.7],
        'ai_augmented_productivity_ratio': [0.7], 'critical_ai_judgment_accuracy': [0.65],
        'appropriate_trust_decisions_ratio': [0.75],
        'proficiency_gain': [0.10], 'hours_invested': [50],
        'education_level': ['Master\'s in Finance'], 'experience_years': [7],
        'portfolio_score': [0.7], 'recognition_score': [0.6], 'credentials_score': [0.8],
        'cognitive_flexibility': [0.75], 'social_emotional_intelligence': [0.8],
        'strategic_career_management': [0.7]
    }
    pd.DataFrame(id_data).to_csv('idiosyncratic_data.csv', index=False)

    # systematic_opportunity_data.csv
    so_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'ai_enhancement_potential': [0.85, 0.90, 0.80, 0.75],
        'current_jobs': [5000, 4500, 6000, 7000],
        'projected_jobs_10yr': [7500, 7000, 8500, 9000],
        'ai_skilled_wage': [180000, 195000, 160000, 150000],
        'median_wage': [120000, 130000, 110000, 105000],
        'education_years_required': [18, 18, 16, 16],
        'experience_years_required': [5, 6, 4, 3],
        'remote_work_factor': [0.6, 0.5, 0.7, 0.75]
    }
    pd.DataFrame(so_data).to_csv('systematic_opportunity_data.csv', index=False)

    # job_postings_data.csv
    jp_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'] * 2,
        'month': [1,2]*4,
        'job_postings_t': [500, 520, 450, 480, 600, 630, 700, 720],
        'job_postings_t_minus_1': [490, 500, 440, 450, 590, 600, 680, 700]
    }
    pd.DataFrame(jp_data).to_csv('job_postings_data.csv', index=False)

    # regional_demand_data.csv
    rd_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'local_demand': [1.1, 0.9, 1.2, 1.0],
        'national_avg_demand': [1.0, 1.0, 1.0, 1.0]
    }
    pd.DataFrame(rd_data).to_csv('regional_demand_data.csv', index=False)

    # skill_requirements.csv
    sr_data = {
        'role': ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist'],
        'Python': [9, 10, 8, 9], 'SQL': [7, 8, 9, 8], 'ML_basics': [8, 9, 7, 8],
        'Risk_Analysis': [9, 6, 10, 7], 'Financial_Modeling': [9, 7, 8, 8],
        'Data_Viz': [7, 8, 7, 8], 'Quant_Models': [10, 8, 7, 6], 'AI_Ethics': [7, 8, 9, 7],
        'GenAI_Tools': [6, 7, 6, 7], 'Cloud_Platforms': [7, 9, 7, 8]
    }
    pd.DataFrame(sr_data).to_csv('skill_requirements.csv', index=False)

    # learning_pathways.csv
    lp_data = {
        'pathway_id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008'],
        'pathway_name': ['Prompt Engineering for Finance', 'Advanced ML for Trading',
                         'AI Ethics in Risk Management', 'Generative AI for Financial Data',
                         'Deep Learning Fundamentals', 'Human-AI Collaboration Skills',
                         'Financial Domain-Specific AI', 'Strategic Career Planning with AI'],
        'type': ['AI-Fluency', 'Domain+AI', 'Adaptive Capacity', 'AI-Fluency',
                 'Domain+AI', 'Adaptive Capacity', 'Domain+AI', 'Adaptive Capacity'],
        'impact_ai_fluency': [10, 5, 2, 12, 8, 3, 6, 2],
        'impact_domain_expertise': [3, 15, 1, 4, 10, 1, 18, 1],
        'impact_adaptive_capacity': [1, 2, 8, 1, 2, 7, 2, 9],
        'estimated_time_hours': [40, 80, 30, 50, 70, 25, 90, 35],
        'estimated_cost_usd': [300, 800, 200, 450, 700, 180, 950, 250],
        # The prerequisites list elements must be quoted for ast.literal_eval to work directly.
        # e.g., '["P001"]' instead of '[P001]'.
        # Since we cannot change previous cells, we'll implement a workaround in optimize_learning_pathways.
        'prerequisites': ['[]', '[P001]', '[]', '[]', '[P001]', '[]', '[P001]', '[]']
    }
    pd.DataFrame(lp_data).to_csv('learning_pathways.csv', index=False)

# Ensure simulated data exists
create_simulated_data()

# Alice's current professional profile
alice_profile = {
    'persona_id': 'Alice',
    'education_level': 'Master\'s in Finance',
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

# Target AI-enabled financial roles Alice is considering
target_roles = ['AI Quant Analyst', 'ML Engineer in Trading', 'AI Risk Analyst', 'Financial Data Scientist']

# Load pre-simulated dataframes
idiosyncratic_df = pd.read_csv('idiosyncratic_data.csv')
systematic_df = pd.read_csv('systematic_opportunity_data.csv')
job_postings_df = pd.read_csv('job_postings_data.csv')
regional_demand_df = pd.read_csv('regional_demand_data.csv')
skill_requirements_df = pd.read_csv('skill_requirements.csv')
learning_pathways_df = pd.read_csv('learning_pathways.csv')

print(f"Alice's Profile:")
for key, value in alice_profile.items():
    if key != 'current_skills' and key != 'ai_fluency_subfactors' and key != 'domain_expertise_subfactors' and key != 'adaptive_capacity_subfactors':
        print(f"- {key.replace('_', ' ').title()}: {value}")
print(f"- Current Skills: {', '.join([f'{s}: {l}' for s,l in alice_profile['current_skills'].items()])}")
print(f"\nTarget AI-enabled Roles: {', '.join(target_roles)}")


def calculate_ai_fluency(subfactors, theta_weights):
    """Calculates AI-Fluency score based on sub-factors."""
    s1 = np.mean([subfactors['prompting'], subfactors['ai_tools'], subfactors['understanding'], subfactors['data_literacy']])
    s2 = subfactors['ai_augmented_productivity'] 
    s3 = subfactors['critical_ai_judgment']
    s4 = subfactors['proficiency_gain'] / subfactors['hours_invested'] if subfactors['hours_invested'] > 0 else 0
    s4 = np.clip(s4 * 100, 0, 1)

    ai_fluency_score = (
        theta_weights['technical_ai_skills'] * s1 +
        theta_weights['ai_augmented_productivity'] * s2 +
        theta_weights['critical_ai_judgment'] * s3 +
        theta_weights['ai_learning_velocity'] * s4
    )
    return np.clip(ai_fluency_score, 0, 1)

def calculate_domain_expertise(education_level, experience_years, specialization_depth_scores, gamma_exp):
    """Calculates Domain-Expertise score."""
    edu_map = {
        'PhD in target field': 1.0,
        'Master\'s in Finance': 0.85,
        'Master\'s in target field': 0.85,
        'Bachelor\'s in target field': 0.70,
        'Associate\'s/Certificate': 0.60,
        'HS + significant coursework': 0.50
    }
    e_education = edu_map.get(education_level, 0.50)

    e_experience = 1 - np.exp(-gamma_exp * experience_years)

    e_specialization = (
        0.4 * specialization_depth_scores['portfolio'] +
        0.3 * specialization_depth_scores['recognition'] +
        0.3 * specialization_depth_scores['credentials']
    )
    
    domain_expertise_score = e_education * e_experience * e_specialization
    return np.clip(domain_expertise_score, 0, 1)

def calculate_adaptive_capacity(subfactors):
    """Calculates Adaptive-Capacity score."""
    c_cognitive = subfactors['cognitive_flexibility']
    c_social = subfactors['social_emotional_intelligence']
    c_strategic = subfactors['strategic_career_management']
    
    adaptive_capacity_score = (c_cognitive + c_social + c_strategic) / 3
    return np.clip(adaptive_capacity_score, 0, 1)

def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, vr_weights):
    """Calculates total Idiosyncratic Readiness (VR) score."""
    vr_score = (
        vr_weights['ai_fluency'] * ai_fluency +
        vr_weights['domain_expertise'] * domain_expertise +
        vr_weights['adaptive_capacity'] * adaptive_capacity
    )
    return np.clip(vr_score * 100, 0, 100)

# Execute VR calculation for Alice
alice_id_data = idiosyncratic_df[idiosyncratic_df['persona_id'] == alice_profile['persona_id']].iloc[0]

alice_ai_fluency_subfactors = {
    'prompting': alice_id_data['prompting'],
    'ai_tools': alice_id_data['ai_tools'],
    'understanding': alice_id_data['understanding'],
    'data_literacy': alice_id_data['data_literacy'],
    'ai_augmented_productivity': alice_id_data['ai_augmented_productivity_ratio'],
    'critical_ai_judgment': alice_id_data['critical_ai_judgment_accuracy'],
    'appropriate_trust_decisions': alice_id_data['appropriate_trust_decisions_ratio'],
    'proficiency_gain': alice_id_data['proficiency_gain'],
    'hours_invested': alice_id_data['hours_invested']
}

alice_domain_expertise_subfactors = {
    'portfolio': alice_id_data['portfolio_score'],
    'recognition': alice_id_data['recognition_score'],
    'credentials': alice_id_data['credentials_score']
}

alice_adaptive_capacity_subfactors = {
    'cognitive_flexibility': alice_id_data['cognitive_flexibility'],
    'social_emotional_intelligence': alice_id_data['social_emotional_intelligence'],
    'strategic_career_management': alice_id_data['strategic_career_management']
}

alice_ai_fluency_score = calculate_ai_fluency(alice_ai_fluency_subfactors, AI_FLUENCY_THETA_WEIGHTS)
alice_domain_expertise_score = calculate_domain_expertise(
    alice_id_data['education_level'], 
    alice_id_data['experience_years'], 
    alice_domain_expertise_subfactors, 
    GAMMA_EXPERIENCE_DECAY
)
alice_adaptive_capacity_score = calculate_adaptive_capacity(alice_adaptive_capacity_subfactors)

alice_vr_score = calculate_vr(
    alice_ai_fluency_score, alice_domain_expertise_score, alice_adaptive_capacity_score, VR_COMPONENT_WEIGHTS
)

print(f"--- Alice's Idiosyncratic Readiness (VR) Breakdown ---")
print(f"AI-Fluency Score (normalized): {alice_ai_fluency_score:.2f}")
print(f"Domain-Expertise Score (normalized): {alice_domain_expertise_score:.2f}")
print(f"Adaptive-Capacity Score (normalized): {alice_adaptive_capacity_score:.2f}")
print(f"\nAlice's Total Idiosyncratic Readiness (VR) Score: {alice_vr_score:.2f}")


def normalize_growth(growth_rate):
    """Normalizes job growth rate to a [0, 100] scale."""
    return np.clip(((growth_rate + 0.5) / 2.0) * 100, 0, 100)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    """Calculates wage premium as a ratio."""
    if median_wage == 0:
        return 0
    return np.clip((ai_skilled_wage - median_wage) / median_wage, 0, 1)

def calculate_entry_accessibility(education_years_required, experience_years_required):
    """Calculates entry accessibility."""
    total_requirements = education_years_required + experience_years_required
    return np.clip(1 - (total_requirements / 28), 0, 1)

def calculate_hbase(ai_enhancement, growth_normalized, wage_premium, entry_accessibility, hbase_weights):
    """Calculates the base opportunity score for a role."""
    hbase_score = (
        hbase_weights['ai_enhancement'] * ai_enhancement +
        hbase_weights['job_growth'] * (growth_normalized / 100) +
        hbase_weights['wage_premium'] * wage_premium +
        hbase_weights['entry_accessibility'] * entry_accessibility
    )
    return np.clip(hbase_score, 0, 1)

def calculate_mgrowth(job_postings_t, job_postings_t_minus_1, lambda_param):
    """Calculates the growth multiplier based on job posting momentum."""
    if job_postings_t_minus_1 == 0:
        return 1.0
    momentum = (job_postings_t / job_postings_t_minus_1) - 1
    return 1 + lambda_param * momentum

def calculate_mregional(local_demand, national_avg_demand, remote_work_factor, gamma_param):
    """Calculates the regional multiplier."""
    if national_avg_demand == 0:
        return 1.0
    demand_ratio = local_demand / national_avg_demand
    return demand_ratio * (1 + gamma_param * remote_work_factor)

def calculate_hr(hbase_score, mgrowth_score, mregional_score):
    """Calculates total Systematic Opportunity (HR) score."""
    hr_score = hbase_score * mgrowth_score * mregional_score
    return np.clip(hr_score * 100, 0, 100)

# Execute HR calculation for each target role for Alice
hr_scores = {}
for role in target_roles:
    role_data = systematic_df[systematic_df['role'] == role].iloc[0]
    jp_role_data = job_postings_df[job_postings_df['role'] == role].iloc[-1]
    rd_role_data = regional_demand_df[regional_demand_df['role'] == role].iloc[0]

    # Calculate base components
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
    hr_scores[role] = hr_score

print(f"--- Systematic Opportunity (HR) Scores for Alice's Target Roles ---")
for role, score in hr_scores.items():
    print(f"{role}: {score:.2f}")

alice_hr_df = pd.DataFrame(list(hr_scores.items()), columns=['Role', 'HR_Score'])


def calculate_skills_match_score(current_skills_dict, required_skills_series, max_possible_match_val):
    """Calculates the skills match score based on current vs. required skills."""
    match_score = 0
    skills_in_common = 0
    current_skills_level = 0
    required_skills_level = 0
    
    req_skills = required_skills_series.drop('role', errors='ignore').to_dict()

    for skill, req_level in req_skills.items():
        if skill in current_skills_dict:
            match_score += min(current_skills_dict[skill], req_level)
            skills_in_common += 1
            current_skills_level += current_skills_dict[skill]
        required_skills_level += req_level
            
    if max_possible_match_val == 0:
        return 0, {}, {}, 0, 0
    
    normalized_match_score = match_score / max_possible_match_val
    
    skill_gaps = {}
    for skill, req_level in req_skills.items():
        current_level = current_skills_dict.get(skill, 0)
        skill_gaps[skill] = {'current': current_level, 'required': req_level}

    return np.clip(normalized_match_score, 0, 1), skill_gaps, req_skills, current_skills_level, required_skills_level


def calculate_timing_factor(years_experience):
    """Calculates the timing factor based on years of experience."""
    if years_experience <= 5:
        return 1.0
    elif 5 < years_experience <= 15:
        return 1.0
    else:
        return 0.8

def calculate_alignment(skills_match_score, timing_factor):
    """Calculates the alignment factor."""
    return np.clip(skills_match_score * timing_factor, 0, 1)

def calculate_synergy(vr_score, hr_score, alignment_score):
    """Calculates the synergy percentage."""
    synergy_base = (vr_score * hr_score) / 100
    return np.clip(synergy_base * alignment_score, 0, 100)

def calculate_air(vr_score, hr_score, synergy_score, alpha, beta):
    """Calculates the total AI-Readiness Score."""
    air_score = alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_score
    return np.clip(air_score, 0, 100)

# Store results
air_results = []
all_skill_gaps = {}

for role in target_roles:
    current_hr_score = hr_scores[role]

    required_skills_for_role = skill_requirements_df[skill_requirements_df['role'] == role].iloc[0]
    
    max_possible_match_for_role = required_skills_for_role.drop('role', errors='ignore').sum() 
    
    skills_match, skill_gaps, required_skills_dict, current_skills_total, required_skills_total = calculate_skills_match_score(
        alice_profile['current_skills'], 
        required_skills_for_role,
        max_possible_match_for_role
    )
    all_skill_gaps[role] = skill_gaps

    timing_factor = calculate_timing_factor(alice_profile['experience_years'])

    alignment_score = calculate_alignment(skills_match, timing_factor)

    synergy_score = calculate_synergy(alice_vr_score, current_hr_score, alignment_score)

    air_score = calculate_air(alice_vr_score, current_hr_score, synergy_score, ALPHA, BETA)
    
    air_results.append({
        'Role': role,
        'VR_Score': alice_vr_score,
        'HR_Score': current_hr_score,
        'Skills_Match_Score': skills_match * 100,
        'Timing_Factor': timing_factor,
        'Alignment_Score': alignment_score * 100,
        'Synergy_Score': synergy_score,
        'AI_R_Score': air_score
    })

air_df = pd.DataFrame(air_results)
print("\n--- Alice's AI-Readiness Scores (AI-R) for Target Roles ---")
print(air_df.round(2))

top_role = air_df.loc[air_df['AI_R_Score'].idxmax()]
print(f"\nAlice's Top AI-R Role: {top_role['Role']} (AI-R: {top_role['AI_R_Score']:.2f})")

air_df_plot = air_df[['Role', 'AI_R_Score', 'VR_Score', 'HR_Score']].set_index('Role')
air_df_plot.plot(kind='bar', figsize=(12, 7), title='Alice\'s AI-Readiness Scores Across Target Roles')
plt.ylabel('Score (0-100)')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Component')
plt.tight_layout()
plt.show()

top_role_skills = all_skill_gaps[top_role['Role']]
skills_df = pd.DataFrame(top_role_skills).T.reset_index().rename(columns={'index': 'Skill'}) 
labels = skills_df['Skill'].tolist()
current_levels = skills_df['current'].tolist()
required_levels = skills_df['required'].tolist()

labels += labels[:1]
current_levels += current_levels[:1]
required_levels += required_levels[:1]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
# angles_degrees = np.degrees(angles) 

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, current_levels, color='blue', alpha=0.25, label='Current Skill Level')
ax.plot(angles, current_levels, color='blue', linewidth=2)
ax.fill(angles, required_levels, color='red', alpha=0.25, label='Required Skill Level')
ax.plot(angles, required_levels, color='red', linewidth=2)

ax.set_yticklabels([f'{i}' for i in range(0, 11, 2)])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels[:-1])
ax.set_title(f'Skill Gaps for {top_role["Role"]}', size=16, y=1.08)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()


def simulate_learning_pathway_impact(current_vr_subscores, pathway_impacts):
    """
    Simulates the impact of a learning pathway on VR sub-scores (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
    Impacts are added to the normalized sub-scores, then re-clipped to [0,1].
    """
    new_vr_subscores = current_vr_subscores.copy()
    
    new_vr_subscores['ai_fluency'] = np.clip(new_vr_subscores['ai_fluency'] + (pathway_impacts['impact_ai_fluency'] / 100), 0, 1)
    new_vr_subscores['domain_expertise'] = np.clip(new_vr_subscores['domain_expertise'] + (pathway_impacts['impact_domain_expertise'] / 100), 0, 1)
    new_vr_subscores['adaptive_capacity'] = np.clip(new_vr_subscores['adaptive_capacity'] + (pathway_impacts['impact_adaptive_capacity'] / 100), 0, 1)
    
    return new_vr_subscores

def optimize_learning_pathways(current_air_score, current_vr_score, current_vr_subscores, target_hr_score, 
                               learning_pathways_df, max_time, max_cost, 
                               alpha, beta, lambda_cost_weight, alice_exp_years, alice_current_skills_dict):
    """
    Optimizes a sequence of learning pathways using a greedy heuristic.
    Selects pathways that offer the highest "return" (AI-R point gain per unit of weighted time/cost) until constraints are met,
    respecting prerequisites.
    """
    available_pathways = learning_pathways_df.copy()
    recommended_pathways = []
    total_time = 0
    total_cost = 0
    
    current_vr_subscores_normalized = current_vr_subscores.copy()
    current_vr = current_vr_score
    
    # target_role_name is derived from the globally available air_df and then skill_requirements_df
    # This requires air_df and skill_requirements_df to be accessible globally or passed.
    # Given the notebook context, they are expected to be globally available.
    target_role_name = air_df.loc[air_df['AI_R_Score'].idxmax(), 'Role']
    required_skills_for_target_role = skill_requirements_df[skill_requirements_df['role'] == target_role_name].iloc[0].drop('role').to_dict()
    max_possible_match_for_target_role = sum(required_skills_for_target_role.values())
    
    simulated_current_skills = alice_current_skills_dict.copy()

    initial_skills_match, _, _, _, _ = calculate_skills_match_score(
        simulated_current_skills, 
        pd.Series(required_skills_for_target_role, name='skills'), 
        max_possible_match_for_target_role
    )
    initial_timing_factor = calculate_timing_factor(alice_exp_years)
    initial_alignment = calculate_alignment(initial_skills_match, initial_timing_factor)
    initial_synergy = calculate_synergy(current_vr, target_hr_score, initial_alignment)
    
    current_air = calculate_air(current_vr, target_hr_score, initial_synergy, alpha, beta)


    while True:
        best_pathway = None
        max_return_on_investment = -1
        
        eligible_pathways = available_pathways[~available_pathways['pathway_id'].isin([p['pathway_id'] for p in recommended_pathways])]
        
        eligible_pathways_with_prereqs = []
        completed_pathway_ids = [p['pathway_id'] for p in recommended_pathways]
        for _, pathway in eligible_pathways.iterrows():
            # Corrected: Safely parse the prerequisites string which might contain unquoted identifiers like 'P001'
            prereq_str = pathway['prerequisites']
            if prereq_str == '[]':
                prereqs = []
            else:
                # Assuming format is like '[P001]' where P001 is an unquoted identifier.
                # Transform to "['P001']" so ast.literal_eval can handle it.
                inner_content = prereq_str[1:-1].strip()
                if inner_content:
                    # Enclose each identifier in quotes
                    quoted_items = [f"'{item.strip()}'" for item in inner_content.split(',')]
                    prereqs = ast.literal_eval(f"[{', '.join(quoted_items)}]")
                else:
                    prereqs = []
            
            if all(p_id in completed_pathway_ids for p_id in prereqs):
                eligible_pathways_with_prereqs.append(pathway)
        
        if not eligible_pathways_with_prereqs:
            break

        for pathway_data in eligible_pathways_with_prereqs:
            if total_time + pathway_data['estimated_time_hours'] <= max_time and \
               total_cost + pathway_data['estimated_cost_usd'] <= max_cost:
                
                projected_vr_subscores = simulate_learning_pathway_impact(current_vr_subscores_normalized, pathway_data)
                
                projected_vr = calculate_vr(
                    projected_vr_subscores['ai_fluency'], 
                    projected_vr_subscores['domain_expertise'], 
                    projected_vr_subscores['adaptive_capacity'], 
                    VR_COMPONENT_WEIGHTS
                )

                temp_simulated_skills = simulated_current_skills.copy()
                # Ensure skill keys exist in temp_simulated_skills before attempting to increment
                # The provided alice_profile has all these keys, but defensive coding is good.
                if pathway_data['type'] == 'AI-Fluency':
                    if 'GenAI_Tools' in temp_simulated_skills:
                        temp_simulated_skills['GenAI_Tools'] = min(10, temp_simulated_skills['GenAI_Tools'] + 1)
                elif pathway_data['type'] == 'Domain+AI':
                    if 'ML_basics' in temp_simulated_skills:
                        temp_simulated_skills['ML_basics'] = min(10, temp_simulated_skills['ML_basics'] + 1)
                    if 'Quant_Models' in temp_simulated_skills:
                        temp_simulated_skills['Quant_Models'] = min(10, temp_simulated_skills['Quant_Models'] + 1)
                elif pathway_data['type'] == 'Adaptive Capacity':
                    if 'AI_Ethics' in temp_simulated_skills:
                        temp_simulated_skills['AI_Ethics'] = min(10, temp_simulated_skills['AI_Ethics'] + 1)
                    
                
                projected_skills_match, _, _, _, _ = calculate_skills_match_score(
                    temp_simulated_skills, 
                    pd.Series(required_skills_for_target_role, name='skills'), 
                    max_possible_match_for_target_role
                )
                projected_alignment = calculate_alignment(projected_skills_match, initial_timing_factor)
                projected_synergy = calculate_synergy(projected_vr, target_hr_score, projected_alignment)
                
                projected_air = calculate_air(projected_vr, target_hr_score, projected_synergy, alpha, beta)
                
                air_gain = projected_air - current_air
                
                normalized_cost = pathway_data['estimated_cost_usd'] / MAX_LEARNING_BUDGET_USD
                normalized_time = pathway_data['estimated_time_hours'] / MAX_LEARNING_TIME_HOURS
                
                investment = (normalized_cost * lambda_cost_weight) + normalized_time
                
                if investment > 0:
                    roi = air_gain / investment
                else:
                    roi = air_gain # If investment is 0, ROI is simply the gain
                
                if roi > max_return_on_investment:
                    max_return_on_investment = roi
                    best_pathway = pathway_data
                    
        if best_pathway is None:
            break

        recommended_pathways.append(best_pathway)
        total_time += best_pathway['estimated_time_hours']
        total_cost += best_pathway['estimated_cost_usd']
        
        current_vr_subscores_normalized = simulate_learning_pathway_impact(current_vr_subscores_normalized, best_pathway)
        current_vr = calculate_vr(
            current_vr_subscores_normalized['ai_fluency'], 
            current_vr_subscores_normalized['domain_expertise'], 
            current_vr_subscores_normalized['adaptive_capacity'], 
            VR_COMPONENT_WEIGHTS
        )
        # Update simulated_current_skills with the effect of the chosen pathway
        if best_pathway['type'] == 'AI-Fluency':
            if 'GenAI_Tools' in simulated_current_skills:
                simulated_current_skills['GenAI_Tools'] = min(10, simulated_current_skills['GenAI_Tools'] + 1)
        elif best_pathway['type'] == 'Domain+AI':
            if 'ML_basics' in simulated_current_skills:
                simulated_current_skills['ML_basics'] = min(10, simulated_current_skills['ML_basics'] + 1)
            if 'Quant_Models' in simulated_current_skills:
                simulated_current_skills['Quant_Models'] = min(10, simulated_current_skills['Quant_Models'] + 1)
        elif best_pathway['type'] == 'Adaptive Capacity':
            if 'AI_Ethics' in simulated_current_skills:
                simulated_current_skills['AI_Ethics'] = min(10, simulated_current_skills['AI_Ethics'] + 1)
        
        # Recalculate current_air based on the updated state for the next iteration's air_gain comparison
        current_skills_match, _, _, _, _ = calculate_skills_match_score(
            simulated_current_skills, 
            pd.Series(required_skills_for_target_role, name='skills'), 
            max_possible_match_for_target_role
        )
        current_alignment = calculate_alignment(current_skills_match, initial_timing_factor)
        current_synergy = calculate_synergy(current_vr, target_hr_score, current_alignment)
        current_air = calculate_air(current_vr, target_hr_score, current_synergy, alpha, beta)


    final_skills_match, _, _, _, _ = calculate_skills_match_score(
        simulated_current_skills, 
        pd.Series(required_skills_for_target_role, name='skills'), 
        max_possible_match_for_target_role
    )
    final_alignment = calculate_alignment(final_skills_match, initial_timing_factor)
    final_synergy = calculate_synergy(current_vr, target_hr_score, final_alignment)
    projected_air_final = calculate_air(current_vr, target_hr_score, final_synergy, alpha, beta)
    
    return recommended_pathways, total_time, total_cost, projected_air_final, current_vr, current_vr_subscores_normalized, simulated_current_skills


# --- Execute Optimization for Alice's Top Role ---
current_top_role = top_role['Role']
current_hr_for_top_role = top_role['HR_Score']
current_air_for_top_role = top_role['AI_R_Score']

alice_current_vr_subscores_normalized = {
    'ai_fluency': alice_ai_fluency_score,
    'domain_expertise': alice_domain_expertise_score,
    'adaptive_capacity': alice_adaptive_capacity_score
}

recommended_paths, total_time_invested, total_cost_invested, projected_air, final_vr_after_paths, final_vr_subscores_normalized, final_skills_after_paths = optimize_learning_pathways(
    current_air_for_top_role,
    alice_vr_score,
    alice_current_vr_subscores_normalized,
    current_hr_for_top_role,
    learning_pathways_df,
    MAX_LEARNING_TIME_HOURS,
    MAX_LEARNING_BUDGET_USD,
    ALPHA, BETA, LAMBDA_COST_WEIGHT,
    alice_profile['experience_years'],
    alice_profile['current_skills']
)

print(f"\n--- Recommended Learning Pathway for {current_top_role} ---")
if recommended_paths:
    for i, path in enumerate(recommended_paths):
        print(f"{i+1}. {path['pathway_name']} (Type: {path['type']}, Time: {path['estimated_time_hours']}h, Cost: ${path['estimated_cost_usd']})")
    print(f"\nTotal estimated time investment: {total_time_invested} hours")
    print(f"Total estimated cost investment: ${total_cost_invested}")
    print(f"Initial AI-R for {current_top_role}: {current_air_for_top_role:.2f}")
    print(f"Projected AI-R after pathways: {projected_air:.2f} (Improvement: {projected_air - current_air_for_top_role:.2f})")
else:
    print("No learning pathways recommended within the specified constraints.")

fig, ax = plt.subplots(figsize=(8, 6))
bar_width = 0.35
roles = [current_top_role]
current_airs = [current_air_for_top_role]
projected_airs = [projected_air]

index = np.arange(len(roles))

bar1 = ax.bar(index, current_airs, bar_width, label='Current AI-R', color='skyblue')
bar2 = ax.bar(index + bar_width, projected_airs, bar_width, label='Projected AI-R', color='lightcoral')

ax.set_xlabel('Role')
ax.set_ylabel('AI-Readiness Score')
ax.set_title(f'Current vs. Projected AI-R for {current_top_role} After Optimized Learning')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(roles)
ax.set_ylim(0, 100)
ax.legend()

for bar in bar1 + bar2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')

plt.tight_layout()
plt.show()

alice_profile_after_paths = alice_profile.copy()
alice_profile_after_paths['vr_score'] = final_vr_after_paths
alice_profile_after_paths['ai_fluency_score'] = final_vr_subscores_normalized['ai_fluency']
alice_profile_after_paths['domain_expertise_score'] = final_vr_subscores_normalized['domain_expertise']
alice_profile_after_paths['adaptive_capacity_score'] = final_vr_subscores_normalized['adaptive_capacity']
alice_profile_after_paths['current_skills'] = final_skills_after_paths
def run_what_if_scenario(initial_vr_score, initial_vr_subscores_normalized, initial_skills, 
                         target_role_name, hr_data, skill_req_data, learning_pathways_for_scenario, 
                         alice_exp_years, alpha, beta):
    """
    Runs a 'What-If' scenario by applying proposed pathways and calculating projected AI-R.
    """
    current_vr = initial_vr_score
    current_vr_subscores = initial_vr_subscores_normalized.copy()
    current_skills_dict = initial_skills.copy()

    for pathway in learning_pathways_for_scenario:
        current_vr_subscores = simulate_learning_pathway_impact(current_vr_subscores, pathway)
        # Safely update skills, checking if the key exists before attempting to increment
        if pathway['type'] == 'AI-Fluency':
            if 'GenAI_Tools' in current_skills_dict:
                current_skills_dict['GenAI_Tools'] = min(10, current_skills_dict['GenAI_Tools'] + 1)
        elif pathway['type'] == 'Domain+AI':
            if 'ML_basics' in current_skills_dict:
                current_skills_dict['ML_basics'] = min(10, current_skills_dict['ML_basics'] + 1)
            if 'Quant_Models' in current_skills_dict:
                current_skills_dict['Quant_Models'] = min(10, current_skills_dict['Quant_Models'] + 1)
        elif pathway['type'] == 'Adaptive Capacity':
            if 'AI_Ethics' in current_skills_dict:
                current_skills_dict['AI_Ethics'] = min(10, current_skills_dict['AI_Ethics'] + 1)
            
    projected_vr = calculate_vr(
        current_vr_subscores['ai_fluency'], 
        current_vr_subscores['domain_expertise'], 
        current_vr_subscores['adaptive_capacity'], 
        VR_COMPONENT_WEIGHTS
    )

    target_hr_score = hr_data[target_role_name]
    
    required_skills_for_role_series = skill_req_data[skill_req_data['role'] == target_role_name].iloc[0]
    max_possible_match_for_role = required_skills_for_role_series.drop('role', errors='ignore').sum()
    
    skills_match, _, _, _, _ = calculate_skills_match_score(
        current_skills_dict, 
        required_skills_for_role_series, 
        max_possible_match_for_role
    )
    timing_factor = calculate_timing_factor(alice_exp_years)
    alignment_score = calculate_alignment(skills_match, timing_factor)

    synergy_score = calculate_synergy(projected_vr, target_hr_score, alignment_score)
    projected_air = calculate_air(projected_vr, target_hr_score, synergy_score, alpha, beta)
    
    total_time = sum(p['estimated_time_hours'] for p in learning_pathways_for_scenario)
    total_cost = sum(p['estimated_cost_usd'] for p in learning_pathways_for_scenario)

    return projected_air, total_time, total_cost, projected_vr, target_hr_score, synergy_score


# --- Define Scenario Pathways ---
optimal_pathway_details = pd.DataFrame(recommended_paths)
total_optimal_time = optimal_pathway_details['estimated_time_hours'].sum() if not optimal_pathway_details.empty else 0
total_optimal_cost = optimal_pathway_details['estimated_cost_usd'].sum() if not optimal_pathway_details.empty else 0
projected_air_optimal = projected_air
scenario_results = [
    {
        'Scenario': 'Optimized for AI Quant Analyst',
        'Target Role': current_top_role,
        'Projected AI-R': projected_air_optimal,
        'Projected VR': final_vr_after_paths,
        'HR': current_hr_for_top_role,
        'Time (h)': total_optimal_time,
        'Cost ($)': total_optimal_cost
    }
]

scenario_a_pathways = learning_pathways_df[learning_pathways_df['pathway_id'].isin(['P001', 'P004'])].to_dict('records')
projected_air_a, time_a, cost_a, projected_vr_a, hr_a, synergy_a = run_what_if_scenario(
    alice_vr_score, alice_current_vr_subscores_normalized, alice_profile['current_skills'],
    'Financial Data Scientist', hr_scores, skill_requirements_df, scenario_a_pathways,
    alice_profile['experience_years'], ALPHA, BETA
)
scenario_results.append({ # Corrected typo here
    'Scenario': 'Financial Data Scientist w/ GenAI Focus',
    'Target Role': 'Financial Data Scientist',
    'Projected AI-R': projected_air_a,
    'Projected VR': projected_vr_a,
    'HR': hr_a,
    'Time (h)': time_a,
    'Cost ($)': cost_a
})

scenario_b_pathways = learning_pathways_df[learning_pathways_df['pathway_id'].isin(['P001', 'P003'])].to_dict('records')
projected_air_b, time_b, cost_b, projected_vr_b, hr_b, synergy_b = run_what_if_scenario(
    alice_vr_score, alice_current_vr_subscores_normalized, alice_profile['current_skills'],
    current_top_role, hr_scores, skill_requirements_df, scenario_b_pathways,
    alice_profile['experience_years'], ALPHA, BETA
)
scenario_results.append({
    'Scenario': 'AI Quant Analyst w/ Minimal Path',
    'Target Role': current_top_role,
    'Projected AI-R': projected_air_b,
    'Projected VR': projected_vr_b,
    'HR': hr_b,
    'Time (h)': time_b,
    'Cost ($)': cost_b
})

scenario_results_df = pd.DataFrame(scenario_results).round(2)
print("\n--- Alice's 'What-If' Scenario Analysis Results ---")
print(scenario_results_df)

fig, ax = plt.subplots(figsize=(12, 7))
bar_positions = np.arange(len(scenario_results_df))
bars = ax.bar(bar_positions, scenario_results_df['Projected AI-R'], color=sns.color_palette('viridis', len(scenario_results_df)))

ax.set_ylabel('Projected AI-Readiness Score')
ax.set_title('Comparative Projected AI-R for Different Career/Learning Scenarios')
ax.set_xticks(bar_positions)
ax.set_xticklabels(scenario_results_df['Scenario'], rotation=45, ha='right')
ax.set_ylim(0, 100)

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 2), ha='center', va='bottom')

plt.tight_layout()
plt.show()

initial_air_optimal_role = air_df[air_df['Role'] == current_top_role]['AI_R_Score'].iloc[0]
initial_air_data_scientist_role = air_df[air_df['Role'] == 'Financial Data Scientist']['AI_R_Score'].iloc[0]

roi_data = []
for index, row in scenario_results_df.iterrows():
    if row['Scenario'] == 'Optimized for AI Quant Analyst':
        initial_air = initial_air_optimal_role
    elif row['Scenario'] == 'Financial Data Scientist w/ GenAI Focus':
        initial_air = initial_air_data_scientist_role
    elif row['Scenario'] == 'AI Quant Analyst w/ Minimal Path':
        initial_air = initial_air_optimal_role
    else:
        initial_air = 0

    air_gain = row['Projected AI-R'] - initial_air
    
    normalized_cost = row['Cost ($)'] / MAX_LEARNING_BUDGET_USD if MAX_LEARNING_BUDGET_USD > 0 else 0
    normalized_time = row['Time (h)'] / MAX_LEARNING_TIME_HOURS if MAX_LEARNING_TIME_HOURS > 0 else 0
    
    investment_factor = (normalized_cost * LAMBDA_COST_WEIGHT) + normalized_time
    
    if investment_factor > 0:
        roi = air_gain / investment_factor
    else:
        roi = air_gain
    
    roi_data.append({'Scenario': row['Scenario'], 'AI-R Gain': air_gain, 'Investment Score': investment_factor, 'ROI': roi})

roi_df = pd.DataFrame(roi_data).round(2)
print("\n--- Return on Learning Investment (AI-R Gain per Weighted Investment) ---")
print(roi_df)

fig, ax = plt.subplots(figsize=(12, 7))
sns.barplot(x='Scenario', y='ROI', data=roi_df, palette='magma', ax=ax)
ax.set_ylabel('ROI (AI-R Gain / Weighted Investment)')
ax.set_title('Return on Learning Investment for Different Scenarios')
ax.set_xticklabels(roi_df['Scenario'], rotation=45, ha='right')

for index, row in roi_df.iterrows():
    ax.text(index, row['ROI'] + 0.5, f"{row['ROI']:.2f}", color='black', ha="center")

plt.tight_layout()
plt.show()
print("--- Personalized AI Career Strategy Report for Alice ---")
print("\n**1. Current AI-Readiness Profile**")
print(f"   - **Idiosyncratic Readiness (VR):** {alice_vr_score:.2f}")
print(f"     (AI-Fluency: {alice_ai_fluency_score:.2f}, Domain-Expertise: {alice_domain_expertise_score:.2f}, Adaptive-Capacity: {alice_adaptive_capacity_score:.2f})")
print(f"   - **Systematic Opportunity (HR) by Role:**")
for role, score in hr_scores.items():
    print(f"     - {role}: {score:.2f}")

print(f"\n**2. Top AI-Enabled Career Path Recommendation**")
print(f"   - **Recommended Role:** {current_top_role}")
print(f"   - **Initial AI-Readiness Score (AI-R):** {current_air_for_top_role:.2f}")
print(f"   - **Projected AI-Readiness Score (AI-R) after Optimal Learning:** {projected_air:.2f}")
print(f"   - **Estimated AI-R Improvement:** {projected_air - current_air_for_top_role:.2f} points")

print(f"\n**3. Detailed Skill Gaps for {current_top_role}**")
print("   (Comparing Alice's current skills vs. required for this role)")
top_role_skills_gaps_df = pd.DataFrame(all_skill_gaps[current_top_role]).T
top_role_skills_gaps_df['Gap'] = top_role_skills_gaps_df['required'] - top_role_skills_gaps_df['current']
print(top_role_skills_gaps_df[top_role_skills_gaps_df['Gap'] > 0].sort_values(by='Gap', ascending=False))
print("(Skills with a positive 'Gap' need development)")

print(f"\n**4. Recommended Optimal Learning Pathway**")
if recommended_paths:
    for i, path in enumerate(recommended_paths):
        print(f"   {i+1}. {path['pathway_name']} (Type: {path['type']})")
    print(f"   - **Total Estimated Time Investment:** {total_time_invested} hours")
    print(f"   - **Total Estimated Cost Investment:** ${total_cost_invested}")
else:
    print("   No optimal learning pathways identified within current constraints.")

print(f"\n**5. 'What-If' Scenario Analysis Summary**")
print(scenario_results_df.set_index('Scenario'))
print("\nInsight: The 'Optimized for AI Quant Analyst' pathway (original recommendation) yields the highest projected AI-R, indicating it's the most effective strategy for maximizing Alice's career opportunity.")
print("The 'Return on Learning Investment' chart suggests prioritizing pathways with high impact on core VR components that align with high HR roles.")

print("\n--- End of Report ---")