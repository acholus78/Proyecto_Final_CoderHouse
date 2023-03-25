from django.shortcuts import render
from AppCoder.models import Producto, Cliente, Proveedor, Avatar
from django.http import HttpResponse
from AppCoder.forms import ProductoFormulario, ClienteFormulario, ProveedorFormulario, AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from AppCoder.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User



# Create your views here. Prueba de actualización

#class ClaseQueNecesitaLogin (LoginRequiredMixin):


def acerca (request):
    return render(request, 'acerca.html')

def construccion (request):
    return render(request, 'construccion.html')

@login_required
def inicio (request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'inicio.html', {'url':  avatares[0].imagen.url})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm (request, data = request.POST)
        if form.is_valid ():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get ('password')

            user = authenticate (username = usuario, password = contras)
            if user is not None:
                login (request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                contexto = {"url":avatares[0].imagen.url}
                return render (request, "inicio.html", contexto)
            else:
                return render (request, 'inicio.html', {"mensaje":"Error, datos incorrectos."})
        else:
            return render (request, 'inicio.html', {"mensaje":"Error, formulario erroneo."})

    form = AuthenticationForm()
    return render (request, 'login.html', {"form":form})


def register (request):
    if request.method == 'POST':
        #form = UserCreationForm (request.POST)
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            username = form.cleaned_data ['username']
            form.save()
            return render (request, 'inicio.html', {'mensaje': 'Usuario creado. '})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm ()
    return render (request, 'registro.html', {'form': form} )     






#def inicio (request):
    #return HttpResponse ("Vista Inicio")
#    return render (request, 'inicio.html')

@login_required
def productos (request):
    
    if request.method == 'POST':
        
        miFormulario = ProductoFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto=Producto(nombre=informacion['nombre'],anio_fabricacion=informacion['anio_fabricacion'],descripcion=informacion['descripcion'],precio=informacion['precio'])
            producto.save()
            avatares = Avatar.objects.filter(user=request.user.id)
            productos = Producto.objects.all()
            contexto = {"productos":productos, "url":avatares[0].imagen.url}
            return render(request, 'leerProductos.html', contexto)
    else:
        miFormulario = ProductoFormulario()

    miFormulario = ProductoFormulario()
    return render(request, 'Productos.html', {'miFormulario': miFormulario})

@login_required
def clientes (request):
    if request.method == 'POST':
        
        miFormulario = ClienteFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente=Cliente(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],direccion=informacion['direccion'] )
            cliente.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ClienteFormulario()

    miFormulario = ClienteFormulario()
    return render(request, 'clientes.html', {'miFormulario': miFormulario})

@login_required
def clienteFormulario (request):
    if request.method == 'POST':
        
        miFormulario = ClienteFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente=Cliente(nombre=informacion['nombre'],
                            apellido=informacion['apellido'],
                            email=informacion['email'],
                            direccion=informacion['direccion'])
            cliente.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ClienteFormulario()

    miFormulario = ClienteFormulario()
    return render(request, 'clienteFormulario.html', {'miFormulario': miFormulario})


@login_required
def proveedores (request):
    if request.method == 'POST':
        
        miFormulario = ProveedorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            proveedor=Proveedor(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            proveedor.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ProveedorFormulario()

    miFormulario = ProveedorFormulario()
    return render(request, 'proveedores.html', {'miFormulario': miFormulario})

@login_required
def proveedorFormulario (request):
    if request.method == 'POST':
        
        miFormulario = ProveedorFormulario(request.POST)

        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            proveedor = Proveedor(nombre=informacion['nombre'],
                                  apellido=informacion['apellido'],
                                  email=informacion['email'])
            proveedor.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = ProveedorFormulario()

    miFormulario = ProveedorFormulario()
    return render(request, 'proveedorFormulario.html', {'miFormulario': miFormulario})


@login_required
def busquedaProducto(request):
    return render (request, 'busquedaProducto.html')

@login_required
def buscar (request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        producto = Producto.objects.filter(nombre__icontains=nombre)
        precio = Producto.objects.filter(nombre__icontains=nombre)

        #return render(request, 'inicio.html', {"productos":producto, "nombre":nombre})
        return render(request, 'inicio.html', {"productos":producto, "nombre":nombre, "precio":precio}) 
    else:
        respuesta = "No enviaste datos."
        
    #return HttpResponse (respuesta)
    return render (request, 'inicio.html', {"respuesta":respuesta})

@login_required
def leerProductos (request):
    productos = Producto.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    contexto = {"productos":productos, "url":avatares[0].imagen.url}
    return render(request, "LeerProductos.html", contexto)


@login_required
def eliminarProducto (request, producto_nombre):
    producto = Producto.objects.get (nombre=producto_nombre)
    producto.delete()

    productos = Producto.objects.all()
    contexto = {"productos":productos}
    return render (request, "leerProductos.html", contexto)

@login_required
def editarProducto (request, producto_nombre):
    producto = Producto.objects.get(nombre=producto_nombre)
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            producto.nombre = informacion ['nombre']
            producto.anio_fabricacion = informacion ['anio_fabricacion']
            producto.descripcion = informacion ['descripcion']
            producto.precio = informacion ['precio']

            producto.save()
            #return render(request, "inicio.html")
            contexto = {"productos":Producto.objects.all()}
            return render(request, "leerProductos.html", contexto )
    else:
        miFormulario = ProductoFormulario(initial={'nombre': producto.nombre, 
                                                   'anio_fabricacion': producto.anio_fabricacion, 
                                                   'descripcion': producto.descripcion, 
                                                   'precio': producto.precio})
        return render(request, "editarProducto.html", {"miFormulario": miFormulario, "producto_nombre": producto_nombre})


class ClienteList (ListView):
    model = Cliente
    template_name = "cliente_list.html"

class ClienteDetalle (DetailView):
    model = Cliente
    template_name = "cliente_detalle.html"

class ClienteCreacion (CreateView):
    model = Cliente
    template_name = "clientes_form.html"
    success_url = reverse_lazy ("AppCoder:List")
    fields = ['nombre','apellido', 'email', 'direccion']

class ClienteUdpdate (UpdateView):
    model = Cliente
    success_url = "AppCoder/cliente/List"
    template_name = "clientes_form.html"
    fields = ['nombre','apellido', 'email', 'direccion']


class ClienteDelete (DeleteView):
    model = Cliente
    template_name = "cliente_confirm_delete.html"
    success_url = "AppCoder/cliente/List"


@login_required
def leerProveedores (request):
    avatares = Avatar.objects.filter(user=request.user.id)
    proveedores = Proveedor.objects.all()
    contexto = {"proveedores":proveedores, "url":avatares[0].imagen.url}
    return render(request, "leerProveedores.html", contexto)


@login_required
def eliminarProveedor (request, proveedor_nombre):
    proveedor = Proveedor.objects.get(nombre=proveedor_nombre)
    proveedor.delete()

    proveedores = Proveedor.objects.all()
    contexto = {"proveedores":proveedores}
    return render (request, "leerProveedores.html", contexto)

@login_required
def editarProveedor (request, proveedor_nombre):
    proveedor = Proveedor.objects.get(nombre=proveedor_nombre)
    if request.method == 'POST':
        miFormulario = ProveedorFormulario(request.POST)
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            proveedor.nombre = informacion ['nombre']
            proveedor.apellido = informacion ['apellido']
            proveedor.email = informacion ['email']
            
            proveedor.save()
            #return render(request, "inicio.html")
            contexto = {"proveedores":Proveedor.objects.all()}
            return render(request, "leerProveedores.html", contexto)
    else:
        miFormulario = ProveedorFormulario(initial={'nombre': proveedor.nombre, 
                                                   'apellido': proveedor.apellido, 
                                                   'email': proveedor.email})
        return render(request, "editarProveedor.html", {"miFormulario": miFormulario, "proveedor_nombre": proveedor_nombre})
    




@login_required    
def leerClientes (request):
    avatares = Avatar.objects.filter(user=request.user.id)
    clientes = Cliente.objects.all()
    contexto = {"clientes":clientes, "url":avatares[0].imagen.url}
    return render(request, "leerClientes.html", contexto)


@login_required
def eliminarCliente (request, cliente_nombre):
    cliente = Cliente.objects.get(nombre=cliente_nombre)
    cliente.delete()

    clientes = Cliente.objects.all()
    contexto = {"clientes":clientes}
    return render (request, "leerClientes.html", contexto)

@login_required
def editarCliente (request, cliente_nombre):
    cliente = Cliente.objects.get(nombre=cliente_nombre)
    if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST)
        print (miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            cliente.nombre = informacion ['nombre']
            cliente.apellido = informacion ['apellido']
            cliente.email = informacion ['email']
            cliente.direccion = informacion ['direccion']
            
            cliente.save()
            #return render(request, "inicio.html")
            contexto = {"clientes":Cliente.objects.all()}
            return render(request, "leerClientes.html", contexto)
    else:
        miFormulario = ClienteFormulario(initial={'nombre': cliente.nombre, 
                                                   'apellido': cliente.apellido, 
                                                   'email': cliente.email,
                                                   'direccion': cliente.direccion})
        return render(request, "editarCliente.html", {"miFormulario": miFormulario, "cliente_nombre": cliente_nombre})
    

@login_required
def editarPerfil(request):
    usuario = request.user 
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            print(miFormulario)
            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {'mensaje':'Contraseña incorrecta.'})

            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})


@login_required
def agregarAvatar(request):
      avatares = Avatar.objects.filter(user=request.user.id)
      if request.method == 'POST':
            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  u = User.objects.get(username=request.user)
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
                  avatar.save()
                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran
      else: 
            miFormulario= AvatarFormulario() #Formulario vacio para construir el html
      return render(request, "agregarAvatar.html", {"miFormulario":miFormulario, "url":avatares[0].imagen.url})

def urlImagen():
      return "/media/avatares/logo.png"