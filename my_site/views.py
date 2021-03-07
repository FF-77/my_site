from django.shortcuts import render
from .models import Produtos, Sobre_Nos

# Create your views here.
def home(request):

    produtos = Produtos.objects.all()

    return render(request, 'site/main.html', {'produtos': produtos})

def sobre_nos(request):

    sobre_nos = Sobre_Nos.objects.all()

    return render(request, 'site/sobre.html', {'sobre_nos': sobre_nos})
