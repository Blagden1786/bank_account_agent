from django.urls import path
from . import views


urlpatterns = [
    path('', views.chat_view, name='chat-home'),
    path('agent/', views.agent_response, name='agent-response'),  # New endpoint
]
