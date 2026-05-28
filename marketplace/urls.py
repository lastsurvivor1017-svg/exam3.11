from rest_framework.routers import DefaultRouter
from .views import ShopViewSet, ProductViewSet, CartViewSet, OrderViewSet
from django.urls import path
from . import views

router = DefaultRouter()

router.register('shops', ShopViewSet)
router.register('products', ProductViewSet)
router.register('cart', CartViewSet)
router.register('orders', OrderViewSet)

urlpatterns = router.urls + [
    path('page/', views.market, name='market'),
]