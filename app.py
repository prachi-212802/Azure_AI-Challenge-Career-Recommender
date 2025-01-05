import streamlit as st
import numpy as np
import pandas as pd
from page.home_page import *
from surveys.openness_survey import *
from surveys.conscientiousness_page import *  # Import survey page function
from surveys.extraversion_survey import *  # Import survey page function
from surveys.neuroticism_survey import *  # Import survey page function
from surveys.agreeable_survey import *  # Import survey page function
from surveys.eduction_survey import *  # Import survey page function
from surveys.work_environment_survey import *  # Import survey page function
from surveys.interest_survey import *
from surveys.skills_survey import *
from page.result import *
from page.info_form import *






################################################### State to track the current page
if 'page' not in st.session_state:
    st.session_state.page = "home_page"  # Default to the first page

################################################### Navigation function
def go_to_page(page_name):
    st.session_state.page = page_name


if st.session_state.page == "home_page":
    home_page(go_to_page)

elif st.session_state.page == "info_page":
    info_page(go_to_page)

elif st.session_state.page == "openness":
    openness_page(go_to_page)

elif st.session_state.page == "conscientiousness":
    conscientiousness_page(go_to_page)  

elif st.session_state.page == "extraversion":
    extraversion_page(go_to_page)  

elif st.session_state.page == "agreeableness":
    agreeableness_page(go_to_page) 

elif st.session_state.page == "neuroticism":
    neuroticism_page(go_to_page) 

elif st.session_state.page == "education":
    education_page(go_to_page) 

elif st.session_state.page == "work_environment":
    work_environment_page(go_to_page) 

elif st.session_state.page == "interest":
    interests_page(go_to_page) 

elif st.session_state.page == "skills":
    skills_page(go_to_page) 

elif st.session_state.page == "end_survey":
    results_page(go_to_page)
