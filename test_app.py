
from streamlit.testing.v1 import AppTest
import pandas as pd
import numpy as np
import pytest

# Helper to create a temporary app.py file for testing
# In a real scenario, you'd run tests from the directory containing your app.py
# For this example, we'll assume the app code is in a file named 'app.py' in the same directory.
# If the app.py is not in the same directory, you would need to adjust the path in AppTest.from_file()

# Helper function to set up initial data and perform common calculations
def _setup_for_calculations(at: AppTest):
    """Navigates to Data Configuration, generates data, then navigates to AI-Readiness Calculation Walkthrough
    and triggers all necessary calculations by simply visiting the page after data generation.
    """
    # Go to Data Configuration
    at.sidebar.radio[0].set_value("Data Configuration").run()
    # Click the 'Generate/Reset Synthetic Data' button
    at.button[0].click().run()
    assert at.success[0].value == "Synthetic data generated successfully!"

    # Go to AI-Readiness Calculation Walkthrough
    at.sidebar.radio[0].set_value("AI-Readiness Calculation Walkthrough").run()

    # The calculations run automatically on page load after data is in session_state
    # Verify that the core dataframes are in session_state and have been processed
    assert not at.session_state.df_employees.empty
    assert not at.session_state.df_occupations.empty
    assert 'current_ai_r_score' in at.session_state.df_employees.columns
    assert 'hr_r_score' in at.session_state.df_employees.columns
    assert 'vr_score' in at.session_state.df_employees.columns
    assert 'synergy_score' in at.session_state.df_employees.columns
    assert 'h_base_score' in at.session_state.df_occupations.columns

    return at

def test_introduction_page():
    """Verify elements on the Introduction page."""
    at = AppTest.from_file("app.py").run()
    at.sidebar.radio[0].set_value("Introduction").run()

    assert at.header[0].value == "1. Introduction to the AI-Readiness Framework"
    assert "In this lab, we embark on a journey to understand and quantify \"AI Readiness\"" in at.markdown[0].value
    assert "AI-R_{i,t} = \\alpha \\cdot V^R_{i}(t) + (1 - \\alpha) \\cdot H^R(t) + \\beta \\cdot Synergy\\%(V^R, H^R)" in at.markdown[2].value
    assert at.metric[0].label == "Sample Idiosyncratic Readiness ($V^R$)"
    assert float(at.metric[0].value) == 75.0
    assert at.metric[3].label == "Calculated Sample AI-Readiness Score (AI-R)"
    # The exact value depends on default alpha/beta, but it should be a float
    assert isinstance(float(at.metric[3].value), float)

def test_data_configuration_page():
    """Verify data generation and parameter updates on the Data Configuration page."""
    at = AppTest.from_file("app.py").run()
    at.sidebar.radio[0].set_value("Data Configuration").run()

    # Test initial state
    assert at.info[0].value == "No employee data available. Please generate synthetic data."

    # Generate synthetic data
    at.button[0].click().run()
    assert at.success[0].value == "Synthetic data generated successfully!"
    assert not at.session_state.df_employees.empty
    assert not at.session_state.df_occupations.empty
    assert not at.session_state.df_pathways.empty
    assert at.dataframe[0].value.shape[0] > 0 # Check employee head
    assert at.dataframe[1].value.shape[0] > 0 # Check occupation head
    assert at.dataframe[2].value.shape[0] > 0 # Check pathway head

    # Test parameter updates
    initial_alpha = at.session_state.PARAMS['alpha']
    new_alpha = round(initial_alpha + 0.1, 2)
    at.slider[0].set_value(new_alpha).run()
    assert at.session_state.PARAMS['alpha'] == new_alpha

    initial_beta = at.session_state.PARAMS['beta']
    new_beta = round(initial_beta + 0.05, 2)
    at.slider[1].set_value(new_beta).run()
    assert at.session_state.PARAMS['beta'] == new_beta

    initial_lambda_growth = at.session_state.PARAMS['lambda_growth']
    new_lambda_growth = round(initial_lambda_growth + 0.2, 2)
    at.number_input[0].set_value(new_lambda_growth).run()
    assert at.session_state.PARAMS['lambda_growth'] == new_lambda_growth

    # Check one expender parameter
    at.expander[0].click().run() # Open HR Base Weights
    initial_w_ai_enhancement = at.session_state.PARAMS['hr_base_weights']['w_ai_enhancement']
    new_w_ai_enhancement = round(initial_w_ai_enhancement + 0.1, 2)
    at.number_input[3].set_value(new_w_ai_enhancement).run() # Index might vary, careful here
    assert at.session_state.PARAMS['hr_base_weights']['w_ai_enhancement'] == new_w_ai_enhancement

def test_ai_readiness_calculation_walkthrough_page():
    """Verify calculation results on the AI-Readiness Calculation Walkthrough page."""
    at = AppTest.from_file("app.py")
    at = _setup_for_calculations(at)

    employee_id_to_test = at.session_state.df_employees['employee_id'].iloc[0]
    at.selectbox[0].set_value(employee_id_to_test).run()

    # Verify key metrics are displayed for the selected employee
    # Indices are based on the order of expanders and metrics within them
    
    # HR Components
    at.expander[0].click().run() # Open AI-Enhancement Potential
    assert at.metric[0].label == "AI-Enhancement Score"
    assert isinstance(float(at.metric[0].value), float)
    at.expander[0].click().run() # Close

    at.expander[1].click().run() # Open Job Growth Projections
    assert at.metric[1].label == "Raw Job Growth ($g$)"
    assert isinstance(float(at.metric[1].value.replace('%', '')), float)
    at.expander[1].click().run() # Close

    at.expander[2].click().run() # Open Wage Premium & Entry Accessibility
    assert at.metric[3].label == "Wage Premium"
    assert isinstance(float(at.metric[3].value), float)
    at.expander[2].click().run() # Close

    at.expander[3].click().run() # Open Calculate Base Opportunity Score
    assert at.metric[5].label == "Base Opportunity Score ($H_{\\text{base}}$)"
    assert isinstance(float(at.metric[5].value), float)
    at.expander[3].click().run() # Close

    at.expander[4].click().run() # Open Dynamic Multipliers
    assert at.metric[6].label == "Growth Multiplier ($M_{\\text{growth}}$)"
    assert isinstance(float(at.metric[6].value), float)
    at.expander[4].click().run() # Close

    at.expander[5].click().run() # Open Calculate Final Systematic Opportunity
    assert at.metric[8].label == "Final Systematic Opportunity Score ($H^R$)"
    assert isinstance(float(at.metric[8].value), float)
    at.expander[5].click().run() # Close

    # VR Components
    at.expander[6].click().run() # Open AI-Fluency Factor
    assert at.metric[9].label == "Final AI-Fluency Score"
    assert isinstance(float(at.metric[9].value), float)
    at.expander[6].click().run() # Close

    at.expander[7].click().run() # Open Domain-Expertise Factor
    assert at.metric[10].label == "Final Domain-Expertise Score"
    assert isinstance(float(at.metric[10].value), float)
    at.expander[7].click().run() # Close

    at.expander[8].click().run() # Open Adaptive-Capacity Factor
    assert at.metric[11].label == "Final Adaptive-Capacity Score"
    assert isinstance(float(at.metric[11].value), float)
    at.expander[8].click().run() # Close

    at.expander[9].click().run() # Open Calculate Final Idiosyncratic Readiness
    assert at.metric[12].label == "Final Idiosyncratic Readiness Score ($V^R$)"
    assert isinstance(float(at.metric[12].value), float)
    at.expander[9].click().run() # Close

    # Synergy & Overall AI-R
    at.expander[10].click().run() # Open Synergy Function
    assert at.markdown[37].value.startswith("**Skills Match Score**") # Check for synergy markdown
    at.expander[10].click().run() # Close

    at.expander[11].click().run() # Open Calculate Final Synergy Score
    assert at.metric[13].label == "Final Synergy Score"
    assert isinstance(float(at.metric[13].value), float)
    at.expander[11].click().run() # Close

    at.expander[12].click().run() # Open Calculate Overall AI-Readiness Score
    assert at.metric[15].label.startswith("Overall AI-Readiness Score for")
    assert isinstance(float(at.metric[15].value), float)
    at.expander[12].click().run() # Close

def test_ai_r_report_page():
    """Verify the AI-R Report & Skills Gap Analysis page."""
    at = AppTest.from_file("app.py")
    at = _setup_for_calculations(at)

    at.sidebar.radio[0].set_value("AI-R Report & Skills Gap Analysis").run()

    # Check for summary dataframe
    assert at.dataframe[0].value.shape[0] > 0 # Should have group summary
    assert "Average_AI_R" in at.dataframe[0].value.columns

    # Change group by option and re-check
    at.selectbox[0].set_value("job_role").run()
    assert at.dataframe[0].value.shape[0] > 0 # Should still have data
    assert at.dataframe[0].value.index.name == "job_role"

    # Check for heatmap plot
    assert at.pyplot[0].figure is not None

def test_what_if_scenario_engine_page():
    """Verify the What-If Scenario Engine page functionality."""
    at = AppTest.from_file("app.py")
    at = _setup_for_calculations(at)

    at.sidebar.radio[0].set_value("What-If Scenario Engine").run()

    employee_id_to_test = at.session_state.df_employees['employee_id'].iloc[0]
    pathway_id_to_test = at.session_state.df_pathways['pathway_id'].iloc[0]

    at.selectbox[0].set_value(employee_id_to_test).run()
    at.selectbox[1].set_value(pathway_id_to_test).run()

    # Adjust sliders
    at.slider[0].set_value(0.9).run() # Completion rate
    at.slider[1].set_value(0.95).run() # Mastery score

    # Run simulation
    at.button[0].click().run()

    assert at.success[0].value == "Simulation complete!"
    assert at.metric[0].label == "Current AI-Readiness Score"
    assert at.metric[1].label == "Projected AI-Readiness Score"
    assert at.metric[2].label == "Change in AI-Readiness ($\\Delta AI-R$)"
    assert isinstance(float(at.metric[1].value), float)
    assert at.pyplot[0].figure is not None

def test_multi_step_pathway_optimization_page():
    """Verify the Multi-Step Pathway Optimization page functionality."""
    at = AppTest.from_file("app.py")
    at = _setup_for_calculations(at)

    at.sidebar.radio[0].set_value("Multi-Step Pathway Optimization").run()

    employee_id_to_test = at.session_state.df_employees['employee_id'].iloc[0]
    at.selectbox[0].set_value(employee_id_to_test).run()

    # Set optimization parameters
    at.number_input[0].set_value(150).run() # Max Time Budget
    at.number_input[1].set_value(0.02).run() # Cost Weight

    # Run optimization
    at.button[0].click().run()

    assert at.success[0].value == "Optimization complete!"
    assert at.metric[0].label == "Current AI-Readiness Score"
    assert at.metric[1].label == "Projected Final AI-Readiness Score"
    assert at.metric[2].label == "AI-R Improvement"
    assert at.metric[3].label == "Total Estimated Cost"
    assert at.metric[4].label == "Total Estimated Time (hours)"

    assert isinstance(float(at.metric[1].value), float)
    assert isinstance(float(at.metric[3].value.replace('$', '')), float)
    assert isinstance(float(at.metric[4].value.replace(' hrs', '')), float)

    # Check if a recommended sequence is displayed (at least a markdown element after the metrics)
    if at.markdown: # Check if markdown elements exist
        # The recommended sequence is usually a list of markdown items
        # We look for a markdown element that starts with a number, indicating a list item
        found_sequence = False
        for md_element in at.markdown:
            if md_element.value.strip().startswith("1."):
                found_sequence = True
                break
        assert found_sequence, "Expected recommended pathway sequence not found."
    else:
        assert False, "No markdown elements found on the page, expected pathway sequence."
        
    assert at.pyplot[0].figure is not None

def test_strategic_recommendations_page():
    """Verify elements on the Strategic Recommendations page."""
    at = AppTest.from_file("app.py").run()
    at.sidebar.radio[0].set_value("Strategic Recommendations").run()

    assert at.header[0].value == "19. Strategic Recommendations & Conclusion"
    assert at.subheader[0].value == "1. Data-Driven Upskilling Initiatives"
    assert "Leverage the **AI-R Report & Skills Gap Analysis**" in at.markdown[0].value
    assert at.subheader[4].value == "5. Fostering an Adaptive Culture"
    assert "The AI-Readiness & Upskilling Strategizer provides a robust, data-driven framework" in at.markdown[5].value

