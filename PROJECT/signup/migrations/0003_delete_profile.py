# Generated by Django 5.0.4 on 2024-05-07 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_alter_user_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]