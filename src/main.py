from savings_agent import savings_agent, SAVINGS_PROMPT
from triage_agent import triage_agent, TRIAGE_PROMPT
import sys


trace = False

if len(sys.argv) > 1:
    if sys.argv[1] == "True":
        trace = True
        print("DEBUG MODE\nPrinting all agent outputs...")


# Run the agents
prompt = triage_agent(TRIAGE_PROMPT)

if trace:
    print(prompt)
# Feed the output of the triage agent into the savings agent
outcome = savings_agent(SAVINGS_PROMPT + prompt, trace)

print(outcome)
