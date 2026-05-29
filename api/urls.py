from django.urls import path, include
from rest_framework.routers import DefaultRouter
from complaints.views import ComplaintViewSet
from . import views

urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('complaints/', include('complaints.urls')),
    path('map/', include('map.urls')),
    path('social/', include('social.urls')),
    path('ai/', include('ai_system.urls')),
    path('payments/', include('payments.urls')),
    path('taxi/', include('taxi.urls')),
    path('news/', include('news.urls')),
    path('notifications/', include('notifications.urls')),
]