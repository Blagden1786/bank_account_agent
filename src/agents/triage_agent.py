import re
from google import genai
from pyparsing import C

# The triage agent will ask questions until it understands the ask, it will then generate a prompt for the other agent

TRIAGE_PROMPT = """You are a triage agent. Your goal is to find out what type of savings account the user is wanting to open. You should ask easy to understand questions until you get all of the required information and once this has been acquired produce a prompt to tell another agent to find the best account meeting the criteria.
The information you are trying to get is:
Type of account: ISA or not
Rate: Fixed or Variable
Access amount: None, instant, etc
Any interest calculation the user would like done: Eg £100 over 2 years

When asking a question use exactly the following format:
QUESTION: <Question>

When providing the prompt, do not produce any other text other than the prompt.

The information you have so far is:
"""

def triage_agent(prompt):
    client = genai.Client()

    # Generate the response
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )

    return response.text
