import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import minimize
import random
import copy
def calculate_ai_r(vr_score, hr_score, synergy_score, alpha, beta):
    """Computes the overall AI-Readiness Score."""
    # Ensure scores are within 0-100
    vr_score = np.clip(vr_score, 0, 100)
    hr_score = np.clip(hr_score, 0, 100)
    synergy_score = np.clip(synergy_score, 0, 100)

    # Calculate AI-R
    ai_r = (alpha * vr_score) + ((1 - alpha) * hr_score) + (beta * synergy_score)
    return np.clip(ai_r, 0, 100)

# Test the function immediately
print(f"Test AI-R score: {calculate_ai_r(vr_score=75, hr_score=80, synergy_score=51, alpha=0.6, beta=0.15):.2f}")
# Define default parameters for \alpha and \beta
PARAMS = {
    'alpha': 0.6,
    'beta': 0.15,
    'lambda_growth': 0.3,
    'gamma_regional': 0.2,
    'hr_base_weights': {
        'ai_enhancement_weight': 0.30,
        'job_growth_weight': 0.30,
        'wage_premium_weight': 0.25,
        'entry_accessibility_weight': 0.15
    },
    'theta_ai_fluency_weights': {
        'technical_ai_skills_weight': 0.30,
        'ai_augmented_productivity_weight': 0.35,
        'critical_ai_judgment_weight': 0.20,
        'ai_learning_velocity_weight': 0.15
    },
    'gamma_experience_decay': 0.15,
    'domain_specialization_weights': {
        'portfolio_weight': 0.4,
        'recognition_weight': 0.3,
        'credentials_weight': 0.3
    },
    'vr_component_weights': {
        'ai_fluency_weight_vr': 0.45,
        'domain_expertise_weight_vr': 0.35,
        'adaptive_capacity_weight_vr': 0.20
    }
}

# Initialize placeholder values for VR, HRR, and Synergy%
vr_placeholder = 75
hr_placeholder = 80
synergy_placeholder = 51.0

# Execute calculate_ai_r with these placeholder values
final_ai_r_placeholder = calculate_ai_r(vr_placeholder, hr_placeholder, synergy_placeholder, PARAMS['alpha'], PARAMS['beta'])

print(f"Placeholder V^R: {vr_placeholder}")
print(f"Placeholder HR^R: {hr_placeholder}")
print(f"Placeholder Synergy%: {synergy_placeholder}")
print(f"Calculated AI-R with placeholder values: {final_ai_r_placeholder:.2f}")
import pandas as pd
import numpy as np
import pytest
import random

# The functions to be tested are defined here within the test file.
# This ensures tests are self-contained and run against a consistent version of the functions.

def generate_synthetic_employees(num_employees=50):
    employee_data = {
        'employee_id': [f'EMP{i:03d}' for i in range(num_employees)],
        'job_role': random.choices(['Data Scientist', 'ML Engineer', 'AI Ethicist', 'Business Analyst', 'HR Specialist'], k=num_employees),
        'department': random.choices(['R&D', 'Engineering', 'HR', 'Marketing', 'Finance'], k=num_employees),
        'years_experience': np.random.randint(0, 20, num_employees),
        'education_level': random.choices(['HS+Coursework', 'Associate\'s/Certificate', 'Bachelor\'s', 'Master\'s', 'PhD'], k=num_employees),
        'prompting_score': np.random.randint(30, 95, num_employees),
        'tools_score': np.random.randint(20, 90, num_employees),
        'understanding_score': np.random.randint(40, 95, num_employees),
        'data_lit_score': np.random.randint(35, 90, num_employees),
        'output_quality_with_ai': np.random.uniform(0.7, 1.2, num_employees), # Relative to without AI
        'output_quality_without_ai': np.random.uniform(0.5, 1.0, num_employees),
        'time_without_ai': np.random.uniform(1.0, 1.5, num_employees), # Relative to with AI
        'time_with_ai': np.random.uniform(0.7, 1.0, num_employees),
        'errors_caught': np.random.randint(5, 20, num_employees),
        'total_ai_errors': np.random.randint(15, 30, num_employees),
        'appropriate_trust_decisions': np.random.randint(10, 25, num_employees),
        'total_decisions': np.random.randint(20, 35, num_employees),
        'learning_rate': np.random.uniform(0.05, 0.25, num_employees),
        'hours_invested': np.random.randint(50, 500, num_employees),
        'domain_portfolio_score': np.random.randint(20, 90, num_employees),
        'domain_recognition_score': np.random.randint(10, 80, num_employees),
        'domain_credentials_score': np.random.randint(30, 95, num_employees),
        'adaptive_cognitive_flexibility': np.random.randint(40, 95, num_employees),
        'adaptive_social_emotional': np.random.randint(30, 90, num_employees),
        'adaptive_strategic_career': np.random.randint(35, 95, num_employees)
    }
    # Add generic skills for skill match
    for i in range(10):
        employee_data[f'skill_{chr(ord("a") + i)}'] = np.random.randint(0, 100, num_employees) # Corrected syntax for inner string literal

    df = pd.DataFrame(employee_data)

    # Normalize scores to 0-100 where applicable (these are raw inputs)
    df['errors_caught_norm'] = (df['errors_caught'] / df['total_ai_errors'] * 100).fillna(0)
    df['trust_decisions_norm'] = (df['appropriate_trust_decisions'] / df['total_decisions'] * 100).fillna(0)

    # Ensure no division by zero for output_quality_without_ai and time_with_ai
    df['output_quality_without_ai_safe'] = df['output_quality_without_ai'].replace(0, np.nan)
    df['time_with_ai_safe'] = df['time_with_ai'].replace(0, np.nan)

    df['ai_augmented_productivity_raw'] = (df['output_quality_with_ai'] / df['output_quality_without_ai_safe']) * \
                                         (df['time_without_ai'] / df['time_with_ai_safe'])
    df['ai_augmented_productivity_raw'] = df['ai_augmented_productivity_raw'].fillna(0) # Fill NaN if division by zero occurred

    df['ai_augmented_productivity_norm'] = np.clip(df['ai_augmented_productivity_raw'] * 50, 0, 100) # Scale and clip for initial S_i2

    return df

def generate_synthetic_occupations():
    occupation_data = {
        'occupation': ['Data Scientist', 'ML Engineer', 'AI Ethicist', 'Business Analyst', 'HR Specialist'],
        'ai_enhancement_potential': [85, 90, 75, 60, 50],
        'projected_jobs_t': [5000, 4000, 1000, 15000, 12000],
        'projected_jobs_t_plus_10': [8000, 7500, 2000, 16000, 11000],
        'ai_skilled_wage': [140000, 150000, 120000, 90000, 80000],
        'median_wage': [110000, 120000, 100000, 75000, 65000],
        'education_years_required': [18, 18, 16, 16, 14],
        'experience_years_required': [3, 4, 2, 2, 1],
        'remote_work_factor': [0.8, 0.9, 0.7, 0.6, 0.5],
        'job_postings_current_month': [120, 110, 40, 80, 70],
        'job_postings_prev_month': [100, 100, 35, 85, 75],
        'national_avg_demand': [100, 100, 100, 100, 100]
    }
    # Add required skills and importance
    for i in range(10):
        occupation_data[f'required_skill_{chr(ord("a") + i)}'] = np.random.randint(30, 90, len(occupation_data['occupation'])) # Corrected syntax for inner string literal
        occupation_data[f'skill_{chr(ord("a") + i)}_importance'] = np.random.uniform(0.1, 1.0, len(occupation_data['occupation'])) # Corrected syntax for inner string literal

    return pd.DataFrame(occupation_data)

def generate_synthetic_pathways():
    pathway_data = {
        'pathway_id': [f'PATH{i:02d}' for i in range(1, 6)],
        'pathway_name': ['AI Fundamentals Course', 'Advanced ML Specialization', 'AI Ethics & Governance', 'Data Storytelling with AI', 'HR Analytics with AI'],
        'pathway_type': ['Online Course', 'Certification', 'Workshop', 'Online Course', 'Certification'],
        'cost': [500, 2000, 1000, 300, 750],
        'time_hours': [40, 160, 80, 30, 60],
        'delta_ai_fluency': [10, 25, 5, 3, 5],
        'delta_domain_expertise': [5, 10, 15, 8, 12],
        'delta_adaptive_capacity': [5, 5, 10, 7, 8]
    }
    return pd.DataFrame(pathway_data)


# Pytest Unit Tests
# To ensure reproducibility, set a seed for numpy and random
@pytest.fixture(autouse=True)
def set_random_seed():
    np.random.seed(42)
    random.seed(42)


def test_generate_synthetic_employees_structure():
    df = generate_synthetic_employees(10)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10

    expected_cols = [
        'employee_id', 'job_role', 'department', 'years_experience', 'education_level',
        'prompting_score', 'tools_score', 'understanding_score', 'data_lit_score',
        'output_quality_with_ai', 'output_quality_without_ai', 'time_without_ai',
        'time_with_ai', 'errors_caught', 'total_ai_errors',
        'appropriate_trust_decisions', 'total_decisions', 'learning_rate',
        'hours_invested', 'domain_portfolio_score', 'domain_recognition_score',
        'domain_credentials_score', 'adaptive_cognitive_flexibility',
        'adaptive_social_emotional', 'adaptive_strategic_career'
    ]
    # Add generic skill columns
    for i in range(10):
        expected_cols.append(f'skill_{chr(ord("a") + i)}')
    # Add derived columns, including the new safe columns
    expected_cols.extend(['errors_caught_norm', 'trust_decisions_norm', 'output_quality_without_ai_safe',
                          'time_with_ai_safe', 'ai_augmented_productivity_raw', 'ai_augmented_productivity_norm'])

    assert all(col in df.columns for col in expected_cols)
    assert df['employee_id'].nunique() == 10

def test_generate_synthetic_employees_edge_cases():
    df_zero = generate_synthetic_employees(0)
    assert isinstance(df_zero, pd.DataFrame)
    assert len(df_zero) == 0
    # Ensure columns are still defined even with no rows (by checking if columns exist and are of object type for string cols)
    assert 'employee_id' in df_zero.columns
    assert 'years_experience' in df_zero.columns


    df_one = generate_synthetic_employees(1)
    assert isinstance(df_one, pd.DataFrame)
    assert len(df_one) == 1
    assert df_one['employee_id'].iloc[0] == 'EMP000'

def test_generate_synthetic_employees_value_ranges():
    df = generate_synthetic_employees(100)

    # Check normalized scores are within [0, 100]
    for col in ['errors_caught_norm', 'trust_decisions_norm', 'ai_augmented_productivity_norm']:
        assert df[col].min() >= 0
        assert df[col].max() <= 100
        assert not df[col].isnull().any() # No NaNs

    # Check raw scores for typical ranges
    assert df['years_experience'].min() >= 0
    assert df['years_experience'].max() < 20
    assert df['prompting_score'].min() >= 30
    assert df['prompting_score'].max() <= 95 # max possible for randint(30, 95) is 94

    # Check ratios are positive (should be for the original values, before potential divisions by zero)
    assert (df['output_quality_with_ai'] > 0).all()
    assert (df['output_quality_without_ai'] > 0).all()
    assert (df['time_without_ai'] > 0).all()
    assert (df['time_with_ai'] > 0).all()

    # Test division by zero handling in normalized scores by ensuring finite results
    assert np.isfinite(df['errors_caught_norm']).all()
    assert np.isfinite(df['trust_decisions_norm']).all()
    assert np.isfinite(df['ai_augmented_productivity_norm']).all()


def test_generate_synthetic_occupations_structure():
    df = generate_synthetic_occupations()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5 # Fixed number of occupations

    expected_cols = [
        'occupation', 'ai_enhancement_potential', 'projected_jobs_t', 'projected_jobs_t_plus_10',
        'ai_skilled_wage', 'median_wage', 'education_years_required', 'experience_years_required',
        'remote_work_factor', 'job_postings_current_month', 'job_postings_prev_month',
        'national_avg_demand'
    ]
    # Add generic skill and importance columns
    for i in range(10):
        expected_cols.append(f'required_skill_{chr(ord("a") + i)}')
        expected_cols.append(f'skill_{chr(ord("a") + i)}_importance')

    assert all(col in df.columns for col in expected_cols)
    assert df['occupation'].nunique() == 5

def test_generate_synthetic_occupations_value_ranges():
    df = generate_synthetic_occupations()

    assert df['ai_enhancement_potential'].min() >= 50
    assert df['ai_enhancement_potential'].max() <= 90
    assert (df['projected_jobs_t'] > 0).all()
    assert (df['ai_skilled_wage'] > df['median_wage']).all() # AI-skilled wage should be higher
    assert (df['education_years_required'] > 0).all()
    assert (df['experience_years_required'] >= 0).all()
    assert df['remote_work_factor'].min() >= 0.5
    assert df['remote_work_factor'].max() <= 0.9

    for i in range(10):
        assert df[f'required_skill_{chr(ord("a") + i)}'].min() >= 30
        assert df[f'required_skill_{chr(ord("a") + i)}'].max() <= 90
        assert df[f'skill_{chr(ord("a") + i)}_importance'].min() >= 0.1
        assert df[f'skill_{chr(ord("a") + i)}_importance'].max() <= 1.0


def test_generate_synthetic_pathways_structure():
    df = generate_synthetic_pathways()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5 # Fixed number of pathways

    expected_cols = [
        'pathway_id', 'pathway_name', 'pathway_type', 'cost', 'time_hours',
        'delta_ai_fluency', 'delta_domain_expertise', 'delta_adaptive_capacity'
    ]
    assert all(col in df.columns for col in expected_cols)
    assert df['pathway_id'].nunique() == 5
    assert df['pathway_name'].nunique() == 5

def test_generate_synthetic_pathways_value_ranges():
    df = generate_synthetic_pathways()

    assert (df['cost'] >= 0).all()
    assert (df['time_hours'] >= 0).all()
    assert (df['delta_ai_fluency'] > 0).all()
    assert (df['delta_domain_expertise'] > 0).all()
    assert (df['delta_adaptive_capacity'] > 0).all()
# Call the data generation functions to create the DataFrames
df_employees = generate_synthetic_employees(num_employees=50)
df_occupations = generate_synthetic_occupations()
df_pathways = generate_synthetic_pathways()

# Display the .head() of each DataFrame
print("df_employees.head():")
print(df_employees.head())
print("\ndf_occupations.head():")
print(df_occupations.head())
print("\ndf_pathways.head():")
print(df_pathways.head())

# Print the PARAMS dictionary
print("\nGlobal PARAMS dictionary:")
print(PARAMS)
def calculate_ai_enhancement(occupation_data_row):
    """Computes AI-Enhancement Potential for a given occupation."""
    # Directly extract the pre-aggregated ai_enhancement_potential
    return occupation_data_row['ai_enhancement_potential']

# Test the function immediately
example_occupation = df_occupations.iloc[0]
print(f"Test AI-Enhancement Potential for {example_occupation['occupation']}: {calculate_ai_enhancement(example_occupation):.2f}")
def calculate_job_growth_normalized(occupation_data_row):
    """Computes normalized job growth projection for an occupation."""
    current_jobs = occupation_data_row['projected_jobs_t']
    projected_jobs_10_years = occupation_data_row['projected_jobs_t_plus_10']

    if current_jobs == 0:
        return 0 # Handle division by zero

    raw_growth_rate = (projected_jobs_10_years - current_jobs) / current_jobs

    # Normalize to [0, 100] using the affine transformation
    # Growth rate range for normalization: g \in [-0.5, 1.5]
    # -0.5 maps to 0, 1.5 maps to 100.
    normalized_growth = np.clip(((raw_growth_rate + 0.5) / 2.0) * 100, 0, 100)

    return raw_growth_rate, normalized_growth

# Test the function immediately
example_occupation = df_occupations.iloc[0]
raw_growth, normalized_growth = calculate_job_growth_normalized(example_occupation)
print(f"Test Job Growth for {example_occupation['occupation']}: Raw={raw_growth:.2%}, Normalized={normalized_growth:.2f}")
import pandas as pd
import numpy as np
import pytest
import random

# Re-defining the functions as per the requirement for self-contained tests.
# The previous SyntaxError was resolved by changing single quotes 'a' to double quotes "a" in f-strings.
# This correction is applied here as well in helper functions used by tests.

def generate_synthetic_employees(num_employees=50):
    employee_data = {
        'employee_id': [f'EMP{i:03d}' for i in range(num_employees)],
        'job_role': random.choices(['Data Scientist', 'ML Engineer', 'AI Ethicist', 'Business Analyst', 'HR Specialist'], k=num_employees),
        'department': random.choices(['R&D', 'Engineering', 'HR', 'Marketing', 'Finance'], k=num_employees),
        'years_experience': np.random.randint(0, 20, num_employees),
        'education_level': random.choices(['HS+Coursework', 'Associate\'s/Certificate', 'Bachelor\'s', 'Master\'s', 'PhD'], k=num_employees),
        'prompting_score': np.random.randint(30, 95, num_employees),
        'tools_score': np.random.randint(20, 90, num_employees),
        'understanding_score': np.random.randint(40, 95, num_employees),
        'data_lit_score': np.random.randint(35, 90, num_employees),
        'output_quality_with_ai': np.random.uniform(0.7, 1.2, num_employees), # Relative to without AI
        'output_quality_without_ai': np.random.uniform(0.5, 1.0, num_employees),
        'time_without_ai': np.random.uniform(1.0, 1.5, num_employees), # Relative to with AI
        'time_with_ai': np.random.uniform(0.7, 1.0, num_employees),
        'errors_caught': np.random.randint(5, 20, num_employees),
        'total_ai_errors': np.random.randint(15, 30, num_employees),
        'appropriate_trust_decisions': np.random.randint(10, 25, num_employees),
        'total_decisions': np.random.randint(20, 35, num_employees),
        'learning_rate': np.random.uniform(0.05, 0.25, num_employees),
        'hours_invested': np.random.randint(50, 500, num_employees),
        'domain_portfolio_score': np.random.randint(20, 90, num_employees),
        'domain_recognition_score': np.random.randint(10, 80, num_employees),
        'domain_credentials_score': np.random.randint(30, 95, num_employees),
        'adaptive_cognitive_flexibility': np.random.randint(40, 95, num_employees),
        'adaptive_social_emotional': np.random.randint(30, 90, num_employees),
        'adaptive_strategic_career': np.random.randint(35, 95, num_employees)
    }
    # Add generic skills for skill match
    for i in range(10):
        employee_data[f'skill_{chr(ord("a") + i)}'] = np.random.randint(0, 100, num_employees)

    df = pd.DataFrame(employee_data)

    # Normalize scores to 0-100 where applicable (these are raw inputs)
    # Handle division by zero gracefully, though with randint ranges, it's unlikely total_ai_errors/total_decisions are 0
    df['errors_caught_norm'] = (df['errors_caught'] / df['total_ai_errors'] * 100).fillna(0)
    df['trust_decisions_norm'] = (df['appropriate_trust_decisions'] / df['total_decisions'] * 100).fillna(0)

    # Ensure no division by zero for output_quality_without_ai and time_with_ai
    df['output_quality_without_ai_safe'] = df['output_quality_without_ai'].replace(0, np.nan)
    df['time_with_ai_safe'] = df['time_with_ai'].replace(0, np.nan)

    df['ai_augmented_productivity_raw'] = (df['output_quality_with_ai'] / df['output_quality_without_ai_safe']) * \
                                         (df['time_without_ai'] / df['time_with_ai_safe'])
    df['ai_augmented_productivity_raw'] = df['ai_augmented_productivity_raw'].fillna(0) # Fill NaN if division by zero occurred

    df['ai_augmented_productivity_norm'] = np.clip(df['ai_augmented_productivity_raw'] * 50, 0, 100) # Scale and clip for initial S_i2

    return df

def generate_synthetic_occupations():
    occupation_data = {
        'occupation': ['Data Scientist', 'ML Engineer', 'AI Ethicist', 'Business Analyst', 'HR Specialist'],
        'ai_enhancement_potential': [85, 90, 75, 60, 50],
        'projected_jobs_t': [5000, 4000, 1000, 15000, 12000],
        'projected_jobs_t_plus_10': [8000, 7500, 2000, 16000, 11000],
        'ai_skilled_wage': [140000, 150000, 120000, 90000, 80000],
        'median_wage': [110000, 120000, 100000, 75000, 65000],
        'education_years_required': [18, 18, 16, 16, 14],
        'experience_years_required': [3, 4, 2, 2, 1],
        'remote_work_factor': [0.8, 0.9, 0.7, 0.6, 0.5],
        'job_postings_current_month': [120, 110, 40, 80, 70],
        'job_postings_prev_month': [100, 100, 35, 85, 75],
        'national_avg_demand': [100, 100, 100, 100, 100]
    }
    # Add required skills and importance
    for i in range(10):
        occupation_data[f'required_skill_{chr(ord("a") + i)}'] = np.random.randint(30, 90, len(occupation_data['occupation']))
        occupation_data[f'skill_{chr(ord("a") + i)}_importance'] = np.random.uniform(0.1, 1.0, len(occupation_data['occupation']))

    return pd.DataFrame(occupation_data)

def generate_synthetic_pathways():
    pathway_data = {
        'pathway_id': [f'PATH{i:02d}' for i in range(1, 6)],
        'pathway_name': ['AI Fundamentals Course', 'Advanced ML Specialization', 'AI Ethics & Governance', 'Data Storytelling with AI', 'HR Analytics with AI'],
        'pathway_type': ['Online Course', 'Certification', 'Workshop', 'Online Course', 'Certification'],
        'cost': [500, 2000, 1000, 300, 750],
        'time_hours': [40, 160, 80, 30, 60],
        'delta_ai_fluency': [10, 25, 5, 3, 5],
        'delta_domain_expertise': [5, 10, 15, 8, 12],
        'delta_adaptive_capacity': [5, 5, 10, 7, 8]
    }
    return pd.DataFrame(pathway_data)


def calculate_wage_premium(occupation_data_row):
    """Computes wage premium for an occupation."""
    ai_skilled_wage = occupation_data_row['ai_skilled_wage']
    median_wage = occupation_data_row['median_wage']

    if median_wage == 0:
        return 0

    wage_premium = (ai_skilled_wage - median_wage) / median_wage
    # Normalize to a 0-100 scale; assuming typical premiums are between -0.2 and 0.5
    return np.clip(((wage_premium + 0.2) / 0.7) * 100, 0, 100)

def calculate_entry_accessibility(occupation_data_row):
    """Computes entry accessibility for an occupation."""
    education_years_required = occupation_data_row['education_years_required']
    experience_years_required = occupation_data_row['experience_years_required']

    # Using the formula: 1 - (total_years / 10) for a simpler range adjustment
    access_score = 1 - ((education_years_required + experience_years_required) / 10)
    return np.clip(access_score * 100, 0, 100)


# Pytest unit tests
class TestHRRComponents:

    # --- Tests for calculate_wage_premium ---
    @pytest.mark.parametrize("ai_skilled_wage, median_wage, expected_premium", [
        (150000, 100000, 100.0),
        (100000, 100000, 28.57142857142857),
        (80000, 100000, 0.0),
        (70000, 100000, 0.0),
        (200000, 100000, 100.0),
        (0, 100000, 0.0),
        (100000, 0, 0.0),
        (0, 0, 0.0)
    ])
    def test_calculate_wage_premium(self, ai_skilled_wage, median_wage, expected_premium):
        occupation_data = pd.Series({
            'ai_skilled_wage': ai_skilled_wage,
            'median_wage': median_wage
        })
        result = calculate_wage_premium(occupation_data)
        assert isinstance(result, (float, np.floating))
        # Use np.isclose for float comparisons
        assert np.isclose(result, expected_premium)
        assert 0 <= result <= 100

    # --- Tests for calculate_entry_accessibility ---
    @pytest.mark.parametrize("education_years, experience_years, expected_accessibility", [
        (18, 3, 0.0),  # (1 - (21 / 10)) * 100 = -110, clipped to 0
        (12, 0, 0.0),  # (1 - (12 / 10)) * 100 = -20, clipped to 0
        (0, 0, 100.0), # (1 - (0 / 10)) * 100 = 100
        (10, 0, 0.0),  # (1 - (10 / 10)) * 100 = 0
        (8, 1, 10.0),  # (1 - (9 / 10)) * 100 = 10
        (1, 1, 80.0),  # (1 - (2 / 10)) * 100 = 80
        (25, 5, 0.0),  # (1 - (30 / 10)) * 100 = -200, clipped to 0
        (14, 1, 0.0),  # HR Specialist example: (1 - 1.5) * 100 = -50, clipped to 0
        (5, 0, 50.0),  # (1 - (5 / 10)) * 100 = 50
        (0, 5, 50.0),  # (1 - (5 / 10)) * 100 = 50
    ])
    def test_calculate_entry_accessibility(self, education_years, experience_years, expected_accessibility):
        occupation_data = pd.Series({
            'education_years_required': education_years,
            'experience_years_required': experience_years
        })
        result = calculate_entry_accessibility(occupation_data)
        assert isinstance(result, (float, np.floating))
        assert np.isclose(result, expected_accessibility)
        assert 0 <= result <= 100
def calculate_base_opportunity_score(occupation_data_row, weights):
    """Aggregates sub-components into H_base."""
    ai_enhancement = calculate_ai_enhancement(occupation_data_row)
    _, job_growth_normalized = calculate_job_growth_normalized(occupation_data_row)
    wage_premium = calculate_wage_premium(occupation_data_row)
    entry_accessibility = calculate_entry_accessibility(occupation_data_row)

    h_base = (
        weights['ai_enhancement_weight'] * ai_enhancement +
        weights['job_growth_weight'] * job_growth_normalized +
        weights['wage_premium_weight'] * wage_premium +
        weights['entry_accessibility_weight'] * entry_accessibility
    )
    return np.clip(h_base, 0, 100)

# Test the function immediately
example_occupation = df_occupations.iloc[0]
h_base_score = calculate_base_opportunity_score(example_occupation, PARAMS['hr_base_weights'])
print(f"Test Base Opportunity Score for {example_occupation['occupation']}: {h_base_score:.2f}")
# Update df_occupations with the base_opportunity_score for all occupations
df_occupations['base_opportunity_score'] = df_occupations.apply(lambda row: calculate_base_opportunity_score(row, PARAMS['hr_base_weights']), axis=1)

print("df_occupations with 'base_opportunity_score':")
print(df_occupations[['occupation', 'base_opportunity_score']].head())
def calculate_growth_multiplier(occupation_data_row, lambda_val):
    """Computes market momentum growth multiplier."""
    current_postings = occupation_data_row['job_postings_current_month']
    prev_postings = occupation_data_row['job_postings_prev_month']

    if prev_postings == 0:
        return 1.0 # No change if no previous data

    change_factor = (current_postings / prev_postings) - 1
    multiplier = 1 + (lambda_val * change_factor)
    return np.clip(multiplier, 0.7, 1.3) # Clamp to reasonable range

def calculate_regional_multiplier(occupation_data_row, gamma_val):
    """Computes regional demand multiplier."""
    # For simplicity, assume Local Demand equals National Avg Demand (ratio of 1.0) unless specified.
    local_to_national_ratio = occupation_data_row.get('local_demand_ratio', 1.0)
    remote_work_factor = occupation_data_row['remote_work_factor']

    multiplier = local_to_national_ratio * (1 + (gamma_val * remote_work_factor))
    return np.clip(multiplier, 0.8, 1.2) # Clamp to reasonable range

# Test the functions immediately
example_occupation = df_occupations.iloc[0]
growth_mult = calculate_growth_multiplier(example_occupation, PARAMS['lambda_growth'])
regional_mult = calculate_regional_multiplier(example_occupation, PARAMS['gamma_regional'])
print(f"Test Growth Multiplier for {example_occupation['occupation']}: {growth_mult:.2f}")
print(f"Test Regional Multiplier for {example_occupation['occupation']}: {regional_mult:.2f}")
# Update df_occupations with growth_multiplier and regional_multiplier for all occupations
df_occupations['growth_multiplier'] = df_occupations.apply(lambda row: calculate_growth_multiplier(row, PARAMS['lambda_growth']), axis=1)
df_occupations['regional_multiplier'] = df_occupations.apply(lambda row: calculate_regional_multiplier(row, PARAMS['gamma_regional']), axis=1)

print("df_occupations with 'growth_multiplier' and 'regional_multiplier':")
print(df_occupations[['occupation', 'growth_multiplier', 'regional_multiplier']].head())
def calculate_systematic_opportunity(occupation_data_row):
    """Computes total HR^R for a target occupation."""
    base_score = occupation_data_row['base_opportunity_score']
    growth_mult = occupation_data_row['growth_multiplier']
    regional_mult = occupation_data_row['regional_multiplier']

    hr_r = base_score * growth_mult * regional_mult
    return np.clip(hr_r, 0, 100)

# Test the function immediately (using a merged row for simplicity in test)
example_employee_job = df_employees.iloc[0]['job_role']
example_hr_row = df_occupations[df_occupations['occupation'] == example_employee_job].iloc[0]
example_hr_r = calculate_systematic_opportunity(example_hr_row)
print(f"Test HR^R score for {example_employee_job}: {example_hr_r:.2f}")
# Iterate through df_employees to calculate HR^R scores
df_employees['hr_r_score'] = df_employees['job_role'].apply(
    lambda job_role:
        calculate_systematic_opportunity(df_occupations[df_occupations['occupation'] == job_role].iloc[0])
)

print("df_employees with newly calculated 'hr_r_score':")
print(df_employees[['employee_id', 'job_role', 'hr_r_score']].head())
import pandas as pd
import numpy as np
import pytest
import random

# Define default parameters for \alpha and \beta (from Cell 5)
# This PARAMS dictionary is crucial for the functions to be tested and their dependencies
PARAMS = {
    'alpha': 0.6,
    'beta': 0.15,
    'lambda_growth': 0.3,
    'gamma_regional': 0.2,
    'hr_base_weights': {
        'ai_enhancement_weight': 0.30,
        'job_growth_weight': 0.30,
        'wage_premium_weight': 0.25,
        'entry_accessibility_weight': 0.15
    },
    'theta_ai_fluency_weights': {
        'technical_ai_skills_weight': 0.30,
        'ai_augmented_productivity_weight': 0.35,
        'critical_ai_judgment_weight': 0.20,
        'ai_learning_velocity_weight': 0.15
    },
    'gamma_experience_decay': 0.15,
    'domain_specialization_weights': {
        'portfolio_weight': 0.4,
        'recognition_weight': 0.3,
        'credentials_weight': 0.3
    },
    'vr_component_weights': {
        'ai_fluency_weight_vr': 0.45,
        'domain_expertise_weight_vr': 0.35,
        'adaptive_capacity_weight_vr': 0.20
    }
}

# The functions to be tested (redefined for self-containment in unit tests)
def calculate_technical_ai_skills(employee_data_row):
    """Computes S_i,1 (Technical AI Skills)."""
    scores = [
        employee_data_row['prompting_score'],
        employee_data_row['tools_score'],
        employee_data_row['understanding_score'],
        employee_data_row['data_lit_score']
    ]
    return np.mean(scores)

def calculate_ai_augmented_productivity(employee_data_row):
    """Computes S_i,2 (AI-Augmented Productivity)."""
    return employee_data_row['ai_augmented_productivity_norm']

def calculate_critical_ai_judgment(employee_data_row):
    """Computes S_i,3 (Critical AI Judgment)."""
    errors_caught_score = employee_data_row['errors_caught_norm']
    trust_decisions_score = employee_data_row['trust_decisions_norm']
    return np.mean([errors_caught_score, trust_decisions_score])

def calculate_ai_learning_velocity(employee_data_row):
    """Computes S_i,4 (AI Learning Velocity)."""
    learning_rate = employee_data_row['learning_rate']
    return np.clip(learning_rate * 100 * 0.8, 0, 100)

def calculate_ai_fluency(employee_data_row, theta_weights):
    """Aggregates S_i,k into AI-Fluency."""
    s1 = calculate_technical_ai_skills(employee_data_row)
    s2 = calculate_ai_augmented_productivity(employee_data_row)
    s3 = calculate_critical_ai_judgment(employee_data_row)
    s4 = calculate_ai_learning_velocity(employee_data_row)

    ai_fluency = (
        theta_weights['technical_ai_skills_weight'] * s1 +
        theta_weights['ai_augmented_productivity_weight'] * s2 +
        theta_weights['critical_ai_judgment_weight'] * s3 +
        theta_weights['ai_learning_velocity_weight'] * s4
    )
    return np.clip(ai_fluency, 0, 100)

# Pytest unit tests
class TestAIFluencyComponents:

    # Fixture to provide sample employee data row for consistent testing
    @pytest.fixture
    def sample_employee_data_row(self):
        # Create a pandas Series with all required keys and sample values
        return pd.Series({
            'prompting_score': 80,
            'tools_score': 70,
            'understanding_score': 90,
            'data_lit_score': 75,
            'ai_augmented_productivity_norm': 85,
            'errors_caught_norm': 70,
            'trust_decisions_norm': 80,
            'learning_rate': 0.20,
            'hours_invested': 200 # Not directly used in current S4 calculation, but part of context
        })

    @pytest.fixture
    def sample_theta_weights(self):
        return PARAMS['theta_ai_fluency_weights']

    # --- Tests for calculate_technical_ai_skills ---
    def test_calculate_technical_ai_skills_typical(self, sample_employee_data_row):
        expected_s1 = (80 + 70 + 90 + 75) / 4
        assert np.isclose(calculate_technical_ai_skills(sample_employee_data_row), expected_s1)

    def test_calculate_technical_ai_skills_edge_min(self):
        employee_data = pd.Series({
            'prompting_score': 0, 'tools_score': 0, 'understanding_score': 0, 'data_lit_score': 0
        })
        assert np.isclose(calculate_technical_ai_skills(employee_data), 0)

    def test_calculate_technical_ai_skills_edge_max(self):
        employee_data = pd.Series({
            'prompting_score': 100, 'tools_score': 100, 'understanding_score': 100, 'data_lit_score': 100
        })
        assert np.isclose(calculate_technical_ai_skills(employee_data), 100)

    # --- Tests for calculate_ai_augmented_productivity ---
    def test_calculate_ai_augmented_productivity_typical(self, sample_employee_data_row):
        assert np.isclose(calculate_ai_augmented_productivity(sample_employee_data_row), 85)

    def test_calculate_ai_augmented_productivity_edge_min_max(self):
        employee_data_min = pd.Series({'ai_augmented_productivity_norm': 0})
        employee_data_max = pd.Series({'ai_augmented_productivity_norm': 100})
        assert np.isclose(calculate_ai_augmented_productivity(employee_data_min), 0)
        assert np.isclose(calculate_ai_augmented_productivity(employee_data_max), 100)

    # --- Tests for calculate_critical_ai_judgment ---
    def test_calculate_critical_ai_judgment_typical(self, sample_employee_data_row):
        expected_s3 = (70 + 80) / 2
        assert np.isclose(calculate_critical_ai_judgment(sample_employee_data_row), expected_s3)

    def test_calculate_critical_ai_judgment_edge_min(self):
        employee_data = pd.Series({'errors_caught_norm': 0, 'trust_decisions_norm': 0})
        assert np.isclose(calculate_critical_ai_judgment(employee_data), 0)

    def test_calculate_critical_ai_judgment_edge_max(self):
        employee_data = pd.Series({'errors_caught_norm': 100, 'trust_decisions_norm': 100})
        assert np.isclose(calculate_critical_ai_judgment(employee_data), 100)

    # --- Tests for calculate_ai_learning_velocity ---
    def test_calculate_ai_learning_velocity_typical(self, sample_employee_data_row):
        expected_s4 = np.clip(0.20 * 100 * 0.8, 0, 100)
        assert np.isclose(calculate_ai_learning_velocity(sample_employee_data_row), expected_s4)

    def test_calculate_ai_learning_velocity_edge_min(self):
        employee_data = pd.Series({'learning_rate': 0.0})
        assert np.isclose(calculate_ai_learning_velocity(employee_data), 0)

    def test_calculate_ai_learning_velocity_edge_max_clip(self):
        employee_data = pd.Series({'learning_rate': 1.0}) # A learning rate that results in score 80
        expected_s4 = np.clip(1.0 * 100 * 0.8, 0, 100)
        assert np.isclose(calculate_ai_learning_velocity(employee_data), expected_s4)

        employee_data_over_clip = pd.Series({'learning_rate': 1.5}) # Value that should clip to 100
        assert np.isclose(calculate_ai_learning_velocity(employee_data_over_clip), 100)


    # --- Tests for calculate_ai_fluency ---
    def test_calculate_ai_fluency_typical(self, sample_employee_data_row, sample_theta_weights):
        s1 = calculate_technical_ai_skills(sample_employee_data_row)
        s2 = calculate_ai_augmented_productivity(sample_employee_data_row)
        s3 = calculate_critical_ai_judgment(sample_employee_data_row)
        s4 = calculate_ai_learning_velocity(sample_employee_data_row)

        expected_ai_fluency = (
            sample_theta_weights['technical_ai_skills_weight'] * s1 +
            sample_theta_weights['ai_augmented_productivity_weight'] * s2 +
            sample_theta_weights['critical_ai_judgment_weight'] * s3 +
            sample_theta_weights['ai_learning_velocity_weight'] * s4
        )
        assert np.isclose(calculate_ai_fluency(sample_employee_data_row, sample_theta_weights), np.clip(expected_ai_fluency, 0, 100))
        assert 0 <= calculate_ai_fluency(sample_employee_data_row, sample_theta_weights) <= 100

    def test_calculate_ai_fluency_edge_all_zero(self, sample_theta_weights):
        employee_data = pd.Series({
            'prompting_score': 0, 'tools_score': 0, 'understanding_score': 0, 'data_lit_score': 0,
            'ai_augmented_productivity_norm': 0, 'errors_caught_norm': 0, 'trust_decisions_norm': 0,
            'learning_rate': 0.0
        })
        assert np.isclose(calculate_ai_fluency(employee_data, sample_theta_weights), 0)

    def test_calculate_ai_fluency_edge_all_max_scores_within_clip(self, sample_theta_weights):
        # Create an employee with max values for sub-components, checking if total clips to 100
        employee_data = pd.Series({
            'prompting_score': 100, 'tools_score': 100, 'understanding_score': 100, 'data_lit_score': 100,
            'ai_augmented_productivity_norm': 100,
            'errors_caught_norm': 100, 'trust_decisions_norm': 100,
            'learning_rate': 1.0 # S4 will be 80, not 100
        })
        s1_val = 100.0
        s2_val = 100.0
        s3_val = 100.0
        s4_val = 80.0 # From np.clip(1.0 * 100 * 0.8, 0, 100)

        expected_ai_fluency = (
            sample_theta_weights['technical_ai_skills_weight'] * s1_val +
            sample_theta_weights['ai_augmented_productivity_weight'] * s2_val +
            sample_theta_weights['critical_ai_judgment_weight'] * s3_val +
            sample_theta_weights['ai_learning_velocity_weight'] * s4_val
        )
        # Check if the calculated value is correctly clipped if it exceeds 100, or within bounds otherwise
        assert np.isclose(calculate_ai_fluency(employee_data, sample_theta_weights), np.clip(expected_ai_fluency, 0, 100))
        assert calculate_ai_fluency(employee_data, sample_theta_weights) <= 100
# Update df_employees with the calculated ai_fluency_score for all employees
df_employees['ai_fluency_score'] = df_employees.apply(
    lambda row: calculate_ai_fluency(row, PARAMS['theta_ai_fluency_weights']),
    axis=1
)

print("df_employees with newly calculated 'ai_fluency_score':")
print(df_employees[['employee_id', 'job_role', 'ai_fluency_score']].head())
def calculate_educational_foundation(employee_data_row):
    """Computes E_education based on education level."""
    education_map = {
        'HS+Coursework': 0.50,
        'Associate\'s/Certificate': 0.60,
        'Bachelor\'s': 0.70,
        'Master\'s': 0.85,
        'PhD': 1.0
    }
    return education_map.get(employee_data_row['education_level'], 0.50) * 100 # Scale to 0-100

def calculate_practical_experience(employee_data_row, gamma_exp):
    """Computes E_experience with diminishing returns."""
    years = employee_data_row['years_experience']
    experience_score = 1 - np.exp(-gamma_exp * years)
    return np.clip(experience_score * 100, 0, 100)

def calculate_specialization_depth(employee_data_row, weights):
    """Computes E_specialization based on portfolio, recognition, and credentials."""
    portfolio_score = employee_data_row['domain_portfolio_score']
    recognition_score = employee_data_row['domain_recognition_score']
    credentials_score = employee_data_row['domain_credentials_score']

    specialization_depth = (
        weights['portfolio_weight'] * portfolio_score +
        weights['recognition_weight'] * recognition_score +
        weights['credentials_weight'] * credentials_score
    )
    return np.clip(specialization_depth, 0, 100)

def calculate_domain_expertise(employee_data_row, gamma_exp, domain_weights):
    """Aggregates the three sub-factors into Domain-Expertise."""
    e_education = calculate_educational_foundation(employee_data_row) / 100 # Back to 0-1 for multiplication
    e_experience = calculate_practical_experience(employee_data_row, gamma_exp) / 100 # Back to 0-1
    e_specialization = calculate_specialization_depth(employee_data_row, domain_weights) / 100 # Back to 0-1

    domain_expertise = e_education * e_experience * e_specialization
    return np.clip(domain_expertise * 100, 0, 100) # Final score 0-100

# Test the functions immediately with an example employee
example_employee = df_employees.iloc[0]
education_score = calculate_educational_foundation(example_employee)
experience_score = calculate_practical_experience(example_employee, PARAMS['gamma_experience_decay'])
specialization_score = calculate_specialization_depth(example_employee, PARAMS['domain_specialization_weights'])
domain_expertise_score = calculate_domain_expertise(example_employee, PARAMS['gamma_experience_decay'], PARAMS['domain_specialization_weights'])

print(f"Test E_education for EMP000: {education_score:.2f}")
print(f"Test E_experience for EMP000: {experience_score:.2f}")
print(f"Test E_specialization for EMP000: {specialization_score:.2f}")
print(f"Test Domain-Expertise score for EMP000: {domain_expertise_score:.2f}")
# Update df_employees with the calculated domain_expertise_score for all employees
df_employees['domain_expertise_score'] = df_employees.apply(
    lambda row: calculate_domain_expertise(row, PARAMS['gamma_experience_decay'], PARAMS['domain_specialization_weights']),
    axis=1
)

print("df_employees with newly calculated 'domain_expertise_score':")
print(df_employees[['employee_id', 'job_role', 'domain_expertise_score']].head())
def calculate_adaptive_capacity(employee_data_row):
    """Computes Adaptive-Capacity as an average of three meta-skills."""
    c_cognitive = employee_data_row['adaptive_cognitive_flexibility']
    c_social = employee_data_row['adaptive_social_emotional']
    c_strategic = employee_data_row['adaptive_strategic_career']

    adaptive_capacity = np.mean([c_cognitive, c_social, c_strategic])
    return np.clip(adaptive_capacity, 0, 100)

# Test the function immediately with an example employee
example_employee = df_employees.iloc[0]
adaptive_capacity_score = calculate_adaptive_capacity(example_employee)
print(f"Test Adaptive-Capacity score for EMP000: {adaptive_capacity_score:.2f}")
# Update df_employees with the calculated adaptive_capacity_score for all employees
df_employees['adaptive_capacity_score'] = df_employees.apply(
    calculate_adaptive_capacity, axis=1
)

print("df_employees with newly calculated 'adaptive_capacity_score':")
print(df_employees[['employee_id', 'job_role', 'adaptive_capacity_score']].head())
def calculate_idiosyncratic_readiness(employee_data_row, vr_weights):
    """Computes total V^R score from its sub-components."""
    ai_fluency = employee_data_row['ai_fluency_score']
    domain_expertise = employee_data_row['domain_expertise_score']
    adaptive_capacity = employee_data_row['adaptive_capacity_score']

    vr_score = (
        vr_weights['ai_fluency_weight_vr'] * ai_fluency +
        vr_weights['domain_expertise_weight_vr'] * domain_expertise +
        vr_weights['adaptive_capacity_weight_vr'] * adaptive_capacity
    )
    return np.clip(vr_score, 0, 100)

# Test the function immediately with an example employee
example_employee = df_employees.iloc[0]
vr_score_test = calculate_idiosyncratic_readiness(example_employee, PARAMS['vr_component_weights'])
print(f"Test V^R score for EMP000: {vr_score_test:.2f}")
# Update df_employees with the calculated vr_score for all employees
df_employees['vr_score'] = df_employees.apply(
    lambda row: calculate_idiosyncratic_readiness(row, PARAMS['vr_component_weights']),
    axis=1
)

print("df_employees with newly calculated 'vr_score':")
print(df_employees[['employee_id', 'job_role', 'vr_score']].head())
def calculate_skills_match_score(employee_skills_series, required_skills_series, skill_importance_series):
    """Computes a skills match score between an employee and a job role."""
    match_score = 0
    skill_cols = [f'skill_{chr(ord("a") + i)}' for i in range(10)]

    for skill_col in skill_cols:
        # Ensure required_skills_series and skill_importance_series are properly aligned
        # In df_occupations, skill importance is `skill_X_importance` and required skills is `required_skill_X`
        required_skill_val = required_skills_series[f'required_{skill_col}']
        skill_importance_val = skill_importance_series[f'{skill_col}_importance']
        individual_skill_val = employee_skills_series[skill_col]

        # Max possible individual skill is 100, so normalize to 0-1 before min operation
        # then multiply by 100 for a final score of 0-100
        match_score += min(individual_skill_val / 100, required_skill_val / 100) * skill_importance_val

    # Normalize the total match_score by the sum of importance weights to get a score 0-1, then scale to 0-100
    total_importance = skill_importance_series[[f'skill_{chr(ord("a") + i)}_importance' for i in range(10)]].sum()
    if total_importance == 0: # Avoid division by zero if no skills defined
        return 0
    return np.clip((match_score / total_importance) * 100, 0, 100)

def calculate_timing_factor(years_experience):
    """Computes career stage timing factor."""
    if years_experience <= 5:
        return 1.0
    elif 5 < years_experience <= 15:
        return 1.0
    else: # years_experience > 15
        return 0.8

def calculate_alignment_factor(skills_match_score, timing_factor):
    """Computes alignment factor based on skills match and timing."""
    # Scale skills_match_score from 0-100 to 0-1 for multiplication
    alignment = (skills_match_score / 100) * timing_factor
    return np.clip(alignment, 0, 1)

# Test the functions immediately with an example employee and their job role
example_employee = df_employees.iloc[0]
example_occupation_row = df_occupations[df_occupations['occupation'] == example_employee['job_role']].iloc[0]

# Extract employee skills for the calculation
employee_skill_data = example_employee[[f'skill_{chr(ord("a") + i)}' for i in range(10)]]
# Extract required skills and importance from the occupation data row
required_skill_data = example_occupation_row[[f'required_skill_{chr(ord("a") + i)}' for i in range(10)]]
skill_importance_data = example_occupation_row[[f'skill_{chr(ord("a") + i)}_importance' for i in range(10)]]

skills_match = calculate_skills_match_score(employee_skill_data, required_skill_data, skill_importance_data)
timing_factor = calculate_timing_factor(example_employee['years_experience'])
alignment_factor = calculate_alignment_factor(skills_match, timing_factor)

print(f"Test Skills Match Score for EMP000 ({example_employee['job_role']}): {skills_match:.2f}")
print(f"Test Timing Factor for EMP000 ({example_employee['years_experience']} years exp): {timing_factor:.2f}")
print(f"Test Alignment Factor for EMP000: {alignment_factor:.2f}")
# Update df_employees with alignment_factor for all employees
def get_alignment_for_employee(employee_row):
    job_role = employee_row['job_role']
    # Ensure df_occupations is accessible in this scope (from previous cells)
    global df_occupations
    occupation_row = df_occupations[df_occupations['occupation'] == job_role].iloc[0]

    # Corrected f-string syntax from \'a\' to "a"
    employee_skill_data = employee_row[[f'skill_{chr(ord("a") + i)}' for i in range(10)]]
    required_skill_data = occupation_row[[f'required_skill_{chr(ord("a") + i)}' for i in range(10)]]
    skill_importance_data = occupation_row[[f'skill_{chr(ord("a") + i)}_importance' for i in range(10)]]

    # Ensure these functions are defined and accessible (from previous cells)
    # They should have been defined in previous cells or imported.
    # For robustness in a test environment, they would typically be imported or passed.
    # Assuming they are globally available from the notebook's execution flow.
    skills_match = calculate_skills_match_score(employee_skill_data, required_skill_data, skill_importance_data)
    timing_factor = calculate_timing_factor(employee_row['years_experience'])
    return calculate_alignment_factor(skills_match, timing_factor)

df_employees['alignment_factor'] = df_employees.apply(get_alignment_for_employee, axis=1)

print("df_employees with newly calculated 'alignment_factor':")
print(df_employees[['employee_id', 'job_role', 'alignment_factor']].head())
def calculate_synergy(vr_score, hr_score, alignment_factor):
    """Computes Synergy%."""
    # Ensure vr_score and hr_score are between 0-100
    vr_norm = vr_score / 100
    hr_norm = hr_score / 100

    synergy = (vr_norm * hr_norm) * alignment_factor
    return np.clip(synergy * 100, 0, 100)

# Test the function immediately
example_employee = df_employees.iloc[0]
synergy_score_test = calculate_synergy(
    example_employee['vr_score'],
    example_employee['hr_r_score'],
    example_employee['alignment_factor']
)
print(f"Test Synergy Score for EMP000: {synergy_score_test:.2f}")
# Update df_employees with the newly calculated synergy_score for all employees
df_employees['synergy_score'] = df_employees.apply(
    lambda row: calculate_synergy(row['vr_score'], row['hr_r_score'], row['alignment_factor']),
    axis=1
)

print("df_employees with newly calculated 'synergy_score':")
print(df_employees[['employee_id', 'job_role', 'vr_score', 'hr_r_score', 'alignment_factor', 'synergy_score']].head())
# The `calculate_ai_r` function was already defined in Section 1.
# Now, apply it to all employees in df_employees.

df_employees['current_ai_r_score'] = df_employees.apply(
    lambda row:
        calculate_ai_r(
            row['vr_score'],
            row['hr_r_score'],
            row['synergy_score'],
            PARAMS['alpha'],
            PARAMS['beta']
        ),
    axis=1
)

print("df_employees with all calculated AI-R components and final score:")
print(df_employees[['employee_id', 'job_role', 'department', 'vr_score', 'hr_r_score', 'synergy_score', 'current_ai_r_score']].head())

# Calculate and print the average AI-R score for the entire workforce
average_ai_r = df_employees['current_ai_r_score'].mean()
print(f"\nAverage AI-R score for the entire workforce: {average_ai_r:.2f}")
def generate_ai_r_report_summary(df_employees_data):
    """Aggregates AI-R scores by group (e.g., department, job role)."""
    summary_df = df_employees_data.groupby(['department', 'job_role']).agg(
        average_current_ai_r=('current_ai_r_score', 'mean'),
        average_vr_score=('vr_score', 'mean'),
        average_hr_r_score=('hr_r_score', 'mean'),
        average_synergy_score=('synergy_score', 'mean'),
        num_employees=('employee_id', 'count')
    ).reset_index()
    return summary_df.round(2)

def plot_skills_gap_heatmap(df_employees_data, group_by_column):
    """Visualizes strengths and weaknesses of V^R sub-components using a heatmap."""
    vr_sub_components = ['ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score']
    heatmap_data = df_employees_data.groupby(group_by_column)[vr_sub_components].mean()

    plt.figure(figsize=(10, 6))
    sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt=".1f", linewidths=.5)
    plt.title(f'Average V^R Sub-Component Scores by {group_by_column}')
    plt.ylabel(group_by_column)
    plt.xlabel('V^R Sub-Component')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Test the functions immediately
print("Test Summary Report:")
print(generate_ai_r_report_summary(df_employees).head())

# No plot generated during test, only for execution cell
# Generate and display the summary table
ai_r_summary_report = generate_ai_r_report_summary(df_employees)
print("Workforce AI-Readiness Summary Report by Department and Job Role:")
print(ai_r_summary_report.to_string())

# Generate the skills gap heatmap
plot_skills_gap_heatmap(df_employees, 'job_role')
plot_skills_gap_heatmap(df_employees, 'department')
import pandas as pd
import numpy as np
import pytest
import random
import matplotlib.pyplot as plt
import seaborn as sns
import copy

# --- Re-defining dependent functions for self-contained tests ---

# From Cell 4
def calculate_ai_r(vr_score, hr_score, synergy_score, alpha, beta):
    """Computes the overall AI-Readiness Score."""
    vr_score = np.clip(vr_score, 0, 100)
    hr_score = np.clip(hr_score, 0, 100)
    synergy_score = np.clip(synergy_score, 0, 100)
    ai_r = (alpha * vr_score) + ((1 - alpha) * hr_score) + (beta * synergy_score)
    return np.clip(ai_r, 0, 100)

# From Cell 45
def calculate_idiosyncratic_readiness(employee_data_row, vr_weights):
    """Computes total V^R score from its sub-components."""
    ai_fluency = employee_data_row['ai_fluency_score']
    domain_expertise = employee_data_row['domain_expertise_score']
    adaptive_capacity = employee_data_row['adaptive_capacity_score']
    vr_score = (
        vr_weights['ai_fluency_weight_vr'] * ai_fluency +
        vr_weights['domain_expertise_weight_vr'] * domain_expertise +
        vr_weights['adaptive_capacity_weight_vr'] * adaptive_capacity
    )
    return np.clip(vr_score, 0, 100)

# From Cell 53
def calculate_synergy(vr_score, hr_score, alignment_factor):
    """Computes Synergy%."""
    vr_norm = vr_score / 100
    hr_norm = hr_score / 100
    synergy = (vr_norm * hr_norm) * alignment_factor
    return np.clip(synergy * 100, 0, 100)

# The function to be tested: plot_current_vs_projected_ai_r
# This is a plotting function, per requirement #5, we return 'NO_TESTS_NEEDED' for it
# However, for completeness within the test suite structure, we keep its definition
# but do not generate explicit tests that rely on matplotlib.show().
def plot_current_vs_projected_ai_r(current_scores, projected_scores, scenario_names):
    """Compares current vs. projected AI-R for an individual or group."""
    labels = ['Current AI-R'] + [f'Projected AI-R ({s})' for s in scenario_names]
    values = [current_scores] + projected_scores

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['skyblue'] + ['lightcoral'] * len(projected_scores))
    plt.ylabel('AI-Readiness Score')
    plt.title('Current vs. Projected AI-Readiness Score')
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    # plt.show() # Comment out plt.show() for testing environments

# The main function to be tested in this cell
def simulate_pathway_impact(employee_id, pathway_id, completion_rate, mastery_score, df_employees_data, df_occupations_data, df_pathways_data, params):
    """Simulates the impact of a learning pathway on an individual's AI-R score."""
    employee_row_original = df_employees_data[df_employees_data['employee_id'] == employee_id].iloc[0]
    employee_row_sim = employee_row_original.copy(deep=True)

    pathway_info = df_pathways_data[df_pathways_data['pathway_id'] == pathway_id].iloc[0]

    # Apply impact to VR sub-components
    employee_row_sim['ai_fluency_score'] = np.clip(
        employee_row_sim['ai_fluency_score'] + pathway_info['delta_ai_fluency'] * completion_rate * mastery_score,
        0, 100
    )
    employee_row_sim['domain_expertise_score'] = np.clip(
        employee_row_sim['domain_expertise_score'] + pathway_info['delta_domain_expertise'] * completion_rate * mastery_score,
        0, 100
    )
    employee_row_sim['adaptive_capacity_score'] = np.clip(
        employee_row_sim['adaptive_capacity_score'] + pathway_info['delta_adaptive_capacity'] * completion_rate * mastery_score,
        0, 100
    )

    # Recalculate VR score
    employee_row_sim['vr_score'] = calculate_idiosyncratic_readiness(employee_row_sim, params['vr_component_weights'])

    # Recalculate Synergy (which depends on VR)
    employee_row_sim['synergy_score'] = calculate_synergy(
        employee_row_sim['vr_score'],
        employee_row_sim['hr_r_score'],
        employee_row_sim['alignment_factor']
    )

    # Recalculate overall AI-R score
    projected_ai_r = calculate_ai_r(
        employee_row_sim['vr_score'],
        employee_row_sim['hr_r_score'],
        employee_row_sim['synergy_score'],
        params['alpha'],
        params['beta']
    )

    delta_ai_r = projected_ai_r - employee_row_original['current_ai_r_score']

    return projected_ai_r, delta_ai_r, pathway_info['pathway_name']

# --- Pytest fixtures and tests ---

@pytest.fixture
def mock_params():
    """Mock PARAMS dictionary with relevant weights for testing."""
    return {
        'alpha': 0.6,
        'beta': 0.15,
        'vr_component_weights': {
            'ai_fluency_weight_vr': 0.45,
            'domain_expertise_weight_vr': 0.35,
            'adaptive_capacity_weight_vr': 0.20
        }
    }

@pytest.fixture
def mock_df_employees():
    """Mock df_employees DataFrame with necessary columns."""
    return pd.DataFrame({
        'employee_id': ['EMP001', 'EMP002'],
        'job_role': ['Data Scientist', 'HR Specialist'],
        'current_ai_r_score': [60.0, 40.0],
        'ai_fluency_score': [70.0, 30.0],
        'domain_expertise_score': [65.0, 50.0],
        'adaptive_capacity_score': [75.0, 45.0],
        'hr_r_score': [80.0, 55.0],
        'alignment_factor': [0.8, 0.6],
        'vr_score': [0.0, 0.0], # These will be recalculated or overwritten
        'synergy_score': [0.0, 0.0] # These will be recalculated or overwritten
    })

@pytest.fixture
def mock_df_occupations():
    """Mock df_occupations DataFrame (minimal for this test's needs)."""
    # This function doesn't directly use df_occupations data besides employee job_role lookup.
    return pd.DataFrame({
        'occupation': ['Data Scientist', 'HR Specialist']
    })

@pytest.fixture
def mock_df_pathways():
    """Mock df_pathways DataFrame with pathway impact coefficients."""
    return pd.DataFrame({
        'pathway_id': ['PATH01', 'PATH02'],
        'pathway_name': ['AI Fundamentals', 'Domain Deep Dive'],
        'delta_ai_fluency': [10, 2],
        'delta_domain_expertise': [5, 15],
        'delta_adaptive_capacity': [3, 5]
    })


class TestSimulatePathwayImpact:

    def test_simulate_pathway_impact_basic_full_completion(self, mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params):
        employee_id = 'EMP001'
        pathway_id = 'PATH01'
        completion_rate = 1.0
        mastery_score = 1.0

        current_employee_row = mock_df_employees[mock_df_employees['employee_id'] == employee_id].iloc[0]
        original_current_ai_r = current_employee_row['current_ai_r_score']

        pathway_info = mock_df_pathways[mock_df_pathways['pathway_id'] == pathway_id].iloc[0]

        projected_ai_r, delta_ai_r, pathway_name = simulate_pathway_impact(
            employee_id, pathway_id, completion_rate, mastery_score,
            mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params
        )

        assert pathway_name == 'AI Fundamentals'
        assert isinstance(projected_ai_r, (float, np.floating))
        assert isinstance(delta_ai_r, (float, np.floating))

        # Manually calculate expected values for verification
        expected_ai_fluency_sim = np.clip(current_employee_row['ai_fluency_score'] + pathway_info['delta_ai_fluency'], 0, 100)
        expected_domain_expertise_sim = np.clip(current_employee_row['domain_expertise_score'] + pathway_info['delta_domain_expertise'], 0, 100)
        expected_adaptive_capacity_sim = np.clip(current_employee_row['adaptive_capacity_score'] + pathway_info['delta_adaptive_capacity'], 0, 100)

        vr_weights = mock_params['vr_component_weights']
        expected_vr_sim = np.clip(
            vr_weights['ai_fluency_weight_vr'] * expected_ai_fluency_sim +
            vr_weights['domain_expertise_weight_vr'] * expected_domain_expertise_sim +
            vr_weights['adaptive_capacity_weight_vr'] * expected_adaptive_capacity_sim,
            0, 100
        )

        hr_r_score = current_employee_row['hr_r_score']
        alignment_factor = current_employee_row['alignment_factor']
        expected_synergy_sim = np.clip((expected_vr_sim / 100 * hr_r_score / 100) * alignment_factor * 100, 0, 100)

        alpha = mock_params['alpha']
        beta = mock_params['beta']
        expected_projected_ai_r = np.clip(
            (alpha * expected_vr_sim) +
            ((1 - alpha) * hr_r_score) +
            (beta * expected_synergy_sim),
            0, 100
        )

        assert np.isclose(projected_ai_r, expected_projected_ai_r)
        assert np.isclose(delta_ai_r, expected_projected_ai_r - original_current_ai_r)
        assert 0 <= projected_ai_r <= 100

    def test_simulate_pathway_impact_partial_completion(self, mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params):
        employee_id = 'EMP001'
        pathway_id = 'PATH01'
        completion_rate = 0.5
        mastery_score = 0.8

        current_employee_row = mock_df_employees[mock_df_employees['employee_id'] == employee_id].iloc[0]
        original_current_ai_r = current_employee_row['current_ai_r_score']

        pathway_info = mock_df_pathways[mock_df_pathways['pathway_id'] == pathway_id].iloc[0]

        projected_ai_r, delta_ai_r, _ = simulate_pathway_impact(
            employee_id, pathway_id, completion_rate, mastery_score,
            mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params
        )

        # Manually calculate expected values for verification
        impact_factor = completion_rate * mastery_score
        expected_ai_fluency_sim = np.clip(current_employee_row['ai_fluency_score'] + pathway_info['delta_ai_fluency'] * impact_factor, 0, 100)
        expected_domain_expertise_sim = np.clip(current_employee_row['domain_expertise_score'] + pathway_info['delta_domain_expertise'] * impact_factor, 0, 100)
        expected_adaptive_capacity_sim = np.clip(current_employee_row['adaptive_capacity_score'] + pathway_info['delta_adaptive_capacity'] * impact_factor, 0, 100)

        vr_weights = mock_params['vr_component_weights']
        expected_vr_sim = np.clip(
            vr_weights['ai_fluency_weight_vr'] * expected_ai_fluency_sim +
            vr_weights['domain_expertise_weight_vr'] * expected_domain_expertise_sim +
            vr_weights['adaptive_capacity_weight_vr'] * expected_adaptive_capacity_sim,
            0, 100
        )

        hr_r_score = current_employee_row['hr_r_score']
        alignment_factor = current_employee_row['alignment_factor']
        expected_synergy_sim = np.clip((expected_vr_sim / 100 * hr_r_score / 100) * alignment_factor * 100, 0, 100)

        alpha = mock_params['alpha']
        beta = mock_params['beta']
        expected_projected_ai_r = np.clip(
            (alpha * expected_vr_sim) +
            ((1 - alpha) * hr_r_score) +
            (beta * expected_synergy_sim),
            0, 100
        )

        assert np.isclose(projected_ai_r, expected_projected_ai_r)
        assert np.isclose(delta_ai_r, expected_projected_ai_r - original_current_ai_r)

    def test_simulate_pathway_impact_zero_impact_factors(self, mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params):
        employee_id = 'EMP001'
        pathway_id = 'PATH01'
        completion_rate = 0.0 # Zero completion
        mastery_score = 1.0

        current_employee_row = mock_df_employees[mock_df_employees['employee_id'] == employee_id].iloc[0]
        original_current_ai_r = current_employee_row['current_ai_r_score']

        projected_ai_r, delta_ai_r, _ = simulate_pathway_impact(
            employee_id, pathway_id, completion_rate, mastery_score,
            mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params
        )

        assert np.isclose(projected_ai_r, original_current_ai_r)
        assert np.isclose(delta_ai_r, 0.0)

    def test_simulate_pathway_impact_max_scores_clipping(self, mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params):
        employee_id = 'EMP001'
        pathway_id = 'PATH01' # delta_ai_fluency=10, delta_domain_expertise=5, delta_adaptive_capacity=3
        completion_rate = 1.0
        mastery_score = 1.0

        # Modify employee to have high initial scores that would exceed 100 with pathway impact
        mock_df_employees.loc[mock_df_employees['employee_id'] == employee_id, 'ai_fluency_score'] = 95
        mock_df_employees.loc[mock_df_employees['employee_id'] == employee_id, 'domain_expertise_score'] = 98
        mock_df_employees.loc[mock_df_employees['employee_id'] == employee_id, 'adaptive_capacity_score'] = 99
        mock_df_employees.loc[mock_df_employees['employee_id'] == employee_id, 'current_ai_r_score'] = 90

        current_employee_row = mock_df_employees[mock_df_employees['employee_id'] == employee_id].iloc[0]
        original_current_ai_r = current_employee_row['current_ai_r_score']

        projected_ai_r, delta_ai_r, _ = simulate_pathway_impact(
            employee_id, pathway_id, completion_rate, mastery_score,
            mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params
        )

        # Expected VR sub-components should be clipped to 100
        expected_ai_fluency_sim = 100.0 # 95 + 10 = 105 -> 100
        expected_domain_expertise_sim = 100.0 # 98 + 5 = 103 -> 100
        expected_adaptive_capacity_sim = 100.0 # 99 + 3 = 102 -> 100

        vr_weights = mock_params['vr_component_weights']
        expected_vr_sim = np.clip(
            vr_weights['ai_fluency_weight_vr'] * expected_ai_fluency_sim +
            vr_weights['domain_expertise_weight_vr'] * expected_domain_expertise_sim +
            vr_weights['adaptive_capacity_weight_vr'] * expected_adaptive_capacity_sim,
            0, 100
        )
        assert expected_vr_sim == 100.0 # Sum of weights is 1.0, so 100 * 1.0 = 100

        hr_r_score = current_employee_row['hr_r_score']
        alignment_factor = current_employee_row['alignment_factor']
        expected_synergy_sim = np.clip((expected_vr_sim / 100 * hr_r_score / 100) * alignment_factor * 100, 0, 100)

        alpha = mock_params['alpha']
        beta = mock_params['beta']
        expected_projected_ai_r = np.clip(
            (alpha * expected_vr_sim) +
            ((1 - alpha) * hr_r_score) +
            (beta * expected_synergy_sim),
            0, 100
        )

        assert np.isclose(projected_ai_r, expected_projected_ai_r)
        assert projected_ai_r <= 100 # Final AI-R should also be clipped

    def test_simulate_pathway_impact_no_employee_found(self, mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params):
        with pytest.raises(IndexError, match="single-row DataFrame"):
            simulate_pathway_impact(
                'NON_EXISTENT_EMP', 'PATH01', 1.0, 1.0,
                mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params
            )

    def test_simulate_pathway_impact_no_pathway_found(self, mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params):
        with pytest.raises(IndexError, match="single-row DataFrame"):
            simulate_pathway_impact(
                'EMP001', 'NON_EXISTENT_PATH', 1.0, 1.0,
                mock_df_employees, mock_df_occupations, mock_df_pathways, mock_params
            )
example_employee_id = df_employees['employee_id'].iloc[random.randint(0, len(df_employees)-1)]
current_ai_r = df_employees[df_employees['employee_id'] == example_employee_id]['current_ai_r_score'].iloc[0]

# Select a pathway randomly for demonstration
selected_pathway = df_pathways.sample(1).iloc[0]
selected_pathway_id = selected_pathway['pathway_id']

completion_rate = 0.9
mastery_score = 0.85

projected_ai_r, delta_ai_r, pathway_name = simulate_pathway_impact(
    example_employee_id, selected_pathway_id, completion_rate, mastery_score,
    df_employees, df_occupations, df_pathways, PARAMS
)

print(f"Simulating impact for employee {example_employee_id}:")
print(f"  Current AI-R: {current_ai_r:.2f}")
print(f"  Chosen Pathway: {pathway_name} (ID: {selected_pathway_id})")
print(f"  Completion Rate: {completion_rate}, Mastery Score: {mastery_score}")
print(f"  Projected AI-R: {projected_ai_r:.2f}")
print(f"  Change in AI-R (\u0394AI-R): {delta_ai_r:.2f}")

# Create a comparative bar chart
plot_current_vs_projected_ai_r(current_ai_r, [projected_ai_r], [pathway_name])
def optimize_pathway_sequence(employee_id, current_ai_r, available_pathways_df, T_max_hours, cost_weight_lambda, df_employees_data, df_occupations_data, params, max_steps=3):
    """Identifies optimal sequence of learning investments using a greedy approach."""
    best_pathways_sequence = []
    max_ai_r_improvement = 0
    current_time_spent = 0
    current_cost_spent = 0
    projected_ai_r = current_ai_r

    # Deep copy employee data for simulation state across steps
    simulated_employee_data = df_employees_data[df_employees_data['employee_id'] == employee_id].iloc[0].copy(deep=True)

    # Iterate for a fixed number of steps (simplified for demo)
    for step in range(max_steps):
        best_pathway_for_step = None
        best_pathway_value = -np.inf # Maximize value
        current_step_ai_r_gain = 0

        # Consider all available pathways
        for idx, pathway in available_pathways_df.iterrows():
            pathway_id = pathway['pathway_id']
            pathway_time = pathway['time_hours']
            pathway_cost = pathway['cost']

            if current_time_spent + pathway_time <= T_max_hours:
                # Simulate impact on the current simulated state of the employee
                # Create a temporary deep copy for this specific pathway simulation
                temp_employee_sim_state = simulated_employee_data.copy(deep=True)

                temp_employee_sim_state['ai_fluency_score'] = np.clip(
                    temp_employee_sim_state['ai_fluency_score'] + pathway['delta_ai_fluency'], 0, 100)
                temp_employee_sim_state['domain_expertise_score'] = np.clip(
                    temp_employee_sim_state['domain_expertise_score'] + pathway['delta_domain_expertise'], 0, 100)
                temp_employee_sim_state['adaptive_capacity_score'] = np.clip(
                    temp_employee_sim_state['adaptive_capacity_score'] + pathway['delta_adaptive_capacity'], 0, 100)

                # Recalculate VR for temp state
                temp_employee_sim_state['vr_score'] = calculate_idiosyncratic_readiness(temp_employee_sim_state, params['vr_component_weights'])

                # Recalculate Synergy (using original HR and alignment as these don't change by VR pathway)
                temp_employee_sim_state['synergy_score'] = calculate_synergy(
                    temp_employee_sim_state['vr_score'],
                    temp_employee_sim_state['hr_r_score'],
                    temp_employee_sim_state['alignment_factor']
                )

                # Recalculate overall AI-R for temp state
                temp_projected_ai_r = calculate_ai_r(
                    temp_employee_sim_state['vr_score'],
                    temp_employee_sim_state['hr_r_score'],
                    temp_employee_sim_state['synergy_score'],
                    params['alpha'],
                    params['beta']
                )

                ai_r_gain = temp_projected_ai_r - projected_ai_r

                # Define "value" metric: AI-R gain per (cost + time_cost)
                # Add a small epsilon to time to avoid division by zero
                time_cost_equivalent = pathway_time / 10 # Convert hours to a rough monetary equivalent for ratio (e.g., $10/hour)
                value = (ai_r_gain - cost_weight_lambda * pathway_cost) / (pathway_cost + time_cost_equivalent + 1e-6)

                if value > best_pathway_value:
                    best_pathway_value = value
                    best_pathway_for_step = pathway
                    current_step_ai_r_gain = ai_r_gain

        if best_pathway_for_step is None: # No pathway found that fits criteria
            break

        # Apply the best pathway found to the simulated employee state and accumulated totals
        best_pathways_sequence.append(best_pathway_for_step['pathway_name'])
        current_time_spent += best_pathway_for_step['time_hours']
        current_cost_spent += best_pathway_for_step['cost']
        projected_ai_r += current_step_ai_r_gain
        max_ai_r_improvement += current_step_ai_r_gain

        # Update the simulated_employee_data with the gains from the chosen pathway
        # This ensures subsequent steps build on the updated scores
        simulated_employee_data['ai_fluency_score'] = np.clip(
            simulated_employee_data['ai_fluency_score'] + best_pathway_for_step['delta_ai_fluency'], 0, 100)
        simulated_employee_data['domain_expertise_score'] = np.clip(
            simulated_employee_data['domain_expertise_score'] + best_pathway_for_step['delta_domain_expertise'], 0, 100)
        simulated_employee_data['adaptive_capacity_score'] = np.clip(
            simulated_employee_data['adaptive_capacity_score'] + best_pathway_for_step['delta_adaptive_capacity'], 0, 100)

    return {
        'recommended_sequence': best_pathways_sequence,
        'projected_final_ai_r': projected_ai_r,
        'total_cost': current_cost_spent,
        'total_time_hours': current_time_spent,
        'ai_r_improvement': max_ai_r_improvement
    }

# Test the function immediately
example_employee_id_opt = df_employees['employee_id'].iloc[0]
current_ai_r_opt = df_employees[df_employees['employee_id'] == example_employee_id_opt]['current_ai_r_score'].iloc[0]
T_max_hours_opt = 300
cost_weight_lambda_opt = 0.005 # Adjusted for a reasonable trade-off

optimization_results_test = optimize_pathway_sequence(
    example_employee_id_opt, current_ai_r_opt, df_pathways, T_max_hours_opt,
    cost_weight_lambda_opt, df_employees, df_occupations, PARAMS
)

print(f"Test Optimization Results for {example_employee_id_opt}:")
for k, v in optimization_results_test.items():
    print(f"  {k}: {v}")
example_employee_id = df_employees['employee_id'].iloc[random.randint(0, len(df_employees)-1)]
current_ai_r = df_employees[df_employees['employee_id'] == example_employee_id]['current_ai_r_score'].iloc[0]

T_max_hours = 300  # e.g., 8 weeks of full-time training (40 hours/week * 8 = 320)
cost_weight_lambda = 0.005 # A parameter to trade-off AI-R improvement vs. cost

optimization_results = optimize_pathway_sequence(
    example_employee_id, current_ai_r, df_pathways, T_max_hours,
    cost_weight_lambda, df_employees, df_occupations, PARAMS
)

print(f"Multi-Step Pathway Optimization Results for Employee {example_employee_id} (Current AI-R: {current_ai_r:.2f}):")
print(f"  Recommended Sequence: {optimization_results['recommended_sequence']}")
print(f"  Projected Final AI-R: {optimization_results['projected_final_ai_r']:.2f}")
print(f"  Total Cost: ${optimization_results['total_cost']:.2f}")
print(f"  Total Time (hours): {optimization_results['total_time_hours']:.2f}")
print(f"  AI-R Improvement: {optimization_results['ai_r_improvement']:.2f}")

# Visualize the optimization results (optional, could be a table or bar chart)
plot_current_vs_projected_ai_r(
    current_ai_r,
    [optimization_results['projected_final_ai_r']],
    ['Optimized Pathway Sequence']
)
print("## Strategic Recommendations for AI Workforce Development\n")

# Insight 1: Identify low AI-R cohorts and their drivers
low_ai_r_cohorts = df_employees.sort_values(by='current_ai_r_score').head(5)
print("### 1. Target Low AI-R Cohorts with Driver-Specific Interventions\n")
print("Identify employees with significantly lower AI-R scores. Analyze whether their low score is primarily driven by low Idiosyncratic Readiness (V^R) or insufficient Systematic Opportunity (HR^R) in their current role. Tailor interventions accordingly.\n")
print("**Example: Top 5 Employees with Lowest AI-R Scores**")
print(low_ai_r_cohorts[['employee_id', 'job_role', 'department', 'current_ai_r_score', 'vr_score', 'hr_r_score']].to_string(index=False))
print("\n*   **Action:** For `EMP023` in 'Marketing' with low V^R, recommend AI-Fluency focused training. For `EMP011` in 'Finance', whose HR^R is relatively low, consider internal mobility options or upskilling for roles with higher market opportunity.\n")

# Insight 2: Pinpoint critical skills gaps from heatmap
# This relies on the heatmap generated earlier, so we'll infer an example.
print("### 2. Address Critical Skills Gaps via Targeted Upskilling\n")
print("The Skills Gap Heatmap (Section 16) revealed common weaknesses. For instance, if 'Business Analyst' roles show lower 'Adaptive-Capacity' scores, a targeted training program focusing on 'Strategic Career Management' or 'Cognitive Flexibility' would be beneficial.\n")
print("*   **Example:** Based on previous heatmap, 'Data Scientist' roles generally excel in 'AI-Fluency' but might show gaps in 'Domain-Expertise' (e.g., specific industry knowledge). Prioritize advanced domain-specific AI applications and certifications.\n")

# Insight 3: Recommend specific learning pathways from optimization results
print("### 3. Implement Optimized Multi-Step Learning Pathways\n")
print(f"For employee {example_employee_id}, the optimization identified the following sequence to maximize AI-R improvement within budget and time constraints:\n")
print(f"*   **Recommended Pathway Sequence:** {optimization_results['recommended_sequence']}")
print(f"*   **Projected AI-R Improvement:** {optimization_results['ai_r_improvement']:.2f}")
print("\n*   **Action:** Leverage such optimized pathways to guide individual career development plans, balancing cost, time, and impact.\n")

# Insight 4: Highlight roles with high HR^R but low V^R
high_hr_low_vr_roles = df_employees[(df_employees['hr_r_score'] > 70) & (df_employees['vr_score'] < 60)]
if not high_hr_low_vr_roles.empty:
    print("### 4. Invest Strategically in High Opportunity, Low Readiness Roles\n")
    print("Identify job roles that have high Systematic Opportunity (HR^R) but where the current workforce has lower Idiosyncratic Readiness (V^R). These are prime candidates for strategic investment.\n")
    print("**Example: Employees in High HR^R / Low V^R Roles**")
    print(high_hr_low_vr_roles[['employee_id', 'job_role', 'hr_r_score', 'vr_score', 'current_ai_r_score']].head().to_string(index=False))
    print("\n*   **Action:** For these roles, focused upskilling on AI-Fluency and Domain-Expertise (specific to the high HR^R area) will yield high returns.\n")
else:
    print("### 4. All employees seem to have balanced HR^R and V^R in this simulation. No explicit high opportunity/low readiness roles identified.\n")

# Insight 5: Emphasize adaptive capacities
print("### 5. Foster Continuous Learning and Adaptive Capacity\n")
print("The rapid pace of AI evolution necessitates a workforce with strong adaptive capacities. Emphasize training that builds cognitive flexibility, social-emotional intelligence for human-AI collaboration, and strategic career management skills across all employee levels.\n")
print("*   **Action:** Integrate 'Adaptive-Capacity' boosting modules into all major learning initiatives and promote a culture of continuous learning and experimentation.\n")