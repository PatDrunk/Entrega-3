from pyexpat import model
from django.db import models
from requests import session

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tipo
    
    class Meta():
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= "productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} -> {self.precio} '

class TipoCliente(models.Model):
    tipo = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tipo

    class Meta():
        db_table = 'db_tipo_cliente'

class Cliente(models.Model):
    codigo = models.IntegerField(null=False,primary_key=True)
    nombre = models.CharField(max_length=90)
    numero_telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)
    pais = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to= "clientes", null=True)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre


class Carrito(models.Model):
    nombre = models.CharField(max_length=90,)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to= "carrito", null=False)

    def __str__(self):
        return self.nombre

    class Meta():
        db_table = 'db_carrito'

class seguimiento(models.Model):
        codigo = models.IntegerField()




#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser