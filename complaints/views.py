from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification
from .models import Complaint
from .serializers import ComplaintSerializer
from ai_system.services import analyze_complaint


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        text = self.request.data.get("description")
        analysis = analyze_complaint(text)

        Notification.objects.create(
            user=self.request.user,
            title="Complaint Submitted",
            message="Your complaint has been submitted successfully.",
            notification_type="complaint"
        )

        serializer.save(
            user=self.request.user,
            category = analysis.get("category", "road")
        )



def complaints_page(request):
    data = Complaint.objects.all().order_by('-created_at')
    return render(request, 'complaints/complaints.html', {'complaints': data})