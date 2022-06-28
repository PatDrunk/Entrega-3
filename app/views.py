import requests
from django.shortcuts import *
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *

# Create your views here.

def home(request):
    return render(request,'app/index.html')

def base(request):
    return render(request,'app/base.html')

def index(request):
    return render(request,'app/index.html')

def login(request):
    form = AuthenticationForm()
    return render(request,'app/registration/login.html',{"form":form})

def logout(request):
    return render(request, 'app/registration/logged_out.html')

def registro(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario Registrado correctamente!')
        datos["form"] = formulario
    return render(request, 'app/registration/registro.html', datos)


def index_login(request):
    return render(request,'app/index_login.html')


def seguimiento(request):
    return render(request, 'app/seguimiento.html')


def historial(request):
    return render(request, 'app/historial.html')

def apiex(request):
    response = requests.get('https://digimon-api.herokuapp.com/api/digimon').json()
    datos ={
        'listaDigimon' : response,
    }
    return render(request, 'app/productos/api_ex.html',datos)


def productos(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()

    productosAll = Producto.objects.all()
    datos ={
         'listaProductos' : productosAll,
         'listaJson' : response
    }
    
    if request.method == 'POST':
        carrito = Carrito()
        carrito.nombre = request.POST.get('nombre')
        carrito.precio = request.POST.get('precio')
        carrito.imagen = request.POST.get('imagen')
        carrito.save()
    
    return render(request, 'app/productos/productos.html',datos)



def listarProductos(request):
    productosAll = Producto.objects.all()
    datos ={ 'listaProductos' : productosAll}

    return render(request, 'app/productos/listarProductos.html',datos)

def agregarProductos(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
    return render(request, 'app/productos/agregarProductos.html',datos)


def modificarProductos(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto guardado correctamente!')
            datos['form'] = formulario
            
    return render(request, 'app/productos/modificarProductos.html',datos)


def eliminarProductos(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect(to="listarProductos")


def listarClientes(request):
    clientesAll = Cliente.objects.all()
    datos ={
        'listaClientes' : clientesAll
    }
    return render(request, 'app/clientes/listarClientes.html',datos)


def agregarClientes(request):
    datos = {
        'formc' : ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Cliente guardado correctamente!'

    return render(request, 'app/clientes/agregarClientes.html',datos)


def modificarClientes(request,codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    datos = {
        'formc' : ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Cliente modificado correctamente"
            datos['formc'] = formulario
            
    return render(request, 'app/clientes/modificarClientes.html',datos)

def eliminarClientes(request,codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()

    return redirect(to="listarClientes")


def carritoCompras(request):
    carrito = Carrito.objects.all()
    datos = { 'listaCarrito' : carrito}

    return render(request, 'app/productos/carritoCompras.html',datos)

def compraExitosa(request):
    carrito = Carrito.objects.all()
    carrito.delete()

    return render(request, 'app/productos/compraExitosa.html')
