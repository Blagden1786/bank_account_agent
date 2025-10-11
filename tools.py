
# Define a dummy tool to use for testing purposes
import re

# Dummy search tool
def dummy_search_tool(search_term:str) -> str:
    return f"Natwest: 3.5% fixed, Monzo: 5% fixed, Suffolk Building Society: 5% variable"

# Tool to calculate return on investment
def interest_calc(rate, investment, time):
    return investment*(1+rate)**time


# Overall regex to match the functions
match_num = r'[+-]?(?:\d*\.\d+|\d+)'

dummy_search_regex = r'(dummy_search_tool\(".*"\))'
interest_calc_regex = f'(interest_calc\({match_num}\,( )*{match_num}\,( )*{match_num}\))'

func_regex = f"{dummy_search_regex}|{interest_calc_regex}"
