from django.urls import path

from . import views

app_name = 'prices'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:ticker>/', views.DetailView.as_view(), name="get_single_crypto"),
]
