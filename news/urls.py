from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import NewsViewSet
from . import views

router = DefaultRouter()
router.register('', NewsViewSet)

urlpatterns = router.urls + [
path('page/', views.news_page, name='news'),
]
