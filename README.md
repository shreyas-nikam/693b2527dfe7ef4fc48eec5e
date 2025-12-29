# QuLab: AI-Readiness Career Navigator

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

**QuLab: AI-Readiness Career Navigator** is a Streamlit-powered web application designed to help financial professionals assess their preparedness for AI-enabled careers, identify high-opportunity roles, pinpoint skill gaps, and optimize personalized learning strategies.

In the rapidly evolving landscape of financial services, the integration of Artificial Intelligence (AI) is reshaping roles and creating new opportunities. This application provides a data-driven framework to quantify an individual's readiness, guiding them through a systematic process to make informed decisions about professional development and maximize career trajectory in the age of AI.

The core of this analysis is the **AI-Readiness Score (AI-R)**, a novel parametric framework that decomposes career opportunity into **Idiosyncratic Readiness ($V^R$)**, representing individual capabilities, and **Systematic Opportunity ($H^R$)**, representing macro-level job growth and demand. It also incorporates a **Synergy Function** to capture compounding benefits when individual preparation aligns with market opportunity.

## Features

This application offers a comprehensive suite of tools organized into interactive tabs:

1.  **Introduction**: Provides an overview of the application, the persona (Alice, a Senior Quantitative Analyst), and the theoretical framework of the AI-Readiness Score ($AI-R$).
2.  **Profile & Goals**:
    *   Allows users to review and adjust a pre-defined professional profile (education, experience, current skills, AI fluency, domain expertise, adaptive capacity sub-factors).
    *   Enables selection of target AI-enabled financial roles.
    *   Calculates initial `Idiosyncratic Readiness ($V^R$)` and `Systematic Opportunity ($H^R$)` scores.
3.  **Opportunity Evaluation**:
    *   Displays a detailed breakdown of the `Idiosyncratic Readiness ($V^R$)` score.
    *   Presents `Systematic Opportunity ($H^R$)` scores for all selected target roles.
    *   Calculates the comprehensive `AI-Readiness Score ($AI-R$)` for each role, incorporating a synergy factor.
    *   Identifies the top-performing role based on the highest $AI-R$ score.
    *   Visualizes skill gaps for the recommended role using a radar chart, comparing current skills against required proficiencies.
4.  **Learning Optimization**:
    *   Allows users to set constraints for learning investment (maximum time in hours, maximum budget in USD).
    *   Enables adjustment of the cost-weight parameter ($\lambda$) for the optimization.
    *   Recommends an optimal sequence of learning pathways (courses, certifications, workshops) that maximize the projected $AI-R$ gain for the top role within the specified constraints.
    *   Displays total estimated time and cost investment for the recommended path.
    *   Compares current vs. projected $AI-R$ after completing the learning pathway.
5.  **"What-If" Scenario Analysis**:
    *   Empowers users to define custom scenarios by selecting a target role and a specific combination of learning pathways.
    *   Compares the projected $AI-R$, time, and cost for custom scenarios against the initial optimal recommendation.
    *   Calculates and visualizes the Return on Learning Investment (ROI) for each scenario, aiding in strategic decision-making.
6.  **Summary Report**:
    *   Consolidates all key findings into a personalized, actionable report.
    *   Summarizes current $V^R$ and $H^R$ scores, the top recommended career path, detailed skill gaps, the optimal learning pathway, and a summary of "What-If" analysis results.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository** (or download the project files):

    ```bash
    git clone https://github.com/your-username/qu Lab-ai-readiness-navigator.git
    cd qu Lab-ai-readiness-navigator
    ```
    *(Note: Replace `https://github.com/your-username/qu Lab-ai-readiness-navigator.git` with the actual repository URL if available)*

2.  **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:

    *   **On Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install dependencies**:
    Create a `requirements.txt` file in the project root with the following content:

    ```
    streamlit
    pandas
    numpy
    matplotlib
    seaborn
    ```
    Then, install them:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: The `ast` module is part of Python's standard library and doesn't need to be listed in `requirements.txt`.)*

5.  **Ensure `source.py` and data files exist**:
    The application imports functions from `source.py`. Make sure this file is present in the same directory as your main Streamlit script. The `create_simulated_data()` function within the application is designed to generate the necessary CSV data files (`idiosyncratic_data.csv`, `systematic_opportunity_data.csv`, `job_postings_data.csv`, `regional_demand_data.csv`, `skill_requirements.csv`, `learning_pathways.csv`) if they don't exist, typically upon the first run or initialization.

## Usage

1.  **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```
    *(Assuming your main application file is named `app.py`)*

2.  **Access the application**:
    The command above will open the application in your default web browser (or provide a local URL, usually `http://localhost:8501`).

3.  **Navigate the tabs**:
    *   Start with the **"Introduction"** tab to understand the project.
    *   Proceed to **"Profile & Goals"** to review/adjust Alice's profile and select target roles. Click "Calculate Initial Readiness & Opportunity".
    *   Move to **"Opportunity Evaluation"** to see $V^R$, $H^R$, $AI-R$ scores, and skill gaps.
    *   Use **"Learning Optimization"** to define constraints and find the best learning path for the top role.
    *   Experiment with **"What-If Analysis"** to compare different strategies.
    *   Finally, review the consolidated **"Summary Report"**.

## Project Structure

```
.
├── app.py                  # Main Streamlit application script
├── source.py               # Contains all backend logic, calculations, and global constants
├── requirements.txt        # Lists Python dependencies
├── README.md               # This README file
└── (data files generated by create_simulated_data() on first run)
    ├── idiosyncratic_data.csv
    ├── systematic_opportunity_data.csv
    ├── job_postings_data.csv
    ├── regional_demand_data.csv
    ├── skill_requirements.csv
    └── learning_pathways.csv
```

## Technology Stack

*   **Python**: Programming language
*   **Streamlit**: For creating interactive web applications
*   **Pandas**: For data manipulation and analysis
*   **NumPy**: For numerical operations, especially in calculations
*   **Matplotlib**: For creating static, interactive, and animated visualizations
*   **Seaborn**: For statistical data visualization based on Matplotlib

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes and ensure the code passes any tests.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please reach out to:

*   **QuantUniversity** - [info@quantuniversity.com](mailto:info@quantuniversity.com)
*   **Project Link**: [https://www.quantuniversity.com/](https://www.quantuniversity.com/) (Hypothetical, replace with actual project link)