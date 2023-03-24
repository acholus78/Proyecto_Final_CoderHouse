from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    anio_fabricacion = forms.IntegerField()
    descripcion = forms.CharField(max_length=50)
    precio = forms.CharField(max_length=50)


class ProveedorFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    

class ClienteFormulario (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=30)



class UserRegisterForm (UserCreationForm):
    #email = forms.EmailField()
    #password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    #password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


    ''''
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        # Aplicar estilos CSS personalizados a los widgets de los campos
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 250px; display: inline-block; width: 30%'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 250px; display: inline-block; width: 30%'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 250px; display: inline-block; width: 30%'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'style': 'max-width: 250px; display: inline-block; width: 30%'})
    '''



class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):
    #Especificar los campos
    username = forms.ModelChoiceField (queryset = User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
        help_texts = {k:"" for k in fields}