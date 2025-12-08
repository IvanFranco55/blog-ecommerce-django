from django.shortcuts import render
from .models import Articulo, Categoria
from django.views.generic import DetailView

#PERMISOS
#1) PRIMERO SEGURAR QUE EL USUARIO ESTA LOGUEADO. (SEPARO USUARIO VISITANTE Y REGISTRADO)

#DEPENDE SI LA VISTA ES VBF O VBC
#VBF
from django.contrib.auth.decorators import login_required
#@login_required

#VBC
from django.contrib.auth.mixins import LoginRequiredMixin
# class Detalle_Producto_Clase(LoginRequiredMixin, DetailView):


#2) una vez que el usuario se logueo,verificar permisos mas especificos

#VBF
from django.contrib.admin.views.decorators import staff_member_required
#@staff_member_required

#VBC
from django.contrib.auth.mixins import UserPassesTextMixin
# class Crear_Proudcot(UserPassesTestMixin, CreateView)


#Categoria
def Filtro_categoria(request,pk):
    ctg = Categoria.objects.get(pk= pk)
    art= Articulo.objects.filter(Categoria= ctg)
    context = {}
    context['blog'] = art
    return render(request,'blog/categoria.html', context)

def Listar_articulos(request):
    #ORM

    todos_articulos = Articulo.objects.all()

    context = {}
    context['articulos'] = todos_articulos

    return render(request, 'blog/listar.html', context)

class Detalle_Articulo_Clase(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'

