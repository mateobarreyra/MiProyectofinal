import datetime

from django.contrib.auth.models import User
from django.db import models
import datetime


class Receta(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_de_creacion = models.DateTimeField(default=datetime.datetime.now())
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="recetas")

    def __str__(self):
        return f'Receta{self.titulo}- Autor {self.autor}'

class Comentario(models.Model):
    comentario = models.ForeignKey(Receta, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)