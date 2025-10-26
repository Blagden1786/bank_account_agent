from agents.savings_agent import savings_agent, SAVINGS_PROMPT
from agents.triage_agent import triage_agent, TRIAGE_PROMPT
from agents.orchestrator_agent import orchestrator_agent
import sys


trace = False

if len(sys.argv) > 1:
    if sys.argv[1] == "True":
        trace = True
        print("DEBUG MODE\nPrinting all agent outputs...")

print(orchestrator_agent())
# Run the triage agent first to get the user requirements
prompt = triage_agent(TRIAGE_PROMPT)


if trace:
    print(prompt)
# Feed the output of the triage agent into the savings agent
outcome = savings_agent(SAVINGS_PROMPT + prompt, trace)

print(outcome)
