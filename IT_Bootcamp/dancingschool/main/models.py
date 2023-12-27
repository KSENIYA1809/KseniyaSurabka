from django.db import models
from django.utils import timezone


class Price(models.Model):
    number_of_classes = models.IntegerField()
    price_60_min = models.CharField(max_length=10)
    price_90_min = models.CharField(max_length=10)


class Timetable(models.Model):
    time_lesson = models.CharField(max_length=20)
    monday = models.CharField(max_length=20)
    tuesday = models.CharField(max_length=20)
    wednesday = models.CharField(max_length=20)
    thursday = models.CharField(max_length=20)
    friday = models.CharField(max_length=20)
    saturday = models.CharField(max_length=20)
    sunday = models.CharField(max_length=20)

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)


class Review(models.Model):
    RATINGS = [('★', '1'), ( '★★', '2'), ('★★★', '3'), ('★★★★', '4'), ('★★★★★', '5')]
    Type_of_classes = [("Yoga", "Yoga"), ("Dance", "Dance")]
    
    rating = models.CharField(max_length=10, choices=RATINGS)
    type_of_classes = models.CharField(max_length=10, choices=Type_of_classes)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    date_publish = models.DateTimeField(default=timezone.now)#проверить, возможно не работает
