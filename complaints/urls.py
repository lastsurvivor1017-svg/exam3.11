from rest_framework.routers import DefaultRouter
from .views import ComplaintViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register('', ComplaintViewSet)

urlpatterns = router.urls + [
    path('page/', views.complaints_page, name='complaints'),
]