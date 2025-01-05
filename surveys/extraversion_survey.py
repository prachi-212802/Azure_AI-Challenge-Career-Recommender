import streamlit as st

def extraversion_page(go_to_page):
    st.title("Extraversion Survey")

    if 'extraversion_submitted' not in st.session_state:
        st.session_state.extraversion_submitted = False

    if not st.session_state.extraversion_submitted:
        st.write("Please rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).")
        extraversion_questions = [
            "I feel comfortable around people.",
            "I enjoy being the center of attention.",
            "I thrive in social gatherings.",
            "I feel energized by spending time with others.",
            "I am talkative in conversations."
        ]

        # Initialize responses
        if 'extraversion_responses' not in st.session_state:
            st.session_state.extraversion_responses = {}

        # Collect responses
        for i, question in enumerate(extraversion_questions, start=1):
            st.session_state.extraversion_responses[f"q{i}"] = st.radio(
                label=f"{i}. {question}",
                options=[1, 2, 3, 4, 5],
                index=None,  # No default selection
                key=f"extraversion_q{i}"
            )

        # Validate and submit
        if st.button("Submit Extraversion Survey"):
            if None in st.session_state.extraversion_responses.values():
                st.warning("Please answer all questions before proceeding.")
            else:
                st.session_state.extraversion_submitted = True
                go_to_page("agreeableness")
                if st.button("Next Survey : Agreeableness Survey"):
                    go_to_page("agreeableness")
                    