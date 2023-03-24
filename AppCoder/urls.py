from django.urls import path, include
from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path ('', views.inicio, name ="Inicio"),
    path ('altaproducto', views.productos, name ="altaProducto"),
    path ('altaproveedor', views.proveedores, name ="altaProveedor"),
    path ('altacliente', views.clientes, name ="altaCliente"),
   
    path ('productos', views.leerProductos, name ="Productos"),
    path ('proveedores', views.leerProveedores, name ="Proveedores"),
    path ('clientes', views.leerClientes, name ="Clientes"),

    path ('leerProductos', views.leerProductos, name="LeerProductos"),
    path ('leerProveedor', views.leerProveedores, name="LeerProveedor"),
    path ('leerCliente', views.leerClientes, name="LeerCliente"),

    #path ('clientes', views.clientes, name ="Clientes"),
    #path ('proveedores', views.proveedores, name ="Proveedores"),
    
    path ('clienteFormulario', views.clienteFormulario, name="ClienteFormulario"),
    path ('proveedorFormulario', views.proveedorFormulario, name="ProveedorFormulario"),


    path ('busquedaProducto', views.busquedaProducto, name="BusquedaProducto"),
    path ('buscar/', views.buscar),
    path ('login', views.login_request, name = "Login"),
    path ('register', views.register, name = "Registro"),
    path ('logout', LogoutView.as_view(template_name = 'logout.html'), name = "Logout"),
    
    path ('eliminarProducto/<producto_nombre>/', views.eliminarProducto, name="EliminarProducto"),
    path ('eliminarProveedor/<proveedor_nombre>/', views.eliminarProveedor, name="EliminarProveedor"),
    path ('eliminarCliente/<cliente_nombre>/', views.eliminarCliente, name="EliminarCliente"),
    

    path ('editarProducto/<producto_nombre>/', views.editarProducto, name="EditarProducto"),
    path ('editarProveedor/<proveedor_nombre>/', views.editarProveedor, name="EditarProveedor"),
    path ('editarCliente/<cliente_nombre>/', views.editarCliente, name="EditarCliente"),
    


    #ABM utilizando vistas de Django
    path ('cliente/List', views.ClienteList.as_view(), name = "List"),
    path ('<int:pk>', views.ClienteDetalle.as_view(), name = "Details"),
    path ('nuevo', views.ClienteCreacion.as_view(), name = "New"),
    path ('editar/<int:pk>', views.ClienteUdpdate.as_view(), name = "Edit"),
    path ('borrar/<int:pk>', views.ClienteDelete.as_view(), name = "delete"),

    path ('editarPerfil', views.editarPerfil, name = 'EditarPerfil'),

    path ('agregarAvatar', views.agregarAvatar, name = 'AgregarAvatar'),

    path ('acerca', views.acerca, name="Acerca"),

    path ('construccion', views.construccion, name="Construccion")

]