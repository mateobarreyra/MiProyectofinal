import datetime

from django.db import models
import datetime


class Receta(models.Model):
    autor = models.CharField(max_length=25)
    fecha_de_creacion = models.DateTimeField(default=datetime.datetime.now())
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="recetas")

    def __str__(self):
        return f'Receta{self.titulo}- Autor {self.autor}'
