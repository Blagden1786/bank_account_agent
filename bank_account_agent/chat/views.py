from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from agent_code.agents.triage_agent import triage_agent_django

import re

def chat_view(request):
    # Clear the prompt file at the start of a new chat
    prompt_file = open('triage_prompt.txt', 'w')
    prompt_file.close()
    """Render the simple chat page."""
    return render(request, 'chat.html')

# AJAX endpoint to handle chat messages
@csrf_exempt
def agent_response(request):
    """Respond to AJAX POST request with agent reply"""
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        reply = triage_agent_django(user_message)
        return JsonResponse({'reply': reply})
    return JsonResponse({'error': 'Invalid request'}, status=400)
