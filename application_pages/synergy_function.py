
import streamlit as st

def run_page():
    st.title("Synergy Function")
    st.header("Conceptual Basis")
    st.markdown("The Synergy function captures the multiplicative benefits when individual readiness ($V^R$) aligns with market opportunity ($H^R$). It is defined as:")
    st.markdown(r"$$Synergy\%(V^R, H^R) = \frac{V^R \times H^R}{100} \times Alignment_i$$")
    st.markdown(r"where both $V^R$ and $H^R$ are on $[0,100]$ scale, and $Alignment_i \in [0,1]$ ensures $Synergy\% \in [0,100]$.")
    st.markdown("The Synergy score formalizes the idea that career success is more than just individual capability plus market demand; it also depends on how well these two factors align. A high synergy score indicates a 'sweet spot' where an individual's unique skills and career stage perfectly intersect with market opportunities.")

    st.subheader("Alignment Factor: Skills Match & Timing Factor")
    st.markdown("The $Alignment_i$ factor measures how well individual skills match occupation requirements and career stage:")
    st.markdown(r"$$Alignment_i = \frac{\text{Skills Match Score}_i}{\text{Maximum Possible Match}} \times \text{Timing Factor}_i$$")
    st.markdown("**1. Skills Match Score:** Using O*NET-like task-skill mappings (simulated through `skill_a` to `skill_j` in our synthetic data), we compute:")
    st.markdown(r"$$Match_i = \sum_{s \in S} \min(\text{Individual Skill}_{i,s}, \text{Required Skill}_{o,s}) \cdot \text{Importance}_s$$")
    st.markdown("where $S$ is the set of all skills, and the minimum operator ensures that excess skill in one area doesn't compensate for deficiency in critical areas. For `Maximum Possible Match`, we assume a perfect match of 1.0 (after normalization of individual and required skills to 0-1).")
    st.markdown("**2. Timing Factor:** Career stage affects transition ease:")
    st.markdown(r"$$Timing(y) = \begin{cases} 1.0 & \text{if } y \in [0,5] \text{ (early career)} \\ 1.0 & \text{if } y \in (5,15] \text{ (mid-career)} \\ 0.8 & \text{if } y > 15 \text{ (late career, transition friction)} \end{cases}$$")
    st.markdown("where $y$ is years of experience. Note that all timing values are $\leq 1.0$ to ensure Alignment remains bounded at $[0, 1]$.")
    st.markdown("The Alignment Factor provides a nuanced measure of how well an individual's skills and career stage align with a specific occupational target. This factor is critical for determining the true 'fit' and the potential for synergy between an individual's readiness and market opportunity.")
