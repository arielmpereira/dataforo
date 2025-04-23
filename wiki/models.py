from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Wiki(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

