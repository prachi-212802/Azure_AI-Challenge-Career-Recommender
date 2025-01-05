import streamlit as st
from datetime import datetime

def info_page(go_to_page):
    st.title("Basic Information")

    # Create session state to store user data
    if 'user_details' not in st.session_state:
        st.session_state.user_details = {}

    # Collect user information
    with st.form(key='user_details_form'):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        dob = st.date_input("Date of Birth")
        email = st.text_input("Email")
        place = st.text_input("Place")
        
        submit_button = st.form_submit_button(label='Submit')

        # Validate the form and store details
        if submit_button:
            if not first_name or not last_name or not dob or not email or not place:
                st.error("Please fill out all fields before proceeding.")
            else:
                # Store user details in session state
                st.session_state.user_details = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "dob": dob,
                    "email": email,
                    "place": place
                }
                
                # Once the form is submitted and validated, go to the survey page
                st.success("Details saved successfully! Proceeding to survey...")
                go_to_page("openness")

