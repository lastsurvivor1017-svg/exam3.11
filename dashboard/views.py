from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import User
from complaints.models import Complaint
from marketplace.models import Order


class DashboardStatsView(APIView):
    def get(self, request):
        data = {
            "total_users": User.objects.count(),
            "total_complaints": Complaint.objects.count(),
            "pending_complaints": Complaint.objects.filter(status="pending").count(),
            "resolved_complaints": Complaint.objects.filter(status="resolved").count(),
            "total_orders": Order.objects.count(),
        }

        return Response(data)