from django.db import migrations
from django.utils import timezone
from django.contrib.auth.hashers import make_password

def create_initial_comments(apps, schema_editor):
    Post = apps.get_model('posts', 'Post')
    User = apps.get_model('auth', 'User')
    Comment = apps.get_model('posts', 'Comment')

    post1 = Post.objects.get(id=1)
    post3 = Post.objects.get(id=3)

    user1, created = User.objects.get_or_create(username="Lucas Araújo")
    if created:
        user1.password = make_password("password1")
        user1.save()
        
    user2, created = User.objects.get_or_create(username="Charles Oliveira")
    if created:
        user2.password = make_password("password2")
        user2.save()
        
    user3, created = User.objects.get_or_create(username="Éverton Ribeiro")
    if created:
        user3.password = make_password("password3")
        user3.save()
        
    user4, created = User.objects.get_or_create(username="Ticiane Dois")
    if created:
        user4.password = make_password("password4")
        user4.save()
        
    user5, created = User.objects.get_or_create(username="Artur Skull")
    if created:
        user5.password = make_password("password5")
        user5.save()

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