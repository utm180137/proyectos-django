# Generated by Django 3.2.5 on 2021-08-11 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0003_auto_20210811_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='lenguaje',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
