from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=200) #Clube
    year = models.CharField(max_length=5) #Ano 
    conteudo = models.TextField() #Conteúdo/Descrição
    goleiro = models.CharField(max_length=100)
    defesa = models.CharField(max_length=700)
    meio = models.CharField(max_length=700)
    ataque = models.CharField(max_length=700)
    poster_url = models.URLField(max_length=200, null=True) #Poster       
    data = models.DateTimeField(auto_now_add=True) #Data de Postagem
    
    def __str__(self):
        return f'{self.title} ({self.year})'

class Comentario(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'