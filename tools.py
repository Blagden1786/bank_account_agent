
# Define a dummy tool to use for testing purposes
import re
import requests
from bs4 import BeautifulSoup

from web_scraper_llm import web_search

# Dummy search tool
def dummy_search_tool(search_term:str) -> str:
    return f"Natwest: 3.5% fixed, Monzo: 5% fixed, Suffolk Building Society: 5% variable"

# Proper search tool
def web_search_tool(search_term):
    # We will extract plain text from this webpage
    urls = ['https://www.natwest.com/savings.html', 'https://www.hsbc.co.uk/savings/products/']
    # Get HTML source code of the webpage
    response = str([web_search(url) for url in urls])

    return response

# Tool to calculate return on investment
def interest_calc(rate, investment, time):
    return investment*(1+rate)**time


# Overall regex to match the functions
match_num = r'[+-]?(?:\d*\.\d+|\d+)'

dummy_search_regex = r'(dummy_search_tool\(".*"\))'
web_search_regex = r'(web_search_tool\((search_term=)*".*"\))'
interest_calc_regex = f'(interest_calc\((rate=)*{match_num}\,( )*(investment=)*{match_num}\,( )*(time=)*{match_num}\))'

func_regex = f"{web_search_regex}|{interest_calc_regex}"
