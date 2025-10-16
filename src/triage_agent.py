import re
from google import genai

# The triage agent will ask questions until it understands the ask, it will then generate a prompt for the other agent

TRIAGE_PROMPT = """You are a triage agent. Your goal is to find out what type of savings account the user is wanting to open. You should ask easy to understand questions until you get all of the required information and once this has been acquired produce a prompt to tell another agent to find the best account meeting the criteria.
The information you are trying to get is:
Rate: Fixed or Variable
Access amount: None, instant, etc
Type of account: ISA or Savings account

When asking a question use exactly the following format:
QUESTION: <Question>

When providing the prompt, do not produce any other text other than the prompt.

The information you have so far is:
"""

def triage_agent(prompt):
    client = genai.Client()

    while True:
        # Generate the response
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )

        # Find the tool that is wanted to be used
        next_question=re.search("^QUESTION",response.text)
        # No tool is called then the agent has sufficient info so it can produce an answer
        if next_question == None:
            print("Thanks, I will now find the best account for you.")
            return response.text

        print(response.text)
        answer = input("ANSWER: ")

        prompt += f"\n{response.text}: ANSWER: {answer}"
