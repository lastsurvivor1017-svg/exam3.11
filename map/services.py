from .models import Place
import math

def distance(lat1, lng1, lat2, lng2):
    return ((lat1-lat2)**2 + (lng1-lng2)**2) ** 0.5


def get_nearest_place(lat, lng, category=None):
    places = Place.objects.all()
    if category:
        places = places.filter(category=category)
    nearest = None
    min_dist = 999999

    for p in places:
        d = distance(lat, lng, p.lat, p.lng)
        if d < min_dist:
            min_dist = d
            nearest = p

    return nearest