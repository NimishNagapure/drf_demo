# Generated by Django 3.1.7 on 2021-10-16 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
