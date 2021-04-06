from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('curso/<slug:slug>', views.curso_detalhes, name='curso_detalhes'),
    path('categoria/<slug:slug>', views.lista_cursos_categoria, name='categoria'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),

]