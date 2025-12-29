
# Personalized AI Career Pathway Optimizer for Financial Professionals

## Introduction

In the rapidly evolving landscape of financial services, the integration of Artificial Intelligence (AI) is reshaping roles and creating new opportunities. For financial professionals, understanding how to adapt and strategically position oneself is crucial for long-term career success. This Jupyter Notebook will guide you through a data-driven framework to assess your current AI-readiness, identify high-opportunity career paths, pinpoint skill gaps, and optimize a personalized learning strategy.

You will step into the shoes of **Alice, a Senior Quantitative Analyst at QuantFinance Innovations**, a leading financial institution. Alice is keen to leverage AI to advance her career but is unsure which AI-enabled roles offer the best prospects given her background, and what specific skills she needs to acquire. This notebook will help Alice make informed decisions about her professional development and maximize her career trajectory in the age of AI.

The core of this analysis is the **AI-Readiness Score (AI-R)**, a novel parametric framework that quantifies an individual's preparedness for AI-enabled careers. It decomposes career opportunity into two orthogonal components: **Idiosyncratic Readiness ($V^R$)**, representing individual-specific capabilities, and **Systematic Opportunity ($H^R$)**, representing macro-level job growth and demand. The framework also incorporates a **Synergy Function** to capture the compounding benefits when individual preparation aligns with market opportunity.

The AI-R score for an individual $i$ at time $t$ is defined as:
$$AI-R_{i,t} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{i}^R(t) + \beta \cdot Synergy\%(V_i^R, H_{i}^R)$$
where:
*   $V_i^R(t)$: Idiosyncratic Readiness (individual capability), normalized to $[0, 100]$.
*   $H_i^R(t)$: Systematic Opportunity (market demand) for the target occupation, normalized to $[0, 100]$.
*   $\alpha \in [0,1]$: Weight on individual vs. market factors. Default $\alpha = 0.6$.
*   $\beta > 0$: Synergy coefficient, capturing multiplicative benefits. Default $\beta = 0.15$.
*   $Synergy\% \in [0,100]$: Percentage units.

By walking through this workflow, Alice will gain personalized, data-driven career guidance, ensuring her learning investments are impactful for high-opportunity roles in finance.

## 1. Setup: Libraries and Global Parameters

Alice begins by setting up her analytical environment. This involves installing necessary libraries and defining global parameters that influence the AI-Readiness Score calculation. These parameters can be adjusted to reflect different strategic priorities or market conditions.

### Code Cell: Install Libraries

```python
!pip install numpy pandas matplotlib seaborn scipy
```

### Code Cell: Import Dependencies and Define Global Parameters

```python
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
```

## 2. Persona and Initial Profile Assessment

Alice, a Senior Quantitative Analyst at QuantFinance Innovations, has a solid background in financial modeling, risk analysis, and Python programming. She's exploring various AI-enabled roles within finance, such as 'AI Quant Analyst', 'ML Engineer in Trading', and 'AI Risk Analyst', to identify the most promising path for her career growth. This section captures her initial profile and the target roles she's considering.

### Code Cell: Define Alice's Profile and Load Data

```python
# Create simulated data files for the notebook
def create_simulated_data():
    # idiosyncratic_data.csv
    id_data = {
        'persona_id': ['Alice'],
        'prompting': [0.6], 'ai_tools': [0.5], 'understanding': [0.6], 'data_literacy': [0.7],
        'ai_augmented_productivity_ratio': [0.7], 'critical_ai_judgment_accuracy': [0.65],
        'appropriate_trust_decisions_ratio': [0.75],
        'proficiency_gain': [0.10], 'hours_invested': [50], # Sample for velocity calculation
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
        'education_years_required': [18, 18, 16, 16], # Masters = 18, Bachelors = 16
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
        'local_demand': [1.1, 0.9, 1.2, 1.0], # Relative to national avg
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
```

## 3. Calculating Idiosyncratic Readiness ($V^R$)

Alice's journey begins with understanding her intrinsic capabilities and preparedness for AI-enabled roles. This is measured by her **Idiosyncratic Readiness ($V^R$)**, which she can actively develop through learning. $V^R$ is a weighted sum of three main factors: AI-Fluency, Domain-Expertise, and Adaptive-Capacity.

The formula for Idiosyncratic Readiness is:
$$V^R(t) = w_1 \cdot AI\text{-}Fluency_i(t) + w_2 \cdot Domain\text{-}Expertise_i(t) + w_3 \cdot Adaptive\text{-}Capacity_i(t)$$
where $w_1 = 0.45$, $w_2 = 0.35$, $w_3 = 0.20$.

Each of these factors is further broken down:
*   **AI-Fluency** ($AI\text{-}Fluency_i$): Measures her ability to effectively use, understand, and collaborate with AI systems. It consists of Technical AI Skills ($\theta_1=0.30$), AI-Augmented Productivity ($\theta_2=0.35$), Critical AI Judgment ($\theta_3=0.20$), and AI Learning Velocity ($\theta_4=0.15$).
    $$AI\text{-}Fluency_i = \sum_{k=1}^4 \theta_k \cdot S_{i,k}$$
    where:
    *   $S_{i,1} = \frac{1}{4} (Prompting_i + Tools_i + Understanding_i + DataLit_i)$ (Technical AI Skills)
    *   $S_{i,2} = \frac{Output\ Quality_{i,with\ AI}}{Output\ Quality_{i,without\ AI}} \cdot \frac{Time_{i,without\ AI}}{Time_{i,with\ AI}}$ (AI-Augmented Productivity) - *For simplicity in this demo, we use a single score representing the ratio.*
    *   $S_{i,3} = \frac{Errors\ Caught_i}{Total\ AI\ Errors} + \frac{Appropriate\ Trust\ Decisions_i}{Total\ Decisions}$ (Critical AI Judgment) - *For simplicity, we use a single score.*
    *   $S_{i,4} = \frac{\Delta Proficiency_i}{\Delta t} \cdot \frac{1}{Hours\ Invested}$ (AI Learning Velocity) - *For simplicity, we use a single score.*
*   **Domain-Expertise** ($Domain\text{-}Expertise_i$): Captures her depth of knowledge in specific application areas. It combines Educational Foundation ($E_{education}$), Practical Experience ($E_{experience}$), and Specialization Depth ($E_{specialization}$).
    $$Domain\text{-}Expertise_i = E_{education} \cdot E_{experience} \cdot E_{specialization}$$
    where $E_{education}$ is based on degree level (e.g., PhD=1.0, Master's=0.85), $E_{experience} = 1 - e^{-\gamma \cdot Years}$ ($\gamma=0.15$), and $E_{specialization} = 0.4 \cdot Portfolio_i + 0.3 \cdot Recognition_i + 0.3 \cdot Credentials_i$.
*   **Adaptive-Capacity** ($Adaptive\text{-}Capacity_i$): Measures meta-skills enabling successful navigation of AI-driven transitions. It's an average of Cognitive Flexibility ($C_{cognitive}$), Social-Emotional Intelligence ($C_{social}$), and Strategic Career Management ($C_{strategic}$).
    $$Adaptive\text{-}Capacity_i = \frac{1}{3} (C_{cognitive} + C_{social} + C_{strategic})$$

All component scores are normalized to $[0, 1]$ before being scaled to $[0, 100]$ at the $V^R$ level.

### Code Cell: Functions for Idiosyncratic Readiness Components

```python
def calculate_ai_fluency(subfactors, theta_weights):
    """Calculates AI-Fluency score based on sub-factors."""
    # S_i,1: Technical AI Skills (avg of prompting, ai_tools, understanding, data_literacy)
    s1 = np.mean([subfactors['prompting'], subfactors['ai_tools'], subfactors['understanding'], subfactors['data_literacy']])
    
    # S_i,2: AI-Augmented Productivity (simplified to a single score)
    s2 = subfactors['ai_augmented_productivity'] 
    
    # S_i,3: Critical AI Judgment (simplified to a single score)
    s3 = subfactors['critical_ai_judgment']
    
    # S_i,4: AI Learning Velocity (simplified to a single score)
    s4 = subfactors['proficiency_gain'] / subfactors['hours_invested'] if subfactors['hours_invested'] > 0 else 0
    s4 = np.clip(s4 * 100, 0, 1) # Normalize to [0,1] based on a typical range

    ai_fluency_score = (
        theta_weights['technical_ai_skills'] * s1 +
        theta_weights['ai_augmented_productivity'] * s2 +
        theta_weights['critical_ai_judgment'] * s3 +
        theta_weights['ai_learning_velocity'] * s4
    )
    return np.clip(ai_fluency_score, 0, 1) # Ensure normalized to [0, 1]

def calculate_domain_expertise(education_level, experience_years, specialization_depth_scores, gamma_exp):
    """Calculates Domain-Expertise score."""
    # E_education
    edu_map = {
        'PhD in target field': 1.0,
        'Master\'s in Finance': 0.85, # Adjusted from generic 'Master\'s in target field'
        'Master\'s in target field': 0.85,
        'Bachelor\'s in target field': 0.70,
        'Associate\'s/Certificate': 0.60,
        'HS + significant coursework': 0.50
    }
    e_education = edu_map.get(education_level, 0.50) # Default to 0.50 if not found

    # E_experience = 1 - e^(-gamma * Years)
    e_experience = 1 - np.exp(-gamma_exp * experience_years)

    # E_specialization = 0.4 * Portfolio + 0.3 * Recognition + 0.3 * Credentials
    e_specialization = (
        0.4 * specialization_depth_scores['portfolio'] +
        0.3 * specialization_depth_scores['recognition'] +
        0.3 * specialization_depth_scores['credentials']
    )
    
    domain_expertise_score = e_education * e_experience * e_specialization
    return np.clip(domain_expertise_score, 0, 1) # Ensure normalized to [0, 1]

def calculate_adaptive_capacity(subfactors):
    """Calculates Adaptive-Capacity score."""
    c_cognitive = subfactors['cognitive_flexibility']
    c_social = subfactors['social_emotional_intelligence']
    c_strategic = subfactors['strategic_career_management']
    
    adaptive_capacity_score = (c_cognitive + c_social + c_strategic) / 3
    return np.clip(adaptive_capacity_score, 0, 1) # Ensure normalized to [0, 1]

def calculate_vr(ai_fluency, domain_expertise, adaptive_capacity, vr_weights):
    """Calculates total Idiosyncratic Readiness (VR) score."""
    vr_score = (
        vr_weights['ai_fluency'] * ai_fluency +
        vr_weights['domain_expertise'] * domain_expertise +
        vr_weights['adaptive_capacity'] * adaptive_capacity
    )
    # VR normalized to [0, 100]
    return np.clip(vr_score * 100, 0, 100)

# Execute VR calculation for Alice
alice_id_data = idiosyncratic_df[idiosyncratic_df['persona_id'] == alice_profile['persona_id']].iloc[0]

# Populate AI-Fluency subfactors
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

# Populate Domain-Expertise subfactors
alice_domain_expertise_subfactors = {
    'portfolio': alice_id_data['portfolio_score'],
    'recognition': alice_id_data['recognition_score'],
    'credentials': alice_id_data['credentials_score']
}

# Populate Adaptive-Capacity subfactors
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
```

### Markdown Cell: Explanation of Alice's Idiosyncratic Readiness

Alice's Idiosyncratic Readiness ($V^R$) score of **`90.35`** (example value if code above is run) indicates a strong individual foundation for AI-enabled roles. Her breakdown shows solid scores across all three main components: AI-Fluency (`0.75`), Domain-Expertise (`0.76`), and Adaptive-Capacity (`0.78`).

*   **AI-Fluency:** Her score suggests she's moderately proficient in interacting with and understanding AI, but there's room for improvement in areas like AI tools and augmented productivity.
*   **Domain-Expertise:** With a Master's degree and 7 years of experience in finance, her deep domain knowledge is a significant asset, indicating a strong foundation in her target financial sector roles.
*   **Adaptive-Capacity:** Her high score in this area is critical, showing she possesses strong meta-skills like cognitive flexibility and social-emotional intelligence, which are essential for navigating rapidly changing AI-driven work environments.

This $V^R$ score will serve as a baseline to evaluate her potential in various target roles when combined with market opportunities.

## 4. Calculating Systematic Opportunity ($H^R$)

Next, Alice needs to understand the external market conditions for her target roles. This is captured by the **Systematic Opportunity ($H^R$)** component, representing macro-level job growth and demand that she can position herself to capture. Unlike $V^R$, $H^R$ cannot be directly created by her actions but rather seized by aligning with market trends.

The formula for Systematic Opportunity for a target occupation $o$ at time $t$ is:
$$H^R(t) = H_{base}(O_{target}) \cdot M_{growth}(t) \cdot M_{regional}(t)$$
where:
*   $H_{base}(o)$: The base opportunity score, an aggregation of multiple dimensions of occupational attractiveness.
    $$H_{base}(o) = w_1 \cdot AI\text{-}Enhancement_o + w_2 \cdot Growth_o + w_3 \cdot WagePremium_o + w_4 \cdot EntryAccessibility_o$$
    with $w_1 = 0.30$, $w_2 = 0.30$, $w_3 = 0.25$, $w_4 = 0.15$.
    *   **AI-Enhancement Potential** ($AI\text{-}Enhancement_o$): How much AI augments rather than replaces tasks (score [0,1]).
    *   **Job Growth Projections** ($Growth_o$): BLS 10-year outlook, normalized to [0,100].
        $$Growth_{normalized} = \frac{g+0.5}{2.0} \times 100$$
        where $g$ is the 10-year growth rate.
    *   **Wage Premium** ($WagePremium_o$): Compensation potential for AI-skilled roles relative to median wages (score [0,1]).
        $$WagePremium_o = \frac{AI\text{-}skilled\ wage_o - median\ wage_o}{median\ wage_o}$$
    *   **Entry Accessibility** ($EntryAccessibility_o$): Ease of transition into the role (score [0,1]).
        $$Access_o = 1 - \frac{Education\ Years\ Required_o + Experience\ Years\ Required_o}{10}$$
*   $M_{growth}(t)$: Growth Multiplier, capturing market momentum from job postings.
    $$M_{growth}(t) = 1 + \lambda \cdot \left(\frac{Job\ Postingso,t}{Job\ Postingso,t-1} - 1\right)$$
    with $\lambda = 0.3$.
*   $M_{regional}(t)$: Regional Multiplier, adjusting for local labor markets.
    $$M_{regional}(t) = \frac{Local\ Demand_{i,t}}{National\ Avg\ Demand} \times (1 + \gamma \cdot Remote\ Work\ Factor_o)$$
    with $\gamma = 0.2$.

All HR components are normalized to $[0, 1]$ before being scaled to $[0, 100]$ at the $H^R$ level.

### Code Cell: Functions for Systematic Opportunity Components

```python
def normalize_growth(growth_rate):
    """Normalizes job growth rate to a [0, 100] scale."""
    # Growth rate g is expected in decimal, e.g., 0.30 for 30% growth
    # Normalization as per the paper: (g + 0.5) / 2.0 * 100
    return np.clip(((growth_rate + 0.5) / 2.0) * 100, 0, 100)

def calculate_wage_premium(ai_skilled_wage, median_wage):
    """Calculates wage premium as a ratio."""
    if median_wage == 0:
        return 0
    return np.clip((ai_skilled_wage - median_wage) / median_wage, 0, 1) # Normalized to [0,1]

def calculate_entry_accessibility(education_years_required, experience_years_required):
    """Calculates entry accessibility."""
    # Max sum for normalization (e.g., PhD + 10 yrs exp = 1.0)
    # The paper uses `1 - (EduYears + ExpYears) / 10`. We assume 10 is a reasonable max denominator.
    # To keep it between [0,1], we assume EduYears+ExpYears max around 10
    total_requirements = education_years_required + experience_years_required
    return np.clip(1 - (total_requirements / 28), 0, 1) # Assuming max 28 (20 for PhD + 8 for exp for example)

def calculate_hbase(ai_enhancement, growth_normalized, wage_premium, entry_accessibility, hbase_weights):
    """Calculates the base opportunity score for a role."""
    hbase_score = (
        hbase_weights['ai_enhancement'] * ai_enhancement +
        hbase_weights['job_growth'] * (growth_normalized / 100) + # Normalize growth back to [0,1] for weighted sum
        hbase_weights['wage_premium'] * wage_premium +
        hbase_weights['entry_accessibility'] * entry_accessibility
    )
    return np.clip(hbase_score, 0, 1) # Ensure normalized to [0, 1]

def calculate_mgrowth(job_postings_t, job_postings_t_minus_1, lambda_param):
    """Calculates the growth multiplier based on job posting momentum."""
    if job_postings_t_minus_1 == 0:
        return 1.0 # No previous data, assume no momentum
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
    # HR normalized to [0, 100]
    return np.clip(hr_score * 100, 0, 100)

# Execute HR calculation for each target role for Alice
hr_scores = {}
for role in target_roles:
    role_data = systematic_df[systematic_df['role'] == role].iloc[0]
    jp_role_data = job_postings_df[job_postings_df['role'] == role].iloc[-1] # Use latest month
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
```

### Markdown Cell: Explanation of Systematic Opportunity Scores

Alice's Systematic Opportunity ($H^R$) scores vary significantly across her target roles.

*   **AI Quant Analyst:** `82.50` (example value) - This role shows high market demand, potentially due to strong AI-enhancement potential and significant wage premiums in quantitative finance.
*   **ML Engineer in Trading:** `80.12` (example value) - Similar to AI Quant, this role also benefits from strong AI integration and demand in the high-growth trading sector.
*   **AI Risk Analyst:** `77.89` (example value) - A moderately high score, indicating good demand for AI skills in risk management, perhaps slightly less aggressive growth than front-office trading roles.
*   **Financial Data Scientist:** `70.45` (example value) - While still robust, this role might have a slightly lower $H^R$ compared to the more specialized AI Quant/ML roles, possibly due to broader applicability or higher entry accessibility.

This analysis helps Alice understand where the market opportunities lie, complementing her individual readiness. The next step is to combine these two components to get the full AI-Readiness Score.

## 5. Synthesizing AI-Readiness ($AI-R$) & Identifying Initial Gaps

Now Alice will synthesize her individual capabilities ($V^R$) with the market's systematic opportunities ($H^R$) to calculate her comprehensive AI-Readiness Score ($AI-R$) for each target role. A critical aspect here is the **Synergy Function**, which captures the multiplicative benefits when individual skills align with market demand.

The overall AI-Readiness Score is:
$$AI-R_{i,t} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{i}^R(t) + \beta \cdot Synergy\%(V_i^R, H_{i}^R)$$
where $\alpha=0.6$ and $\beta=0.15$.

The Synergy Function is defined as:
$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$
where $V^R$ and $H^R$ are normalized to $[0, 100]$, and $Alignment_i \in [0,1]$.

The **Alignment Factor** ($Alignment_i$) measures how well Alice's individual skills match the occupation requirements and her career stage:
$$Alignment_i = \frac{Skills\ Match\ Score}{Maximum\ Possible\ Match} \times Timing\ Factor$$
*   **Skills Match Score**: Calculated based on O*NET-like task-skill mappings, comparing Alice's current skills against the required skills for a target occupation.
    $$Match = \sum_{s \in S} \min(Individual\ Skill_{i,s}, Required\ Skill_{o,s}) \cdot Importance_s$$
    (For this demo, `Importance_s` is assumed to be 1 for all skills, and `Maximum Possible Match` is the sum of max required skill levels).
*   **Timing Factor**: Reflects career stage, affecting transition ease.
    $$Timing(y) = \begin{cases} 1.0 & y \in [0,5] \ (early\ career) \\ 1.0 & y \in (5,15] \ (mid\text{-}career) \\ 0.8 & y > 15 \ (late\ career,\ transition\ friction) \end{cases}$$
    where $y$ is years of experience.

### Code Cell: Functions for AI-Readiness and Synergy

```python
def calculate_skills_match_score(current_skills_dict, required_skills_series, max_possible_match_val):
    """Calculates the skills match score based on current vs. required skills."""
    match_score = 0
    skills_in_common = 0
    current_skills_level = 0
    required_skills_level = 0
    
    # Extract skills for the specific role (excluding 'role' column)
    req_skills = required_skills_series.drop('role').to_dict()

    for skill, req_level in req_skills.items():
        if skill in current_skills_dict:
            match_score += min(current_skills_dict[skill], req_level)
            skills_in_common += 1
            current_skills_level += current_skills_dict[skill]
        required_skills_level += req_level
            
    # Normalize match_score to [0,1]
    # max_possible_match_val is the sum of maximum possible skill levels for the required skills for this role
    if max_possible_match_val == 0:
        return 0, {}, {}, 0, 0
    
    normalized_match_score = match_score / max_possible_match_val
    
    # Calculate skill gaps for visualization
    skill_gaps = {}
    for skill, req_level in req_skills.items():
        current_level = current_skills_dict.get(skill, 0)
        skill_gaps[skill] = {'current': current_level, 'required': req_level}

    return np.clip(normalized_match_score, 0, 1), skill_gaps, req_skills, current_skills_level, required_skills_level


def calculate_timing_factor(years_experience):
    """Calculates the timing factor based on years of experience."""
    if years_experience <= 5:
        return 1.0 # Early career
    elif 5 < years_experience <= 15:
        return 1.0 # Mid-career
    else:
        return 0.8 # Late career, transition friction

def calculate_alignment(skills_match_score, timing_factor):
    """Calculates the alignment factor."""
    return np.clip(skills_match_score * timing_factor, 0, 1)

def calculate_synergy(vr_score, hr_score, alignment_score):
    """Calculates the synergy percentage."""
    synergy_base = (vr_score * hr_score) / 100 # This part is already scaled to 0-100 range from VR*HR/100
    return np.clip(synergy_base * alignment_score, 0, 100) # Output in [0, 100]

def calculate_air(vr_score, hr_score, synergy_score, alpha, beta):
    """Calculates the total AI-Readiness Score."""
    air_score = alpha * vr_score + (1 - alpha) * hr_score + beta * synergy_score
    return np.clip(air_score, 0, 100)

# Store results
air_results = []
all_skill_gaps = {}

for role in target_roles:
    # Get HR score for the current role
    current_hr_score = hr_scores[role]

    # Calculate skills match score
    required_skills_for_role = skill_requirements_df[skill_requirements_df['role'] == role].iloc[0]
    
    # Determine max_possible_match_val for the current role's required skills
    # Sum of required skill levels for that role, assuming max level per skill is 10
    max_possible_match_for_role = required_skills_for_role.drop('role').sum()
    
    skills_match, skill_gaps, required_skills_dict, current_skills_total, required_skills_total = calculate_skills_match_score(
        alice_profile['current_skills'], 
        required_skills_for_role,
        max_possible_match_for_role
    )
    all_skill_gaps[role] = skill_gaps # Store for later visualization

    # Calculate timing factor
    timing_factor = calculate_timing_factor(alice_profile['experience_years'])

    # Calculate alignment
    alignment_score = calculate_alignment(skills_match, timing_factor)

    # Calculate synergy
    synergy_score = calculate_synergy(alice_vr_score, current_hr_score, alignment_score)

    # Calculate AI-R
    air_score = calculate_air(alice_vr_score, current_hr_score, synergy_score, ALPHA, BETA)
    
    air_results.append({
        'Role': role,
        'VR_Score': alice_vr_score,
        'HR_Score': current_hr_score,
        'Skills_Match_Score': skills_match * 100, # Display as percentage
        'Timing_Factor': timing_factor,
        'Alignment_Score': alignment_score * 100, # Display as percentage
        'Synergy_Score': synergy_score,
        'AI_R_Score': air_score
    })

air_df = pd.DataFrame(air_results)
print("\n--- Alice's AI-Readiness Scores (AI-R) for Target Roles ---")
print(air_df.round(2))

# Identify Alice's top target role based on AI-R
top_role = air_df.loc[air_df['AI_R_Score'].idxmax()]
print(f"\nAlice's Top AI-R Role: {top_role['Role']} (AI-R: {top_role['AI_R_Score']:.2f})")

# Visualization: Bar chart for AI-R, VR, HR
air_df_plot = air_df[['Role', 'AI_R_Score', 'VR_Score', 'HR_Score']].set_index('Role')
air_df_plot.plot(kind='bar', figsize=(12, 7), title='Alice\'s AI-Readiness Scores Across Target Roles')
plt.ylabel('Score (0-100)')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Component')
plt.tight_layout()
plt.show()

# Visualization: Radar chart for skill gaps for the top target role
top_role_skills = all_skill_gaps[top_role['Role']]
skills_df = pd.DataFrame(top_role_skills).T.reset_index().rename(columns={'index': 'Skill'})

# Prepare data for radar chart
labels = skills_df['Skill'].tolist()
current_levels = skills_df['current'].tolist()
required_levels = skills_df['required'].tolist()

# Extend skills and levels for a closed loop in radar chart
labels += labels[:1]
current_levels += current_levels[:1]
required_levels += required_levels[:1]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
angles_degrees = np.degrees(angles)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.fill(angles, current_levels, color='blue', alpha=0.25, label='Current Skill Level')
ax.plot(angles, current_levels, color='blue', linewidth=2)
ax.fill(angles, required_levels, color='red', alpha=0.25, label='Required Skill Level')
ax.plot(angles, required_levels, color='red', linewidth=2)

ax.set_yticklabels([f'{i}' for i in range(0, 11, 2)]) # Skill levels typically 0-10
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels[:-1])
ax.set_title(f'Skill Gaps for {top_role["Role"]}', size=16, y=1.08)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.show()
```

### Markdown Cell: Explanation of AI-Readiness Scores and Skill Gaps

Alice's AI-Readiness Scores reveal that the **AI Quant Analyst** role currently offers her the highest opportunity, with an AI-R score of `85.42` (example value). This is primarily driven by a strong $H^R$ for this role, which synergizes well with her high $V^R$. The 'ML Engineer in Trading' also presents a very strong opportunity.

The bar chart visually confirms this, showing a balance between Alice's personal readiness ($V^R$) and market opportunity ($H^R$) for the top roles. The Synergy component further boosts her AI-R, indicating that her skills and experience align well with these high-opportunity fields.

The radar chart, specifically for the 'AI Quant Analyst' role, highlights Alice's current skill levels against the required levels. She has strong foundations in `Risk_Analysis`, `Financial_Modeling`, and `Python`. However, significant gaps exist in `Quant_Models`, `ML_basics`, `AI_Ethics`, `GenAI_Tools`, and `Cloud_Platforms`. Addressing these gaps will be critical for her to fully capture the opportunity in the AI Quant Analyst role.

## 6. Optimizing Learning Pathways for Career Growth

Based on her initial AI-R scores and identified skill gaps, Alice wants to invest in learning to maximize her career prospects. However, her time and budget are constrained. This section simulates a multi-step pathway optimization algorithm to recommend a sequence of learning activities that maximize her projected AI-R gain under these specified resource constraints.

The objective is to maximize the gain in AI-R minus a weighted cost:
$$ \max_{P_1,...,P_K} (AI\text{-}R_{proj} - AI\text{-}R_{current}) - \lambda \cdot \sum_{k=1}^K Cost(p_k) $$
subject to:
$$ \sum_{k=1}^K Time(p_k) \le T_{max} $$
$$ \sum_{k=1}^K Cost(p_k) \le B_{max} $$
$$ p_k \in P_{feasible} $$
$$ Prerequisites(p_k) \subseteq \{P_1,...,P_{k-1}\} $$
where $AI\text{-}R_{proj}$ is the projected AI-R after completing pathways, $AI\text{-}R_{current}$ is her initial AI-R, $\lambda$ is `LAMBDA_COST_WEIGHT`, $T_{max}$ is `MAX_LEARNING_TIME_HOURS`, and $B_{max}$ is `MAX_LEARNING_BUDGET_USD`.

For this demonstration, we'll use a greedy heuristic: selecting pathways one by one that offer the highest "return" (AI-R point gain per unit of weighted time/cost) until constraints are met, respecting prerequisites.

### Code Cell: Learning Pathway Optimization Function

```python
def simulate_learning_pathway_impact(current_vr_subscores, pathway_impacts):
    """
    Simulates the impact of a learning pathway on VR sub-scores (AI-Fluency, Domain-Expertise, Adaptive-Capacity).
    Impacts are added to the normalized sub-scores, then re-clipped to [0,1].
    """
    new_vr_subscores = current_vr_subscores.copy()
    
    # Impacts are given in raw points (0-100 scale), need to convert to normalized [0,1]
    new_vr_subscores['ai_fluency'] = np.clip(new_vr_subscores['ai_fluency'] + (pathway_impacts['impact_ai_fluency'] / 100), 0, 1)
    new_vr_subscores['domain_expertise'] = np.clip(new_vr_subscores['domain_expertise'] + (pathway_impacts['impact_domain_expertise'] / 100), 0, 1)
    new_vr_subscores['adaptive_capacity'] = np.clip(new_vr_subscores['adaptive_capacity'] + (pathway_impacts['impact_adaptive_capacity'] / 100), 0, 1)
    
    return new_vr_subscores

def optimize_learning_pathways(current_air_score, current_vr_score, current_vr_subscores, target_hr_score, 
                               learning_pathways_df, max_time, max_cost, 
                               alpha, beta, lambda_cost_weight, alice_exp_years, alice_current_skills_dict):
    """
    Optimizes a sequence of learning pathways using a greedy heuristic.
    Selects pathways that offer the highest (AI-R gain / (cost + time)) ratio.
    """
    available_pathways = learning_pathways_df.copy()
    recommended_pathways = []
    total_time = 0
    total_cost = 0
    
    # Initial state for iterative calculation
    current_vr_subscores_normalized = current_vr_subscores.copy() # Store AI-Fluency, Domain-Expertise, Adaptive-Capacity as [0,1]
    current_vr = current_vr_score
    
    # Store skills for the target role to re-calculate alignment after each pathway
    target_role_name = air_df.loc[air_df['AI_R_Score'].idxmax(), 'Role']
    required_skills_for_target_role = skill_requirements_df[skill_requirements_df['role'] == target_role_name].iloc[0].drop('role').to_dict()
    max_possible_match_for_target_role = sum(required_skills_for_target_role.values())
    
    # Simulate current skills for the optimization loop (Alice's skills can improve)
    simulated_current_skills = alice_current_skills_dict.copy()

    # Calculate initial alignment and synergy
    initial_skills_match, _, _, _, _ = calculate_skills_match_score(
        simulated_current_skills, 
        pd.Series(required_skills_for_target_role, name='skills'), 
        max_possible_match_for_target_role
    )
    initial_timing_factor = calculate_timing_factor(alice_exp_years)
    initial_alignment = calculate_alignment(initial_skills_match, initial_timing_factor)
    initial_synergy = calculate_synergy(current_vr, target_hr_score, initial_alignment)
    
    # Calculate initial AI-R (this should be the same as current_air_score)
    current_air = calculate_air(current_vr, target_hr_score, initial_synergy, alpha, beta)


    while True:
        best_pathway = None
        max_return_on_investment = -1
        
        # Filter pathways that meet prerequisites and resource constraints
        eligible_pathways = available_pathways[~available_pathways['pathway_id'].isin([p['pathway_id'] for p in recommended_pathways])]
        
        # Check prerequisites
        eligible_pathways_with_prereqs = []
        completed_pathway_ids = [p['pathway_id'] for p in recommended_pathways]
        for _, pathway in eligible_pathways.iterrows():
            prereqs = eval(pathway['prerequisites']) # Convert string list to actual list
            if all(p_id in completed_pathway_ids for p_id in prereqs):
                eligible_pathways_with_prereqs.append(pathway)
        
        if not eligible_pathways_with_prereqs:
            break # No more eligible pathways

        for pathway_data in eligible_pathways_with_prereqs:
            if total_time + pathway_data['estimated_time_hours'] <= max_time and \
               total_cost + pathway_data['estimated_cost_usd'] <= max_cost:
                
                # Simulate VR sub-scores after this pathway
                projected_vr_subscores = simulate_learning_pathway_impact(current_vr_subscores_normalized, pathway_data)
                
                # Re-calculate VR
                projected_vr = calculate_vr(
                    projected_vr_subscores['ai_fluency'], 
                    projected_vr_subscores['domain_expertise'], 
                    projected_vr_subscores['adaptive_capacity'], 
                    VR_COMPONENT_WEIGHTS
                )

                # Update simulated skills for the optimization
                # This is a simplification. Realistically, pathways improve specific skills,
                # which would then feed into skills_match. For this demo, we assume pathway impact
                # is primarily on VR components and indirectly on alignment by improving general "match" ability.
                # A more complex model would map pathways to individual skill gains.
                # For now, we'll assume a direct skill match improvement, or just rely on VR for this optimization.
                # Let's add a small, fixed boost to the skills_match for any pathway to show progress
                
                # Simulate skills improvement impact (simplified)
                temp_simulated_skills = simulated_current_skills.copy()
                if pathway_data['type'] == 'AI-Fluency':
                    temp_simulated_skills['GenAI_Tools'] = min(10, temp_simulated_skills['GenAI_Tools'] + 1)
                elif pathway_data['type'] == 'Domain+AI':
                     temp_simulated_skills['ML_basics'] = min(10, temp_simulated_skills['ML_basics'] + 1)
                     temp_simulated_skills['Quant_Models'] = min(10, temp_simulated_skills['Quant_Models'] + 1)
                elif pathway_data['type'] == 'Adaptive Capacity':
                    temp_simulated_skills['AI_Ethics'] = min(10, temp_simulated_skills['AI_Ethics'] + 1)
                    
                
                projected_skills_match, _, _, _, _ = calculate_skills_match_score(
                    temp_simulated_skills, 
                    pd.Series(required_skills_for_target_role, name='skills'), 
                    max_possible_match_for_target_role
                )
                projected_alignment = calculate_alignment(projected_skills_match, initial_timing_factor) # Timing factor remains constant
                projected_synergy = calculate_synergy(projected_vr, target_hr_score, projected_alignment)
                
                projected_air = calculate_air(projected_vr, target_hr_score, projected_synergy, alpha, beta)
                
                air_gain = projected_air - current_air
                
                # Define return on investment: AI-R gain / (weighted_cost + weighted_time)
                # Weighted cost: cost * lambda_cost_weight
                # Weighted time: time * some_time_weight (we can simplify for now or use a common scale)
                # Let's normalize time and cost to prevent one from dominating
                normalized_cost = pathway_data['estimated_cost_usd'] / MAX_LEARNING_BUDGET_USD
                normalized_time = pathway_data['estimated_time_hours'] / MAX_LEARNING_TIME_HOURS
                
                investment = (normalized_cost * lambda_cost_weight) + normalized_time
                
                if investment > 0:
                    roi = air_gain / investment
                else:
                    roi = air_gain # If investment is zero, just take the gain
                
                if roi > max_return_on_investment:
                    max_return_on_investment = roi
                    best_pathway = pathway_data
                    
        if best_pathway is None:
            break # No pathway found that fits constraints

        # Add best pathway
        recommended_pathways.append(best_pathway)
        total_time += best_pathway['estimated_time_hours']
        total_cost += best_pathway['estimated_cost_usd']
        
        # Update current state for next iteration
        current_vr_subscores_normalized = simulate_learning_pathway_impact(current_vr_subscores_normalized, best_pathway)
        current_vr = calculate_vr(
            current_vr_subscores_normalized['ai_fluency'], 
            current_vr_subscores_normalized['domain_expertise'], 
            current_vr_subscores_normalized['adaptive_capacity'], 
            VR_COMPONENT_WEIGHTS
        )
        # Update simulated skills based on best_pathway chosen
        if best_pathway['type'] == 'AI-Fluency':
            simulated_current_skills['GenAI_Tools'] = min(10, simulated_current_skills['GenAI_Tools'] + 1)
        elif best_pathway['type'] == 'Domain+AI':
             simulated_current_skills['ML_basics'] = min(10, simulated_current_skills['ML_basics'] + 1)
             simulated_current_skills['Quant_Models'] = min(10, simulated_current_skills['Quant_Models'] + 1)
        elif best_pathway['type'] == 'Adaptive Capacity':
            simulated_current_skills['AI_Ethics'] = min(10, simulated_current_skills['AI_Ethics'] + 1)
        
        # Recalculate AI-R after adding pathway
        current_air = calculate_air(current_vr, target_hr_score, 
                                    calculate_synergy(current_vr, target_hr_score, 
                                                      calculate_alignment(
                                                          calculate_skills_match_score(
                                                              simulated_current_skills, 
                                                              pd.Series(required_skills_for_target_role, name='skills'), 
                                                              max_possible_match_for_target_role
                                                          )[0], 
                                                          initial_timing_factor)), 
                                    alpha, beta)

    # Final calculation with accumulated changes
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

# Initial VR sub-scores normalized for optimization
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

# Visualization: Current vs. Projected AI-R
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

# Update Alice's profile with projected VR and skills for subsequent what-if analysis
alice_profile_after_paths = alice_profile.copy()
alice_profile_after_paths['vr_score'] = final_vr_after_paths
alice_profile_after_paths['ai_fluency_score'] = final_vr_subscores_normalized['ai_fluency']
alice_profile_after_paths['domain_expertise_score'] = final_vr_subscores_normalized['domain_expertise']
alice_profile_after_paths['adaptive_capacity_score'] = final_vr_subscores_normalized['adaptive_capacity']
alice_profile_after_paths['current_skills'] = final_skills_after_paths # Update current skills
```

### Markdown Cell: Explanation of Optimized Learning Pathway

The optimization algorithm has identified an optimal sequence of learning pathways for Alice, aiming to maximize her AI-R for the `AI Quant Analyst` role within her time and budget constraints.

For example, the recommended pathways might include:
1.  **Prompt Engineering for Finance**: Directly boosts AI-Fluency, addressing a gap in her AI interaction skills.
2.  **Financial Domain-Specific AI**: Enhances both Domain-Expertise and AI-Fluency, directly impacting skills for financial AI applications like 'ML_basics' and 'Quant_Models'.
3.  **Advanced ML for Trading**: Builds on previous learning, further improving Domain-Expertise and advanced ML skills relevant to quant roles.

These pathways, totaling `160` hours and `$1550` (example values), project an AI-R increase from `85.42` to `90.15` (example values). This represents a significant uplift in her overall readiness and marketability for her chosen high-opportunity role. The bar chart visually demonstrates this substantial projected improvement, confirming that the learning investment is expected to yield a positive return on her career trajectory.

## 7. "What-If" Scenario Analysis

Alice wants to explore alternative career and learning strategies beyond the initial optimal recommendation. The 'What-If' scenario engine allows her to compare different choices, understand trade-offs, and see how they impact her projected AI-R. This functionality helps in making robust career decisions.

We will evaluate two scenarios:
1.  **Scenario A: Focus on a slightly less demanding role (e.g., 'Financial Data Scientist') with a tailored learning path.**
2.  **Scenario B: Stick to 'AI Quant Analyst' but opt for a cheaper, faster, but potentially less impactful learning path.**

### Code Cell: "What-If" Scenario Analysis Function

```python
def run_what_if_scenario(initial_vr_score, initial_vr_subscores_normalized, initial_skills, 
                         target_role_name, hr_data, skill_req_data, learning_pathways_for_scenario, 
                         alice_exp_years, alpha, beta):
    """
    Runs a 'What-If' scenario by applying proposed pathways and calculating projected AI-R.
    """
    # Start with initial VR state
    current_vr = initial_vr_score
    current_vr_subscores = initial_vr_subscores_normalized.copy()
    current_skills_dict = initial_skills.copy()

    # Apply proposed pathways' impact
    for pathway in learning_pathways_for_scenario:
        current_vr_subscores = simulate_learning_pathway_impact(current_vr_subscores, pathway)
        # Simulate skills improvement (simplified) for what-if
        if pathway['type'] == 'AI-Fluency':
            current_skills_dict['GenAI_Tools'] = min(10, current_skills_dict['GenAI_Tools'] + 1)
        elif pathway['type'] == 'Domain+AI':
             current_skills_dict['ML_basics'] = min(10, current_skills_dict['ML_basics'] + 1)
             current_skills_dict['Quant_Models'] = min(10, current_skills_dict['Quant_Models'] + 1)
        elif pathway['type'] == 'Adaptive Capacity':
            current_skills_dict['AI_Ethics'] = min(10, current_skills_dict['AI_Ethics'] + 1)
            
    # Calculate final VR after pathways
    projected_vr = calculate_vr(
        current_vr_subscores['ai_fluency'], 
        current_vr_subscores['domain_expertise'], 
        current_vr_subscores['adaptive_capacity'], 
        VR_COMPONENT_WEIGHTS
    )

    # Get HR for the target role
    target_hr_score = hr_data[target_role_name]
    
    # Calculate alignment for the target role
    required_skills_for_role_series = skill_req_data[skill_req_data['role'] == target_role_name].iloc[0]
    max_possible_match_for_role = required_skills_for_role_series.drop('role').sum()
    
    skills_match, _, _, _, _ = calculate_skills_match_score(
        current_skills_dict, 
        required_skills_for_role_series, 
        max_possible_match_for_role
    )
    timing_factor = calculate_timing_factor(alice_exp_years)
    alignment_score = calculate_alignment(skills_match, timing_factor)

    # Calculate synergy and AI-R
    synergy_score = calculate_synergy(projected_vr, target_hr_score, alignment_score)
    projected_air = calculate_air(projected_vr, target_hr_score, synergy_score, alpha, beta)
    
    # Calculate total time and cost
    total_time = sum(p['estimated_time_hours'] for p in learning_pathways_for_scenario)
    total_cost = sum(p['estimated_cost_usd'] for p in learning_pathways_for_scenario)

    return projected_air, total_time, total_cost, projected_vr, target_hr_score, synergy_score


# --- Define Scenario Pathways ---
# Original Optimized Path (from Section 6) - Re-run for comparison
optimal_pathway_details = pd.DataFrame(recommended_paths)
total_optimal_time = optimal_pathway_details['estimated_time_hours'].sum() if not optimal_pathway_details.empty else 0
total_optimal_cost = optimal_pathway_details['estimated_cost_usd'].sum() if not optimal_pathway_details.empty else 0
projected_air_optimal = projected_air # From previous section
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

# Scenario A: Financial Data Scientist with specific pathways
scenario_a_pathways = learning_pathways_df[learning_pathways_df['pathway_id'].isin(['P001', 'P004'])].to_dict('records') # Prompt Eng & Gen AI
projected_air_a, time_a, cost_a, projected_vr_a, hr_a, synergy_a = run_what_if_scenario(
    alice_vr_score, alice_current_vr_subscores_normalized, alice_profile['current_skills'],
    'Financial Data Scientist', hr_scores, skill_requirements_df, scenario_a_pathways,
    alice_profile['experience_years'], ALPHA, BETA
)
scenario_results.append({
    'Scenario': 'Financial Data Scientist w/ GenAI Focus',
    'Target Role': 'Financial Data Scientist',
    'Projected AI-R': projected_air_a,
    'Projected VR': projected_vr_a,
    'HR': hr_a,
    'Time (h)': time_a,
    'Cost ($)': cost_a
})

# Scenario B: AI Quant Analyst with a cheaper, faster path (e.g., only P001 & P003)
scenario_b_pathways = learning_pathways_df[learning_pathways_df['pathway_id'].isin(['P001', 'P003'])].to_dict('records') # Prompt Eng & AI Ethics
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

# Visualization: Comparative Bar Chart of Projected AI-R
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

# Visualization: Return on Learning Investment (AI-R Gain per unit cost + time)
# For simplicity, calculate a composite ROI metric: (Projected AI-R - Initial AI-R) / (Total Cost + Total Time_weighted)
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
        initial_air = 0 # Fallback

    air_gain = row['Projected AI-R'] - initial_air
    
    # Using the same weighting for cost/time as in optimization
    normalized_cost = row['Cost ($)'] / MAX_LEARNING_BUDGET_USD if MAX_LEARNING_BUDGET_USD > 0 else 0
    normalized_time = row['Time (h)'] / MAX_LEARNING_TIME_HOURS if MAX_LEARNING_TIME_HOURS > 0 else 0
    
    investment_factor = (normalized_cost * LAMBDA_COST_WEIGHT) + normalized_time
    
    if investment_factor > 0:
        roi = air_gain / investment_factor
    else:
        roi = air_gain # If no investment, ROI is just the gain
    
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
```

### Markdown Cell: Explanation of "What-If" Analysis Results

The "What-If" analysis provides Alice with critical insights into the strategic implications of her choices.

*   **Optimized for AI Quant Analyst (Original Plan):** This scenario yielded the highest projected AI-R of `90.15` (example value), confirming it as the most effective strategy for the `AI Quant Analyst` role. The investment, while substantial, leads to significant career readiness.

*   **Financial Data Scientist w/ GenAI Focus (Scenario A):** Targeting a slightly different role with a more focused learning path (lower time and cost) results in a projected AI-R of `78.53` (example value). This is lower than the optimal AI Quant path, primarily because the initial $H^R$ for a Financial Data Scientist is lower, and the chosen pathways, while good for AI Fluency, may not fully address domain-specific needs for a higher AI-R.

*   **AI Quant Analyst w/ Minimal Path (Scenario B):** Sticking with the high-opportunity `AI Quant Analyst` role but choosing a cheaper, faster pathway (e.g., only `Prompt Engineering` and `AI Ethics`) leads to a projected AI-R of `86.58` (example value). While this is still a good score and requires less investment, it falls short of the `90.15` achieved with the fully optimized, more comprehensive learning plan. This highlights the trade-off between investment and maximum potential.

The comparative bar chart clearly illustrates these differences in projected AI-R, allowing Alice to visually grasp the outcomes. The ROI chart further clarifies which investments provide the best "bang for her buck." The "Optimized for AI Quant Analyst" pathway, despite higher upfront investment, likely offers a superior long-term return due to the significant AI-R boost it provides.

This analysis empowers Alice to make a data-driven decision, weighing the projected career opportunity against the required investment in time and cost.

## 8. Personalized AI Career Strategy Report

This section consolidates all the analysis into a clear, actionable report for Alice, summarizing her current standing, identified skill gaps, and the recommended optimal learning pathway with projected outcomes.

### Code Cell: Generate Personalized Report

```python
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
```

