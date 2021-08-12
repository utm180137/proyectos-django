from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
from ckeditor.fields import RichTextField 

# Create your models here.
class Profesores(models.Model):#Define la estructura de la tabla
    id = models.AutoField(primary_key=True, verbose_name='Clave Cursos')
    nombre = models.TextField()  
    apellidos = models.TextField()
    materia = models.TextField()
    edad = models.IntegerField()
    email = models.EmailField()  #campo de email
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registro") 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["-created"]
        #el menos indica que se ordena del mas reciente al mas viejo
    def __str__(self):
        return self.nombre
        #indica el nombre del alumno, no el objeto

class Cursos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    titulo = models.TextField(verbose_name="Nombre Curso")    
    categoria = models.CharField(max_length=50)
    duracion = models.DurationField(verbose_name="Duracion en Horas")
    lenguaje = models.CharField(null=True, max_length=25)
    profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE,verbose_name='Profesor')
    descripcion = RichTextField(null=True)
    lecciones =  RichTextField(null=True)
    precio = models.DecimalField(null=True, max_digits=6, decimal_places=0,verbose_name="Costo")
    imagen = models.ImageField(null=True,upload_to="media",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Registro")
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["-created"]
        #el menos indica que se ordena del mas reciente al mas viejo
    def __str__(self):
        return self.titulo
        #indica el nombre del alumno, no el objeto

class Usuario(models.Model):#Define la estructura de la tabla
    nombre = models.TextField()  
    apellidos = models.TextField()
    edad = models.IntegerField()
    email = models.EmailField()  #campo de email
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE,verbose_name='Curso')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registro") 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created"]
        #el menos indica que se ordena del mas reciente al mas viejo
    def __str__(self):
        return self.nombre
        #indica el nombre del alumno, no el objeto



