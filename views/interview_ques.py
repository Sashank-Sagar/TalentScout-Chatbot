import streamlit as st
import re
from CB_logic import get_LLM_response
from prompts import generate_greeting_prompt

# Function to clean question text
def clean_question(q):
    try:
        cleaned = q.strip()
        # Remove leading numbers or bullet symbols if present
        if cleaned and cleaned[0].isdigit() and (cleaned[1] in [".", ")", " "]):
            cleaned = cleaned[2:].strip()
        elif cleaned.startswith(("-", "*")):
            cleaned = cleaned[1:].strip()
        # Reformat difficulty tags if present (e.g., "(Easy) ...")
        match = re.match(r"\((Easy|Medium|Hard|Easy/Medium|Medium/Hard)\)\s*(.+)", cleaned)
        if match:
            difficulty, question = match.groups()
            cleaned = f"{question.strip()} ({difficulty})"
        return cleaned or q.strip()
    except Exception:
        return q.strip()

def render_interview_questions():
    st.header("Interview Questions")
    try:
        # Verify candidate data is present
        if "candidate_info" not in st.session_state:
            st.warning("No candidate data found. Please fill the form first!")
            st.stop()
        
        candidate = st.session_state["candidate_info"]
        name = candidate.get("name", "").strip()
        tech_stack_raw = candidate.get("tech_stack", "").strip()

        # If inputs are missing, display a warning and stop
        if not name or not tech_stack_raw:
            st.warning("Candidate data is incomplete. Please re-enter the form.")
            st.stop()

        st.success(f"Generating Questions for {name}")
        st.markdown(generate_greeting_prompt(name))
        
        # Processing tech stack
        techs = [tech.strip() for tech in tech_stack_raw.split(",") if tech.strip()]
        if not techs:
            st.warning("No valid technologies found in Tech Stack.")
            st.stop()
        
        # Dictionary to hold generated questions for each tech
        questions_dict = {}
        
        for tech in techs:
            with st.spinner(f"Generating questions for {tech}..."):
                try:
                    questions = get_LLM_response(tech)
                    if not isinstance(questions, list) or not questions:
                        st.warning(f"Couldn't generate questions for: {tech}")
                        continue
                    # Save generated questions
                    questions_dict[tech] = questions

                    # Display the questions in an expander for the current technology
                    st.markdown("---")
                    st.subheader(f"Questions for {tech}:")
                    with st.expander(f"Here are your questions for {tech}:"):
                        for q in questions:
                            st.markdown(f"• {clean_question(q)}")
                except Exception as e:
                    st.error(f"Error while generating questions for: {tech}")
                    st.exception(e)
        
        # Caching the generated questions in session state
        st.session_state["questions"] = questions_dict

        # Processing all questions for download
        questions_text = ""
        for tech, qlist in questions_dict.items():
            questions_text += f"Questions for {tech}:\n"
            for q in qlist:
                questions_text += f"• {clean_question(q)}\n"
            questions_text += "\n"

        # Download Button to download generated questions
        st.download_button(
            label="Download Interview Questions",
            data=questions_text,
            file_name="interview_questions.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error("Error: An unexpected error occurred")
        st.exception(e)
