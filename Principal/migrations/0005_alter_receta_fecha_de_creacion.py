# Generated by Django 4.2.8 on 2023-12-11 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0004_remove_receta_autor_alter_receta_fecha_de_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='fecha_de_creacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 19, 21, 44, 203577)),
        ),
    ]
