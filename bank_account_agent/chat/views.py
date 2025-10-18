from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from src.agents.triage_agent import triage_agent, TRIAGE_PROMPT

def chat_view(request):
    """Render the simple chat page."""
    return render(request, 'chat.html')

@csrf_exempt
def agent_response(request):
    """Respond to AJAX POST request with agent reply"""
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        reply = run_agent(user_message)
        return JsonResponse({'reply': reply})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def run_agent(user_message):
    # Replace this with your real agent logic
    return triage_agent(TRIAGE_PROMPT)
