# Generated by Django 4.1.7 on 2023-03-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='anio_publicacion',
            field=models.IntegerField(),
        ),
    ]
