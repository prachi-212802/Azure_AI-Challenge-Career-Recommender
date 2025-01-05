import streamlit as st
import pandas as pd
import numpy as np
from .functions import *
from datetime import datetime
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from model import *

def results_page(go_to_page):

    ########################################## Check if all responses are available
    if (
        'openness_responses' in st.session_state and
        'conscientiousness_responses' in st.session_state and
        'extraversion_responses' in st.session_state and
        'agreeableness_responses' in st.session_state and 
        'neuroticism_responses' in st.session_state and 
        'education_response' in st.session_state and 
        'work_environment_response' in st.session_state and 
        'interests_response' in st.session_state and 
        'skills_response' in st.session_state 
    ):

        
        ########################################## Define the DataFrame structure
        columns = [
            'Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness', 'Neuroticism',
            "Bachelor's in Arts", "Bachelor's in Business", "Bachelor's in CS",
            "Bachelor's in Engineering", "Diploma in Design", "MBA",
            "Master's in Data Science", "Master's in Engineering",
            'Flexible', 'Hybrid', 'On-site', 'Remote',
            'Artistic', 'Conventional', 'Enterprising', 'Investigative', 'Realistic', 'Social',
            'Data Analysis', 'Engineering Design', 'Graphic Design', 'Illustration', 'Java', 'MATLAB',
            'Machine Learning', 'Marketing', 'Negotiation', 'Photoshop', 'Public Speaking', 'Python', 'SQL', 'Sales', 'Writing'
        ]

        # Initialize the DataFrame with zeros
        data = pd.DataFrame(0, index=[0], columns=columns)


        ########################################## Display Scores
        st.title("**Personality Survey Results**")


        # Calculate and display the scores for each trait
        traits = {
            "Openness": st.session_state.get("openness_responses"),
            "Extraversion": st.session_state.get("extraversion_responses"),
            "Agreeableness": st.session_state.get("agreeableness_responses"),
            "Conscientiousness": st.session_state.get("conscientiousness_responses"),
            "Neuroticism": st.session_state.get("neuroticism_responses")
        }

        ########################################## Personalized greeting
        first_name = st.session_state["user_details"].get("first_name", "User")
        st.markdown(f"### Hello, **{first_name}**! 🎉 Welcome to your **Personality Report**")

        ########################################## Display personality scores with highlights
        st.header("**Personality Scores**")
        for trait, responses in traits.items():
            if responses:
                score = calculate_mean_score(responses)
                st.markdown(f"**{trait}:** *{score * 100:.1f}%*") 
                data.at[0, trait] = score

                # Displaying trait description with styling
                description = get_trait_description(trait, score)
                if score >= 0.7:
                    st.markdown(f"<p style='color: green; font-size: 16px;'><strong>{description}</strong></p>", unsafe_allow_html=True)
                elif score >= 0.35:
                    st.markdown(f"<p style='color: orange; font-size: 16px;'>{description}</p>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<p style='color: red; font-size: 16px;'>{description}</p>", unsafe_allow_html=True)
            else:
                st.write(f"**{trait}:** No responses submitted.")
                
        ########################################## Display other responses
        st.header("**Other Survey Responses**")

        # Education
        education_response = st.session_state.get("education_response", [])
        st.subheader("**Education**")
        if education_response:
            st.markdown(f"Your education choices: **{', '.join(education_response)}**")
        else:
            st.markdown("No education response submitted.")

        # Skills
        skills_response = st.session_state.get("skills_response", [])
        st.subheader("**Skills**")
        if skills_response:
            st.markdown(f"Your skills: **{', '.join(skills_response)}**")
        else:
            st.markdown("No skills response submitted.")

        # Interests
        interests_response = st.session_state.get("interests_response", [])
        st.subheader("**Interests**")
        if interests_response:
            st.markdown(f"Your interests: **{', '.join(interests_response)}**")
        else:
            st.markdown("No interests response submitted.")

        # Work Environment
        work_env_response = st.session_state.get("work_environment_response", [])
        st.subheader("**Work Environment Preferences**")
        if work_env_response:
            st.markdown(f"Your preferred work environment: **{', '.join(work_env_response)}**")
        else:
            st.markdown("No work environment preferences submitted.")

        ########################################## Additional Highlights
        st.markdown("---")
        st.markdown(f"**Summary for {first_name}:**")
        st.markdown("Here's a quick summary of your responses to the survey:")
        st.markdown("- **Openness, Extraversion, Neuroticism, Agreeableness, Conscientiousness** have been assessed based on your answers.")
        st.markdown("- You have provided valuable insights into your education, skills, interests, and preferred work environments.")

        ########################################## Update the DataFrame
        data.loc[0, [f"{edu}" for edu in education_response if f"{edu}" in data.columns]] = 1
        data.loc[0, [f"{work}" for work in work_env_response if f"{work}" in data.columns]] = 1
        data.loc[0, [f"{skill}" for skill in skills_response if f"{skill}" in data.columns]] = 1
        data.loc[0, [f"{interest}" for interest in interests_response if f"{interest}" in data.columns]] = 1
        

        ########################################## Prepare the JSON in the required format
        json_data = {
                        "input_data": {
                            "columns": list(range(len(data.columns))),  # List of column indices
                            "index": list(data.index),  # List of row indices
                            "data": data.values.tolist()  # List of rows
                        }
                    }

        ########################################## Calling the Model
        try:        
            ml_model_output = modelCall(json_data)
            output_array = np.array(eval(ml_model_output.decode()))
            career_labels = [
                                'AI Researcher',
                                'Business Analyst',
                                'Data Scientist',
                                'Graphic Designer',
                                'Marketing Specialist',
                                'Mechanical Engineer',
                                'Sales Manager',
                                'Software Engineer',
                                'UX Designer'
                            ]

            recommended_careers = [
                                    career_labels[i]
                                    for i, value in enumerate(output_array[0])
                                    if value == 1.0
                                    ]

            # Display the recommendations in a user-friendly way
            if recommended_careers:
                st.header("**Career Recommendations**")
                st.markdown("Based on your responses, we recommend the following career paths for you:")
                for career in recommended_careers:
                    st.markdown(
                        f"""
                        <div style='
                            background-color: #f0f8ff; 
                            border: 2px solid #4682b4; 
                            padding: 10px; 
                            margin: 10px 0; 
                            border-radius: 8px; 
                            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);'>
                            <p style='color: #2c3e50; font-size: 18px; font-weight: bold; margin: 0;'>
                            &#9989; {career}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.markdown(
                    "<p style='color: red; font-size: 16px;'><strong>No clear career recommendations were found. Please review your responses.</strong></p>",
                    unsafe_allow_html=True
                )

        except Exception as e:
            st.markdown(
                        """
                        <div style="color: red; font-size: 18px; font-weight: bold; text-align: center; border: 2px solid red; padding: 10px; border-radius: 5px; background-color: #ffe6e6;">
                            Error: Unable to connect with the backend. Please try again later!
                        </div>
                        """, 
                        unsafe_allow_html=True
                        )

    else:
        st.write("You have not completed all the surveys. Please go back and finish them.")
