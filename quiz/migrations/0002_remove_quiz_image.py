# Generated by Django 3.0.7 on 2020-06-07 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='image',
        ),
    ]
