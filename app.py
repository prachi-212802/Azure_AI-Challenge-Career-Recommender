import streamlit as st

# Function to recommend career based on skills and experience
def recommend_career(skills, experience):
    recommendations = []
    
    # Example recommendation logic
    if "Python" in skills and experience >= 3:
        recommendations.append("Software Developer")
    if "Machine Learning" in skills and experience >= 2:
        recommendations.append("Data Scientist")
    if "Business Analysis" in skills and experience >= 1:
        recommendations.append("Business Analyst")
    if "Project Management" in skills and experience >= 3:
        recommendations.append("Project Manager")
    
    if not recommendations:
        return ["Explore more skills and experience to find the best fit."]
    return recommendations

# Streamlit UI
st.title("Career Recommendation App")

# Form for user input
with st.form(key='career_form'):
    st.header("Enter Your Skills and Experience")

    # Two inputs for skills and experience
    skills_input = st.text_input("Enter your skills (comma-separated):", "Python, Machine Learning")
    experience_input = st.number_input("Enter your years of experience:", min_value=0, max_value=50, value=3)

    # Submit button
    submit_button = st.form_submit_button(label="Get Career Recommendations")

# Processing the input and displaying recommendations
if submit_button:
    skills_list = [skill.strip() for skill in skills_input.split(",")]
    career_options = recommend_career(skills_list, experience_input)
    
    st.subheader("Recommended Careers:")
    for career in career_options:
        st.write(f"- {career}")
