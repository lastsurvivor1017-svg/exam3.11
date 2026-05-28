from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Complaint
from .serializers import ComplaintSerializer
from notifications.models import Notification
from ai_system.services import analyze_complaint


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all().order_by('-created_at')
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        complaint = serializer.save(user=self.request.user)

        analysis = analyze_complaint(complaint.description)

        complaint.category = analysis.get("category", "road")
        complaint.save()

        Notification.objects.create(
            user=self.request.user,
            title="Complaint Submitted",
            message="Your complaint has been submitted successfully.",
            notification_type="complaint"
        )

    @action(detail=False, methods=['get'])
    def page(self, request):
        complaints = self.queryset
        serializer = self.get_serializer(complaints, many=True)

        return Response(serializer.data)

def complaints_page(request):
    data = Complaint.objects.all().order_by('-created_at')
    return render(request, 'complaints/complaints.html', {'complaints': data})