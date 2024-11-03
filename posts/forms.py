from django import forms
from django.forms import ModelForm
from .models import Post, Comment

# class PostForm(forms.Form):
#     title = forms.CharField(label='Clube', max_length=100)
#     year = forms.IntegerField(label='Ano', min_value=1857, max_value=2024)
#     conteudo = forms.CharField(label='Descrição', max_length=1500)
#     goleiro = forms.CharField(label='Goleiro', max_length=100)
#     defesa = forms.CharField(label='Defesa', max_length=300)
#     meio = forms.CharField(label='Meio-Campo', max_length=300)
#     ataque = forms.CharField(label='Ataque', max_length=300)
#     poster_url = forms.URLField(label='URL do Poster', max_length=600)

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'year',
            'categories',
            'conteudo',
            'goleiro',
            'defesa',
            'meio',
            'ataque',
            'poster_url',
        ]
        labels = {
            'title': 'Clube',
            'year': 'Ano',
            'categories': 'Categorias',
            'conteudo': 'Conteúdo',
            'goleiro': 'Goleiro',
            'defesa': 'Defesa',
            'meio': 'Meio-Campo',
            'ataque': 'Ataque',
            'poster_url': 'URL do Poster',
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }