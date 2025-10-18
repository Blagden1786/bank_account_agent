from agents.savings_agent import savings_agent, SAVINGS_PROMPT
from agents.triage_agent import triage_agent, TRIAGE_PROMPT
import sys
import re


trace = False

if len(sys.argv) > 1:
    if sys.argv[1] == "True":
        trace = True
        print("DEBUG MODE\nPrinting all agent outputs...")


# Run the triage agent first to get the user requirements
prompt = TRIAGE_PROMPT
while True:
    response = triage_agent(prompt)

    next_question=re.search("^QUESTION", response)

    # No tool is called then the agent has sufficient info so it has produced the final prompt to be used by the savings agent
    if next_question == None:
        print("Thanks, I will now find the best account for you.")
        break

    print(response)
    answer = input("ANSWER: ")

    # Append the answer to the prompt for the next iteration
    prompt += f"\n{response}: ANSWER: {answer}"



if trace:
    print(prompt)
# Feed the output of the triage agent into the savings agent
outcome = savings_agent(SAVINGS_PROMPT + prompt, trace)

print(outcome)
