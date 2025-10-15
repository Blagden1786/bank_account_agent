import requests
from bs4 import BeautifulSoup

# Program to test the websites to make sure we can scrape meaningful information from them

# We will extract plain text from this webpage
url = 'https://www.hsbc.co.uk/savings/products/'
print(url)
# Get HTML source code of the webpage
response = requests.get(url)

# Parse the source code using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the plain text content
text = soup.get_text()

# Print the plain text
print(text)
