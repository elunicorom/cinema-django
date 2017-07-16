from django import forms
from models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario

        fields = [
            'nombre',
            'apellido',
            'username',
            'password',
            'dni',
            'email',
            'tipo_usuario',
            'sexo',
        ]

        labels={
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'username': 'Nombre de usuario',
            'password': 'Password',
            'dni':'DNI',
            'email':'Correo Electronico',
            'sexo':'Sexo',
            'tipo_usuario':'Tipo de Usuario',
        }

        widgets = {

            'nombre':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Nombre','name':'nombre',}),
            'apellido':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Apellido','name':'nombre',}),
            'username':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Username','name':'nombre',}),
            'password':forms.TextInput(attrs={'class':'w3-input w3-border','type':'password','placeholder':'Password','name':'nombre',}),
            'dni':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Dni','name':'nombre',}),
            'email':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Email','name':'nombre',}),
            'tipo_usuario':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Tipo Usuario','name':'nombre',}),
            'sexo':forms.TextInput(attrs={'class':'w3-input w3-border','type':'text','placeholder':'Sexo','name':'nombre',}),
        }
