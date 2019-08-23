from django.shortcuts import render, redirect
from django.db.models import Avg
from church.forms import ChurchCreateForm, ServiceTemplateCreateForm, ServiceCreateForm
from .models import Church, ServiceTemplate, Service
import datetime

import json


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

def service_template(request, id):


    template = ServiceTemplate.objects.get(pk=id)
    services = Service.objects.filter(template=template).order_by('-date')

    average = services.aggregate(Avg('attendance_count'))
    average_attendance = int(average['attendance_count__avg'])

    if len(services) > 1:
        attendance_delta = services[0].attendance_count - services[1].attendance_count
    else:
        attendance_delta = None

    data_array = [['Date', 'Attendance']]

    for service in services:
        data_array.append([service.date.strftime('%m/%d'), service.attendance_count])

    context = {
        "template": template,
        "services": services,
        "average_attendance": average_attendance,
        "attendance_delta": attendance_delta,
        "data_array": json.dumps(data_array)
    }

    return render(request, 'church/service_detail.html', context)
