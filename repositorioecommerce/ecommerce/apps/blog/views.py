from django .shortcuts import render 
from .models import Articulo, Categoria
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin # Para que solo entren logueados
from django.urls import reverse_lazy
from .forms import FormularioCrearArticulo

def Listar_articulos(request):
    #ORM

    todos_articulos = Articulo.objects.all()

    context = {}
    context['articulos'] = todos_articulos

    return render(request, 'blog/listar.html', context)

class Detalle_Articulo_Clase(DetailView):
    model = Articulo
    template_name = 'blog/detalle.html'

class Crear_Articulo(CreateView):
    model = Articulo
    template_name = 'blog/crear.html'
    form_class = FormularioCrearArticulo
    succes_url = reverse_lazy('blog: path_listar.html')

    def form_valid(self, form):
            form.instance.autor = self.request.user
            return super().form_valid(form)