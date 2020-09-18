from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_mod = models.DateTimeField(auto_now=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    user = models.CharField(max_length=75, default='', null=True, blank=True)

    def __str__(self):
        return self.title


class Comentario(models.Model):
    contenido = models.TextField()
    fecha_pub = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    usuario = models.CharField(max_length=75)
    votos_plus = models.IntegerField(default=0)
    votos_minus = models.IntegerField(default=0)
    'Related name es el nombre que va a recibir la relacion en el otro modelo'
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
