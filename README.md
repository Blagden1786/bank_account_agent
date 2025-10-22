<h1>BANK ACCOUNT AGENT</h1>

<h3>What is it?</h3>
The bank account agent is a LLM based agent that finds the best savings accounts based on the users preferences. It has two stages: a triage stage and a search stage.

<h3>Triage Agent</h3>
The triage agent is the first of two agents. It's goal is to find out what the customer wants. It does this by repeatedly asking questions until it finds out what type of account the customer wants to open. 

<h3>Savings Agent</h3>
The savings agent takes the details found by the triage agent and uses tools to complete the request. It uses an LLM based web scraper to find the suitable accounts and then chooses the best one from this. It can also perform interest calculations if requested by the triage stage.

<h3>Result</h3>
These two agents work together to produce a fully functional system that finds the best rate account satisfying the user requests.

<h1>Running the Agent</h1>
<h3>Libraries</h3>
<ul>
  <li>Django</li>
  <li>Google Genai</li>
  <li>Requests</li>
  <li>BeautifulSoup</li>
  <li>re</li>
  <li>sys</li>
  
</ul>

You will also need to get a google API key from [this site](https://aistudio.google.com/api-keys) and replace all instances of ```client = genai.Client()``` with ```client = genai.Client(api_key="YOUR_API_KEY")```. These instances are spread across the files in agent_code and agent_code/tools.

<h3>In the terminal</h3>
Run the file bank_account_agent/agent_code/terminal_app.py in the terminal.

<h3>The web app</h3>
Run the command: python .\bank_account_agent\manage.py runserver</br> from a terminal and follow the link it produces.
