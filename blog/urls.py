from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='blog'),
    path('buscar/', views.buscar, name='buscar'),
    path('home/', views.home, name='home'),
    path('nova_publicacao/', views.nova_publicacao, name='nova_publicacao'),
    path('info_materia/<int:id>/', views.info_materia, name='info_materia'),
    path('get_comentario/<int:id>/', views.get_comentario, name='get_comentario'),
    path('criar_comentario/<int:id>/', views.criar_comentario, name='criar_comentario'),
    path('lista_favoritos/<int:id>/', views.lista_favoritos, name='lista_favoritos'),
    path('exibir_favoritos/<int:id>/', views.exibir_favoritos, name='exibir_favoritos'),
]