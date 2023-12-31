from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.http import HttpResponse

from Principal.forms import FormularioComentario, BusquedaRecetaForm
from Principal.models import Receta, Comentario



def busqueda_Receta(request):
    if request.method == 'GET':
        form = BusquedaRecetaForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            recetas = Receta.objects.filter(titulo__icontains=titulo)

            contexto = {
                'titulo': recetas,
                'form': form,
            }

            return render(request, 'Principal/recetasencontradas.html', contexto)

    else:
        form = BusquedaRecetaForm()

    contexto = {
        'form': form,
    }

    return render(request, 'Principal/recetasencontradas.html', contexto)
class CrearReceta(LoginRequiredMixin, CreateView):
    model = Receta
    template_name = "Principal/crear_receta.html"
    success_url = "show"
    fields = ["titulo", "subtitulo", "cuerpo", "imagen", "fecha_de_creacion"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

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

def show_aboutme(request):
    contexto={ }
    return render(request, template_name='Principal/aboutme.html', context=contexto)



class ComentarioPagina(CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'Principal/comentario.html'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

