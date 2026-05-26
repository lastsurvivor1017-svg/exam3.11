from django.urls import path
from .views import ChatBotView
from . import views

urlpatterns = [
    path('', views.ai, name='ai'),
    path('chat/', ChatBotView.as_view()),
]