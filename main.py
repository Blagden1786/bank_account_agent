from savings_account_agent import savings_agent, SAVINGS_PROMPT
from triage_agent import triage_agent, TRIAGE_PROMPT

# Run the agents

prompt = triage_agent(TRIAGE_PROMPT)

print(savings_agent(SAVINGS_PROMPT + prompt, True))
