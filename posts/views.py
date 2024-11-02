from django.http import HttpResponse
from .temp_data import elencos_i_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Post

def detail_elenco(request, Post_id):
    post = get_object_or_404(Post, id=Post_id)
    context = {'Post': post}
    return render(request, 'posts/detail.html', context)

def list_elencos(request):
    post_list = Post.objects.all()
    context = {"Post_list": post_list}
    return render(request, 'posts/index.html', context)

def create_elenco(request):
    if request.method == 'POST':
        Post_title = request.POST['title']
        Post_year = request.POST['year']
        Post_conteudo = request.POST['conteudo']
        Post_goleiro = request.POST['goleiro']
        Post_defesa = request.POST['defesa']
        Post_meio = request.POST['meio']
        Post_ataque = request.POST['ataque']
        Post_poster_url = request.POST['poster_url']
        post = Post(title=Post_title, year=Post_year, conteudo=Post_conteudo, goleiro=Post_goleiro, defesa=Post_defesa, meio=Post_meio, ataque=Post_ataque,poster_url=Post_poster_url)
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    else:
        return render(request, 'posts/create.html', {})
    
def update_elenco(request, Post_id):
    post = get_object_or_404(Post, pk=Post_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.year = request.POST['year']
        post.conteudo = request.POST['conteudo']
        post.goleiro = request.POST['goleiro']
        post.defesa = request.POST['defesa']
        post.meio = request.POST['meio']
        post.ataque = request.POST['ataque']
        post.poster_url = request.POST['poster_url']
        post.save()
        return HttpResponseRedirect(
            reverse('posts:detail', args=(post.id, )))
    context = {'Post': post}
    return render(request, 'posts/update.html', context)
    
def delete_elenco(request, Post_id):
    post = get_object_or_404(Post, pk=Post_id)
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('posts:index'))
    context = {'Post': post}
    return render(request, 'posts/delete.html', context)