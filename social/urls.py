from rest_framework.routers import DefaultRouter
from .views import PostViewSet,CommentViewSet,LikeViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)
urlpatterns = router.urls