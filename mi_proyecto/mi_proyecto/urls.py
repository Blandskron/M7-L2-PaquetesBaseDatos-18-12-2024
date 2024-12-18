"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi_app.views import lista_usuarios, productos_en_stock
#from mi_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('productos/', productos_en_stock, name='productos_en_stock'),
    """
    path('users/', views.list_users, name='list_users'),
    path('products/', views.products_in_stock, name='products_in_stock'),
    """
]
