import random


def genrate_tech_prompt(tech_stack):
    return (
        f"You are an AI interview assistant. Generate exactly 5 technical interview questions "
        f"for candidate skill in {tech_stack}.\n\n"
        f"Guidelines:\n"
        f"- Questions should be clear, concise, and relevant to {tech_stack}.\n"
        f"- Cover a mix of difficulty levels: Basic, Intermediate, Advanced.\n"
        f"- Do not add numbering, bullet points, or symbols.\n"
        f"- Do not add the difficulty level at the END of the question.\n"
        f"- Example:\n"
        f"  What is the difference between a list and a tuple in Python?\n"
        f"  How do garbage collectors work in Java?\n\n"
        f"Generate questions now:"
    )

fallback_prompt = "Sorry, I didn’t understand that. Could you please clarify or rephrase?"

def generate_greeting_prompt(name):
    greetings = [
        f"Hi {name}, Here Are Your Interview Questions!",
        f"Hello {name}, Ready To Challenge Yourself? Here's Your Interview Questions.",
        f"Great To See You, {name}! Let's Start With These Interview Questions.",
    ]
    return random.choice(greetings)