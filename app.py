import streamlit as st
from helper_functions import render_sidebar
from views.candidate_form import render_candidate_form
from views.interview_ques import render_interview_questions

# Set up page
st.set_page_config(
    page_title="TalentScout",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Set default page
if 'page' not in st.session_state:
    st.session_state['page'] = "Home"

# Sidebar
render_sidebar()

# Routing logic
if st.session_state['page'] == "Home":
    st.markdown("""
        <style>
            .main-title { font-size: 50px !important; font-weight: bold; }
            .intro-text { font-size: 25px; color: #555; }
        </style>
        <p class='main-title'>Welcome to TalentScout</p>
        <p class='intro-text'>
            TalentScout is your AI‐powered hiring assistant designed to simplify candidate screening.<br>
            Our app gathers your essential details and then generates tailored technical interview questions based on your skills.    
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
        <style>
            .main-title-content { font-size: 28px !important; font-weight: bold; }
        </style>
        <p class='main-title-content'>How to Use TalentScout:</p>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .main-title-guide { font-size: 20px !important; font-weight: bold; }
        </style>
        <p class='main-title-guide'>1. Fill Out the Candidate Form:</p>
    """, unsafe_allow_html=True)
    st.markdown("- Navigate to the 'Candidate Form' section from the sidebar menu.")
    st.markdown("- Enter your full name, email, phone number, years of experience, desired position, current location, and your tech stack (e.g., Python, Java, C++).")
    st.markdown("")
    st.markdown("""
        <style>
            .main-title-guide { font-size: 20px !important; font-weight: bold; }
        </style>
        <p class='main-title-guide'>2. Interview Questions:</p>
    """, unsafe_allow_html=True) 
    st.markdown("- Once the candidate form is submitted, the page will switch to the 'Interview Questions' page.")
    st.markdown("- The app uses your declared tech stack to generate 3-5 technical questions for each technology.")
    st.markdown("")
    st.markdown("""
        <style>
            .main-title-guide { font-size: 20px !important; font-weight: bold; }
        </style>
        <p class='main-title-guide'>3. Review & Download:</p>
    """, unsafe_allow_html=True) 
    st.markdown("- Review the generated questions for each technology.")
    st.markdown("- You can download the complete set of questions for further analysis or record keeping.")  

elif st.session_state['page'] == "Candidate Form":
    render_candidate_form()

elif st.session_state['page'] == "Interview Questions":
    render_interview_questions()
