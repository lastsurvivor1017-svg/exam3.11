from rest_framework.permissions import BasePermission

class IsShopOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'shop_owner'