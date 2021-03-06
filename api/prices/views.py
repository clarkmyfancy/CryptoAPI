from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Favorite

def index(request):
    cryptos = Favorite.objects.all()
    context = {
        'cryptos': cryptos
    }
    return render(request, 'prices/index.html', context)

class IndexView(ListView):
    template_name = 'prices/index.html'
    context_object_name = 'cryptos'

    def get_queryset(self):
        return Favorite.objects.all()

class DetailView(DetailView):
    template_name = 'prices/detail.html'
    context_object_name = 'crypto'

    def get_object(self):
        thing = get_object_or_404(Favorite, ticker__exact=self.kwargs['ticker'])
        return thing
