# Generated by Django 3.0.7 on 2020-06-07 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0002_remove_quiz_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='creator',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
