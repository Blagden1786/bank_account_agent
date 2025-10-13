from smolagents import DuckDuckGoSearchTool
from googlesearch import search
from ddgs import DDGS
import requests
from bs4 import BeautifulSoup

results = DDGS().text("Best savings accounts uk", max_results=5)



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
print(text)
