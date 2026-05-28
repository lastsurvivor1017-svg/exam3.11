from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'is_breaking',
        'created_at'
    )
    list_filter = (
        'category',
        'is_breaking'
    )
    search_fields = (
        'title',
        'content'
    )

