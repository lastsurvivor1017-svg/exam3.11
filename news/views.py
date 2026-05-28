from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from .models import News
from .serializers import NewsSerializer
from .permissions import IsAdminUserRole
from accounts.models import User
from notifications.models import Notification


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_at')
    serializer_class = NewsSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdminUserRole()]
        return [IsAuthenticatedOrReadOnly()]
    def perform_create(self, serializer):
        news = serializer.save(author=self.request.user)
        users = User.objects.all()

        for user in users:
            Notification.objects.create(
                user=user,
                title="📰 New City News",
                message=news.title,
                notification_type="news"
            )


def news_page(request):
    news = News.objects.all().order_by('-created_at')
    return render(request,'news/news.html',{'news_list': news})