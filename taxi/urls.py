from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RideViewSet
from . import views

router = DefaultRouter()
router.register('', RideViewSet)

urlpatterns = router.urls + [
path('page/', views.taxi_page, name='taxi'),
]
