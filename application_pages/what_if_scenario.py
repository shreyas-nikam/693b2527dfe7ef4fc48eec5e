
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from source import simulate_pathway_impact

def run_page():
    st.title("What-If Scenario Engine")
    st.markdown("Simulate the impact of learning pathways on individual employee AI-Readiness scores.")
    st.markdown("---")
    st.header("Simulating Learning Pathway Impact")
    st.markdown("The 'What-If' scenario engine allows HR leaders to simulate the impact of various training programs and learning pathways on an individual's AI-Readiness. This dynamic tool helps assess potential improvements to $V^R$ sub-components and the overall AI-R score.")
    st.markdown(r"The update formula for AI-R is conceptually:$$AI-R_{i,t+1} = AI-R_{i,t} + \sum_{p \in P} \Delta_p \cdot Completion_p \cdot Mastery_p$$")
    st.markdown(r"where $\Delta_p$ is the pre-calibrated impact coefficient for pathway $p$ (from `df_pathways`), $Completion_p \in [0,1]$ is the fraction completed, and $Mastery_p \in [0,1]$ is the assessment performance score.")
    st.markdown(r"The pathway impact ($\Delta_p$) will directly affect the AI-Fluency, Domain-Expertise, or Adaptive-Capacity scores, which then propagate to $V^R$ and subsequently AI-R.")
    st.markdown("This simulation demonstrates the predictive power of the framework, allowing leaders to evaluate the effectiveness of different training programs. By adjusting completion and mastery rates, they can gain insights into the potential ROI of various learning investments and tailor programs to maximize workforce AI-readiness.")

    # Employee Selector
    employee_ids = st.session_state.df_employees['employee_id'].tolist()
    current_employee_index = employee_ids.index(st.session_state.selected_employee_id_whatif) if st.session_state.selected_employee_id_whatif in employee_ids else 0
    selected_employee_id = st.selectbox(
        "Select Employee:",
        employee_ids,
        index=current_employee_index,
        key='whatif_employee_select'
    )
    st.session_state.selected_employee_id_whatif = selected_employee_id

    # Pathway Selector
    pathway_names = st.session_state.df_pathways['pathway_name'].tolist()
    pathway_map = st.session_state.df_pathways.set_index('pathway_name')['pathway_id'].to_dict()
    
    default_pathway_name_whatif = pathway_names[0] # Fallback to first pathway name
    if st.session_state.selected_pathway_id_whatif != "N/A":
        # Find the name corresponding to the stored ID
        try:
            default_pathway_name_whatif = st.session_state.df_pathways[st.session_state.df_pathways['pathway_id'] == st.session_state.selected_pathway_id_whatif]['pathway_name'].iloc[0]
        except IndexError:
            pass # Keep default if ID not found

    current_pathway_index = pathway_names.index(default_pathway_name_whatif) if default_pathway_name_whatif in pathway_names else 0
    selected_pathway_name = st.selectbox(
        "Select Learning Pathway:",
        pathway_names,
        index=current_pathway_index,
        key='whatif_pathway_select'
    )
    selected_pathway_id = pathway_map.get(selected_pathway_name, "N/A")
    st.session_state.selected_pathway_id_whatif = selected_pathway_id

    # Completion Rate Slider
    completion_rate = st.slider("Completion Rate", 0.0, 1.0, st.session_state.completion_rate_whatif, 0.05, key='whatif_completion_rate')
    st.session_state.completion_rate_whatif = completion_rate

    # Mastery Score Slider
    mastery_score = st.slider("Mastery Score", 0.0, 1.0, st.session_state.mastery_score_whatif, 0.05, key='whatif_mastery_score')
    st.session_state.mastery_score_whatif = mastery_score

    # Simulate Button
    if st.button("Simulate Pathway Impact"):
        if st.session_state.selected_employee_id_whatif != "N/A" and st.session_state.selected_pathway_id_whatif != "N/A":
            current_ai_r_val = st.session_state.df_employees[st.session_state.df_employees['employee_id'] == st.session_state.selected_employee_id_whatif]['current_ai_r_score'].iloc[0]
            projected_ai_r, delta_ai_r, pathway_name_res = simulate_pathway_impact(
                st.session_state.selected_employee_id_whatif,
                st.session_state.selected_pathway_id_whatif,
                st.session_state.completion_rate_whatif,
                st.session_state.mastery_score_whatif,
                st.session_state.df_employees,
                st.session_state.df_occupations,
                st.session_state.df_pathways,
                st.session_state.PARAMS
            )
            st.session_state.whatif_results = {
                "current_ai_r": current_ai_r_val,
                "projected_ai_r": projected_ai_r,
                "delta_ai_r": delta_ai_r,
                "pathway_name": pathway_name_res,
                "selected_employee_id": st.session_state.selected_employee_id_whatif # Store selected employee ID for results display
            }
        else:
            st.warning("Please ensure an employee and a pathway are selected for simulation.")

    # Display Results (if simulation completed):
    if st.session_state.whatif_results and st.session_state.whatif_results["selected_employee_id"] == st.session_state.selected_employee_id_whatif:
        res = st.session_state.whatif_results
        st.subheader("Simulation Results:")
        st.markdown(f"Employee ID: **{res['selected_employee_id']}**")
        st.markdown(f"Current AI-R Score: **{res['current_ai_r']:.2f}**")
        st.markdown(f"Chosen Pathway: **{res['pathway_name']}**")
        st.markdown(f"Projected AI-R Score: **{res['projected_ai_r']:.2f}**")
        st.markdown(f"Change in AI-R ($\Delta$AI-R): **{res['delta_ai_r']:.2f}**")

        # Plotly visualization
        fig_whatif = go.Figure()
        fig_whatif.add_trace(go.Bar(name='Current AI-R', x=['Current AI-R'], y=[res['current_ai_r']], marker_color='skyblue'))
        fig_whatif.add_trace(go.Bar(name='Projected AI-R', x=[f'Projected ({res["pathway_name"]})'], y=[res['projected_ai_r']], marker_color='lightcoral'))
        
        fig_whatif.update_layout(
            title_text='Current vs. Projected AI-Readiness Score',
            yaxis_title='AI-R Score',
            yaxis_range=[0, 100],
            barmode='group'
        )
        st.plotly_chart(fig_whatif)
