from django.db import models
from accounts.models import User

class Ride(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('on_way', 'On Way'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides')
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='driver_rides')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.id}"