from django.contrib import admin
from .models import Shop, Product, Cart, Order, OrderItem

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)