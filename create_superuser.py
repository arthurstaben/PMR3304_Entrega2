from django.contrib.auth import get_user_model
import os

User = get_user_model()

# Informações do superusuário
username = 'admin'
password = 'adminpassword'
email = 'admin@example.com'

# Criação do superusuário se ele não existir
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superusuário criado com sucesso!")
else:
    print("Superusuário já existe!")