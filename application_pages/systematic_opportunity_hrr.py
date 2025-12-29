
import streamlit as st

def run_page():
    st.title("Systematic Opportunity ($H^R$) Component")
    st.header("Conceptual Definition")
    st.markdown("Systematic Opportunity ($H^R$) represents the macro-level demand and growth potential in AI-enabled occupations. Following portfolio theory, this is analogous to market beta—an individual cannot create these opportunities through their own actions, but they can position themselves to benefit from favorable market conditions.")
    st.markdown(r"For individual $i$ targeting occupation $o_{target}$ at time $t$:$$H^R(t) = H_{\text{base}}(O_{\text{target}}) \cdot M_{\text{growth}}(t) \cdot M_{\text{regional}}(t)$$")
    st.markdown(r"where $H_{\text{base}}$ is the base opportunity score, $M_{\text{growth}}$ captures temporal momentum, and $M_{\text{regional}}$ adjusts for geographic factors.")

    st.subheader("Base Opportunity Score ($H_{\text{base}}$)")
    st.markdown(r"The Base Opportunity Score ($H_{\text{base}}(o)$) aggregates the various dimensions of occupational attractiveness: AI-Enhancement Potential, Job Growth Projections, Wage Premium, and Entry Accessibility. It is calculated as a weighted sum:$$H_{\text{base}}(o) = w_1 \cdot AI\text{-}Enhancement_o + w_2 \cdot Growth_{\text{normalized}} + w_3 \cdot Wage_o + w_4 \cdot Access_o$$")
    st.markdown(r"The weights ($w_j$) reflect the relative importance of each factor, as defined in the `PARAMS` dictionary ($w_1 = 0.30$, $w_2 = 0.30$, $w_3 = 0.25$, $w_4 = 0.15$). The final score is then scaled to $[0,100]$.")
    
    st.markdown("**1. AI-Enhancement Potential**")
    st.markdown("Measures how much AI augments rather than replaces tasks:")
    st.markdown(r"$$AI\text{-}Enhancement_o = \frac{1}{|T_o|} \sum_{t \in T_o} (1 - Automation_t) \cdot AI\text{-}Augmentation_t$$")
    st.markdown("where $T_o$ is the set of tasks for occupation $o$, $Automation_t \in [0,1]$ measures replaceability, and $AI\text{-}Augmentation_t \in [0,1]$ measures productivity enhancement. For simplicity in our synthetic data, we directly include an aggregated `ai_enhancement_potential` for each occupation.")
    st.markdown("This step demonstrates how the AI-Enhancement Potential, a key sub-component of $H^R$, is retrieved for a specific job role. This value reflects the degree to which AI is expected to augment, rather than automate, tasks within that occupation, indicating its future relevance.")
    
    st.markdown("**2. Job Growth Projections**")
    st.markdown("Quantify the expected increase or decrease in employment for an occupation over a given period (e.g., 10 years). The raw growth rate $g$ is calculated as:")
    st.markdown(r"$$Growth_o = \frac{\text{Projected Jobs}_{o,t+10} - \text{Current Jobs}_{o,t}}{\text{Current Jobs}_{o,t}}$$")
    st.markdown("This raw growth rate is then normalized to a scale of $[0, 100]$ using an affine transformation:")
    st.markdown(r"$$Growth_{\text{normalized}} = \frac{g + 0.5}{2.0} \times 100$$")
    st.markdown(r"This transformation maps a growth rate range of $g \in [-0.5, 1.5]$ (representing -50% to +150% change) to $[0,100]$.")
    st.markdown("The normalized job growth score provides a standardized measure of an occupation's future demand, directly contributing to its Systematic Opportunity. A higher normalized score indicates a greater projected increase in job availability, making the occupation more attractive in the AI-transformed labor market.")

    st.markdown("**3. Wage Premium & Entry Accessibility**")
    st.markdown("Two other critical factors contributing to Systematic Opportunity are Wage Premium and Entry Accessibility.")
    st.markdown(r"**Wage Premium** ($Wage_o$) measures the compensation potential for AI-skilled roles relative to the median wage in that occupation:$$Wage_o = \frac{\text{AI-skilled wage}_o - \text{median wage}_o}{\text{median wage}_o}$$")
    st.markdown("This provides an indication of the economic value placed on AI-related skills within a role.")
    st.markdown(r"**Entry Accessibility** ($Access_o$) quantifies the ease of transitioning into a role, based on typical educational and experience requirements:$$Access_o = 1 - \frac{\text{Education Years Required} + \text{Experience Years Required}}{10}$$")
    st.markdown("This linear formula provides a simplified measure, where a higher score indicates easier entry.")
    st.markdown("These calculations complete the primary sub-components of the Base Opportunity Score. Wage Premium highlights the financial attractiveness of an AI-enabled role, while Entry Accessibility provides insight into the practical barriers for individuals considering a transition, both being crucial for assessing Systematic Opportunity.")

    st.subheader("Dynamic Multipliers: Growth & Regional")
    st.markdown("Beyond the static Base Opportunity Score, Systematic Opportunity is modulated by dynamic, time-varying market factors:")
    st.markdown("**1. Growth Multiplier ($M_{\text{growth}}(t)$):** Captures market momentum based on recent changes in job postings.")
    st.markdown(r"$$M_{\text{growth}}(t) = 1 + \lambda \cdot \left( \frac{\text{Job Postings}_{o,t}}{\text{Job Postings}_{o,t-1}} - 1 \right)$$")
    st.markdown(r"where $\lambda = 0.3$ dampens volatility, keeping the multiplier typically between $0.7$ and $1.3$.")
    st.markdown("**2. Regional Multiplier ($M_{\text{regional}}(t)$):** Adjusts for local labor market conditions and remote work suitability.")
    st.markdown(r"$$M_{\text{regional}}(t) = \frac{\text{Local Demand}_{i,t}}{\text{National Avg Demand}} \times (1 + \gamma \cdot \text{Remote Work Factor}_o)$$")
    st.markdown(r"where $\gamma = 0.2$ and $Remote Work Factor \in [0,1]$ measures the occupation's suitability for remote work. For simplicity, we assume `Local Demand` equals `National Avg Demand` for the primary calculation and focus on the `Remote Work Factor` contribution.")
    st.markdown("The dynamic multipliers introduce responsiveness to market fluctuations. The Growth Multiplier reflects current hiring trends, while the Regional Multiplier accounts for geographical demand and the increasing prevalence of remote work. These factors ensure that the Systematic Opportunity score remains relevant to contemporary market conditions.")
    st.markdown(r"The final Systematic Opportunity score ($H^R(t)$) for an individual $i$ targeting occupation $o_{\text{target}}$ at time $t$ is calculated by combining the Base Opportunity Score with the dynamic multipliers.")
    st.markdown("This step completes the calculation of the Systematic Opportunity component for each employee, linking their current job role to market conditions. This score highlights external career potential that individuals can position themselves to capture.")
