from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

from . import views

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='index'),              
    path('create/', PostCreateView.as_view(), name='create'),      
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),    
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
    path('<int:Post_id>/comment/', views.create_comment, name='comment'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'), 
]