
from django.urls import path

from Principal.views import show_html, CrearReceta, RecetasList, DetalleReceta, RecetaEliminar, ActualizarReceta, \
    ComentarioPagina

urlpatterns = [
    path('show/', show_html, name="base"),
    path('crear', CrearReceta.as_view(), name="RecetaCreate"),
    path('recetas', RecetasList.as_view(), name="RecetasList"),
    path('receta/<int:pk>', DetalleReceta.as_view(), name="RecetaDetail"),
    path('eliminar/<int:pk>', RecetaEliminar.as_view(), name="RecetaEliminar"),
    path('actualizar/<int:pk>', ActualizarReceta.as_view(), name="RecetaUpdate"),
    path('receta/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),


    ]