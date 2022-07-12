from django.urls import path
from . import views

urlpatterns = [
    path('add_producto', views.ProductoCreate.as_view(), name="add_producto"),

    path('list_producto/', views.ProductoList.as_view(), name='list_producto'),

    path('edit_producto/<int:pk>', views.ProductoUpdate.as_view(), name='edit_producto'),

    path('del_producto/<int:pk>', views.ProductoDelete.as_view(), name='del_producto'),
    
     # api
    path('productos/',  views.producto_collection , name='producto_collection'),
    path('productos/<int:pk>/', views.producto_element ,name='producto_element')
]
