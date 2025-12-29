
import streamlit as st
import plotly.graph_objects as go
from source import optimize_pathway_sequence

def run_page():
    st.title("Multi-Step Pathway Optimization")
    st.markdown("Generate an optimized sequence of learning pathways to maximize AI-Readiness within defined constraints.")
    st.markdown("---")
    st.header("Multi-Step Pathway Optimization")
    st.markdown("For complex skill transitions or broader workforce development, identifying an optimal sequence of learning pathways is crucial. This involves balancing AI-R improvement with constraints like total cost and time. The multi-step pathway optimization problem can be formulated as:")
    st.markdown(r"$$\max_{P_1,...,P_K} AI-R(P_1,..., P_K) - \lambda_{\text{cost}} \cdot \sum_{k=1}^K Cost(P_k)$$")
    st.markdown("subject to:")
    st.markdown(r"$$ \sum_{k=1}^K Time(P_k) \leq T_{\text{max}} $$")
    st.markdown(r"$$ P_k \in P_{\text{feasible}} $$")
    st.markdown(r"$$ Prerequisites(P_k) \subseteq \{P_1,...,P_{k-1}\} $$")
    st.markdown("For this application, we implement a simplified greedy optimization strategy to identify a sequence of pathways that maximizes AI-R improvement within a given time budget, considering the cost.")
    st.markdown("The pathway optimization function provides a strategic roadmap for investing in talent development. By considering multiple pathways, their costs, and time commitments, organizations can make data-driven decisions to maximize the AI-Readiness of their workforce efficiently, identifying high-ROI learning initiatives.")

    # Employee Selector
    employee_ids_opt = st.session_state.df_employees['employee_id'].tolist()
    current_employee_opt_index = employee_ids_opt.index(st.session_state.selected_employee_id_opt) if st.session_state.selected_employee_id_opt in employee_ids_opt else 0
    selected_employee_id_opt = st.selectbox(
        "Select Employee for Optimization:",
        employee_ids_opt,
        index=current_employee_opt_index,
        key='opt_employee_select'
    )
    st.session_state.selected_employee_id_opt = selected_employee_id_opt

    # Max Time Hours Slider
    T_max_hours = st.slider("Maximum Time (hours)", 50, 500, st.session_state.T_max_hours_opt, 10, key='opt_max_time')
    st.session_state.T_max_hours_opt = T_max_hours

    # Cost Weight Lambda Slider
    cost_weight_lambda = st.slider("Cost Weight ($\lambda_{\text{cost}}$)", 0.001, 0.01, st.session_state.cost_weight_lambda_opt, 0.001, key='opt_cost_weight', format="%.3f")
    st.session_state.cost_weight_lambda_opt = cost_weight_lambda

    # Optimize Button
    if st.button("Optimize Pathways"):
        if st.session_state.selected_employee_id_opt != "N/A":
            current_ai_r_opt_val = st.session_state.df_employees[st.session_state.df_employees['employee_id'] == st.session_state.selected_employee_id_opt]['current_ai_r_score'].iloc[0]
            optimization_results = optimize_pathway_sequence(
                st.session_state.selected_employee_id_opt,
                current_ai_r_opt_val,
                st.session_state.df_pathways,
                st.session_state.T_max_hours_opt,
                st.session_state.cost_weight_lambda_opt,
                st.session_state.df_employees,
                st.session_state.df_occupations, # Not directly used in this `optimize_pathway_sequence` but kept for consistency with source.py signature
                st.session_state.PARAMS
            )
            st.session_state.optimization_results = {
                "current_ai_r": current_ai_r_opt_val,
                "selected_employee_id": st.session_state.selected_employee_id_opt, # Store selected employee ID for results display
                **optimization_results # Unpack results from the function
            }
        else:
            st.warning("Please select an employee for optimization.")

    # Display Results (if optimization completed):
    if st.session_state.optimization_results and st.session_state.optimization_results["selected_employee_id"] == st.session_state.selected_employee_id_opt:
        opt_res = st.session_state.optimization_results
        st.subheader("Optimization Results:")
        st.markdown(f"Employee ID: **{opt_res['selected_employee_id']}**")
        st.markdown(f"Current AI-R Score: **{opt_res['current_ai_r']:.2f}**")
        st.markdown(f"Recommended Pathway Sequence: **{\', \'.join(opt_res['recommended_sequence']) if opt_res['recommended_sequence'] else 'No pathways recommended within constraints'}**")
        st.markdown(f"Projected Final AI-R: **{opt_res['projected_final_ai_r']:.2f}**")
        st.markdown(f"Total Cost: **${opt_res['total_cost']:.2f}**")
        st.markdown(f"Total Time (hours): **{opt_res['total_time_hours']:.2f}**")
        st.markdown(f"AI-R Improvement: **{opt_res['ai_r_improvement']:.2f}**")

        # Plotly visualization
        fig_opt = go.Figure()
        fig_opt.add_trace(go.Bar(name='Current AI-R', x=['Current AI-R'], y=[opt_res['current_ai_r']], marker_color='skyblue'))
        fig_opt.add_trace(go.Bar(name='Projected AI-R', x=['Optimized Pathway Sequence'], y=[opt_res['projected_final_ai_r']], marker_color='lightcoral'))
        
        fig_opt.update_layout(
            title_text='Current vs. Projected AI-Readiness Score',
            yaxis_title='AI-R Score',
            yaxis_range=[0, 100],
            barmode='group'
        )
        st.plotly_chart(fig_opt)
