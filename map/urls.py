from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet
from django.urls import path
from . import views



urlpatterns =  [
    path('', views.map_view, name='map'),
]