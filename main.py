import re
from google import genai
import ddgs

# Get API key
client = genai.Client()

# The system prompt that will be used for the agent
#ques = input("Task: ")

SYSTEM_PROMPT = """Answer the following question as best you can. You have access to the following tools:

dummy_search_tool: Get the result of a web search
    Input
        - search_term (str): The search term to use

The way you use the tools is by specifying python code.
Specifically, this python code should be a single function call to the tool that you wish to use.

The only values that should be in the "action" field are:
dummy_search_tool: Get the current weather in a given location, args: {"search_term": {type: string}}
example use :

dummy_search_tool("What is the weather in London?")


ALWAYS use the following exact format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:$Python Function Call


Now begin! Reminder to ALWAYS use the exact characters when you provide a definitive answer.

Question: Find me the worst instant access savings accounts"""

# Define a dummy tool to use for testing purposes
def dummy_search_tool(search_term:str) -> str:
    return f"Natwest: 3.5%, Monzo: 5%, Suffolk Building Society: 8%"

def interest_calc(rate, investment, time):
    return investment*rate**time

# Generate the response
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=SYSTEM_PROMPT
)
print(response.text)

# Find the tool that the agent has called
tool_use=re.search("(dummy_search_tool)\(.*\)$",response.text)

if tool_use:
    print(tool_use.group())

    outcome = eval(tool_use.group())
    print(outcome)

    new_prompt = SYSTEM_PROMPT + f"\nThe result of the first tool use was:\n{outcome}.\nIf this is sufficient information to make a recommendation "
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=new_prompt
    )

    print("\n-----------FINAL ANSWER------------\n")
    print(response.text)


# Error if no text generated
else:
    print("Code not formatted right. Try again")
