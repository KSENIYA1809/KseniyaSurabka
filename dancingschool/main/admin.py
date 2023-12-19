from django.contrib import admin
from .models import Author, Price, Review, Timetable

# Register your models here.
admin.site.register(Author)
admin.site.register(Price)
admin.site.register(Review)
admin.site.register(Timetable)
