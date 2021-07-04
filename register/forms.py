from django import forms
from django.forms import widgets
from .models  import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'messages': forms.Textarea(attrs={'cols':60,'rows':5}),
        }



# Registering User
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

    def clean_username(self):
        data = self.cleaned_data['username']
        lower_case = data.lower()
        return lower_case


# Updating User information
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean_username(self):
        data = self.cleaned_data['username']
        lower_case = data.lower()
        return lower_case

# Updating or Adding User Bio
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blogtitle','blogpost']
    



