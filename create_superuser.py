from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'  
password = 'adminpassword'  
email = 'admin@example.com'  

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superusuário criado com sucesso!")
else:
    print("Superusuário já existe!")