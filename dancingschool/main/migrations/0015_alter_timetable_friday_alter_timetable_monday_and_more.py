# Generated by Django 4.2.7 on 2023-12-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_timetable_alter_review_type_of_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='friday',
            field=models.CharField(blank=True, default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='monday',
            field=models.CharField(blank=True, default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='saturday',
            field=models.CharField(blank=True, default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='sunday',
            field=models.CharField(blank=True, default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='thursday',
            field=models.CharField(blank=True, default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='tuesday',
            field=models.CharField(blank=True, default='-', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='wednesday',
            field=models.CharField(blank=True, default='-', max_length=10, null=True),
        ),
    ]
