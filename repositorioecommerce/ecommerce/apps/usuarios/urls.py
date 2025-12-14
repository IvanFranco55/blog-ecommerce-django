from django.urls import path
from . import views
from django.contrib.auth import views as auth
app_name = 'usuarios'

urlpatterns = [

    path('login/', auth.LoginView.as_view(template_name = 'usuarios/login.html'), name = 'path_login'),
    
    path('logout/', auth.LogoutView.as_view(), name = 'path_logout'),

    path('registro/', views.RegistroUsuario.as_view(), name = 'path_registro'),

    path('perfil/', views.VerPerfil, name='path_ver_perfil'),

    path('perfil/editar/', views.EditarPerfil, name='path_editar_perfil'),

]
     