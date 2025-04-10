import streamlit as st
import re

# Function to check email is valid
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Function to check phone no is valid
def is_valid_phone(phone):
    return phone.isdigit() and (7 <= len(phone) <= 15)

# For validating inputs
def validate_inputs(name, email, phone, tech_stack, desired_position, current_location):
    # Check each field separately and return the first error encountered.
    if not name:
        return "Please fill the name!"
    if not email:
        return "Please fill the email!"
    elif not is_valid_email(email):
        return "Invalid email format."
    if not phone:
        return "Please fill the phone number!"
    elif not is_valid_phone(phone):
        return "Invalid phone number!"
    if not desired_position:
        return "Please fill the desired position!"
    if current_location == "Select your location":
        return "Please select your current location!"
    if not tech_stack:
        return "Please fill the Tech Stack!"
    return None

def render_candidate_form():
    try:
        st.header("Candidate Info Form")
        with st.form(key="candidate_form"):
            name = st.text_input("NAME:", placeholder="Enter your full name")
            email = st.text_input("EMAIL:", placeholder="Enter your email")
            phone_no = st.text_input("CONTACT NO.:", placeholder="Enter your contact no.")
            experience = st.number_input("EXPERIENCE:", min_value=0, max_value=50)
            desired_position = st.text_input("DESIRED POSITION:", placeholder="e.g. Software Engineer, Data Analyst")
            
            locations = ["Select your location", "Delhi", "Bangalore", "Hyderabad", "Mumbai", "Chennai", "Panipat", "Other"]
            current_location = st.selectbox("CURRENT LOCATION:", locations)
            
            tech_stack = st.text_input("TECHNICAL STACK:", placeholder="e.g. Python, Java, C++", help="Separate technologies with commas")
            
            submitted = st.form_submit_button("Submit")
        
        candidate_info = {
            "name": name.strip(),
            "email": email.strip(),
            "phone_no": phone_no.strip(),
            "experience": experience,
            "desired_position": desired_position.strip(),
            "current_location": current_location,
            "tech_stack": tech_stack.strip(),
            "submitted": submitted
        }
    
        if candidate_info["submitted"]:
            errors = validate_inputs(
                candidate_info["name"],
                candidate_info["email"],
                candidate_info["phone_no"],
                candidate_info["tech_stack"],
                candidate_info["desired_position"],
                candidate_info["current_location"]
            )
            if errors:
                st.error(errors)
            else:
                st.session_state['candidate_info'] = candidate_info
                st.success("Candidate information saved! Redirecting...")
                # Instead of using switch_page, uesd set the session state page and call st.rerun()
                st.session_state['page'] = "Interview Questions"
                st.rerun()
    
    except Exception as e:
        st.error("Error: Unable to collect candidate data")
        st.exception(e)
