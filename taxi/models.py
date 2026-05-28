from django.db import models
from django.contrib.auth.models import User

class Ride(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    price = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')