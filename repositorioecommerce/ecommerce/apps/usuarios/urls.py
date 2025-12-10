from django.urls import path
from . import views
from django.contrib.auth import views as auth
<<<<<<< HEAD

app_name = 'usuarios'

urlpatterns = [
    #path login y del logout
   path('login/', auth.LoginView.as_view(template_name = 'usuarios/login.html'), name = 'path_login'),
   path('logout/', auth.LogoutView.as_view(), name = 'path_logout'),

   path('registro/', views.RegistroUsuario.as_view(), name="path_registro"),
]
=======
app_name = 'usuarios'

urlpatterns = [

    path('login/', auth.LoginView.as_view(template_name = 'usuarios/login.html'), name = 'path_login'),
    
    path('logout/', auth.LogoutView.as_view(), name = 'path_logout'),

    path('registro/', views.RegistroUsuario.as_view(), name = 'path_registro')

]
     
>>>>>>> 5c29aac8efeb3f283a275fa6a57f752884bd4018
