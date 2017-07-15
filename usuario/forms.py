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

        labels=[
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'username': 'Nombre de usuario',
            'password': 'Password',
            'dni':'DNI',
            'email':'Correo Electronico',
            'sexo':'Sexo',
            'tipo_usuario':'Tipo de Usuario',
        ]
