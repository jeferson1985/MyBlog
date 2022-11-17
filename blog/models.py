from django.db import models
from django.contrib.auth.models import User


class Materia(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    data_publicacao = models.DateField()
    imagem = models.ImageField()
    
    def __str__(self):
        return self.titulo
    
    
class Comentario(models.Model):
    pk_materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nome_usuario = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255)
    data_comentario = models.DateField()
    
    def __str__(self):
       return self.nome_usuario 
   
class Favoritos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return str(self.usuario)