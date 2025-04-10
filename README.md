# TalentScout Hiring Assistant

## Project Overview
TalentScout is an AI-powered hiring assistant designed to streamline the candidate screening process. It gathers essential candidate details and then uses a large language model (LLM) to generate tailored technical interview questions based on the candidate's declared tech stack. Built with Python and Streamlit, this application demonstrates the effective use of prompt engineering, session-based routing, and custom UI navigation to create a user-friendly recruitment tool.

## Installation Instructions

1.  Clone the Repository
    ```bash
    git clone https://github.com/Sashank-Sagar/TalentScout-Chatbot.git
    cd TalentScout-Chatbot
    
2.  Create a Virtual Environment
    python -m venv env

3.  Activate the Virtual Environment 
    On Windows:
      env\Scripts\activate
    On Powershell:
      env\Scripts\Activate.ps1
    On macOS/Linux:
      source env/bin/activate

4.  Install Dependencies
    pip install -r requirements.txt

5.  Run the Application
    streamlit run app.py

## Usage Guide
1.  Navigation
    Use the custom sidebar navigation to move between pages:
    Home: Overview and instructions
    Candidate Form: Enter candidate details (name, email, phone, experience, position, location, tech stack)
    Interview Questions: View and download tailored technical questions

2.  Candidate Form
    Complete all required fields. After submission, data is stored in session state.

3.  Interview Questions
    Questions are generated for each technology in the candidate’s stack. Users can review and download them as a text file.

## Technical Details

1.  Architecture & Code Structure
    app.py: Entry point with session-based page routing using st.session_state
    helper_functions.py: Contains render_sidebar() for custom sidebar UI
    views/: Folder with individual pages
    candidate_form.py: Captures candidate data
    interview_ques.py: Generates and displays questions
    CB_logic.py: Calls LLM API to generate questions based on the tech stack
    prompts.py: Stores prompt templates for both data collection and question generation

2.  Design Decisions
    Session-based Routing: Uses st.session_state for smooth page transitions instead of default Streamlit multipage setup
    Input Validation: Ensures valid email, phone number, and completeness of form
    Prompt Design: Prompts guide the LLM to produce questions that are:
      Relevant to the candidate’s skills
      Diverse in difficulty
      Clearly worded and concise

3.  Prompt Design Explanation
    Candidate Info Prompt
    Extracts unambiguous candidate details

4.  Technical Question Prompt
    Generate 5 questions per technology
    Questions span difficulty levels and are easy to interpret

5.  Challenges & Solutions
    API Rate Limits: Solved with error handling and question caching in st.session_state
    Navigation Bugs: Fixed using st.rerun() and session logic
    UI Enhancements: Implemented clean sidebar navigation and styled UI using embedded HTML/CSS
    Input Validation: Added robust checks for form inputs

6. Data Privacy and Simulated Data
   Simulated Data: All candidate data is anonymized for demo purposes
   Data Privacy: No data is permanently stored or transmitted, aligning with GDPR-friendly design

## Author

[Sashank Sagar](https://github.com/Sashank-Sagar)
