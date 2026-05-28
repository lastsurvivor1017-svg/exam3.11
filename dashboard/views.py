from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import complaint_by_category
from accounts.models import User
from complaints.models import Complaint
from marketplace.models import Order
from django.contrib.auth.decorators import login_required



class DashboardStatsView(APIView):
    def get(self, request):
        return Response({
            "total_users": User.objects.count(),
            "total_complaints": Complaint.objects.count(),
            "pending_complaints": Complaint.objects.filter(status="pending").count(),
            "resolved_complaints": Complaint.objects.filter(status="resolved").count(),
            "total_orders": Order.objects.count(),
            "by_category": complaint_by_category(),
        })

        return Response(data)
    

class DashboardStatsView(APIView):
    def get(self, request):
        return Response({
            "total_users": User.objects.count(),
            "total_complaints": Complaint.objects.count(),
            "by_category": complaint_by_category(),
        })
    


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def news(request):
    return render(request, 'dashboard/news.html')

from django.shortcuts import render

def taxi(request):
    return render(request, 'taxi.html')