# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'input_field'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input_field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'input_field'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
