
# Define a dummy tool to use for testing purposes
import re
import requests
from bs4 import BeautifulSoup

# Dummy search tool
def dummy_search_tool(search_term:str) -> str:
    return f"Natwest: 3.5% fixed, Monzo: 5% fixed, Suffolk Building Society: 5% variable"

# Proper search tool
def web_search_tool(search_term):
    # We will extract plain text from this webpage
    url = 'https://www.which.co.uk/money/savings-and-isas/savings-accounts/how-to-find-the-best-savings-account-aAWTh2N0jTx5'
    print(url)
    # Get HTML source code of the webpage
    response = requests.get(url)

    # Parse the source code using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the plain text content
    text = soup.get_text()

    # Print the plain text
    return text

# Tool to calculate return on investment
def interest_calc(rate, investment, time):
    return investment*(1+rate)**time


# Overall regex to match the functions
match_num = r'[+-]?(?:\d*\.\d+|\d+)'

dummy_search_regex = r'(dummy_search_tool\(".*"\))'
web_search_regex = r'(web_search_tool\((search_term=)*".*"\))'
interest_calc_regex = f'(interest_calc\({match_num}\,( )*{match_num}\,( )*{match_num}\))'

func_regex = f"{web_search_regex}|{interest_calc_regex}"
