from django.urls import path
from . import views

urlpatterns = [
    path('add_perro', views.PerroCreate.as_view(), name="add_perro"),

    path('list_perros/', views.PerroList.as_view(), name='list_perros'),

    path('edit_perro/<int:pk>', views.PerroUpdate.as_view(), name='edit_perro'),

    path('del_perro/<int:pk>', views.PerroDelete.as_view(), name='del_perro'),
    
     # api
    path('perros/',  views.perro_collection , name='perro_collection'),
    path('perros/<int:pk>/', views.perro_element ,name='perro_element')
]