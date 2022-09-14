from django.conf.urls import url
from app.libros.views import index, listarEditores, listarLibros, crearEditores, updateEditor, deleteEditor, crearLibros, updateLibros, deleteLibros, listarAutores, crearAutor,\
updateAutor, deleteAutor, listarEditorC, crearEditorC, updateEditorC, deleteEditorC, listarLibrosC, createLibrosC, updateLibrosC, deleteLibrosC, listarAutoresC, \
createAutoresC, updateAutoresC, deleteAutoresC

urlpatterns = [
    url(r'^$', index, name='Inicio'),
    #EDITOR
    url(r'^libros/listar_editores_F$', listarEditores, name='listar_editores_F'),
    url(r'^libros/listar_libros_F$', listarLibros, name='listar_libros_F'),
    url(r'^libros/crear_editor_F$', crearEditores, name='crear_editor_F'),
    url(r'^libros/editar_editor_F/(?P<id_editor>\d+)/$', updateEditor, name='editar_editor_F'),
    url(r'^libros/eliminar_editor_F/(?P<id_editor>\d+)/$', deleteEditor, name='eliminar_editor_F'),
    #LIBRO
    url(r'^libros/crear_libro_F/$', crearLibros, name='crear_libro_F'),
    url(r'^libros/editar_libro_F/(?P<id_libro>\d+)/$', updateLibros, name='editar_libro_F'),
    url(r'^libros/eliminar_libro_F/(?P<id_libro>\d+)/$', deleteLibros, name='eliminar_libro_F'),
    #AUTOR
    url(r'^libros/listar_autores_F$', listarAutores, name='listar_autores_F'),
    url(r'^libros/crear_autores_F$', crearAutor, name='crear_autores_F'),
    url(r'^libros/editar_autores_F/(?P<id_autor>\d+)/$', updateAutor, name='editar_autores_F'),
    url(r'^libros/eliminar_autores_F/(?P<id_autor>\d+)/$', deleteAutor, name='eliminar_autores_F'),
    #EDITOR CLASES
    url(r'^libros/listar_editores_C$', listarEditorC.as_view(), name='listar_editores_C'),
    url(r'^libros/crear_editor_C/$', crearEditorC.as_view(), name='crear_editor_C'),
    url(r'^libros/editar_editor_C/(?P<pk>\d+)/$', updateEditorC.as_view(), name='editar_editor_C'),
    url(r'^libros/eliminar_editor_C/(?P<pk>\d+)/$', deleteEditorC.as_view(), name='eliminar_editor_C'),
    #LIRBO CLASES
    url(r'^libros/listar_libros_C$', listarLibrosC.as_view(), name='listar_libros_C'),
    url(r'^libros/crear_libros_C$', createLibrosC.as_view(), name='crear_libros_C'),
    url(r'^libros/editar_libros_C/(?P<pk>\d+)/$', updateLibrosC.as_view(), name='editar_libros_C'),
    url(r'^libros/eliminar_libros_C/(?P<pk>\d+)/$', deleteLibrosC.as_view(), name='eliminar_libros_C'),
    #AUTOR CLASES
    url(r'^libros/listar_autores_C$', listarAutoresC.as_view(), name='listar_autores_C'),
    url(r'^libros/crear_autores_C$', createAutoresC.as_view(), name='crear_autores_C'),
    url(r'^libros/editar_autores_C/(?P<pk>\d+)/$', updateAutoresC.as_view(), name='editar_autores_C'),
    url(r'^libros/eliminar_autores_C/(?P<pk>\d+)/$', deleteAutoresC.as_view(), name='eliminar_autores_C'),
]