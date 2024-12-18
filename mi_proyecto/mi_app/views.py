from django.shortcuts import render
from .models import Usuario, Producto
# Create your views here.

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def productos_en_stock(request):
    productos = Producto.objects.filter(stock__gt=0)
    return render(request, 'lista_productos.html', {'productos': productos})
