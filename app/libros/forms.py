from django import forms
from app.libros.models import Libros, Autor, Editor

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = [
            'nombre',
            'domicilio',
            'ciudad',
            'estado',
            'pais',
            'website',
        ]

        labels = {
            'nombre':'Nombre',
            'domicilio':'Domicilio',
            'ciudad':'Ciudad',
            'estado':'Estado',
            'pais':'Pais',
            'website':'Website'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LibrosForm(forms.ModelForm):
    class Meta:
        model = Libros
        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada',
        ]

        labels = {
            'titulo':'Titulo',
            'autores':'Autores',
            'editor':'Editor',
            'fecha_publicacion':'Fecha de publicacion',
            'portada':'Portada',
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autores': forms.Select(attrs={'class': 'form-control'}),
            'editor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control'}),
            #'portada': forms.ImageField(),
        }

class AutoresForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre',
            'apellidos',
            'email'
        ]

        labels = {
            'nombre':'Nombre(s)',
            'apellidos':'Apellido(s)',
            'email':'Correo electronico',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
        }