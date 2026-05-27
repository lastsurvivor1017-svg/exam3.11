from django.urls import path
from .views import DashboardStatsView
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('stats/', DashboardStatsView.as_view()),
    path('news/', views.news, name='news'),
    path('taxi/', views.news, name='taxi')
]