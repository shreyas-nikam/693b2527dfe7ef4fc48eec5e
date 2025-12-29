
import streamlit as st
import pandas as pd
import plotly.express as px
from source import generate_ai_r_report_summary

def run_page():
    st.title("Workforce AI-Readiness Dashboard")
    st.markdown("Gain a high-level overview of your workforce's AI-Readiness, broken down by key organizational groups.")
    st.markdown("---")
    st.header("Aggregated AI-Readiness Report")
    st.markdown("The 'Workforce AI-Readiness Report' summarizes the aggregated AI-R scores, providing a high-level overview of the organization's AI-readiness across different segments.")

    # Group By Selector
    report_group_by_options = ['job_role', 'department']
    current_index = report_group_by_options.index(st.session_state.report_group_by) if st.session_state.report_group_by in report_group_by_options else 0
    
    selected_group_by = st.selectbox(
        "Group AI-Readiness Report by:",
        report_group_by_options,
        index=current_index,
        key='dashboard_group_by_select'
    )
    if selected_group_by != st.session_state.report_group_by:
        st.session_state.report_group_by = selected_group_by
        st.rerun() # Rerun to update the heatmap based on new grouping

    # Summary Table Display
    ai_r_summary_report = generate_ai_r_report_summary(st.session_state.df_employees)
    st.dataframe(ai_r_summary_report)
    st.markdown(f"Average AI-R score for the entire workforce: **{st.session_state.df_employees['current_ai_r_score'].mean():.2f}**")

    # Skills Gap Heatmap
    st.header("Skills Gap Analysis Heatmap")
    st.markdown(r"""This heatmap visualizes the average scores for Idiosyncratic Readiness ($V^R$) sub-components (AI-Fluency, Domain-Expertise, Adaptive-Capacity) across different employee groups.""")
    st.markdown(r"""The heatmap offers a granular view, clearly highlighting which $V^R$ sub-components are strong or weak within specific job roles/departments, thereby pinpointing areas for targeted upskilling efforts.""")
    
    vr_sub_components = ['ai_fluency_score', 'domain_expertise_score', 'adaptive_capacity_score']
    heatmap_data = st.session_state.df_employees.groupby(st.session_state.report_group_by)[vr_sub_components].mean().reset_index()
    heatmap_data_melted = heatmap_data.melt(id_vars=[st.session_state.report_group_by], var_name='VR Sub-Component', value_name='Average Score')
    
    fig_heatmap = px.heatmap(
        heatmap_data_melted,
        x='VR Sub-Component',
        y=st.session_state.report_group_by,
        z='Average Score',
        color_continuous_scale='Viridis',
        text_auto=".1f",
        title=f'Average $V^R$ Sub-Component Scores by {st.session_state.report_group_by}'
    )
    st.plotly_chart(fig_heatmap)
