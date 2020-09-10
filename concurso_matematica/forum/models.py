from django.db import models

# Create your models here.


class Tema(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='post')
    contenido = models.TextField()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=75)
    votos_plus = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return self.contenido


class Respuesta(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=75)
    votos_plus = models.IntegerField(default=0)
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='respuestas')

    def __str__(self):
        return self.contenido
