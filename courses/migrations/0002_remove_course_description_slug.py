# Generated by Django 4.2.1 on 2023-06-25 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_description',
            name='slug',
        ),
    ]
