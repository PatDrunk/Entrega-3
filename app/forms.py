from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#creamos un template
class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

class RegistroUsuarioForm(UserCreationForm):

        class Meta:
                model = User
                fields = ['username','first_name','last_name','email','password1','password2']

