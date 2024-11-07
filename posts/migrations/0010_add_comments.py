from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_initial_users(apps, schema_editor):
    User = apps.get_model('auth', 'User')

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

class Migration(migrations.Migration):
    dependencies = [
        ('posts', '0009_categories'),  
    ]

    operations = [
        migrations.RunPython(create_initial_users),
    ]