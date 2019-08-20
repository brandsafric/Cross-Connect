from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django import forms

# Create your views here.
def register(request):
    print(request)
    if request.method == "POST":
        print('Method is Post')
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            form.save()
            new_user = authenticate(email=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('homepage')
        else:
            print(form.errors)
    else:
        print("Not valid")
        form = CustomUserCreationForm()

    context = {
    'form': form
    }

    return render(request, 'users/register.html', context)

def profile(request):
    return
