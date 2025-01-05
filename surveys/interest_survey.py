import streamlit as st

def interests_page(go_to_page):
    st.title("Interests Survey")

    if 'interests_submitted' not in st.session_state:
        st.session_state.interests_submitted = False

    if not st.session_state.interests_submitted:
        st.write("Please select your interests from the options below.")

        # Interests options
        interests_options = [
            "Artistic",
            "Conventional",
            "Enterprising",
            "Realistic",
            "Social",
            "Investigative"
        ]

        # Multi-select for interests
        st.session_state.interests_response = st.multiselect(
            "Choose your interests:",
            interests_options,
            key="interests"
        )

        # Custom bubble style
        if st.session_state.interests_response:
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

            for item in st.session_state.interests_response:
                st.markdown(f'<span class="bubble">{item}</span>', unsafe_allow_html=True)

        # Validate submission
        if st.button("Submit Interests Survey"):
            if not st.session_state.interests_response:
                st.warning("Please select at least one interest before submitting.")
            else:
                st.session_state.interests_submitted = True
                go_to_page("skills")
                if st.button("Next Survey : Skills Survey"):
                    go_to_page("skills")