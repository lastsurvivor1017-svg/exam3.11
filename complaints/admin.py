from django.contrib import admin
from .models import Complaint

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'category', 'created_at', 'user')
    list_filter = ('status', 'category')
    search_fields = ('title', 'description')