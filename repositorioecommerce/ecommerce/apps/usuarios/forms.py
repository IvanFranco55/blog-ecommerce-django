from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormularioRegistroUsuario(UserCreationForm):
<<<<<<< HEAD

	class Meta:
		model = User
		fields = ['username','first_name','last_name', 'email', 'password1','password2']
=======
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
>>>>>>> 5c29aac8efeb3f283a275fa6a57f752884bd4018
