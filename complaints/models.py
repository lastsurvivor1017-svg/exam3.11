from django.db import models
from django.db import models
from django.conf import settings

class Complaint(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    CATEGORY_CHOICES = (
        ('road', 'Road'),
        ('water', 'Water'),
        ('electricity', 'Electricity'),
        ('garbage', 'Garbage'),
        ('traffic', 'Traffic'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    image = models.ImageField(upload_to='complaints/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title