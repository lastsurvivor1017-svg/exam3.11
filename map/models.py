from django.db import models


class Place(models.Model):
    CATEGORY_CHOICES = (
        ('hospital', 'Hospital'),
        ('school', 'School'),
        ('restaurant', 'Restaurant'),
        ('police', 'Police'),
        ('gas_station', 'Gas Station'),
    )

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name