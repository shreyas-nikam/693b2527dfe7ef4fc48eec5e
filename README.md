# QuLab: Workforce AI-Readiness & Upskilling Strategizer

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

The **"Workforce AI-Readiness & Upskilling Strategizer"** is a Streamlit application designed to empower AI Workforce leaders and HR executives with a data-driven tool to assess, simulate, and optimize their workforce's preparedness for AI-enabled careers. It implements the **AI-Readiness Score (AI-R)** framework, quantifying individual capabilities and market opportunities to guide strategic talent development and upskilling initiatives.

By providing dynamic insights into an individual's "Idiosyncratic Readiness" ($V^R$) and market-driven "Systematic Opportunity" ($H^R$), alongside a "Synergy" factor, the application enables organizations to proactively identify skill gaps, simulate the impact of learning pathways, and strategically invest in upskilling programs to ensure their workforce remains competitive and adaptable in the evolving AI landscape.

## Features

The application provides a structured workflow through several key features, accessible via the sidebar navigation:

1.  **AI-Readiness Framework Deep Dive**:
    *   **AI-R Overview**: Explores the core AI-Readiness Score (AI-R) framework, its components, and underlying formulas.
    *   **Systematic Opportunity ($H^R$)**: Details the macro-level demand and growth potential in AI-enabled occupations.
    *   **Idiosyncratic Readiness ($V^R$)**: Explains how individual capabilities (AI-Fluency, Domain-Expertise, Adaptive-Capacity) are quantified.
    *   **Synergy Function**: Describes the multiplicative benefits when individual readiness aligns with market opportunity.

2.  **Interactive Workforce Dashboard**:
    *   Provides an aggregated overview of the workforce's current AI-R scores.
    *   Visualizes broad skill gaps through heatmaps, broken down by departments or job roles.
    *   Offers a quick, high-level assessment of the current talent pool's state.

3.  **What-If Scenario Engine**:
    *   Allows selection of an individual employee and a specific learning pathway.
    *   Simulates the immediate impact of completing that pathway on their AI-R score, considering completion and mastery rates.
    *   Helps evaluate program effectiveness at an individual level.

4.  **Multi-Step Pathway Optimization**:
    *   Identifies an optimal sequence of learning pathways for a selected employee.
    *   Balances AI-R improvement with user-defined time and cost constraints.
    *   Offers a strategic roadmap for more complex skill transitions.

5.  **Strategic Recommendations**:
    *   Synthesizes insights from the dashboard, simulations, and optimizations.
    *   Generates actionable recommendations for targeted upskilling initiatives and overall workforce development plans.

## Getting Started

Follow these instructions to set up and run the Streamlit application on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)
*   Git (for cloning the repository)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd QuLab-AI-Readiness-Strategizer # Or whatever your project folder is named
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**
    Create a `requirements.txt` file in your project root with the following content:
    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    numpy>=1.20.0
    matplotlib>=3.3.0
    seaborn>=0.11.0
    ```
    Then, install the packages:
    ```bash
    pip install -r requirements.txt
    ```

    *Note: The `source.py` file is expected to be present in the same directory as `app.py`, containing the core dataframes (`df_employees`, `df_occupations`, `df_pathways`) and functions required for the application's logic.*

### Usage

1.  **Run the Streamlit application:**
    Ensure your virtual environment is active and you are in the project's root directory.
    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**
    Your web browser should automatically open to `http://localhost:8501`. If it doesn't, navigate to this URL manually.

3.  **Navigate the application:**
    *   Use the **sidebar navigation** on the left to switch between different sections of the application (Dashboard, What-If Scenario, Pathway Optimization, Strategic Recommendations, and Framework details).
    *   Interact with **select boxes, sliders, and buttons** in each section to explore data, run simulations, and generate insights.

## Project Structure

The project is structured as follows:

```
.
├── app.py                  # Main Streamlit application file
├── source.py               # Contains core dataframes (df_employees, etc.) and
                            # all business logic functions (e.g., calculate_ai_r,
                            # simulate_pathway_impact, optimize_pathway_sequence,
                            # generate_ai_r_report_summary, plot_current_vs_projected_ai_r)
├── requirements.txt        # Lists all Python dependencies
└── README.md               # This file
```

## Technology Stack

*   **Streamlit**: For building the interactive web application and user interface.
*   **Python**: The core programming language for all backend logic and data processing.
*   **Pandas**: Essential for data manipulation and analysis, handling tabular data structures.
*   **NumPy**: Provides support for large, multi-dimensional arrays and mathematical functions.
*   **Matplotlib**: Used for creating static, interactive, and animated visualizations in Python.
*   **Seaborn**: A high-level data visualization library based on Matplotlib, providing a simpler interface for drawing attractive statistical graphics.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes and ensure the code adheres to existing style guidelines.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (If you don't have a LICENSE file, you might want to create one or state "Proprietary" for a lab project).

## Contact

For questions or inquiries about this project, please contact:

QuantUniversity
Website: [www.quantuniversity.com](https://www.quantuniversity.com/)
