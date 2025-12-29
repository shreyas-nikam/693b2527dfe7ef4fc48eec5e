id: 693b2527dfe7ef4fc48eec5e_user_guide
summary: AI Readiness score User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: AI-Readiness Career Navigator

## 1. Introduction to AI-Readiness and Alice's Journey
Duration: 00:05:00

Welcome to the **AI-Readiness Career Navigator**! This tool is designed to help professionals strategically navigate the rapidly evolving landscape of AI-enabled roles, particularly in financial services. Understanding how to adapt and leverage AI is crucial for long-term career success. This application provides a data-driven framework to assess your current AI-readiness, identify high-opportunity career paths, pinpoint skill gaps, and optimize a personalized learning strategy.

<aside class="positive">
<b>Why is this important?</b> The integration of AI is creating new roles and transforming existing ones across industries. This tool helps you gain clarity on your career trajectory in the age of AI, ensuring your professional development efforts are impactful.
</aside>

You will step into the shoes of **Alice, a Senior Quantitative Analyst at QuantFinance Innovations**. Alice has a strong background but is keen to advance her career by leveraging AI. She needs guidance on which AI-enabled roles offer the best prospects and what specific skills she needs to acquire. This codelab will guide you through the process, helping Alice make informed decisions.

The core of this analysis is the **AI-Readiness Score (AI-R)**, a novel framework that quantifies an individual's preparedness for AI-enabled careers. It breaks down career opportunity into two main components:

*   **Idiosyncratic Readiness ($V^R$)**: This represents your individual-specific capabilities, skills, and preparedness. This is the part you can actively influence through learning and development.
*   **Systematic Opportunity ($H^R$)**: This represents macro-level job growth, market demand, and industry trends for specific roles. This is about identifying where the opportunities lie in the market.

The framework also incorporates a **Synergy Function** to capture the compounding benefits when individual preparation aligns with market opportunity. The overall AI-R is calculated using the following formula:

$$AI-R_{i,t} = \alpha \cdot V_i^R(t) + (1 - \alpha) \cdot H_{i}^R(t) + \beta \cdot Synergy\%(V_i^R, H_{i}^R)$$

where:
*   $V_i^R(t)$ is Idiosyncratic Readiness (individual capability), normalized to $[0, 100]$.
*   $H_i^R(t)$ is Systematic Opportunity (market demand) for the target occupation, normalized to $[0, 100]$.
*   $\alpha \in [0,1]$ is the weight on individual vs. market factors. The default is $\alpha = 0.6$.
*   $\beta > 0$ is the synergy coefficient, capturing multiplicative benefits. The default is $\beta = 0.2$.
*   $Synergy\% \in [0,100]$ is in percentage units.

By completing this codelab, you will gain a personalized, data-driven career strategy, ensuring Alice's learning investments are impactful for high-opportunity roles in finance.

## 2. Defining Your Professional Profile and Target Roles
Duration: 00:08:00

In this step, you will define Alice's professional profile, including her education, experience, skill levels, and the AI-enabled roles she is considering. This information forms the foundation for calculating her initial AI-Readiness.

Navigate to the **"Profile & Goals"** tab in the application.

### 2.1. Professional Background

On the left side, you'll find sections to define Alice's professional background.

*   **General Information**:
    *   **Education Level**: Select Alice's highest education level from the dropdown. For this codelab, Alice has a 'Master\'s in Finance'.
    *   **Years of Experience**: Input her total years of professional experience. Alice has 7 years of experience.
*   **AI-Fluency Sub-Factors**: These sliders (ranging from 0 to 1) represent different aspects of Alice's ability to interact with and understand AI. Adjust these sliders to reflect her proficiency in areas like `prompting`, `AI tools`, `understanding`, `data literacy`, `AI-augmented productivity`, `critical AI judgment`, `appropriate trust decisions`, `proficiency gain`, and `hours invested`.
*   **Domain-Expertise Sub-Factors**: These sliders (0 to 1) represent aspects of her expertise within her specific financial domain, such as `portfolio management`, `industry recognition`, and `credentials`.
*   **Adaptive-Capacity Sub-Factors**: These sliders (0 to 1) assess her "meta-skills" vital for adapting to change, including `cognitive flexibility`, `social-emotional intelligence`, and `strategic career management`.

### 2.2. Current Skill Levels

On the right side, you'll see sliders (0 to 10) for various **Current Skill Levels**. These represent Alice's proficiency in key technical and domain-specific skills. Review and adjust these to accurately reflect her current capabilities in areas like `Python`, `SQL`, `ML_basics`, `Risk_Analysis`, `Financial_Modeling`, `Data_Viz`, `Quant_Models`, `AI_Ethics`, `GenAI_Tools`, and `Cloud_Platforms`.

### 2.3. Target AI-Enabled Financial Roles

Below the skills, use the multi-select box to choose the **Target AI-Enabled Financial Roles** Alice is considering. These are the roles for which the application will calculate her AI-Readiness Score. For this exercise, the default roles are a good starting point, but feel free to explore others.

### 2.4. Calculate Initial Readiness & Opportunity

Once you've reviewed and adjusted Alice's profile and target roles, click the **"Calculate Initial Readiness & Opportunity"** button.

<aside class="positive">
<b>What happens next?</b> Clicking this button triggers the calculation of Alice's individual Idiosyncratic Readiness ($V^R$) based on her profile and the Systematic Opportunity ($H^R$) for each of her selected target roles. This is the essential first step before evaluating overall career opportunities.
</aside>

You will see a success message once the calculations are complete.

## 3. Evaluating Opportunities: AI-Readiness, VR, HR & Skill Gaps
Duration: 00:10:00

Now that Alice's initial readiness and market opportunities have been calculated, this step focuses on synthesizing these components into a comprehensive AI-Readiness Score (AI-R) for each target role and identifying specific skill gaps.

Navigate to the **"Opportunity Evaluation"** tab.

<aside class="negative">
If you see a warning to "Please go to 'Profile & Goals' tab and calculate initial readiness", go back to the previous tab and click the "Calculate Initial Readiness & Opportunity" button.
</aside>

### 3.1. Idiosyncratic Readiness ($V^R$) Breakdown

This section shows Alice's **Idiosyncratic Readiness ($V^R$)** score and its breakdown into three main components: AI-Fluency, Domain-Expertise, and Adaptive-Capacity.

The formula for $V^R$ is:
$$V^R(t) = w_1 \cdot AI‑Fluency_i(t) + w_2 \cdot Domain‑Expertise_i(t) + w_3 \cdot Adaptive‑Capacity_i(t)$$
where $w_1 = 0.35$, $w_2 = 0.40$, $w_3 = 0.25$.

*   **Total VR Score**: This is Alice's overall individual capability score.
*   **AI-Fluency**: Reflects her ability to understand and interact with AI.
*   **Domain-Expertise**: Measures her knowledge and experience in her financial sector.
*   **Adaptive-Capacity**: Indicates her meta-skills for adapting to change.

<aside class="positive">
<b>Interpreting VR:</b> A high $V^R$ score indicates a strong individual foundation for AI-enabled roles. It's important to understand the breakdown to identify areas of strength and areas that might need development.
</aside>

### 3.2. Systematic Opportunity ($H^R$) by Target Role

This section presents the **Systematic Opportunity ($H^R$)** score for each of Alice's selected target roles. This score reflects external market conditions, job growth, and demand.

The formula for $H^R$ is:
$$H^R(t) = H_{base}(O_{target}) \cdot M_{growth}(t) \cdot M_{regional}(t)$$
where $H_{base}(o)$ is the base opportunity score, $M_{growth}(t)$ is the growth multiplier, and $M_{regional}(t)$ is the regional multiplier.

You will see a table displaying the $H^R$ score for each role. Roles with higher $H^R$ scores generally indicate greater market demand and growth potential.

### 3.3. Overall AI-Readiness ($AI-R$) Scores and Skill Gaps

This is where the individual capabilities ($V^R$) are combined with market opportunities ($H^R$) to calculate the comprehensive **AI-Readiness Score (AI-R)** for each role. The synergy function also comes into play here:

$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$
where $V^R$ and $H^R$ are normalized to $[0, 100]$, and $Alignment_i \in [0,1]$ combines skill match and timing.

You will see:
*   A **table** summarizing the `AI-R Score` for each target role, along with its contributing components (`VR_Score`, `HR_Score`, `Skills_Match_Score`, `Alignment_Score`, `Synergy_Score`).
*   The **"Top AI-R Role"** recommendation, which is the role with the highest AI-R score.
*   A **bar chart** visually comparing the AI-R, VR, and HR scores across all target roles. This helps Alice see at a glance which roles offer the best overall readiness based on her profile and market demand.
*   A **radar chart** illustrating the **Skill Gaps** for the recommended top role. This chart compares Alice's `Current Skill Level` against the `Required Skill Level` for that specific role.

<aside class="positive">
<b>Interpreting Skill Gaps:</b> Areas where the "Required Skill Level" polygon extends significantly beyond the "Current Skill Level" polygon represent critical skill gaps that Alice needs to address to be fully prepared for that role.
</aside>

This analysis provides a clear understanding of Alice's current standing and the specific areas she needs to focus on for her most promising career paths.

## 4. Optimizing Learning Pathways for Career Growth
Duration: 00:10:00

With Alice's AI-Readiness assessed and skill gaps identified, the next step is to strategize her learning. This section helps optimize a personalized learning pathway that maximizes her projected AI-R gain under specific time and budget constraints.

Navigate to the **"Learning Optimization"** tab.

<aside class="negative">
If you see a warning to "Please go to 'Opportunity Evaluation' tab to identify the top role first", ensure you have completed the previous tab's calculations.
</aside>

The objective here is to maximize the gain in AI-R minus a weighted cost, subject to time and budget limits:

$$ \max_{P_1,...,P_K} (AI‑R_{proj} - AI‑R_{current}) - \lambda \cdot \sum_{k=1}^K Cost(p_k) $$

subject to:
$$ \sum_{k=1}^K Time(p_k) \le T_{max} $$
$$ \sum_{k=1}^K Cost(p_k) \le B_{max} $$
$$ p_k \in P_{feasible} $$
$$ Prerequisites(p_k) \subseteq \{P_1,...,P_{k-1}\} $$

where $AI‑R_{proj}$ is the projected AI-R after completing pathways, $AI‑R_{current}$ is her initial AI-R, $\lambda$ is the `Cost Weight (Lambda)`, $T_{max}$ is `Maximum Learning Time (hours)`, and $B_{max}$ is `Maximum Learning Budget (USD)`.

### 4.1. Set Learning Constraints

You'll see the **Target Role for Optimization** (Alice's top AI-R role) and her initial AI-R for this role.
Below this, set the following constraints for the learning optimization:

*   **Maximum Learning Time (hours)**: The total number of hours Alice can realistically commit to learning. The default is 200 hours.
*   **Maximum Learning Budget (USD)**: The total budget Alice has for learning resources. The default is $1000.
*   **Cost Weight (Lambda - higher means more cost-averse)**: This slider allows you to prioritize minimizing cost over maximizing AI-R gain. A higher lambda means the optimization will penalize cost more heavily. The default is 0.05.

### 4.2. Optimize Learning Pathway

Once the constraints are set, click the **"Optimize Learning Pathway"** button.
The application will then run a greedy heuristic to recommend a sequence of learning activities.

Upon completion, you will see:
*   A list of **Recommended Optimal Learning Pathways**, detailing each course or resource, its type, estimated time, and cost.
*   **Total estimated time investment** and **total estimated cost investment**.
*   **Initial AI-R** and **Projected AI-R** after completing the recommended pathways, along with the estimated improvement.
*   A **bar chart** visually comparing Alice's `Current AI-R` vs. `Projected AI-R` for her target role after undertaking the optimized learning path.

<aside class="positive">
<b>Understanding the Optimization:</b> The algorithm selects pathways that offer the best "return" (AI-R gain per unit of weighted time/cost) until the constraints are met, while also respecting any prerequisites between learning paths.
</aside>

This step helps Alice make a data-driven decision on how to invest her time and money for maximum career impact.

## 5. "What-If" Scenario Analysis
Duration: 00:08:00

Alice wants to explore alternative career and learning strategies beyond the initial optimal recommendation. The "What-If" scenario engine allows her to compare different choices, understand trade-offs, and see how they impact her projected AI-R. This functionality helps in making robust career decisions.

Navigate to the **"What-If Analysis"** tab.

<aside class="negative">
If you see a warning about initial readiness, please go back to the "Profile & Goals" tab and ensure you have clicked "Calculate Initial Readiness & Opportunity".
</aside>

### 5.1. Define Custom Scenarios

This section allows you to create and compare custom "What-If" scenarios.

*   **Select a Target Role for this Scenario**: Choose an AI-enabled role that Alice might consider.
*   **Select Learning Pathways for this Scenario**: From the available list of learning pathways, select a custom set that Alice might undertake for the chosen role.

### 5.2. Run Custom Scenario Analysis

After defining your scenario, click the **"Run Custom Scenario Analysis"** button. The application will calculate the projected AI-R, time, and cost for this custom scenario.

<aside class="positive">
<b>Comparing Scenarios:</b> The results will automatically include the "Optimized for [Top Role]" scenario (if you ran the optimization in the previous step) alongside your custom scenario, allowing for direct comparison.
</aside>

### 5.3. Scenario Analysis Results

Once the analysis is complete, you will see:
*   A **table summarizing the `Scenario Analysis Results`**, including the `Projected AI-R`, `Projected VR`, `HR`, `Time (h)`, and `Cost ($)` for each scenario.
*   A **bar chart** titled "Comparative Projected AI-R for Different Career/Learning Scenarios," which visually compares the projected AI-R for all run scenarios.
*   A **table showing the `Return on Learning Investment (ROI)`**, which calculates `AI-R Gain`, `Investment Score`, and `ROI` for each scenario.
*   A **bar chart** titled "Return on Learning Investment for Different Scenarios," visualizing the ROI.

<aside class="positive">
<b>Interpreting ROI:</b> ROI is calculated as `AI-R Gain / Weighted Investment`. A higher ROI indicates a more efficient use of resources (time and cost) to achieve AI-R improvement. This helps Alice understand which learning paths provide the most "bang for her buck."
</aside>

This analysis empowers Alice to make a data-driven decision, weighing projected career opportunities against the required investment in time and cost for various strategies.

## 6. Personalized AI Career Strategy Report
Duration: 00:03:00

This final step consolidates all the analysis into a clear, actionable report for Alice, summarizing her current standing, identified skill gaps, and the recommended optimal learning pathway with projected outcomes.

Navigate to the **"Summary Report"** tab.

<aside class="negative">
If you see a warning to "Please complete the previous steps to generate a full report," navigate through the previous tabs and ensure all calculations and optimizations have been run.
</aside>

The report will include:

### 6.1. Current AI-Readiness Profile
This section provides a summary of Alice's calculated Idiosyncratic Readiness ($V^R$) and its components, as well as the Systematic Opportunity ($H^R$) for her target roles.

### 6.2. Top AI-Enabled Career Path Recommendation
This highlights the recommended role (the one with the highest AI-R score), her initial AI-R for this role, and the projected AI-R after undertaking the optimal learning pathway (if optimization was run).

### 6.3. Detailed Skill Gaps for [Top Role Name]
A table showing the specific skills where Alice has a gap (where `required` skill level is higher than `current`). This is a direct, actionable list for her development efforts.

### 6.4. Recommended Optimal Learning Pathway
A list of the learning pathways identified by the optimization engine, along with the total estimated time and cost investment.

### 6.5. "What-If" Scenario Analysis Summary
A table summarizing the results of any "What-If" scenarios you ran, offering a quick comparison of different strategies.

<aside class="positive">
<b>Actionable Insights:</b> This report serves as a personalized roadmap for Alice. It clearly identifies her strengths, areas for development, the most promising career directions, and a concrete plan for achieving her career goals through targeted learning.
</aside>

** End of Report **
