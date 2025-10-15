import re
from tools import *
from google import genai
from smolagents import DuckDuckGoSearchTool
import ddgs


# The system prompt that will be used for the agent
#ques = input("Task: ")

BANK_ACCOUNT_PROMPT = """Answer the following question as best you can. You have access to the following tools:

account_finder_tool: Get information about different savings account

interest_calc: Calculate the growth of an investment over a few years.
    Input
        - rate (float): the interest rate as a number (eg 5%=0.05)
        - investment (float): the initial investment
        - time (float): the number of years to leave the investment for

The way you use the tools is by specifying python code.
Specifically, this python code should be a single function call to the tool that you wish to use.

The only values that should be in the "action" field are:
account_finder_tool: Run a search for the given term, args: None
interest_calc: Calculate the growth of an investment over a few years, args: {"rate": {type: float}, "investment": {type: float}, "time": {type: float}}
example uses :

account_finder_tool(),

interest_calc(0.04, 1000, 1)


ALWAYS use the following exact format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:$Python Function Call

Now begin, remember to use the EXACT format as above.
Once you have sufficient information to provide an answer give a natural answer to the question.

Task: """


def run_agent(prompt, trace) -> str:
    # Get API key
    client = genai.Client()

    while True:
        # Generate the response
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=prompt
        )
        if trace:
            print(f"----------Debug Agent Response----------\n{response.text}\n----------------------------------------\n")
        # Find the tool that is wanted to be used
        tool_use=re.search(func_regex,response.text)
        # No tool is called then the agent has sufficient info so it can produce an answer
        if tool_use == None:
            return response.text

        # Use the tool
        outcome = eval(tool_use.group())
        if trace:
            print(f"----------Tool Use----------\n{tool_use.group()}\n----------------------------\n")
            print(f"----------Outcome----------\n{outcome}\n---------------------------\n")

        prompt += f"\nAgent response: {response.text}\nThe outcome of the usage of the tool use was {outcome}"
