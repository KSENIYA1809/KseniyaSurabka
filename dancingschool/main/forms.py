from django import forms
from .models import Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddReviewModelForm(forms.ModelForm): #для модели Review
    class Meta:
        model = Review
        fields = ('rating', 'type_of_classes', 'content', 'image')
        labels = {'rating':"Rating", 'type_of_classes': "Type of classes", 'content':"Content", 'image':"Image"}
        widgets = {'content':forms.Textarea(attrs={'class' : 'form'})}

    def clean_content(self):
        content = self.cleaned_data['content'].strip()#очищаем от символов вначале и в конце
        return content
    


class SignUpForm(forms.Form): #если нет модели
        
    name = forms.CharField(max_length=50, label='Write your name')
    phone_number = forms.IntegerField(label='Write your phone number')
    type_of_classes = forms.ChoiceField(choices = (("Yoga", "Yoga"), ("Dance", "Dance")), label="Choose the type of classes")
    message = forms.CharField(widget=forms.Textarea, max_length=2000, label = "Write an additional information")
    
    def clean_name(self):
        name = self.cleaned_data['name'].strip()#очищаем от символов вначале и в конце
        return name
    
    def clean_message(self):
        message = self.cleaned_data['message'].strip()#очищаем от символов вначале и в конце
        return message
    



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
