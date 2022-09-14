from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from app.libros.models import Autor, Libros, Editor
from app.libros.forms import EditorForm, LibrosForm, AutoresForm
# Create your views here.
def index(request):
    return render(request, 'base/index.html')

#FUNCIONES
#EDITOR
def listarEditores(request):
    editores = Editor.objects.all()
    contexto = {'editores':editores}
    return render(request, 'templates/funciones/editores/listar_editoresF.html', contexto)

def crearEditores(request):
    if request.method == 'POST':
        form = EditorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_editores_F')
    else:
        form = EditorForm()
    return render(request, 'templates/funciones/editores/editor_form_F.html', {'form':form})

def updateEditor(request, id_editor):
    editores = Editor.objects.get(id=id_editor)
    if request.method == 'GET':
        form = EditorForm(instance=editores)
    else:
        form = EditorForm(request.POST, instance=editores)
        if form.is_valid():
            form.save()
        return redirect('listar_editores_F')
    return render(request, 'templates/funciones/editores/editor_form_F.html', {'form':form})

def deleteEditor(request, id_editor):
    editores = Editor.objects.get(id=id_editor)
    if request.method == 'POST':
        editores.delete()
        return redirect('listar_editores_F')
    return render(request, 'templates/funciones/editores/editores_delete_F.html', {'editores':editores})
#FIN EDITOR

#LIBROS
def listarLibros(request):
    libros = Libros.objects.all()
    return render(request, 'templates/funciones/libros/listar_libros_F.html', {'libros':libros})

def crearLibros(request):
    if request.method == 'POST':
        form = LibrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_libros_F')
    else:
        form = LibrosForm()
    return render(request, 'templates/funciones/libros/libro_form_F.html', {'form':form})

def updateLibros(request, id_libro):
    libros = Libros.objects.get(id=id_libro)
    if request.method == 'GET':
        form = LibrosForm(instance=libros)
    else:
        form = LibrosForm(request.POST, request.FILES, instance=libros)
        if form.is_valid():
            form.save()
        return redirect('listar_libros_F')
    return render(request, 'templates/funciones/libros/libro_form_F.html', {'form':form})

def deleteLibros(request, id_libro):
    libros = Libros.objects.get(id=id_libro)
    if request.method == 'POST':
        libros.delete()
        return redirect('listar_libros_F')
    return render(request, 'templates/funciones/libros/delete_libro_F.html', {'libros':libros})
#FIN LIBROS

#AUTORES
def listarAutores(request):
    autores = Autor.objects.all()
    return render(request, 'templates/funciones/autores/listar_autores_F.html', {'autores':autores})

def crearAutor(request):
    if request.method == 'POST':
        form = AutoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores_F')
    else:
        form = AutoresForm()
    return render(request, 'templates/funciones/autores/autores_form_F.html', {'form':form})

def updateAutor(request, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if request.method == 'GET':
        form = AutoresForm(instance=autor)
    else:
        form = AutoresForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
        return redirect('listar_autores_F')
    return render(request, 'templates/funciones/autores/autores_form_F.html', {'form':form})

def deleteAutor(requets, id_autor):
    autor = Autor.objects.get(id=id_autor)
    if requets.method == 'POST':
        autor.delete()
        return redirect('listar_autores_F')
    return render(requets, 'templates/funciones/autores/delete_autor_F.html', {'autor':autor})
#FIN AUTORES
#FIN FUNCIONES

#CLASES
#EDITOR
class listarEditorC(ListView):
    model = Editor
    template_name = 'templates/clases/editores/listar_editor_C.html'

class crearEditorC(CreateView):
    model = Editor
    form_class = EditorForm
    template_name = 'templates/clases/editores/editor_form_C.html'
    success_url = reverse_lazy('listar_editores_C')

class updateEditorC(UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = 'templates/clases/editores/editor_form_C.html'
    success_url = reverse_lazy('listar_editores_C')

class deleteEditorC(DeleteView):
    model = Editor
    template_name = 'templates/clases/editores/editor_delete_C.html'
    success_url = reverse_lazy('listar_editores_C')
#FIN EDITOR

#LIBROS
class listarLibrosC(ListView):
    model = Libros
    template_name = 'templates/clases/libros/listar_libros_C.html'

class createLibrosC(CreateView):
    model = Libros
    form_class = LibrosForm
    template_name = 'templates/clases/libros/libro_form_C.html'
    success_url = reverse_lazy('listar_libros_C')

class updateLibrosC(UpdateView):
    model = Libros
    form_class = LibrosForm
    template_name = 'templates/clases/libros/libro_form_C.html'
    success_url = reverse_lazy('listar_libros_C')

class deleteLibrosC(DeleteView):
    model = Libros
    template_name = 'templates/clases/libros/delete_libro_C.html'
    success_url = reverse_lazy('listar_libros_C')
#FIN LIBROS

#AUTORES
class listarAutoresC(ListView):
    model = Autor
    template_name = 'templates/clases/autores/listar_autores_C.html'

class createAutoresC(CreateView):
    model = Autor
    form_class = AutoresForm
    template_name = 'templates/clases/autores/autores_form_C.html'
    success_url = reverse_lazy('listar_autores_C')

class updateAutoresC(UpdateView):
    model = Autor
    form_class = AutoresForm
    template_name = 'templates/clases/autores/autores_form_C.html'
    success_url = reverse_lazy('listar_autores_C')

class deleteAutoresC(DeleteView):
    model = Autor
    template_name = 'templates/clases/autores/delete_autor_C.html'
    success_url = reverse_lazy('listar_autores_C')
#FIN AUTORES
#FIN CLASES