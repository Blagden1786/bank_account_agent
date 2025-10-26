from google import genai
from .triage_agent import triage_agent
import re
# The triage agent will ask questions until it understands the ask, it will then generate a prompt for the other agent

ORCHESTRATOR_PROMPT = """You are an orchestrator agent that's is to find out what the user is enquiring about and then hand over to the relevant agent. You will ask the user a series of questions to understand their needs. Once you have enough information, you will return python code that runs the correct agent. Make sure that your first message explains what you can do and asks the user what they need help with.

You have access to the following agents:
1. Savings Agent: Finds the best savings account for the user. Run with savings_agent()

When calling an agent, use exactly the following format:
TOOL: <agent_name>()

For example, to call the savings agent, you would write:
TOOL: savings_agent()


The information you have so far is:
"""

def orchestrator_agent():
    """The orchestrator agent function that interacts with the user to determine their needs and delegate to the appropriate agent.

    Returns:
        str: The final outcome from the delegated agent.
    """
    prompt = ORCHESTRATOR_PROMPT

    while True:
        # Run the orchestrator agent
        client = genai.Client()
        # Generate the response
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt).text

        next_question=re.search("^TOOL", response)

        # No tool is called then the agent has sufficient info so it has produced the final prompt to be used by the relevant agent
        if next_question != None:
            print("Thanks, I will now find the best account for you.")
            break

        print(response)
        answer = input("ANSWER: ")

        # Append the answer to the prompt for the next iteration
        prompt += f"\nQUESTION:{response}: ANSWER: {answer}"


    return response
