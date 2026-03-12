from django.contrib import admin
from .models import Categoria, Producto, Marca, Almacen, Inventario

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Almacen)
admin.site.register(Inventario)