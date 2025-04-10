import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from prompts import genrate_tech_prompt


# To load environment variable from .env file | here environment variable is GOOGLE API KEY
load_dotenv()


# Ensuring if API Key is available in environment variable
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found in environment variables")
    exit(1)

# Gemini API  Config
genai.configure(api_key = api_key)

# Defining get_LLM_response function
def get_LLM_response(tech_stack):
    
    # check if there is a tech stack
    if not tech_stack:
        st.error("Tech stack input is empty")
        return("Error: No tech stack is provided")
    
    # Prompt Generation
    prompt = genrate_tech_prompt(tech_stack)
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(prompt, generation_config={"max_output_tokens": 300})

        # Extracting response from google gemini 
        if response and hasattr(response, "text") and response.text:
            questions = [q.strip() for q in response.text.split("\n") if q.strip()]
            return questions
        else:
            st.warning("No questions generated. Try refining the prompt.")
            return ["No questions generated. Try refining the prompt."]
    except Exception as e:
        st.exception(f"Error: Unexpected error {e}")
        return ["Error: Failed to fetch questions"]
    

