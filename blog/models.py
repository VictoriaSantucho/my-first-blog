from django.db import models
from django.utils import timezone  #!agregado
# Create your models here.


class Post(models.Model):
    """ Class indica que estamos definiendo un objeto,models.Model, 
    indica que es un modelo de django para que lo guarde en la base de 
    datos.author, title, etc, son las propiedades del objeto Post.
    ForeingKey: es una relacion (link) con otro modelo.
    CharField:define que va a ser un texto con un limite de caracteres.
    TextField:define un texto sin limites.
    DataTimeField:fecha y horario."""
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def publish(self):
        """definimos un metodo de la 
        clase (una funcion)"""
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        """este metodo devulve un string que es 
        el titulo del Post"""
        return self.title
