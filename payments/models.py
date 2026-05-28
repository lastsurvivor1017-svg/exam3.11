from django.db import models
from accounts.models import User


class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )

    PAYMENT_TYPE_CHOICES = (
        ('bill', 'Bill'),
        ('order', 'Order'),
        ('tax', 'Tax'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20,choices=PAYMENT_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    reference_id = models.CharField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reference_id