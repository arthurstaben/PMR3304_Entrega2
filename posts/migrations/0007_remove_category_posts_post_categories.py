# Generated by Django 5.1.1 on 2024-11-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='posts', to='posts.category'),
        ),
    ]
