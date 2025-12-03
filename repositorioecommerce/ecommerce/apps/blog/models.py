from django.db import models

from django.contrib.auth.models import User

# Esta tabla extiende al usuario de Django para agregarle datos extra
class Perfil(models.Model):
    # Relacionamos con el usuario base de Django
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='usuarios/', default='usuarios/user_default.png', null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
# Create your models here.
