from django.shortcuts import render
from rest_framework import viewsets
from .models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


def map_view(request):
    return render(request, 'map/map.html')