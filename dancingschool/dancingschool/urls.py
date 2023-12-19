"""
URL configuration for dancingschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main import views as main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start/', main_views.main_name, name = 'start'),
    path('', main_views.main_name), 
    path('reviews/', main_views.reviews, name = 'reviews'),
    path('reviews/<int:review_id>', main_views.review, name = 'review'),
    path('add_free_form', main_views.add_free_form, name ="add_free_form"),#форма для записи
    path('reviews/add/model', main_views.add_model, name ="add_model"),
    path('price', main_views.price, name ="price"),
    path('timetable', main_views.timetable, name ="timetable"),
    path('contacts', main_views.contacts, name ="contacts"),
    path('thanks', main_views.thanks, name ="thanks"),
    # path('register', main_views.register, name ="register"),
    # path('register_done', main_views.register_done, name ="register_done")
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
