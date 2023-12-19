from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author, Review, Price, Timetable
from .forms import AddReviewModelForm, SignUpForm
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import UserRegisterForm




def main_name(request):
    start = "Welcome to our yoga and dance school - a beautiful place of harmony, beauty and self-development."
    start_2 = "If you are interested and want to join our classes, sign up using the link below."
    return render (request, 'start.html', {'start' : start, 'start_2' : start_2 })


def price(request):
    price_list = Price.objects.all()
    return render(request, 'price.html', {'price_list' : price_list})


def timetable(request):
    timetable_list = Timetable.objects.all()
    return render(request, 'timetable.html', {'timetable_list' : timetable_list})


def contacts(request):
    start = 'Do you want to get in touch with us?'
    phone = 'Number: +000 00 000 00 00 (Telegram, Viber, WhatsApp)'
    instagram = 'Instagram: @Yoga_Dance_School'
    email = 'Email: Yoga_Dance_School@gmail.com'
    adress = 'Adress: 220000, Belarus, Minsk'
    working_hours = 'Working hours: Monday-Saturday from 6 am till 9 pm'
    return render (request, 'contacts.html', {'start' : start, 'phone' : phone, 'instagram' : instagram, 'email' : email, 'adress' : adress, 'working_hours': working_hours})


def reviews(request):
    reviews = Review.objects.all().order_by('-date_publish')
    viewed_reviews = request.session.get('viewed_reviews', [])
    return render(request, 'reviews.html', {'reviews' : reviews, 'viewed_reviews':viewed_reviews})


def review(request, review_id):
    try:
        r = Review.objects.get(id=review_id)
        viewed_reviews = request.session.get('viewed_reviews', [])
        if r.id not in viewed_reviews:
            viewed_reviews.append(r.id)
        request.session['viewed_reviews'] = viewed_reviews
        return render(request, 'review.html', {'r' : r})
    except:
        return HttpResponse(f'<h3>Cannot find the review</h3>')



@permission_required('main.add_review')
def add_model(request):
    if request.method == 'POST':
        form = AddReviewModelForm(request.POST, request.FILES)

        if form.is_valid():
            review_entry = form.save(commit=False)#сохраняет модель, но не отправляет в БД
            try:
                review_entry.author = Author.objects.get(email=request.user.email)
            except:
                review_entry.author = Author.objects.all()[0]    
            review_entry.save()     

            return redirect('review', review_entry.id)      
        else:
            pass
    else:
        form = AddReviewModelForm()
    return render(request, 'add_form.html', {'form':form})



def add_free_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            subject = "Sign up for a lesson"
            body = {
                'name' : form.cleaned_data['name'],
                'phone_number' : form.cleaned_data['phone_number'],
                'type_of_classes' : form.cleaned_data['type_of_classes'],
                'message' : form.cleaned_data['message'],
            }
            body['phone_number'] = str(form.cleaned_data['phone_number'])
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, None, ['admin@mail.ru'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('thanks')
    else:
        form = SignUpForm()
    return render(request, 'add_free_form.html', {'form':form})



def thanks(request):
    thanks = 'Thank you for your contact! We will definitely contact you soon and find a suitable class time for you!'
    return render (request, 'thanks.html', {'thanks' : thanks})




# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Создан аккаунт {username}!')
#             return redirect('register_done')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html', {'form': form})


# def register_done(request):
#     register_done = 'Yes! '
#     return render (request, 'register_done.html', {'register_done' : register_done})

