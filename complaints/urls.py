from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet
from django.urls import path
from . import views

urlpatterns =  [
    path('', views.complaints_page, name='complaints'),
]