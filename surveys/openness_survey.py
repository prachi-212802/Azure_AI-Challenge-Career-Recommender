import streamlit as st

def openness_page(go_to_page):
    st.title("Openness Survey")

    if 'openness_submitted' not in st.session_state:
        st.session_state.openness_submitted = False

    if not st.session_state.openness_submitted:
        st.write("Please rate each statement from 1 (Strongly Disagree) to 5 (Strongly Agree).")
        
        # List of questions
        openness_questions = [
            "I enjoy exploring new ideas and concepts.",
            "I am curious about many different things.",
            "I have a vivid imagination.",
            "I enjoy artistic and cultural experiences.",
            "I often think about abstract concepts."
        ]

        # Initialize a dictionary for storing responses
        st.session_state.openness_responses = {}

        # Collect responses
        for i, question in enumerate(openness_questions, start=1):
            st.session_state.openness_responses[f"q{i}"] = st.radio(
                label=f"{i}. {question}",
                options=[1, 2, 3, 4, 5],
                index=None,  # No default selection
                key=f"openness_q{i}"
            )
        # Validate and submit
        if st.button("Submit Openness Survey"):
            if None in st.session_state.openness_responses.values():
                st.warning("Please answer all questions before proceeding.")
            else:
                st.session_state.openness_submitted = True
                go_to_page("conscientiousness")
                if st.button("Next Survey : Conscientiousness Survey"):
                    go_to_page("conscientiousness")
