import re
from google import genai
import ddgs

# Debug settings
trace = True

# Get API key
client = genai.Client()

# The system prompt that will be used for the agent
#ques = input("Task: ")

SYSTEM_PROMPT = """Answer the following question as best you can. You have access to the following tools:

dummy_search_tool: Get the result of a web search
    Input
        - search_term (str): The search term to use

interest_calc: Calculate the growth of an investment over a few years.
    Input
        - rate (float): the interest rate as a number (eg 5%=0.05)
        - investment (float): the initial investment
        - time (float): the number of years to leave the investment for

The way you use the tools is by specifying python code.
Specifically, this python code should be a single function call to the tool that you wish to use.

The only values that should be in the "action" field are:
dummy_search_tool: Run a search for the given term, args: {"search_term": {type: string}}
interest_calc: Calculate the growth of an investment over a few years, args: {"rate": {type: float}, "investment": {type: float}, "time": {type: float}}
example uses :

dummy_search_tool("What is the weather in London?"),

interest_calc(0.04, 1000, 1)


ALWAYS use the following exact format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:$Python Function Call


Now begin! Reminder to ALWAYS use the exact characters when you provide a definitive answer.

Question: Find me the best instant access savings accounts"""

# Define a dummy tool to use for testing purposes
def dummy_search_tool(search_term:str) -> str:
    return f"Natwest: 3.5%, Monzo: 5%, Suffolk Building Society: 8%"

def interest_calc(rate, investment, time):
    return investment*(1+rate)**time

# Generate the response
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=SYSTEM_PROMPT
)
if trace:
    print(response.text)

# Find the tool that the agent has called
tool_use=re.search("(dummy_search_tool)\(.*\)$",response.text)

if tool_use:
    if trace:
        print(tool_use.group())

    outcome = eval(tool_use.group())
    if trace:
        print(outcome)

    new_prompt = SYSTEM_PROMPT + response.text + f"\nThe result of the first tool use was:\n{outcome}.\nIf this is sufficient information to make a recommendation, Respond in exactly the same way to call a tool to find out how much a £100 investment would grow to over 5 years using the best investment. If not, write another search term"
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=new_prompt
    )

    if trace:
        print(response.text)

    tool_use=re.search("(interest_calc)\(.*\)$",response.text)

    if tool_use:
        if trace:
            print(tool_use.group())

        outcome = eval(tool_use.group())
        if trace:
            print(outcome)

        prompt = new_prompt + f"\n{response.text}" + f"\nThe result of the second tool use was:\n{outcome}.\n Now make a recommendation of the best account to use and the calculated return."
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )

        print(response.text)
# Error if no text generated
else:
    print("Code not formatted right. Try again")
