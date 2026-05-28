from rest_framework.routers import DefaultRouter
from .views import PlaceViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register('', PlaceViewSet)
urlpatterns = router.urls


urlpatterns = router.urls + [
    path('map/', views.map_view, name='map')
]