import re
from google import genai
import ddgs

client = genai.Client()

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


ALWAYS use the following format:

Question: the input question you must answer
Thought: you should always think about one action to take. Only one action at a time in this format:
Action:$Python Function Call


Now begin! Reminder to ALWAYS use the exact characters when you provide a definitive answer.

Question: Provide me with a list of the best savings accounts"""


def dummy_search_tool(search_term:str) -> str:
    return "Hello this was the result of the search"


#response = client.models.generate_content(
#    model="gemini-2.5-flash", contents=SYSTEM_PROMPT
#)
response = "Hello dummy_search_toolx() dummy_search_tool('Test')"

tool_use=re.search("(dummy_search_tool)\(.*\)$",response)

if tool_use:
    print(tool_use.group())
