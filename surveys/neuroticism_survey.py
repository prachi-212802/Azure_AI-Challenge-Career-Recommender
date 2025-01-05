import streamlit as st

def neuroticism_page(go_to_page):
    st.title("Neuroticism Survey")

    if 'neuroticism_submitted' not in st.session_state:
        st.session_state.neuroticism_submitted = False

    if not st.session_state.neuroticism_submitted:
        st.write("Please rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).")
        neuroticism_questions = [
            "I often feel anxious or worried.",
            "I get upset easily.",
            "I frequently feel sad or down.",
            "I overthink situations.",
            "I experience mood swings."
        ]

        # Initialize responses
        if 'neuroticism_responses' not in st.session_state:
            st.session_state.neuroticism_responses = {}

        # Collect responses
        for i, question in enumerate(neuroticism_questions, start=1):
            st.session_state.neuroticism_responses[f"q{i}"] = st.radio(
                label=f"{i}. {question}",
                options=[1, 2, 3, 4, 5],
                index=None,  # No default selection
                key=f"neuroticism_q{i}"
            )

        # Validate and submit
        if st.button("Submit Neuroticism Survey"):
            if None in st.session_state.neuroticism_responses.values():
                st.warning("Please answer all questions before proceeding.")
            else:
                st.session_state.neuroticism_submitted = True
                go_to_page("education")
                if st.button("Next Survey : Education Survey"):
                    go_to_page("education")
