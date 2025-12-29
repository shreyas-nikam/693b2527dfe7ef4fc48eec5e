
import streamlit as st

def run_page():
    st.title("The AI-Readiness Framework: Core Concepts")
    st.header("Introduction to the AI-Readiness Framework")
    st.markdown("The AI-Readiness Score (AI-R) is a novel parametric framework designed to quantify an individual's preparedness for success in AI-enabled careers. It decomposes career opportunity into two orthogonal components: Systematic Opportunity ($H^R$), representing macro-level job growth and demand, and Idiosyncratic Readiness ($V^R$), representing individual-specific capabilities. A Synergy factor captures the multiplicative benefits when individual readiness aligns with market opportunity.")
    st.markdown(r"The core formula for the AI-Readiness Score for individual $i$ at time $t$ is defined as:$$AI-R_{i,t} = \alpha \cdot V^R_{i}(t) + (1 - \alpha) \cdot H^R(t) + \beta \cdot Synergy\%(V^R, H^R)$$")
    st.markdown("where:")
    st.markdown(r"*   $V^R_{i}(t)$: Idiosyncratic Readiness (individual capability).")
    st.markdown(r"*   $H^R(t)$: Systematic Opportunity (market demand).")
    st.markdown(r"*   $\alpha \in [0,1]$: Weight on individual vs. market factors. For this notebook, we'll use $\alpha = 0.6$.")
    st.markdown(r"*   $\beta > 0$: Synergy coefficient. For this notebook, we'll use $\beta = 0.15$.")
    st.markdown(r"*   Both $V^R$ and $H^R$ are normalized to $[0, 100]$.")
    st.markdown(r"*   $Synergy\% \in [0,100]$ (percentage units).")
    st.markdown("This framework allows for dynamic 'what-if' scenario planning, helping to guide targeted upskilling initiatives and talent development.")
    st.markdown("This section demonstrates how the final AI-R score is computed by combining the Idiosyncratic Readiness ($V^R$), Systematic Opportunity ($H^R$), and Synergy components, weighted by the parameters $\alpha$ and $\beta$. The example reflects a scenario where an individual has strong readiness in a high-opportunity field with good alignment, resulting in a high AI-R score.")
