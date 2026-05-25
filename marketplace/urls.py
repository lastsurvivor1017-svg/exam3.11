from rest_framework.routers import DefaultRouter
from .views import ShopViewSet, ProductViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register('shops', ShopViewSet)
router.register('products', ProductViewSet)
router.register('cart', CartViewSet)
router.register('orders', OrderViewSet)

urlpatterns = router.urls