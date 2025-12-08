from django .shortcuts import render 
from .models import Articulo, Categoria
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # Para que solo entren logueados
from django.urls import reverse_lazy
from .forms import FormularioCrearArticulo, FormularioModificarArticulo

def Listar_articulos(request):
    #ORM

    todos_articulos = Articulo.objects.all()

    context = {}
    context['articulos'] = todos_articulos

    categorias = Categoria.objects.all()
    context['categorias'] = categorias

    return render(request, 'blog/listar.html', context)

class Detalle_Articulo_Clase(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'

class Crear_Articulo(CreateView):
    model = Articulo
    template_name = 'blog/crear.html'
    form_class = FormularioCrearArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

    def form_valid(self, form):
            form.instance.autor = self.request.user
            return super().form_valid(form)
            #esto es para que cuando querramos subir un articulo no pida el campo autor y asigne automaticamente al ususario

class Modificar_Articulo(UpdateView):
    model = Articulo
    template_name = 'blog/modificar.html'
    form_class = FormularioModificarArticulo
    success_url = reverse_lazy('blog:path_listar_articulos')

class Eliminar_Articulo(DeleteView):
     model = Articulo
     template_name = 'blog/eliminar.html'
     success_url = reverse_lazy('blog:path_listar_articulos')

def Filtro_Categoria(request, pk):
    ca = Categoria.objects.get(pk = pk)

    ar = Articulo.objects.filter(categoria = ca)
    context = {}
    context['articulos'] = ar
    categorias = Categoria.objects.all()
    context['categorias'] = categorias

    return render(request, 'blog/listar.html', context)
    