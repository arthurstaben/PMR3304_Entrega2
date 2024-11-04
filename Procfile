web: gunicorn PMR3304_Entrega2.wsgi:application --log-file -
release: python manage.py migrate && python create_superuser.py