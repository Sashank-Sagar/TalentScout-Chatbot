import streamlit as st

def render_sidebar():
    st.sidebar.title("Menu")
    
    # Ensure default page value exists in session state
    if "page" not in st.session_state:
        st.session_state["page"] = "Home"
    
    # When a button is clicked, update session state and force a rerun to immediately reflect the change.
    if st.sidebar.button("Home"):
        st.session_state.page = "Home"
        st.rerun() 
        
    if st.sidebar.button("Candidate Form"):
        st.session_state.page = "Candidate Form"
        st.rerun()
    
    if st.sidebar.button("Interview Questions"):
        st.session_state.page = "Interview Questions"
        st.rerun()
