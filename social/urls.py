from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet
from django.urls import path
from . import views

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)

urlpatterns = router.urls + [
    path('page/', views.social, name='social'),
]