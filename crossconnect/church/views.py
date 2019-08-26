from django.shortcuts import render, redirect
from church.forms import ChurchCreateForm, ServiceTemplateCreateForm, ServiceCreateForm
from .models import Church, ServiceTemplate, Service
from church.functions import *
import json
from django.http import JsonResponse


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

    one_month_service_count_average = get_service_count_date_range_average(30, all_services)
    three_month_service_count_average = get_service_count_date_range_average(60, all_services)
    six_month_service_count_average = get_service_count_date_range_average(180, all_services)
    one_year_service_count_average = get_service_count_date_range_average(364, all_services)

    one_month_service_count_change = get_service_count_date_range_change(30, all_services)
    three_month_service_count_change = get_service_count_date_range_change(60, all_services)
    six_month_service_count_change = get_service_count_date_range_change(180, all_services)
    one_year_service_count_change = get_service_count_date_range_change(364, all_services)

    data_array = [['Date', 'Attendance']]
    # one_month_data_array = data_array
    # three_month_data_array = data_array
    # six_month_data_array = data_array
    # one_year_data_array = data_array
    # all_data_array = data_array

    data = list(all_services.values('date', 'attendance_count'))
    data_json = JsonResponse(data, safe=False)
    print(data)
    # services = Service.objects.filter(template=template).order_by('-date')

    if len(all_services) > 1:
        attendance_delta = all_services[0].attendance_count - all_services[1].attendance_count
    else:
        attendance_delta = None

    context = {
        # "template": template,
        # "services": services,
        # "average_attendance": average_attendance,
        # "attendance_delta": attendance_delta,
        "data_array": json.dumps(data_array)
    }

    return render(request, 'church/service_template_detail.html', context)

def service_detail(request, id):
    return render(request, 'church/service_detail.html')
