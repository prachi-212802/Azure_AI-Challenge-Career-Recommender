import streamlit as st

def education_page(go_to_page):
    st.title("Education Survey")

    if 'education_submitted' not in st.session_state:
        st.session_state.education_submitted = False

    if not st.session_state.education_submitted:
        st.write("Please select your level of education from the options below.")

        # Education options
        education_options = [
            "Diploma in Design",
            "Bachelor's in CS",
            "Bachelor's in Arts",
            "Bachelor's in Engineering",
            "Bachelor's in Business",
            "MBA",
            "Master's in Data Science",
            "Master's in Engineering"
        ]

        # Multi-select for education levels
        st.session_state.education_response = st.multiselect(
            "Choose your level of education:",
            education_options,
            key="education"
        )

        # Custom bubble style
        if st.session_state.education_response:
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

            for item in st.session_state.education_response:
                st.markdown(f'<span class="bubble">{item}</span>', unsafe_allow_html=True)

        # Validate submission
        if st.button("Submit Education Survey"):
            if not st.session_state.education_response:
                st.warning("Please select at least one level of education before submitting.")
            else:
                st.session_state.education_submitted = True
                go_to_page("work_environment")
                if st.button("Next Survey : WorkEnvironment Survey"):
                    go_to_page("work_environment")
