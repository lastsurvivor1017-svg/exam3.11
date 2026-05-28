from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet
from django.urls import path
from . import views

router = DefaultRouter()

router.register('', NotificationViewSet, basename='notifications')

urlpatterns = router.urls + [
    path('page/', views.notifications_page, name='notifications'),
]