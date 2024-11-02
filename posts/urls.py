from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from . import views

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='index'),               # Rota para a listagem de elencos
    path('create/', PostCreateView.as_view(), name='create'),      # Rota para criação de novo elenco
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),    # Rota para detalhes do elenco
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),  # Rota para atualização do elenco
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),  # Rota para deletar o elenco
]