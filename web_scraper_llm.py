import requests
from bs4 import BeautifulSoup
from google import genai

'''

'''

def sumamrise(text:str)-> str:
    """Use an llm to summarise the text/html code of a website and pull out the savings in a machine readable format

    Args:
        text (str): The website

    Returns:
        str: The machie readable text
    """

    PROMPT = """You are a helpful bot that summarises the input website. Your main goal is to extract the following information for each savings account:
Bank, Account type, Interest rate, withdrawal limits, ISA or savings account?, Fixed or variable rate?

After finding this information, place it into a format that is easily machine readable (eg JSON).

For example:
Input site: HSBC: account1 5% variable instant access, account2 10% fixed rate ISA no access
Output: {{Bank: HSBC, Name: account1, Rate: 5%, Withdrawals: Instant access, Type: Savings, Rate Change: Variable}, {Bank: HSBC, Name: account2, Rate: 10%, Withdrawals: None, Type: ISA, Rate Change: Fixed}}

The input you will receive will either be plain text or html code for the website. Now go and find all of the savings accounts!\n""" + text

    client = genai.Client()
    response = client.models.generate_content(
            model="gemini-2.5-flash", contents=PROMPT
        )

    return response

def web_search(url) -> str:
    """Web search a collection of webpages to get savings info

    Args:
        url (str): url of website

    Returns:
        str: Output of LLM for the url search
    """
    # Get HTML source code of the webpage
    response = requests.get(url)

    # Parse the source code using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    return sumamrise(text)
