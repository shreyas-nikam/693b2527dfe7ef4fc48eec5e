# QuLab: AI Readiness Score

![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

This repository hosts the Streamlit application for the "Workforce AI-Readiness & Upskilling Strategizer" lab project. Designed for AI Workforce leaders and HR executives, this powerful tool offers a data-driven approach to assess, simulate, and optimize your workforce's preparedness for AI-enabled careers.

## Table of Contents

1.  [Project Description](#project-description)
2.  [Features](#features)
3.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
    *   [Data](#data)
4.  [Usage](#usage)
5.  [Project Structure](#project-structure)
6.  [Technology Stack](#technology-stack)
7.  [Framework Overview](#framework-overview)
8.  [Contributing](#contributing)
9.  [License](#license)
10. [Contact](#contact)

---

## 1. Project Description

In this lab, we present the "Workforce AI-Readiness & Upskilling Strategizer," a powerful Streamlit application designed for AI Workforce leaders and HR executives. This tool provides a data-driven approach to assess, simulate, and optimize your workforce's preparedness for AI-enabled careers.

The application allows users to:
*   Understand the foundational AI-Readiness Score (AI-R) framework.
*   Gain aggregated insights into workforce AI-R scores and skill gaps.
*   Simulate the impact of learning pathways on individual employee scores.
*   Optimize multi-step learning pathways within constraints.
*   Receive strategic recommendations for upskilling initiatives.

Navigate through the sections using the sidebar to unlock the full potential of your AI-ready workforce!

## 2. Features

The application is structured around a high-level story flow and provides detailed insights into its underlying AI-Readiness framework:

### Core Workflow
1.  **Workforce Dashboard**: Get an aggregated overview of your workforce's current AI-R scores and broad skill gaps, segmented by departments or job roles. This allows for rapid assessment of your talent pool's current state.
2.  **What-If Scenario Engine**: Simulate the immediate impact of specific learning pathways (with adjustable completion and mastery rates) on an individual employee's AI-R score. This helps evaluate program effectiveness at a micro-level.
3.  **Multi-Step Pathway Optimization**: For more complex development, identify an optimal sequence of learning pathways for a selected employee, balancing AI-R improvement with time and cost constraints. This generates a strategic roadmap for talent investment.
4.  **Strategic Recommendations**: Based on the comprehensive analysis and simulations, receive synthesized insights and actionable recommendations for targeted upskilling initiatives and overall workforce development plans.

### Framework Details
1.  **AI-R Overview**: Explore the foundational AI-Readiness Score (AI-R) framework, its components, and underlying formulas. This section provides the theoretical grounding for all metrics used.
2.  **Systematic Opportunity (H^R)**: Delve into the macro-level job growth and demand component, analogous to market beta.
3.  **Idiosyncratic Readiness (V^R)**: Understand individual-specific capabilities that can be improved through learning.
4.  **Synergy Function**: Learn how the multiplicative benefits of aligning individual readiness with market opportunity are captured.

## 3. Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

*   **Python 3.7+**
*   **Git** (optional, for cloning the repository)

### Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/your-username/quolab-ai-readiness.git
    cd quolab-ai-readiness
    ```
    *(Replace `your-username/quolab-ai-readiness` with the actual repository path)*

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```
    If `requirements.txt` is not provided, you can generate one or install manually:
    ```bash
    pip install streamlit pandas numpy matplotlib seaborn
    ```

### Data

The core dataframes (`df_employees`, `df_occupations`, `df_pathways`) and system parameters (`PARAMS`) are loaded from the `source.py` file. This file acts as the data source and houses the core logic for the AI-Readiness framework calculations. When the application starts, these are copied into Streamlit's session state to ensure dynamic modifications do not alter the original data.

## 4. Usage

To run the Streamlit application:

1.  Ensure your virtual environment is activated and dependencies are installed.
2.  Navigate to the directory containing `app.py` (and `source.py`).
3.  Execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```

This will open the application in your default web browser.

**Basic Navigation:**
*   Use the **sidebar** on the left to navigate between different sections of the application, including the main workflow pages (Dashboard, What-If, Optimization, Recommendations) and the detailed framework explanations.
*   Interact with **dropdowns**, **sliders**, and **buttons** on each page to explore data, run simulations, and generate insights.

## 5. Project Structure

The project has a straightforward structure:

```
quolab-ai-readiness/
├── app.py              # Main Streamlit application file
├── source.py           # Contains data definitions (df_employees, df_occupations, df_pathways, PARAMS)
                        # and core functions for AI-R calculation, simulation, and optimization.
└── README.md           # This file
├── requirements.txt    # List of Python dependencies (generated or manually created)
```

*   `app.py`: This is the main entry point for the Streamlit application. It defines the layout, user interface components, and calls functions from `source.py` to perform computations and display results.
*   `source.py`: This file is crucial as it contains the data models (e.g., synthetic employee data, occupation details, learning pathways) and the implementation of the AI-Readiness framework, including all calculation functions and optimization algorithms.

## 6. Technology Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web user interface.
*   **Pandas**: For data manipulation and analysis.
*   **NumPy**: For numerical operations.
*   **Matplotlib**: For static data visualizations.
*   **Seaborn**: For enhanced statistical data visualizations.

## 7. Framework Overview

The AI-Readiness Score (AI-R) is a novel parametric framework that quantifies an individual's preparedness for success in AI-enabled careers. It decomposes career opportunity into two orthogonal components: Systematic Opportunity ($H^R$) and Idiosyncratic Readiness ($V^R$), with a Synergy factor capturing their alignment.

The core formula is:
$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$
Where:
*   $V^R_{i}(t)$: **Idiosyncratic Readiness** (individual capability, from 0-100).
*   $H^R(t)$: **Systematic Opportunity** (market demand for an occupation, from 0-100).
*   $Synergy\%(V^R, H^R)$: Measures the alignment and multiplicative benefits (from 0-100).
*   $\alpha$: Weight on individual vs. market factors (e.g., 0.6).
*   $\beta$: Synergy coefficient (e.g., 0.15).

Each of these components, along with their sub-components, is explained in detail within the application's "Framework Details" section.

## 8. Contributing

Contributions to this lab project are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please ensure your code adheres to good practices and includes appropriate comments and documentation.

## 9. License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 10. Contact

For questions, feedback, or collaborations, please contact [QuantUniversity](https://www.quantuniversity.com/).

## License

## QuantUniversity License

© QuantUniversity 2025  
This notebook was created for **educational purposes only** and is **not intended for commercial use**.  

- You **may not copy, share, or redistribute** this notebook **without explicit permission** from QuantUniversity.  
- You **may not delete or modify this license cell** without authorization.  
- This notebook was generated using **QuCreate**, an AI-powered assistant.  
- Content generated by AI may contain **hallucinated or incorrect information**. Please **verify before using**.  

All rights reserved. For permissions or commercial licensing, contact: [info@quantuniversity.com](mailto:info@quantuniversity.com)
