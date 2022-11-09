from django.db import models


class Materia(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    data_publicacao = models.DateField()
    imagem = models.ImageField()
    
    def __str__(self):
        return self.titulo