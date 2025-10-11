import re
from tools import *
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

Now begin, remember to use the EXACT format as above.
Once you have sufficient information to provide an answer give a natural answer to the question.

Question: Find me the best instant access savings accounts and find the value of an investment of £100 over 5 years for that account."""


def run_agent(prompt, trace) -> str:
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

print(run_agent(SYSTEM_PROMPT, True))
