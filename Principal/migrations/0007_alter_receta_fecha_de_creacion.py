# Generated by Django 4.2.8 on 2023-12-15 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Principal', '0006_alter_receta_fecha_de_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='fecha_de_creacion',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 15, 12, 12, 21, 490806)),
        ),
    ]
