from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.list_elencos, name='index'),
    path('create/', views.create_elenco, name='create'),
    path('delete/<int:Post_id>/', views.delete_elenco, name='delete'),
    path('<int:Post_id>/', views.detail_elenco, name='detail'),
    path('update/<int:Post_id>/', views.update_elenco, name='update'),
    path('delete/<int:Post_id>/', views.delete_elenco, name='delete'),
]