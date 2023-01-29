from django.db import models

# Create your models here.
class usuario(models.Model):
    nombres = models.CharField(max_length=175)
    apellidos = models.CharField(max_length=175)
    correo = models.CharField(max_length=225)
    contrasena = models.CharField(max_length=11)
    
    def __str__(self):
        return self.nombres + " - " + self.correo;

class sitio(models.Model):
    nombre_sitio = models.CharField(max_length=150)
    aforo = models.IntegerField(default=0)
    hora_entrada=models.DateTimeField(auto_now_add=True)
    hora_salida=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_sitio + " - " + self.aforo;


class visitante(models.Model):
    nomb_visitante = models.CharField(max_length=175)
    apell_visitante = models.CharField(max_length=175)
    tipo_documento = models.CharField(max_length=20)
    num_documento = models.CharField(max_length=11)
    nacionalidad = models.CharField(max_length=100)
    
    def __str__(self):
        return f'%s (%s)' % (self.nomb_visitante, self.apell_visitante, self.num_documento, self.nacionalidad)


class guia(models.Model):
    
    nomb_guia = models.CharField(max_length=175)
    apell_guia = models.CharField(max_length=175)
    num_documento = models.CharField(max_length=11)
    
    def __str__(self):
        return f'%s (%s)' % (self.nomb_guia, self.apell_guia, self.num_documento)
