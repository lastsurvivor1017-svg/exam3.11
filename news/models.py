from django.db import models
from accounts.models import User

class News(models.Model):

    CATEGORY_CHOICES = (
        ('traffic', 'Traffic'),
        ('weather', 'Weather'),
        ('emergency', 'Emergency'),
        ('events', 'Events'),
        ('general', 'General'),
    )

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news/',blank=True,null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='general')
    is_breaking = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
