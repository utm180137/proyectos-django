# Generated by Django 3.2.5 on 2021-08-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_alter_cursos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='lecciones',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cursos',
            name='lenguaje',
            field=models.TextField(null=True, verbose_name='Idioma'),
        ),
        migrations.AddField(
            model_name='cursos',
            name='precio',
            field=models.DecimalField(decimal_places=0, max_digits=6, null=True, verbose_name='Costo'),
        ),
    ]
