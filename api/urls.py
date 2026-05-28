from django.urls import path, include


urlpatterns = [
    path('auth/', include('accounts.urls')),
    path('complaints/', include('complaints.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('map/', include('map.urls')),
    path('social/', include('social.urls')),
    path('ai/', include('ai_system.urls')),
    path('payments/', include('payments.urls')),
    path('taxi/', include('taxi.urls')),
    path('news/', include('news.urls')),
    path('notifications/', include('notifications.urls')),
]