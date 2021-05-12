from django.db import models

# Create your models here.
class Categoria(models.Model):
    tipoCategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.tipoCategoria

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='imgJugador', null = True , blank = True)
 
    def __str__(self):
        return self.nombre     

class Equipo(models.Model):
    nombreEquipo = models.CharField(max_length=100)
    Escudo = models.ImageField(upload_to = 'imgEquipo',null=True,blank=True)

    def __str__(self):
        return self.nombreEquipo               

class Video(models.Model):
    nombreVideo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    videoArchivo = models.FileField(upload_to='videos', null = True, blank = True)
    fechaPublicacion = models.DateTimeField(auto_now=True)
    Jugador = models.ForeignKey(Jugador,models.PROTECT)
    Equipo = models.ForeignKey(Equipo,models.PROTECT)
    categoria = models.ManyToManyField(Categoria, null = True, blank = True)

    def __str__(self):
        return self.nombreVideo  