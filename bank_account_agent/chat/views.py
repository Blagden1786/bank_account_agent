from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from src.agents.triage_agent import triage_agent, TRIAGE_PROMPT
from src.agents.savings_agent import savings_agent, SAVINGS_PROMPT

import re

def chat_view(request):
    # Clear the prompt file at the start of a new chat
    prompt_file = open('triage_prompt.txt', 'w')
    prompt_file.close()
    """Render the simple chat page."""
    return render(request, 'chat.html')

@csrf_exempt
def agent_response(request):
    """Respond to AJAX POST request with agent reply"""
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        reply = run_triage_agent(user_message)
        return JsonResponse({'reply': reply})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def run_triage_agent(user_message):
    # Read the triage prompt file
    prompt_file = open('triage_prompt.txt', 'r+')

    # If it is empty: add the triage prompt
    if not prompt_file.read(1):
        prompt_file.write(TRIAGE_PROMPT)

    # Append the user's message to the prompt file
    prompt_file.write(f"\nANSWER: {user_message}\n")

    # Get the prompt from the file
    prompt_file.seek(0)
    prompt = prompt_file.read()
    prompt_file.close()

    # Run the triage agent
    response = triage_agent(prompt)
    next_question=re.search("^QUESTION", response)

    # If the agent hasn't asked a question, it has enough info
    if next_question == None:
        # Switch to savings agent
        return savings_agent(SAVINGS_PROMPT + response, True)
    else:
        # Append the question to the prompt file
        prompt_file = open('triage_prompt.txt', 'a')
        prompt_file.write(f"\n{response}")
        prompt_file.close()
        return response
