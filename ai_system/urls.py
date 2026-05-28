from django.urls import path
from .views import ChatBotView, smart_api
from . import views

urlpatterns = [
    path('', views.ai, name='ai'),
    path('chat/', ChatBotView.as_view()),
    path("smart/", smart_api, name='smart'),
]