from django.db import models

# Create your models here.

class Estudiante(models.Model):
    ApellidoPaterno = models.CharField(max_length=30)
    ApellidoMaterno = models.CharField(max_length=30)
    Nombres = models.CharField(max_length=30)
    DNI = models.CharField(max_length=6)
    FechaNacimiento = models.DateField()
    SEX = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo= models.CharField(max_length=1, choices=SEX, default='M')


    def NombreCompleto(self):
        cadena="{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Materia(models.Model):
    Nombre = models.CharField(max_length=40)
    Creditos = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    def __str__(self):
        return "{0} ({1})".format(self.Nombre, self.Creditos)

class Matricula(models.Model):
    Estudiante=models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    Materia=models.ForeignKey(Materia, null=False, blank=False, on_delete=models.CASCADE)
    FechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Estudiante, self.Materia.Nombre)
