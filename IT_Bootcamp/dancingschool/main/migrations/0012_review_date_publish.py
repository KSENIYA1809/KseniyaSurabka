# Generated by Django 4.2.7 on 2023-12-04 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date_publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]