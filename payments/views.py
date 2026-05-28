from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from .services import generate_reference, process_payment
from django.shortcuts import render
from notifications.models import Notification



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        payment_status = process_payment()
        
        Notification.objects.create(
        user=self.request.user,
        title="Payment Successful",
        message="Your payment completed successfully.",
        notification_type="payment"
        
        )
        serializer.save(
            reference_id=generate_reference(),
            status=payment_status
        )

def payment(request):
    return render(request, 'payments/payments.html')