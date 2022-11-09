from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='blog'),
    path('buscar/', views.buscar, name='buscar'),
    path('nova_publicacao/', views.nova_publicacao, name='nova_publicacao'),
]