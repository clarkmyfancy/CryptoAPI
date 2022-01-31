from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # /prices/btc
    path('<str:name>/', views.single, name="get_single_crypto"),
]
