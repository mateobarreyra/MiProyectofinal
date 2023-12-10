from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.http import HttpResponse

from Principal.models import Receta

class CrearReceta(CreateView):
    model = Receta
    template_name = "Principal/crear_receta.html"
    success_url = "show"
    fields = "__all__"

class DetalleReceta(DetailView):
    model = Receta
    template_name = "Principal/receta_detalle.html"


class ActualizarReceta(UpdateView):
    model = Receta
    success_url = "/main/recetas"
    template_name = "Principal/crear_receta.html"
    fields = ["titulo", "subtitulo", "cuerpo", "imagen", "fecha_de_creacion"]

class RecetasList(ListView):
    model = Receta
    template_name = "Principal/recetas.html"

class RecetaEliminar(DeleteView):
    model = Receta
    success_url = "/main/recetas"
    template_name = "Principal/eliminar_receta.html"


def show_html(request):
    contexto={}
    return render(request, template_name='base.html', context=contexto)



