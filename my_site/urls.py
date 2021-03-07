from django.urls import path
from .views import home, sobre_nos

urlpatterns = [
    path('', home),
    path('sobre/', sobre_nos),
]