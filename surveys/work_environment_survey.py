import streamlit as st

def work_environment_page(go_to_page):
    st.title("Work Environment Survey")

    if 'work_environment_submitted' not in st.session_state:
        st.session_state.work_environment_submitted = False

    if not st.session_state.work_environment_submitted:
        st.write("Please select your preferred work environment from the options below.")

        # Work environment options
        work_environment_options = [
            "Flexible",
            "Hybrid",
            "Remote",
            "On-site"
        ]

        # Multi-select for work environment preferences
        st.session_state.work_environment_response = st.multiselect(
            "Select your preference of work environment:",
            work_environment_options,
            key="work_environment"
        )

        # Custom bubble style
        if st.session_state.work_environment_response:
            st.markdown("""
                <style>
                    .bubble {
                        display: inline-block;
                        padding: 10px;
                        margin: 5px;
                        background-color: #0078d4;
                        color: white;
                        border-radius: 50px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                </style>
            """, unsafe_allow_html=True)

            for item in st.session_state.work_environment_response:
                st.markdown(f'<span class="bubble">{item}</span>', unsafe_allow_html=True)

        # Validate submission
        if st.button("Submit Work Environment Survey"):
            if not st.session_state.work_environment_response:
                st.warning("Please select at least one work environment preference before submitting.")
            else:
                st.session_state.work_environment_submitted = True
                go_to_page("interest")
                if st.button("Next Survey : Interest Survey"):
                    go_to_page("interest")
