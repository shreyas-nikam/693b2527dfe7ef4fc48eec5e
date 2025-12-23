id: 693b2527dfe7ef4fc48eec5e_documentation
summary: AI Readiness score Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: AI Workforce Readiness & Upskilling Strategizer

## Introduction to QuLab and the AI-Readiness Framework
Duration: 05:00

Welcome to the **"Workforce AI-Readiness & Upskilling Strategizer"** codelab! This guide will walk you through a powerful Streamlit application designed for AI Workforce leaders and HR executives. The application provides a data-driven approach to assess, simulate, and optimize your workforce's preparedness for AI-enabled careers.

Understanding the AI-Readiness of your workforce is critical in today's rapidly evolving technological landscape. This application moves beyond traditional skill matrices by introducing the **AI-Readiness Score (AI-R)**, a comprehensive metric that quantifies an individual's readiness for AI-driven roles. It enables strategic talent development by identifying skill gaps, simulating the impact of learning programs, and optimizing pathways for upskilling. By the end of this codelab, you will have a deep understanding of the AI-R framework and how to leverage the application's functionalities to build an AI-ready workforce.

### High-Level Story Flow of the Application:

1.  **Framework Introduction**: Explore the foundational AI-Readiness Score (AI-R) framework, its components, and underlying formulas. This section provides the theoretical grounding for all metrics used.
2.  **Workforce Dashboard**: Get an aggregated overview of your workforce's current AI-R scores and broad skill gaps, segmented by departments or job roles. This allows for rapid assessment of your talent pool's current state.
3.  **What-If Scenario Engine**: Simulate the immediate impact of specific learning pathways (with adjustable completion and mastery rates) on an individual employee's AI-R score. This helps evaluate program effectiveness at a micro-level.
4.  **Multi-Step Pathway Optimization**: For more complex development, identify an optimal sequence of learning pathways for a selected employee, balancing AI-R improvement with time and cost constraints. This generates a strategic roadmap for talent investment.
5.  **Strategic Recommendations**: Based on the comprehensive analysis and simulations, receive synthesized insights and actionable recommendations for targeted upskilling initiatives and overall workforce development plans.

You can navigate through the different sections of the application using the sidebar on the left.

The application initializes its core dataframes and parameters in the Streamlit `st.session_state` to ensure persistence and mutability across user interactions:

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from source import * # Imports all functions and global variables like df_employees, PARAMS etc.

st.set_page_config(page_title="QuLab: AI Readiness score", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: AI Readiness score")
st.divider()

st.markdown("""
In this lab, we present the "Workforce AI-Readiness & Upskilling Strategizer," a powerful Streamlit application designed for AI Workforce leaders and HR executives. This tool provides a data-driven approach to assess, simulate, and optimize your workforce's preparedness for AI-enabled careers.
...
""")

# Initialize core dataframes and parameters from source.py
# Using .copy() to ensure modifications within the app do not alter the original imported data
if 'df_employees' not in st.session_state:
    st.session_state.df_employees = df_employees.copy()
if 'df_occupations' not in st.session_state:
    st.session_state.df_occupations = df_occupations.copy()
if 'df_pathways' not in st.session_state:
    st.session_state.df_pathways = df_pathways.copy()
if 'PARAMS' not in st.session_state:
    st.session_state.PARAMS = PARAMS.copy()

# Initialize variables for application navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Dashboard" # Sets the default landing page

# State for Dashboard page (Workforce Assessment & Skills Gap Analysis)
if 'report_group_by' not in st.session_state:
    st.session_state.report_group_by = 'job_role' # Default grouping for reports/heatmaps

# State for What-If Scenario Engine page
# ... (similar initializations for other pages)
```

<aside class="positive">
<b>Key Takeaway:</b> The AI-R framework offers a dynamic and quantitative approach to workforce planning, moving beyond static skill assessments to predict and optimize readiness for AI-enabled careers.
</aside>

## Understanding the AI-Readiness (AI-R) Framework
Duration: 10:00

The first conceptual section of the application, accessible via the "AI-R Overview" button in the sidebar, introduces the core AI-Readiness Framework.

The AI-Readiness Score (AI-R) is a novel parametric framework designed to quantify an individual's preparedness for success in AI-enabled careers. It decomposes career opportunity into two orthogonal components: **Systematic Opportunity ($H^R$)**, representing macro-level job growth and demand, and **Idiosyncratic Readiness ($V^R$)**, representing individual-specific capabilities. A **Synergy factor** captures the multiplicative benefits when individual readiness aligns with market opportunity.

The main formula for the AI-R score is:

$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$

Where:
*   $\alpha \in [0,1]$: Weight on individual vs. market factors. (e.g., $\alpha = 0.6$)
*   $V^R_{i}(t)$: Idiosyncratic Readiness (individual capability), normalized to $[0, 100]$.
*   $H^R(t)$: Systematic Opportunity (market demand), normalized to $[0, 100]$.
*   $\beta > 0$: Synergy coefficient. (e.g., $\beta = 0.15$)
*   $Synergy\% \in [0,100]$ (percentage units).

This framework allows for dynamic 'what-if' scenario planning, helping to guide targeted upskilling initiatives and talent development.

### Conceptual Architecture of the AI-R Framework

The AI-R score is calculated by combining these three main components. Imagine a tree structure where:
*   The root is **AI-Readiness Score (AI-R)**.
*   It has three main branches:
    *   **Idiosyncratic Readiness ($V^R$)**: Focuses on individual attributes.
    *   **Systematic Opportunity ($H^R$)**: Focuses on market and occupational attributes.
    *   **Synergy**: Captures the alignment between $V^R$ and $H^R$.

Each of these branches further decomposes into sub-components, which we will explore in the following steps. This modular design allows for granular analysis and targeted interventions.

The relevant Streamlit code for this section is displayed when `st.session_state.current_page == "AI-R Overview"`:

```python
elif st.session_state.current_page == "AI-R Overview":
    st.title("The AI-Readiness Framework: Core Concepts")
    st.header("Introduction to the AI-Readiness Framework")
    st.markdown(f"The AI-Readiness Score (AI-R) is a novel parametric framework designed to quantify an individual's preparedness for success in AI-enabled careers. ...")
    st.markdown(r"$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$")
    st.markdown(f"where:")
    st.markdown(r"*   $\alpha \in [0,1]$: Weight on individual vs. market factors. For this notebook, we'll use $\alpha = 0.6$.")
    st.markdown(f"*   $V^R_{i}(t)$: Idiosyncratic Readiness (individual capability).")
    st.markdown(f"*   $H^R(t)$: Systematic Opportunity (market demand).")
    st.markdown(r"*   $\beta > 0$: Synergy coefficient. For this notebook, we'll use $\beta = 0.15$.")
    st.markdown(f"*   Both $V^R$ and $H^R$ are normalized to $[0, 100]$.")
    st.markdown(r"*   $Synergy\% \in [0,100]$ (percentage units).")
    st.markdown(f"This framework allows for dynamic 'what-if' scenario planning, helping to guide targeted upskilling initiatives and talent development.")
    st.markdown(f"This section demonstrates how the final AI-R score is computed by combining the Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and Synergy components, weighted by the parameters $\alpha$ and $\beta$. The example reflects a scenario where an individual has strong readiness in a high-opportunity field with good alignment, resulting in a high AI-R score.")
```

<aside class="positive">
<b>Insight:</b> The modularity of the AI-R framework allows for targeted analysis. By understanding the contribution of $V^R$, $H^R$, and Synergy, organizations can identify whether an individual's AI-readiness challenge is due to personal skills, market conditions, or a mismatch between the two.
</aside>

## Deep Dive into Systematic Opportunity ($H^R$)
Duration: 15:00

The "Systematic Opportunity ($H^R$)" section in the sidebar provides details on this component. Systematic Opportunity ($H^R$) represents the macro-level demand and growth potential in AI-enabled occupations. This is analogous to market beta—an individual cannot create these opportunities through their own actions, but they can position themselves to benefit from favorable market conditions.

The $H^R$ score is calculated as:

$$H^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$

Where:
*   $H_{\text{base}}(O_{\text{target}})$: Base Opportunity Score for the target occupation.
*   $M_{\text{growth}}(t)$: Dynamic Growth Multiplier.
*   $M_{\text{regional}}(t)$: Dynamic Regional Multiplier.

### Base Opportunity Score ($H_{\text{base}}$)

The Base Opportunity Score ($H_{\text{base}}(o)$) aggregates various dimensions of occupational attractiveness: AI-Enhancement Potential, Job Growth Projections, Wage Premium, and Entry Accessibility. It is calculated as a weighted sum:

$$H_{\text{base}}(o) = w_1 \cdot \text{AI-Enhancement}_o + w_2 \cdot \text{Growth}_o + w_3 \cdot \text{Wage Premium}_o + w_4 \cdot \text{Entry Accessibility}_o$$

The weights ($w_j$) reflect the relative importance of each factor, as defined in the `PARAMS` dictionary ($w_1 = 0.30$, $w_2 = 0.30$, $w_3 = 0.25$, $w_4 = 0.15$). The final score is then scaled to $[0,100]$.

Let's break down its sub-components:

#### 1. AI-Enhancement Potential
Measures how much AI augments rather than replaces tasks:
$$AI\text{-}Enhancement_o = \frac{1}{|T_o|} \sum_{t \in T_o} (1 - Automation_t) \cdot AI\text{-}Augmentation_t$$
where $T_o$ is the set of tasks for occupation $o$, $Automation_t \in [0,1]$ measures replaceability, and $AI\text{-}Augmentation_t \in [0,1]$ measures productivity enhancement. For simplicity in our synthetic data, we directly include an aggregated `ai_enhancement_potential` for each occupation.

#### 2. Job Growth Projections
Quantifies the expected increase or decrease in employment for an occupation over a given period (e.g., 10 years). The raw growth rate $g$ is calculated as:
$$Growth_o = \frac{\text{Projected Jobs}_{o,t+10} - \text{Current Jobs}_{o,t}}{\text{Current Jobs}_{o,t}}$$
This raw growth rate is then normalized to a scale of $[0, 100]$ using an affine transformation:
$$Growth_{\text{normalized}} = \frac{g + 0.5}{2.0} \times 100$$
This transformation maps a growth rate range of $g \in [-0.5, 1.5]$ (representing -50% to +150% change) to $[0,100]$.

#### 3. Wage Premium & Entry Accessibility
Two other critical factors contributing to Systematic Opportunity are Wage Premium and Entry Accessibility.
**Wage Premium** ($Wage_o$) measures the compensation potential for AI-skilled roles relative to the median wage in that occupation:
$$Wage_o = \frac{{\text{AI-skilled wage}}}_o - {\text{median wage}}_o}{{\text{median wage}}}_o$$
**Entry Accessibility** ($Access_o$) quantifies the ease of transitioning into a role, based on typical educational and experience requirements:
$$Access_o = 1 - \frac{{\text{Education Years Required}} + {\text{Experience Years Required}}}{{10}}$$

### Dynamic Multipliers: Growth & Regional
Beyond the static Base Opportunity Score, Systematic Opportunity is modulated by dynamic, time-varying market factors:

#### 1. Growth Multiplier ($M_{\text{growth}}(t)$)
Captures market momentum based on recent changes in job postings:
$$M_{\text{growth}}(t) = 1 + \lambda \cdot \left( \frac{{\text{Job Postings}}}_{o,t}}{{\text{Job Postings}}}_{o,t-1}} - 1 \right)$$
where $\lambda = 0.3$ dampens volatility, keeping the multiplier typically between $0.7$ and $1.3$.

#### 2. Regional Multiplier ($M_{\text{regional}}(t)$)
Adjusts for local labor market conditions and remote work suitability:
$$M_{\text{regional}}(t) = \frac{{\text{Local Demand}}}_{i,t}}{{\text{National Avg Demand}}} \times (1 + \gamma \cdot {\text{Remote Work Factor}}_o)$$
where $\gamma = 0.2$ and $Remote Work Factor \in [0,1]$ measures the occupation's suitability for remote work. For simplicity, we assume `Local Demand` equals `National Avg Demand` for the primary calculation and focus on the `Remote Work Factor` contribution.

The final Systematic Opportunity score ($H^R(t)$) for an individual $i$ targeting occupation $o_{\text{target}}$ at time $t$ is calculated by combining the Base Opportunity Score with the dynamic multipliers. This step completes the calculation of the Systematic Opportunity component for each employee, linking their current job role to market conditions.

The relevant Streamlit code for this section is displayed when `st.session_state.current_page == "Systematic Opportunity (HR^R)"`:

```python
elif st.session_state.current_page == "Systematic Opportunity (HR^R)":
    st.title("Systematic Opportunity ($H^R$) Component")
    st.header("Conceptual Definition")
    st.markdown(f"Systematic Opportunity ($H^R$) represents the macro-level demand and growth potential in AI-enabled occupations. ...")
    st.markdown(r"$$H^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$")
    st.subheader("Base Opportunity Score ($H_{\text{base}}$)")
    # ... (detailed explanations and formulas for sub-components)
    st.subheader("Dynamic Multipliers: Growth & Regional")
    # ... (detailed explanations and formulas for sub-components)
```

<aside class="positive">
<b>Insight:</b> $H^R$ provides an external perspective on career viability. By understanding an occupation's $H^R$ score, individuals and organizations can make informed decisions about pursuing roles with high growth potential and favorable market conditions in the AI era.
</aside>

## Deep Dive into Idiosyncratic Readiness ($V^R$)
Duration: 15:00

The "Idiosyncratic Readiness ($V^R$)" section in the sidebar explains this component in detail. Idiosyncratic Readiness ($V^R$) measures an individual's specific preparation to succeed in AI-enabled careers. Unlike systematic opportunity, these factors can be directly improved through deliberate learning and skill development.

The final Idiosyncratic Readiness score ($V^R(t)$) aggregates AI-Fluency, Domain-Expertise, and Adaptive-Capacity. It is a weighted sum:

$$V^R(t) = w_{\text{VR1}} \cdot AI\text{-}Fluency_i(t) + w_{\text{VR2}} \cdot Domain\text{-}Expertise_i(t) + w_{\text{VR3}} \cdot Adaptive\text{-}Capacity_i(t)$$

The weights ($w_{\text{VR1}} = 0.45$, $w_{\text{VR2}} = 0.35$, $w_{\text{VR3}} = 0.20$) reflect the assessment that AI-Fluency is the most critical factor, followed by Domain-Expertise, with Adaptive-Capacity playing a supporting role (weights are from `PARAMS`). The final $V^R$ score is normalized to $[0, 100]$.

### AI-Fluency Factor
The AI-Fluency factor is a key sub-component, representing the ability to effectively use, understand, and collaborate with AI systems. It is calculated as a weighted sum of four sub-components:

$$AI\text{-}Fluency_i = \sum_{k=1}^4 \theta_k \cdot S_{i,k}$$

The sub-components ($S_{i,k}$) and their weights ($\theta_k$ from `PARAMS`) are:

**1. Technical AI Skills** ($S_{i,1}$, $\theta_1 = 0.30$): Based on Prompting, Tools, Understanding, and Data Literacy scores.
$$S_{i,1} = \frac{1}{4} (\text{Prompting}_i + \text{Tools}_i + \text{Understanding}_i + \text{DataLit}_i)$$

**2. AI-Augmented Productivity** ($S_{i,2}$, $\theta_2 = 0.35$): Measures productivity gains with AI assistance.
$$S_{i,2} = \frac{{\text{Output Quality}}}_{i,{\text{with AI}}}}{{\text{Output Quality}}}_{i,{\text{without AI}}}} \cdot \frac{{\text{Time}}}_{i,{\text{without AI}}}}{{\text{Time}}}_{i,{\text{with AI}}}}$$
For simplicity, our synthetic data has `ai_augmented_productivity_norm` pre-calculated based on this concept.

**3. Critical AI Judgment** ($S_{i,3}$, $\theta_3 = 0.20$): Assesses error detection and appropriate trust decisions with AI outputs.
$$S_{i,3} = \frac{{\text{Errors Caught}}}_i}{{\text{Total AI Errors}}} + \frac{{\text{Appropriate Trust Decisions}}}_{i}}{{\text{Total Decisions}}}$$
For simplicity, our synthetic data provides `errors_caught_norm` and `trust_decisions_norm` which we'll combine and re-normalize.

**4. AI Learning Velocity** ($S_{i,4}$, $\theta_4 = 0.15$): Measures improvement rate per unit time investment.
$$S_{i,4} = \frac{{\Delta \text{Proficiency}}}_{i}}{{\Delta t}} \cdot \frac{1}{{\text{Hours Invested}}}$$
For simplicity in this notebook, $\Delta Proficiency_i / \Delta t$ can be approximated as a 'learning_rate' for simulation purposes and then scaled with `hours_invested`.

### Domain-Expertise Factor
Domain-Expertise captures an individual's depth of knowledge in specific application areas, complementing their AI-Fluency. It is a multiplicative combination of Educational Foundation, Practical Experience, and Specialization Depth:

$$Domain\text{-}Expertise_i = E_{\text{education}} \cdot E_{\text{experience}} \cdot E_{\text{specialization}}$$

**1. Educational Foundation ($E_{\text{education}}$):** Discrete values based on education level (e.g., PhD=1.0, Master's=0.85, Bachelor's=0.70, Associate's/Certificate=0.60, HS+Coursework=0.50).

**2. Practical Experience ($E_{\text{experience}}$):** Measured by years of experience with diminishing returns:
$$E_{\text{experience}} = 1 - e^{-\gamma_{\text{exp}} \cdot Years}$$
where $\gamma_{\text{exp}} = 0.15$.

**3. Specialization Depth ($E_{\text{specialization}}$):** Reflects specific achievements and recognition in their field:
$$E_{\text{specialization}} = w_{\text{port}} \cdot \text{Portfolio}_i + w_{\text{recog}} \cdot \text{Recognition}_i + w_{\text{cred}} \cdot \text{Credentials}_i$$
where $w_{\text{port}} = 0.4$, $w_{\text{recog}} = 0.3$, $w_{\text{cred}} = 0.3$.

### Adaptive-Capacity Factor
Adaptive-Capacity measures the meta-skills that enable successful navigation of AI-driven transitions, focusing on an individual's ability to learn, adapt, and interact effectively in new environments. It is an equally weighted sum of three meta-skills:

$$Adaptive\text{-}Capacity_i = \frac{1}{3} (C_{\text{cognitive}} + C_{\text{social}} + C_{\text{strategic}})$$

where each $C$ component is scored on a scale of $[0, 100]$:

*   **Cognitive Flexibility ($C_{\text{cognitive}}$):** Problem-solving in novel contexts, transfer learning, creative application of AI tools.
*   **Social-Emotional Intelligence ($C_{\text{social}}$):** Empathy, negotiation, leadership, human-AI collaboration.
*   **Strategic Career Management ($C_{\text{strategic}}$):** Awareness of AI trends, proactive skill development, network building.

The relevant Streamlit code for this section is displayed when `st.session_state.current_page == "Idiosyncratic Readiness (V^R)"`:

```python
elif st.session_state.current_page == "Idiosyncratic Readiness (V^R)":
    st.title("Idiosyncratic Readiness ($V^R$) Component")
    st.header("Conceptual Definition")
    st.markdown(f"Idiosyncratic Readiness ($V^R$) measures an individual's specific preparation to succeed in AI-enabled careers. ...")
    st.markdown(r"$$V^R(t) = w_{\text{VR1}} \cdot AI\text{-}Fluency_i(t) + w_{\text{VR2}} \cdot Domain\text{-}Expertise_i(t) + w_{\text{VR3}} \cdot Adaptive\text{-}Capacity_i(t)$$")
    st.subheader("AI-Fluency Factor")
    # ... (detailed explanations and formulas for sub-components)
    st.subheader("Domain-Expertise Factor")
    # ... (detailed explanations and formulas for sub-components)
    st.subheader("Adaptive-Capacity Factor")
    # ... (detailed explanations and formulas for sub-components)
```

<aside class="negative">
<b>Warning:</b> Accurately measuring these idiosyncratic factors (especially "AI Learning Velocity" or "Critical AI Judgment") can be challenging in real-world scenarios, often requiring sophisticated assessment tools, performance data, and self-reported metrics, which might introduce bias or require ongoing validation.
</aside>

## Understanding the Synergy Function
Duration: 08:00

The "Synergy Function" section in the sidebar provides details on this component. The Synergy function captures the multiplicative benefits when individual readiness ($V^R$) aligns with market opportunity ($H^R$).

It is defined as:

$$Synergy\%(V^R, H^R) = \frac{{V^R \times H^R}}{{100}} \times Alignment_i$$

where both $V^R$ and $H^R$ are on $[0,100]$ scale, and $Alignment_i \in [0,1]$ ensures $Synergy\% \in [0,100]$.

The Synergy score formalizes the idea that career success is more than just individual capability plus market demand; it also depends on how well these two factors align. A high synergy score indicates a 'sweet spot' where an individual's unique skills and career stage perfectly intersect with market opportunities.

### Alignment Factor: Skills Match & Timing Factor
The $Alignment_i$ factor measures how well individual skills match occupation requirements and career stage:

$$Alignment_i = \frac{{\text{Skills Match Score}}}_{i}}{{\text{Maximum Possible Match}}} \times {\text{Timing Factor}}_{i}$$

#### 1. Skills Match Score
Using O*NET-like task-skill mappings (simulated through `skill_a` to `skill_j` in our synthetic data), we compute:

$$Match_i = \sum_{s \in S} \min({\text{Individual Skill}}_{i,s}, {\text{Required Skill}}_{o,s}) \cdot {\text{Importance}}_s$$

where $S$ is the set of all skills, and the minimum operator ensures that excess skill in one area doesn't compensate for deficiency in critical areas. For `Maximum Possible Match`, we assume a perfect match of 1.0 (after normalization of individual and required skills to 0-1).

#### 2. Timing Factor
Career stage affects transition ease:

$$Timing(y) = \begin{cases} 1.0 & \text{if } y \in [0,5] \text{ (early career)} \\ 1.0 & \text{if } y \in (5,15] \text{ (mid-career)} \\ 0.8 & \text{if } y > 15 \text{ (late career, transition friction)} \end{cases}$$

where $y$ is years of experience. Note that all timing values are $\leq 1.0$ to ensure Alignment remains bounded at $[0, 1]$.

The Alignment Factor provides a nuanced measure of how well an individual's skills and career stage align with a specific occupational target. This factor is critical for determining the true 'fit' and the potential for synergy between an individual's readiness and market opportunity.

The relevant Streamlit code for this section is displayed when `st.session_state.current_page == "Synergy Function"`:

```python
elif st.session_state.current_page == "Synergy Function":
    st.title("Synergy Function")
    st.header("Conceptual Basis")
    st.markdown(f"The Synergy function captures the multiplicative benefits when individual readiness ($V^R$) aligns with market opportunity ($H^R$). ...")
    st.markdown(r"$$Synergy\%(V^R, H^R) = \frac{{V^R \times H^R}}{{100}} \times Alignment_i$$")
    st.subheader("Alignment Factor: Skills Match & Timing Factor")
    # ... (detailed explanations and formulas for sub-components)
```

<aside class="positive">
<b>Best Practice:</b> Maximizing synergy involves not only boosting individual skills ($V^R$) or targeting high-demand roles ($H^R$), but also ensuring a strong match between the two. Strategic HR interventions should aim to improve skill alignment and support career transitions at opportune times.
</aside>

## Workforce AI-Readiness Dashboard
Duration: 10:00

The "Dashboard" is the default landing page and provides an aggregated overview of your workforce's current AI-R scores and broad skill gaps, segmented by departments or job roles. This allows for rapid assessment of your talent pool's current state.

### Aggregated AI-Readiness Report
The 'Workforce AI-Readiness Report' summarizes the aggregated AI-R scores, providing a high-level overview of the organization's AI-readiness across different segments. You can choose to group this report by 'job_role' or 'department' using the provided selectbox.

```python
if st.session_state.current_page == "Dashboard":
    st.title("Workforce AI-Readiness Dashboard")
    st.markdown(f"Gain a high-level overview of your workforce's AI-Readiness, broken down by key organizational groups.")
    st.markdown(f"")
    st.header("Aggregated AI-Readiness Report")
    st.markdown(f"The 'Workforce AI-Readiness Report' summarizes the aggregated AI-R scores, providing a high-level overview of the organization's AI-readiness across different segments.")

    st.session_state.report_group_by = st.selectbox(
        "Group AI-Readiness Report by:",
        ['job_role', 'department'],
        index=0 if st.session_state.report_group_by == 'job_role' else 1,
        key='dashboard_group_by_select'
    )

    ai_r_summary_report = generate_ai_r_report_summary(st.session_state.df_employees, st.session_state.report_group_by)
    st.dataframe(ai_r_summary_report)
    st.markdown(f"Average AI-R score for the entire workforce: **{st.session_state.df_employees['current_ai_r_score'].mean():.2f}**")
```

The `generate_ai_r_report_summary` function (from `source.py`) calculates the average `current_ai_r_score`, `vr_score`, and `hr_r_score` for the selected grouping. This gives a quick insight into which groups are performing well or lagging in overall AI-Readiness, and whether that's driven by individual capabilities ($V^R$) or market opportunity ($H^R$).

### Skills Gap Analysis Heatmap
This heatmap visualizes the average scores for Idiosyncratic Readiness ($V^R$) sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity) across different employee groups. The heatmap offers a granular view, clearly highlighting which $V^R$ sub-components are strong or weak within specific job roles/departments, thereby pinpointing areas for targeted upskilling efforts.

```python
    st.header("Skills Gap Analysis Heatmap")
    st.markdown(f"This heatmap visualizes the average scores for Idiosyncratic Readiness ($V^R$) sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity) across different employee groups.")
    st.markdown(f"The heatmap offers a granular view, clearly highlighting which $V^R$ sub-components are strong or weak within specific job roles/departments, thereby pinpointing areas for targeted upskilling efforts.")
    
    fig_heatmap, ax_heatmap = plt.subplots(figsize=(10, 6))
    vr_sub_components = ['ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score']
    heatmap_data = st.session_state.df_employees.groupby(st.session_state.report_group_by)[vr_sub_components].mean()
    sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt=".1f", linewidths=.5, ax=ax_heatmap)
    ax_heatmap.set_title(f'Average $V^R$ Sub-Component Scores by {st.session_state.report_group_by}')
    ax_heatmap.set_ylabel(st.session_state.report_group_by)
    ax_heatmap.set_xlabel('$V^R$ Sub-Component')
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig_heatmap)
    plt.close(fig_heatmap)
```

The heatmap uses `seaborn` to visualize the average scores of `ai_fluency_score`, `domain_expertise_score`, and `adaptive_capacity_score` (all sub-components of $V^R$) grouped by your selected category. This visual representation quickly reveals strengths (darker colors) and weaknesses (lighter colors) in specific skill areas across different parts of the organization.

<aside class="positive">
<b>Best Practice:</b> Regularly review the Dashboard to identify emerging skill gaps and overall AI-Readiness trends. Use the grouping feature to pinpoint specific departments or job roles that require immediate attention or targeted training initiatives.
</aside>

## What-If Scenario Engine
Duration: 12:00

The "What-If Scenario Engine" section in the sidebar allows you to simulate the impact of learning pathways on individual employee AI-Readiness scores. This dynamic tool helps assess potential improvements to $V^R$ sub-components and the overall AI-R score.

The simulation uses the following formula to project future AI-R scores:

$$AI-R_{i,t+1} = AI-R_{i,t} + \sum_{p \in P} \Delta_p \cdot Completion_p \cdot Mastery_p$$

where $\Delta_p$ is the pre-calibrated impact coefficient for pathway $p$ (from `df_pathways`), $Completion_p \in [0,1]$ is the fraction completed, and $Mastery_p \in [0,1]$ is the assessment performance score. The pathway impact ($\Delta_p$) will directly affect the AI-Fluency, Domain-Expertise, or Adaptive-Capacity scores, which then propagate to $V^R$ and subsequently AI-R.

This simulation demonstrates the predictive power of the framework, allowing leaders to evaluate the effectiveness of different training programs. By adjusting completion and mastery rates, they can gain insights into the potential ROI of various learning investments and tailor programs to maximize workforce AI-readiness.

You can select an employee, a learning pathway, and adjust the expected completion and mastery rates.

```python
elif st.session_state.current_page == "What-If Scenario":
    st.title("What-If Scenario Engine")
    st.markdown(f"Simulate the impact of learning pathways on individual employee AI-Readiness scores.")
    st.markdown(f"")
    st.header("Simulating Learning Pathway Impact")
    st.markdown(f"The 'What-If' scenario engine allows HR leaders to simulate the impact of various training programs and learning pathways on an individual's AI-Readiness. ...")
    st.markdown(r"$$AI-R_{i,t+1} = AI-R_{i,t} + \sum_{p \in P} \Delta_p \cdot Completion_p \cdot Mastery_p$$")
    # ... (more explanation of formula)

    employee_ids = st.session_state.df_employees['employee_id'].tolist()
    selected_employee_id = st.selectbox(
        "Select Employee:",
        employee_ids,
        index=default_employee_index_whatif,
        key='whatif_employee_select'
    )
    st.session_state.selected_employee_id_whatif = selected_employee_id

    pathway_names = st.session_state.df_pathways['pathway_name'].tolist()
    # ... (logic to handle pathway selection)
    if pathway_names:
        selected_pathway_name = st.selectbox(
            "Select Learning Pathway:",
            pathway_names,
            index=default_pathway_index_whatif,
            key='whatif_pathway_select'
        )
        selected_pathway_id = pathway_map.get(selected_pathway_name, "N/A")
    else:
        st.warning("No learning pathways available.")
        selected_pathway_id = "N/A"
    st.session_state.selected_pathway_id_whatif = selected_pathway_id

    completion_rate = st.slider("Completion Rate", 0.0, 1.0, st.session_state.completion_rate_whatif, 0.05, key='whatif_completion_rate')
    st.session_state.completion_rate_whatif = completion_rate

    mastery_score = st.slider("Mastery Score", 0.0, 1.0, st.session_state.mastery_score_whatif, 0.05, key='whatif_mastery_score')
    st.session_state.mastery_score_whatif = mastery_score

    if st.button("Simulate Pathway Impact"):
        if st.session_state.selected_employee_id_whatif != "N/A" and st.session_state.selected_pathway_id_whatif != "N/A":
            # ... (logic to call simulate_pathway_impact and store results)
        else:
            st.warning("Please ensure an employee and a pathway are selected for simulation.")

    if st.session_state.whatif_results and st.session_state.whatif_results["selected_employee_id"] == st.session_state.selected_employee_id_whatif:
        res = st.session_state.whatif_results
        st.subheader("Simulation Results:")
        st.markdown(f"Employee ID: **{res['selected_employee_id']}**")
        st.markdown(f"Current AI-R Score: **{res['current_ai_r']:.2f}**")
        st.markdown(f"Chosen Pathway: **{res['pathway_name']}**")
        st.markdown(f"Projected AI-R Score: **{res['projected_ai_r']:.2f}**")
        st.markdown(rf"Change in AI-R ($\Delta$AI-R): **{res['delta_ai_r']:.2f}**")

        fig_whatif, ax_whatif = plt.subplots(figsize=(8, 5))
        # ... (plotting logic for bar chart)
        st.pyplot(fig_whatif)
        plt.close(fig_whatif)
```

After simulation, the results are displayed, showing the current AI-R, projected AI-R, and the change in AI-R. A bar chart visually compares the current and projected scores.

<aside class="negative">
<b>Warning:</b> The accuracy of 'What-If' scenarios heavily relies on the quality and calibration of `Delta_p` (pathway impact coefficients), as well as realistic estimates for completion and mastery rates. Inaccurate inputs can lead to misleading projections.
</aside>

## Multi-Step Pathway Optimization
Duration: 15:00

The "Pathway Optimization" section in the sidebar is designed for more complex development. It helps identify an optimal sequence of learning pathways for a selected employee, balancing AI-R improvement with time and cost constraints. This generates a strategic roadmap for talent investment.

For complex skill transitions or broader workforce development, identifying an optimal sequence of learning pathways is crucial. This involves balancing AI-R improvement with constraints like total cost and time. The multi-step pathway optimization problem can be formulated as:

$$\max_{P_1,...,P_K} AI-R(P_1,..., P_K) - \lambda_{\text{cost}} \cdot \sum_{k=1}^K Cost(P_k)$$

subject to:
$$ \sum_{k=1}^K Time(P_k) \leq T_{\text{max}} $$
$$ P_k \in P_{\text{feasible}} $$
$$ Prerequisites(P_k) \subseteq \{P_1,...,P_{k-1}\} $$

For this application, a simplified greedy optimization strategy is implemented to identify a sequence of pathways that maximizes AI-R improvement within a given time budget, considering the cost.

The pathway optimization function provides a strategic roadmap for investing in talent development. By considering multiple pathways, their costs, and time commitments, organizations can make data-driven decisions to maximize the AI-Readiness of their workforce efficiently, identifying high-ROI learning initiatives.

You can select an employee, set a maximum time budget for learning, and adjust the `cost_weight_lambda` to control the importance of cost in the optimization.

```python
elif st.session_state.current_page == "Pathway Optimization":
    st.title("Multi-Step Pathway Optimization")
    st.markdown(f"Generate an optimized sequence of learning pathways to maximize AI-Readiness within defined constraints.")
    st.markdown(f"")
    st.header("Multi-Step Pathway Optimization")
    st.markdown(f"For complex skill transitions or broader workforce development, identifying an optimal sequence of learning pathways is crucial. ...")
    st.markdown(r"$$\max_{P_1,...,P_K} AI-R(P_1,..., P_K) - \lambda_{\text{cost}} \cdot \sum_{k=1}^K Cost(P_k)$$")
    # ... (more explanation of constraints)

    employee_ids_opt = st.session_state.df_employees['employee_id'].tolist()
    selected_employee_id_opt = st.selectbox(
        "Select Employee for Optimization:",
        employee_ids_opt,
        index=default_employee_index_opt,
        key='opt_employee_select'
    )
    st.session_state.selected_employee_id_opt = selected_employee_id_opt

    T_max_hours = st.slider("Maximum Time (hours)", 50, 500, st.session_state.T_max_hours_opt, 10, key='opt_max_time')
    st.session_state.T_max_hours_opt = T_max_hours

    cost_weight_lambda = st.slider(r"Cost Weight ($\lambda_{\text{cost}}$)", 0.001, 0.01, st.session_state.cost_weight_lambda_opt, 0.001, key='opt_cost_weight', format="%.3f")
    st.session_state.cost_weight_lambda_opt = cost_weight_lambda

    if st.button("Optimize Pathways"):
        if st.session_state.selected_employee_id_opt != "N/A":
            # ... (logic to call optimize_pathway_sequence and store results)
        else:
            st.warning("Please select an employee for optimization.")

    if st.session_state.optimization_results and st.session_state.optimization_results["selected_employee_id"] == st.session_state.selected_employee_id_opt:
        opt_res = st.session_state.optimization_results
        st.subheader("Optimization Results:")
        st.markdown(f"Employee ID: **{opt_res['selected_employee_id']}**")
        st.markdown(f"Current AI-R Score: **{opt_res['current_ai_r']:.2f}**")
        st.markdown(f"Recommended Pathway Sequence: **{', '.join(opt_res['recommended_sequence']) if opt_res['recommended_sequence'] else 'No pathways recommended within constraints'}**")
        st.markdown(f"Projected Final AI-R: **{opt_res['projected_final_ai_r']:.2f}**")
        st.markdown(f"Total Cost: **${opt_res['total_cost']:.2f}**")
        st.markdown(f"Total Time (hours): **{opt_res['total_time_hours']:.2f}**")
        st.markdown(f"AI-R Improvement: **{opt_res['ai_r_improvement']:.2f}**")

        fig_opt, ax_opt = plt.subplots(figsize=(8, 5))
        # ... (plotting logic for bar chart)
        st.pyplot(fig_opt)
        plt.close(fig_opt)
```

The optimization results include the recommended pathway sequence, projected final AI-R, total cost, total time, and the overall AI-R improvement. A bar chart is generated to compare the current and projected AI-R scores after the optimized sequence.

<aside class="positive">
<b>Tip:</b> Experiment with different `Maximum Time (hours)` and `Cost Weight ($\lambda_{\text{cost}}$)` values to understand the trade-offs between AI-R improvement, budget, and time. This helps in formulating realistic and impactful upskilling strategies.
</aside>

## Strategic Recommendations & Conclusion
Duration: 08:00

The final "Strategic Recommendations" section in the sidebar provides synthesized insights and actionable recommendations for targeted upskilling initiatives and overall workforce development plans. This section leverages the data-driven analysis from the previous steps to offer concrete strategies.

Based on the AI-Readiness assessment, skills gap analysis, and 'What-If' scenario simulations, we can formulate strategic recommendations for workforce development. These insights move beyond static skill inventories, providing a dynamic framework for continuous adaptation in an AI-transformed landscape.

### Summary of Insights:

#### 1. Target Low AI-R Cohorts with Driver-Specific Interventions
Identify employees with significantly lower AI-R scores and analyze whether their low score is primarily driven by low Idiosyncratic Readiness ($V^R$) or insufficient Systematic Opportunity ($H^R$) in their current role. Tailor interventions accordingly.
*   **Action:** For employees with low $V^R$, recommend AI-Fluency focused training. For those with low $H^R$, consider internal mobility options or upskilling for roles with higher market opportunity.

#### 2. Address Critical Skills Gaps via Targeted Upskilling
Based on the Skills Gap Heatmap (from the Dashboard), common weaknesses can be identified. For instance, if 'Business Analyst' roles show lower 'Adaptive-Capacity' scores, a targeted training program focusing on 'Strategic Career Management' or 'Cognitive Flexibility' would be beneficial.
*   **Example:** If 'Data Scientist' roles generally excel in 'AI-Fluency' but show gaps in 'Domain-Expertise', prioritize advanced domain-specific AI applications and certifications.

#### 3. Implement Optimized Multi-Step Learning Pathways
If an optimization has been run, the specific recommended sequence and its projected impact are highlighted.
*   **Action:** Leverage such optimized pathways to guide individual career development plans, balancing cost, time, and impact.

#### 4. Invest Strategically in High Opportunity, Low Readiness Roles
Identify job roles that have high Systematic Opportunity ($H^R$) but where the current workforce has lower Idiosyncratic Readiness ($V^R$). These are prime candidates for strategic investment.
*   **Action:** For these roles, focused upskilling on AI-Fluency and Domain-Expertise (specific to the high $H^R$ area) will yield high returns.

#### 5. Foster Continuous Learning and Adaptive Capacity
The rapid pace of AI evolution necessitates a workforce with strong adaptive capacities. Emphasize training that builds cognitive flexibility, social-emotional intelligence for human-AI collaboration, and strategic career management skills across all employee levels.
*   **Action:** Integrate 'Adaptive-Capacity' boosting modules into all major learning initiatives and promote a culture of continuous learning and experimentation.

The relevant Streamlit code for this section is displayed when `st.session_state.current_page == "Strategic Recommendations"`:

```python
elif st.session_state.current_page == "Strategic Recommendations":
    st.title("Strategic Recommendations & Conclusion")
    st.markdown(f"Leverage data-driven insights to formulate actionable strategies for AI workforce development.")
    st.markdown(f"")
    st.header("Strategic Recommendations for AI Workforce Development")
    # ... (content for each recommendation point)
    st.subheader("1. Target Low AI-R Cohorts with Driver-Specific Interventions")
    low_ai_r_cohorts = st.session_state.df_employees.sort_values(by='current_ai_r_score').head(5)
    st.markdown(f"**Example: Top 5 Employees with Lowest AI-R Scores**")
    st.dataframe(low_ai_r_cohorts[['employee_id', 'job_role', 'department', 'current_ai_r_score', 'vr_score', 'hr_r_score']].set_index('employee_id'))
    st.markdown(f"*   **Action:** For employees with low $V^R$, recommend AI-Fluency focused training. For those with low $H^R$, consider internal mobility options or upskilling for roles with higher market opportunity.")

    # ... (similar structures for other recommendations)

    st.markdown("")
    st.markdown(f"This application provides a robust, quantitative framework for proactive workforce planning. By dynamically assessing AI-Readiness, analyzing skill gaps, and simulating training impacts, organizations can make informed investments in their human capital, ensuring competitiveness and adaptability in the evolving AI landscape. The framework's flexibility allows for continuous recalibration and adaptation as market demands and individual capabilities evolve.")
```

This application provides a robust, quantitative framework for proactive workforce planning. By dynamically assessing AI-Readiness, analyzing skill gaps, and simulating training impacts, organizations can make informed investments in their human capital, ensuring competitiveness and adaptability in the evolving AI landscape. The framework's flexibility allows for continuous recalibration and adaptation as market demands and individual capabilities evolve.

Congratulations! You have now completed the QuLab: AI Workforce Readiness & Upskilling Strategizer codelab. You should have a comprehensive understanding of the AI-R framework and how to utilize this Streamlit application to drive strategic workforce development in the age of AI.
