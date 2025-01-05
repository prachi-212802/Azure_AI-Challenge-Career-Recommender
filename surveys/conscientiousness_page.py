import streamlit as st

def conscientiousness_page(go_to_page):
    st.title("Conscientiousness Survey")

    if 'conscientiousness_submitted' not in st.session_state:
        st.session_state.conscientiousness_submitted = False

    if not st.session_state.conscientiousness_submitted:
        st.write("Please rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).")
        conscientiousness_questions = [
            "I complete tasks efficiently and on time.",
            "I am well-organized in my daily activities.",
            "I set high standards for myself.",
            "I am diligent and hardworking.",
            "I avoid careless mistakes."
        ]

        # Initialize responses
        if 'conscientiousness_responses' not in st.session_state:
            st.session_state.conscientiousness_responses = {}

        # Collect responses
        for i, question in enumerate(conscientiousness_questions, start=1):
            st.session_state.conscientiousness_responses[f"q{i}"] = st.radio(
                label=f"{i}. {question}",
                options=[1, 2, 3, 4, 5],
                index=None,  # No default selection
                key=f"conscientiousness_q{i}"
            )

        # Validate and submit
        if st.button("Submit Conscientiousness Survey"):
            if None in st.session_state.conscientiousness_responses.values():
                st.warning("Please answer all questions before proceeding.")
            else:
                st.session_state.conscientiousness_submitted = True
                go_to_page("extraversion")
                go_to_page("extraversion")
                if st.button("Next Survey : Extraversion Survey"):
                    go_to_page("extraversion")

