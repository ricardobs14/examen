from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, "Stock/listar_producto.html", {'productos': productos})
    
def agregar_productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_productos")
    else:
        form = ProductoForm()
        return render(request, "Stock/agregar_productos.html", {'form': form})
 
def borrar_producto(request, perro_id):
    instancia = Producto.objects.get(id=perro_id)
    instancia.delete()
    return redirect('listar_productos')

def editar_producto(request, producto_id):
    instancia = Producto.objects.get(id=producto_id)
    form = ProductoForm(instance=instancia)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "Stock/editar_producto.html", {'form': form})



class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Stock/producto_form.html'
    success_url = reverse_lazy("add_producto")

class ProductoList(ListView):
    model = Producto
    template_name = 'Stock/list_productos.html'


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Stock/producto_form.html'
    success_url = reverse_lazy('list_producto')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Stock/producto_delete.html'
    success_url = reverse_lazy('list_producto')


# El decorador @api_view verifica que la solicitud HTTP apropiada 
# se pase a la función de vista. En este momento, solo admitimos solicitudes GET
@api_view(['GET', 'PUT', 'DELETE'])
def producto_element(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT': 
        producto_new = JSONParser().parse(request) 
        serializer = ProductoSerializer(producto, data=producto_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'POST'])
def producto_collection(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
