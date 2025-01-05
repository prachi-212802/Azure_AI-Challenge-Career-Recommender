import streamlit as st

def skills_page(go_to_page):
    st.title("Skills Survey")

    if 'skills_submitted' not in st.session_state:
        st.session_state.skills_submitted = False

    if not st.session_state.skills_submitted:
        st.write("Please select your skills from the options below.")

        # Skills options
        skills_options = [
            "Data Analysis",
            "Engineering Design",
            "Graphic Design",
            "Illustration",
            "Java",
            "Machine Learning",
            "Marketing",
            "MATLAB",
            "Negotiation",
            "Photoshop",
            "Public Speaking",
            "Python",
            "Sales",
            "SQL",
            "Writing"
        ]

        # Multi-select for skills
        st.session_state.skills_response = st.multiselect(
            "Choose all that apply:",
            skills_options,
            key="skills"
        )

        # Custom bubble style
        if st.session_state.skills_response:
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

            for item in st.session_state.skills_response:
                st.markdown(f'<span class="bubble">{item}</span>', unsafe_allow_html=True)

        # Validate submission
        if st.button("Submit Skills Survey"):
            if not st.session_state.skills_response:
                st.warning("Please select at least one skill before submitting.")
            else:
                st.session_state.skills_submitted = True
                go_to_page("end_survey")
                if st.button("Conclusion"):
                    go_to_page("end_survey")

    if st.session_state.skills_submitted:
        st.write("Thank you for completing the survey!")
