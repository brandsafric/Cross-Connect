from django.shortcuts import render, redirect
from church.forms import ChurchCreateForm, ServiceTemplateCreateForm, ServiceCreateForm
from .models import Church, ServiceTemplate, Service
from church.functions import *
import json
from django.http import JsonResponse
from datetime import datetime


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
    all_services = Service.objects.filter(template=template).order_by('date')

    today = datetime.now()
    one_month_delta = today + timedelta(-30)
    three_month_delta = today + timedelta(-90)
    six_month_delta = today + timedelta(-180)
    one_year_delta = today + timedelta(-364)

    one_month_range = get_services_date_range(all_services, today, one_month_delta)
    three_month_range = get_services_date_range(all_services, today, three_month_delta)
    six_month_range = get_services_date_range(all_services, today, six_month_delta)
    one_year_range = get_services_date_range(all_services, today, one_year_delta)
    # All services previously declared

    one_month_average = int(one_month_range.aggregate(Avg('attendance_count'))['attendance_count__avg'])
    three_month_average = int(three_month_range.aggregate(Avg('attendance_count'))['attendance_count__avg'])
    six_month_average = int(six_month_range.aggregate(Avg('attendance_count'))['attendance_count__avg'])
    one_year_average = int(one_year_range.aggregate(Avg('attendance_count'))['attendance_count__avg'])
    all_time_average = int(all_services.aggregate(Avg('attendance_count'))['attendance_count__avg'])

    one_month_change = get_service_count_date_range_change(one_month_range)
    three_month_change = get_service_count_date_range_change(three_month_range)
    six_month_change = get_service_count_date_range_change(six_month_range)
    one_year_change = get_service_count_date_range_change(one_year_range)
    all_time_change = get_service_count_date_range_change(all_services)


    one_month_data = get_services_count_data(one_month_range)
    three_month_data = get_services_count_data(three_month_range)
    six_month_data = get_services_count_data(six_month_range)
    one_year_data = get_services_count_data(one_year_range)
    all_time_data = get_services_count_data(all_services)


    one_month_data.insert(0, ['Date', 'Count'])
    three_month_data.insert(0, ['Date', 'Count'])
    six_month_data.insert(0, ['Date', 'Count'])
    one_year_data.insert(0, ['Date', 'Count'])
    all_time_data.insert(0, ['Date', 'Count'])

    context = {
        'template': template,
        'one_month': {
            'change': one_month_change,
            'average': one_month_average,
            'data': json.dumps(one_month_data)
        },
        'three_month': {
            'change': three_month_change,
            'average': three_month_average,
            'data': json.dumps(three_month_data)
        },
        'six_month': {
            'change': six_month_change,
            'average': six_month_average,
            'data': json.dumps(six_month_data)
        },
        'one_year': {
            'change': one_year_change,
            'average': one_year_average,
            'data': json.dumps(one_year_data)
        },
        'all_time': {
            'change': all_time_change,
            'average': all_time_average,
            'data': json.dumps(all_time_data)
        },
        'services': all_services

    }

    return render(request, 'church/service_template_detail.html', context)

def service_detail(request, id):
    return render(request, 'church/service_detail.html')
