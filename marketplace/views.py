from rest_framework import viewsets
from .models import Shop, Product, Cart, Order
from .serializers import ShopSerializer, ProductSerializer, CartSerializer, OrderSerializer
from django.shortcuts import render


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def market(request):
    return render(request, 'marketplace/marketplace.html')