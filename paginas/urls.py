from django.urls import path, include
from . import views

urlpatterns = [
    path('paginas/paginaAdopcion', views.paginaAdopcion, name='paginaAdopcion'),
    path('paginas/paginaAlimento', views.paginaAlimento, name='paginaAlimento'),
    path('paginas/paginaBandana', views.paginaBandana, name='paginaBandana'),
    path('paginas/paginaCollar', views.paginaCollar, name='paginaCollar'),
    path('paginas/paginaCorrea', views.paginaCorrea, name='paginaCorrea'),
    path('paginas/paginaIdentificaciones', views.paginaIdentificaciones, name='paginaIdentificaciones'),
    path('paginas/paginaJuguete', views.paginaJuguete, name='paginaJuguete'),
    path('paginas/paginaRopa', views.paginaRopa, name='paginaRopa'),
]
