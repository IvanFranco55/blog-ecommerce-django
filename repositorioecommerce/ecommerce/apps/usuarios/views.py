from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FormularioRegistroUsuario
<<<<<<< HEAD

class RegistroUsuario(CreateView):
	template_name = 'usuarios/registro.html'
	form_class = FormularioRegistroUsuario
	success_url = reverse_lazy('usuarios:path_login')
=======
# Create your views here.

class RegistroUsuario(CreateView):
    template_name = 'usuarios/registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('usuarios:path_login')
>>>>>>> 5c29aac8efeb3f283a275fa6a57f752884bd4018
