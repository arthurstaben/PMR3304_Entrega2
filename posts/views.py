from django.http import HttpResponse
from .temp_data import elencos_i_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from datetime import datetime
import os, shutil

# def detail_elenco(request, Post_id):
#     post = get_object_or_404(Post, id=Post_id)
#     context = {'Post': post}
#     return render(request, 'posts/detail.html', context)

# def list_elencos(request):
#     post_list = Post.objects.all()
#     context = {"Post_list": post_list}
#     return render(request, 'posts/index.html', context)

# def create_elenco(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             Post_title = request.POST['title']
#             Post_year = request.POST['year']
#             Post_conteudo = request.POST['conteudo']
#             Post_goleiro = request.POST['goleiro']
#             Post_defesa = request.POST['defesa']
#             Post_meio = request.POST['meio']
#             Post_ataque = request.POST['ataque']
#             Post_poster_url = request.POST['poster_url']
#             post = Post(title=Post_title, year=Post_year, conteudo=Post_conteudo, goleiro=Post_goleiro, defesa=Post_defesa, meio=Post_meio, ataque=Post_ataque,poster_url=Post_poster_url)
#             post.save()
#             return HttpResponseRedirect(
#                 reverse('posts:detail', args=(post.id, )))
#     else:
#         form = PostForm()
#         context = {'form': form}
#         return render(request, 'posts/create.html', context)
    
# def update_elenco(request, Post_id):
#     post = get_object_or_404(Post, pk=Post_id)
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post.title = request.POST['title']
#             post.year = request.POST['year']
#             post.conteudo = request.POST['conteudo']
#             post.goleiro = request.POST['goleiro']
#             post.defesa = request.POST['defesa']
#             post.meio = request.POST['meio']
#             post.ataque = request.POST['ataque']
#             post.poster_url = request.POST['poster_url']
#             post.save()
#             return HttpResponseRedirect(
#                 reverse('posts:detail', args=(post.id, )))
#     else:
#         form = PostForm(
#             initial={
#             'title': post.title,
#             'year': post.year,
#             'conteudo': post.conteudo,
#             'goleiro': post.goleiro,
#             'defesa': post.defesa,
#             'meio': post.meio,
#             'ataque': post.ataque,
#             'poster_url': post.poster_url,
#             })
#     context = {'Post': post, 'form': form}
#     return render(request, 'posts/update.html', context)

    
# def delete_elenco(request, Post_id):
#     post = get_object_or_404(Post, pk=Post_id)
#     if request.method == "POST":
#         post.delete()
#         return HttpResponseRedirect(reverse('posts:index'))
#     context = {'Post': post}
#     return render(request, 'posts/delete.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'Post_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'Post'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/create.html'
    success_url = reverse_lazy('posts:index')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/update.html'
    success_url = reverse_lazy('posts:index')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:index')

def create_comment(request, Post_id):
    post = get_object_or_404(Post, pk=Post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(Post, author=comment_author, 
                              text=comment_text,
                              post=post) 
            comment.save()
            return HttpResponseRedirect(reverse('posts:detail', args=(Post_id,)))
    else:
        form = CommentForm()
    
    context = {'form': form, 'post': post}  
    return render(request, 'posts/comment.html', context)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'posts/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.posts.all()
    return render(request, 'posts/category_detail.html', {'posts': posts, 'category': category})
