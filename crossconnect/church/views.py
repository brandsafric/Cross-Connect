from django.shortcuts import render, redirect
from church.forms import ChurchCreateForm, ServiceTemplateCreateForm, ServiceCreateForm
from .models import Church, ServiceTemplate, Service


# Create your views here.
def add_church(request):
    user = request.user
    if request.method == "POST":
        form = ChurchCreateForm(request.POST)
        if form.is_valid():
            obj = Church()
            obj.name = form.cleaned_data['name']
            obj.city = form.cleaned_data['city']
            obj.state = form.cleaned_data['state']
            obj.save()
            user.home_church = obj
            return redirect('homepage')
    else:
        form = ChurchCreateForm()

    context = {
    'form': form
    }

    return render(request, 'church/add_church.html', context)

def add_service_template(request):

    if request.method == 'POST':
        form = ServiceTemplateCreateForm(request.POST)

        if form.is_valid():
            user = request.user
            church = user.home_church
            obj = ServiceTemplate()
            obj.church = church
            obj.name = form.cleaned_data['name']
            obj.time = form.cleaned_data['time']
            obj.day = form.cleaned_data['day']
            obj.save()
            return redirect('homepage')

    form = ServiceTemplateCreateForm()
    context = {
        "form": form
    }

    return render(request, 'church/add_service_template.html', context)

def add_service(request):
    if request.method == 'POST':
        form = ServiceCreateForm(request.POST, user=request.user)

        if form.is_valid():
            obj = Service()
            obj.template = form.cleaned_data['template']
            obj.attendance_count = form.cleaned_data['count']
            obj.date = form.cleaned_data['date']
            obj.save()
            return redirect('homepage')

    form = ServiceCreateForm(user=request.user)
    context = {
        "form": form
    }

    return render(request, 'church/add_service.html', context)
