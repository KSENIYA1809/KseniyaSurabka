# Generated by Django 4.2.7 on 2023-12-08 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_review_type_of_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_lesson', models.CharField(max_length=10)),
                ('monday', models.CharField(default='-', max_length=10)),
                ('tuesday', models.CharField(default='-', max_length=10)),
                ('wednesday', models.CharField(default='-', max_length=10)),
                ('thursday', models.CharField(default='-', max_length=10)),
                ('friday', models.CharField(default='-', max_length=10)),
                ('saturday', models.CharField(default='-', max_length=10)),
                ('sunday', models.CharField(default='-', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='type_of_classes',
            field=models.CharField(choices=[('Yoga', 'Yoga'), ('Dance', 'Dance')], max_length=10),
        ),
    ]
