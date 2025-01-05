import streamlit as st

def agreeableness_page(go_to_page):
    st.title("Agreeableness Survey")

    if 'agreeableness_submitted' not in st.session_state:
        st.session_state.agreeableness_submitted = False

    if not st.session_state.agreeableness_submitted:
        st.write("Please rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).")
        agreeableness_questions = [
            "I am sympathetic to the feelings of others.",
            "I try to see the good in people.",
            "I avoid arguments and conflicts.",
            "I enjoy helping others.",
            "I trust people easily."
        ]

        # Initialize responses
        if 'agreeableness_responses' not in st.session_state:
            st.session_state.agreeableness_responses = {}

        # Collect responses
        for i, question in enumerate(agreeableness_questions, start=1):
            st.session_state.agreeableness_responses[f"q{i}"] = st.radio(
                label=f"{i}. {question}",
                options=[1, 2, 3, 4, 5],
                index=None,  # No default selection
                key=f"agreeableness_q{i}"
            )

        # Validate and submit
        if st.button("Submit Agreeableness Survey"):
            if None in st.session_state.agreeableness_responses.values():
                st.warning("Please answer all questions before proceeding.")
            else:
                st.session_state.agreeableness_submitted = True
                go_to_page("neuroticism")
                if st.button("Next Survey : Neuroticism Survey"):
                    go_to_page("neuroticism")
