from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nome_categoria


class Curso(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nome_curso = models.CharField(max_length=100)
    slug = models.SlugField(max_length=30, null=True, blank=True)
    descricao_curso = models.TextField()
    imagem = models.ImageField(upload_to='img', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)

    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')

    data_publicacao = models.DateTimeField(default=datetime.now(), blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_curso
