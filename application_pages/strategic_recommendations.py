
import streamlit as st
import pandas as pd

def run_page():
    st.title("Strategic Recommendations & Conclusion")
    st.markdown("Leverage data-driven insights to formulate actionable strategies for AI workforce development.")
    st.markdown("---")
    st.header("Strategic Recommendations for AI Workforce Development")
    st.markdown("Based on the AI-Readiness assessment, skills gap analysis, and 'What-If' scenario simulations, we can formulate strategic recommendations for workforce development. These insights move beyond static skill inventories, providing a dynamic framework for continuous adaptation in an AI-transformed landscape.")
    st.markdown("**Summary of Insights:**")

    # Insight 1: Identify low AI-R cohorts and their drivers
    st.subheader("1. Target Low AI-R Cohorts with Driver-Specific Interventions")
    st.markdown("Identify employees with significantly lower AI-R scores and analyze whether their low score is primarily driven by low Idiosyncratic Readiness ($V^R$) or insufficient Systematic Opportunity ($H^R$) in their current role. Tailor interventions accordingly.")
    low_ai_r_cohorts = st.session_state.df_employees.sort_values(by='current_ai_r_score').head(5)
    st.markdown("**Example: Top 5 Employees with Lowest AI-R Scores**")
    st.dataframe(low_ai_r_cohorts[['employee_id', 'job_role', 'department', 'current_ai_r_score', 'vr_score', 'hr_r_score']].set_index('employee_id'))
    st.markdown("*   **Action:** For employees with low $V^R$, recommend AI-Fluency focused training. For those with low $H^R$, consider internal mobility options or upskilling for roles with higher market opportunity.")

    # Insight 2: Pinpoint critical skills gaps (references Dashboard insights)
    st.subheader("2. Address Critical Skills Gaps via Targeted Upskilling")
    st.markdown("Based on the Skills Gap Heatmap (from the Dashboard), common weaknesses can be identified. For instance, if 'Business Analyst' roles show lower 'Adaptive-Capacity' scores, a targeted training program focusing on 'Strategic Career Management' or 'Cognitive Flexibility' would be beneficial.")
    st.markdown("*   **Example:** If 'Data Scientist' roles generally excel in 'AI-Fluency' but show gaps in 'Domain-Expertise', prioritize advanced domain-specific AI applications and certifications.")

    # Insight 3: Recommend specific learning pathways (references Optimization results)
    st.subheader("3. Implement Optimized Multi-Step Learning Pathways")
    if st.session_state.optimization_results:
        opt_res = st.session_state.optimization_results
        st.markdown(f"For employee **{opt_res['selected_employee_id']}** (current AI-R: **{opt_res['current_ai_r']:.2f}**), the optimization identified the following sequence to maximize AI-R improvement within budget and time constraints:")
        st.markdown(f"*   **Recommended Pathway Sequence:** {\', \'.join(opt_res['recommended_sequence']) if opt_res['recommended_sequence'] else 'No pathways recommended'}")
        st.markdown(f"*   **Projected AI-R Improvement:** {opt_res['ai_r_improvement']:.2f}")
        st.markdown(f"*   **Total Cost:** ${opt_res['total_cost']:.2f}, **Total Time (hours):** {opt_res['total_time_hours']:.2f}")
    else:
        st.markdown("No pathway optimization has been run yet. Please use the 'Pathway Optimization' page to generate recommendations.")
    st.markdown("*   **Action:** Leverage such optimized pathways to guide individual career development plans, balancing cost, time, and impact.")

    # Insight 4: Highlight roles with high HR^R but low V^R
    st.subheader("4. Invest Strategically in High Opportunity, Low Readiness Roles")
    high_hr_low_vr_roles = st.session_state.df_employees[(st.session_state.df_employees['hr_r_score'] > 70) & (st.session_state.df_employees['vr_score'] < 60)]
    if not high_hr_low_vr_roles.empty:
        st.markdown("Identify job roles that have high Systematic Opportunity ($H^R$) but where the current workforce has lower Idiosyncratic Readiness ($V^R$). These are prime candidates for strategic investment.")
        st.markdown("**Example: Employees in High $H^R$ / Low $V^R$ Roles**")
        st.dataframe(high_hr_low_vr_roles[['employee_id', 'job_role', 'hr_r_score', 'vr_score', 'current_ai_r_score']].head().set_index('employee_id'))
        st.markdown("*   **Action:** For these roles, focused upskilling on AI-Fluency and Domain-Expertise (specific to the high $H^R$ area) will yield high returns.")
    else:
        st.markdown("All employees in this simulation appear to have a balanced $H^R$ and $V^R$, or no explicit high opportunity/low readiness roles were identified.")

    # Insight 5: Emphasize adaptive capacities
    st.subheader("5. Foster Continuous Learning and Adaptive Capacity")
    st.markdown("The rapid pace of AI evolution necessitates a workforce with strong adaptive capacities. Emphasize training that builds cognitive flexibility, social-emotional intelligence for human-AI collaboration, and strategic career management skills across all employee levels.")
    st.markdown("*   **Action:** Integrate 'Adaptive-Capacity' boosting modules into all major learning initiatives and promote a culture of continuous learning and experimentation.")

    st.markdown("---")
    st.markdown("This application provides a robust, quantitative framework for proactive workforce planning. By dynamically assessing AI-Readiness, analyzing skill gaps, and simulating training impacts, organizations can make informed investments in their human capital, ensuring competitiveness and adaptability in the evolving AI landscape. The framework's flexibility allows for continuous recalibration and adaptation as market demands and individual capabilities evolve.")
