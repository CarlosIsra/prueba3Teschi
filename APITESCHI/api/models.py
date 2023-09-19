from django.db import models

# Create your models here.


#creacion de la BD. 

class alumno(models.Model):
    idAlumno = models.IntegerField(primary_key=True,db_column='idAlumno')
    
    
    class Producto(models.Model):
        nombre = models.CharField(max_length=50)
        precio = models.IntegerField()
        descripcion = models.TextField()d
        nuevo = models.ForeignKey(Marca, on_delete=models.PROTECT)
        fecha_fabricacion = models.DateField()
        
        