# Generated by Django 4.2.7 on 2023-11-25 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_classes', models.IntegerField()),
                ('price_60_min', models.CharField(max_length=10)),
                ('price_90_min', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[('1', 'один'), ('2', 'два'), ('3', 'три'), ('4', 'четыре'), ('5', 'пять')], max_length=1)),
                ('gender', models.CharField(choices=[('ж', 'женский'), ('м', 'мужской')], max_length=1)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.author')),
            ],
        ),
    ]
