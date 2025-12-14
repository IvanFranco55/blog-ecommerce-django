from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import FormularioRegistroUsuario, FormularioEditarPerfil, FormularioEditarAvatar
from django.contrib.auth.decorators import login_required # Para proteger vistas

# Tu registro existente...
class RegistroUsuario(CreateView):
    template_name = 'usuarios/registro.html'
    form_class = FormularioRegistroUsuario
    success_url = reverse_lazy('usuarios:path_login')

# --- VISTA PARA VER EL PERFIL ---
@login_required
def VerPerfil(request):
    # Simplemente renderizamos el template, el usuario ya viene en 'request.user'
    return render(request, 'usuarios/ver_perfil.html')

# --- VISTA PARA EDITAR EL PERFIL ---
@login_required
def EditarPerfil(request):
    usuario = request.user
    perfil = usuario.perfil # Accedemos a la tabla Perfil relacionada

    if request.method == 'POST':
        # Cargamos los datos que mandó el usuario
        mi_formulario = FormularioEditarPerfil(request.POST, instance=usuario)
        mi_avatar = FormularioEditarAvatar(request.POST, request.FILES, instance=perfil)

        if mi_formulario.is_valid() and mi_avatar.is_valid():
            mi_formulario.save()
            mi_avatar.save()
            return redirect('usuarios:path_ver_perfil')
    else:
        # Si es GET, mostramos los datos actuales
        mi_formulario = FormularioEditarPerfil(instance=usuario)
        mi_avatar = FormularioEditarAvatar(instance=perfil)

    context = {
        'form_usuario': mi_formulario,
        'form_imagen': mi_avatar
    }
    return render(request, 'usuarios/editar_perfil.html', context)