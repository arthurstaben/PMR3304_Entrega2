# Generated by Django 5.1.1 on 2024-11-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default='2024-11-03 00:00:00'),
            preserve_default=False,
        ),
    ]
