from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(verbose_name='Usuario', max_length=20)
    password = models.IntegerField(verbose_name='Contraseña')

    def __str__(self) :
        return f'Usuario: {self.username} || contraseña : {self.password}'

class Libro(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    nombre = models.CharField(verbose_name='Titulo', max_length=100)
    descripcion = models.CharField(verbose_name='Autor', max_length=100)
    editorial = models.CharField(verbose_name='Editorial', max_length=100)
    paginas = models.CharField(verbose_name='Pagina del Libro', max_length=100)
    anio_publicacion = models.IntegerField()

class Genero(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    nombre = models.CharField(verbose_name='Genero', max_length=100)
    
class Prestamo(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    fecha_prestamo = models.DateField( auto_created=True)
    fecha_devolucion = models.DateField( auto_created=True)

    
class Detalle_Libro (models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    id_prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)