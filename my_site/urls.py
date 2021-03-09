from django.urls import path
from .views import home, sobre_nos, contato

urlpatterns = [
    path('', home),
    path('sobre/', sobre_nos),
    path('contato/', contato),
]