from bank_account_agent import run_agent, BANK_ACCOUNT_PROMPT
from triage_agent import triage_agent, TRIAGE_PROMPT



prompt = triage_agent(TRIAGE_PROMPT)

print(run_agent(BANK_ACCOUNT_PROMPT + prompt, True))
