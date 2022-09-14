from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return '{}'.format(self.nombre)

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    def __unicode__(self):
        return '{} {}'.format(self.nombre, self.apellidos)

class Libros(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ForeignKey(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return '{}'.format(self.titulo)