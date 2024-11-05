from django.db import migrations
from django.utils import timezone

def create_initial_comments(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    User = apps.get_model('auth', 'User')
    Comment = apps.get_model('posts', 'Comment')

    post1 = Post.objects.get(id=1)
    post3 = Post.objects.get(id=3)

    user1, _ = User.objects.get(username="Lucas Araújo", password='password1') 
    user2, _ = User.objects.get(username="Charles Oliveira", password='password2')
    user3, _ = User.objects.get(username="Éverton Ribeiro", password='password3')
    user4, _ = User.objects.get(username="Ticiane Dois", password='password4') 
    user5, _ = User.objects.get(username="Artur Skull", password='password5')   

    Comment.objects.create(
        post=post1,
        author=user1,
        text="Orgulho de ser nordestino. Bora Bahêa!",
        data=timezone.now()
    )
    Comment.objects.create(
        post=post1,
        author=user2,
        text="Esse time do Bahia era duríssimo. Bobô e Charles eram craques da pelota.",
        data=timezone.now()
    )
    Comment.objects.create(
        post=post1,
        author=user3,
        text="Que time era esse do esquadrão de aço. Lembro como se fosse hoje do 2x1 na Fonte Nova lotada!",
        data=timezone.now()
    )

    Comment.objects.create(
        post=post3,
        author=user4,
        text="Que final. Melhor jogo que vi na vida!",
        data=timezone.now()
    )
    
    Comment.objects.create(
        post=post3,
        author=user5,
        text="Baita de uma final, melhor que assisti. Noite de brilho de Steven Gerrard.",
        data=timezone.now()
    )

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0010_add_initial_posts'),  
    ]

    operations = [
        migrations.RunPython(create_initial_comments),
    ]