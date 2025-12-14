from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class FormularioRegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# Formulario para editar datos personales (User)
class FormularioEditarPerfil(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        help_texts = {k: "" for k in fields} # Quita textos de ayuda molestos

# Formulario para editar la imagen (Perfil)
class FormularioEditarAvatar(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['imagen']