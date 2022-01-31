from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Favorite

def index(request):
    cryptos = Favorite.objects.all()
    context = {
        'cryptos': cryptos.lower()
    }
    return render(request, 'prices/index.html', context)

def single(request, name):
    return HttpResponse(name)
