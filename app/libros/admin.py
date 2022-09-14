from django.contrib import admin
from app.libros.models import Libros, Autor, Editor
# Register your models here.

admin.site.register(Libros)
admin.site.register(Autor)
admin.site.register(Editor)