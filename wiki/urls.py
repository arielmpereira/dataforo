from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    path('', views.lista_wiki, name='lista'),
    path('<slug:slug>/', views.detalle_wiki, name='detalle'),
]

