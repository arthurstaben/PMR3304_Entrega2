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
    categories = models.ManyToManyField('Category', related_name='posts')
    
    def __str__(self):
        return f'{self.title} ({self.year})'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name