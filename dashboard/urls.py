from django.urls import path
from .views import DashboardStatsView
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('stats/', DashboardStatsView.as_view()),
    path('taxi/', views.taxi, name='taxi')
]