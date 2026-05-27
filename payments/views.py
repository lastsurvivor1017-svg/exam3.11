from django.shortcuts import render
from rest_framework import viewsets
from .models import Payment
from .serializers import PaymentSerializer

from .services import generate_reference,process_payment


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    def perform_create(self, serializer):
        status = process_payment()

        serializer.save(
            reference_id=generate_reference(),
            status=status
        )


def payment(request):
    return render(request, 'payments/payments.html')