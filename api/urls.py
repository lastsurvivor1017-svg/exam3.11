from django.urls import path, include

urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('complaints/', include('complaints.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('map/', include('map.urls')),
    path('ai/', include('ai_system.urls')),
    path('social/', include('social.urls')),
]