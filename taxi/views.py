from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from notifications.models import Notification
from .models import Ride
from .serializers import RideSerializer
from .services import calculate_price


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        ride = serializer.save(user=self.request.user)
        Notification.objects.create(
            user=self.request.user,
            title="🚕 Taxi Request Created",
            message=f"Your ride from {ride.pickup_location} is registered.",
            notification_type="taxi"
        )

    @action(detail=True, methods=['POST'])
    def accept(self, request, pk=None):
        ride = self.get_object()
        if request.user.role != 'driver':
            return Response({"error": "Only drivers can accept rides"})
        ride.driver = request.user
        ride.status = 'accepted'
        ride.save()
        return Response({"message": "Ride accepted"})

    @action(detail=True, methods=['POST'])
    def complete(self, request, pk=None):
        ride = self.get_object()
        if ride.driver != request.user:
            return Response({"error": "Not your ride"})
        ride.status = 'completed'
        ride.save()
        return Response({"message": "Ride completed"})

def taxi_page(request):
    rides = Ride.objects.all().order_by('-created_at')
    return render(request,'taxi/taxi.html',{'rides': rides})