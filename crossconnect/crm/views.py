from django.shortcuts import render, redirect
from .forms import ContactCreateForm
from .models import Contact
from django.contrib.auth.decorators import login_required


@login_required
def contacts(request):

    user=request.user
    church = user.home_church
    contacts = Contact.objects.filter(owner=church)

    context = {
        "contacts": contacts
    }

    return render(request, 'crm/contacts.html', context)



def add_contact(request):
    user = request.user
    if request.method == "POST":
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            obj = Contact()
            obj.owner = user.home_church
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            obj.save()
            return redirect('homepage')
    else:
        form = ContactCreateForm()

    context = {
        'form': form
    }

    return render(request, 'crm/add_contact.html', context)
