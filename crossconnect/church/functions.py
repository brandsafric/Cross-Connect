from django.db.models import Avg
from datetime import datetime, timedelta
from datetime import datetime, timedelta

def get_service_count_date_range_average(days, services):
    today = datetime.now()
    date_delta = today + timedelta(-30)
    date_range_services = services.filter(date__range=[date_delta, today])
    average = date_range_services.aggregate(Avg('attendance_count'))
    return int(average['attendance_count__avg'])

def get_service_count_date_range_change(services):
    today = datetime.now()
    date_delta = today + timedelta(-30)
    date_range_services = services.filter(date__range=[date_delta, today])
    recent_service = date_range_services[(date_range_services.count() - 1)]
    oldest_service = date_range_services[0]
    return recent_service.attendance_count - oldest_service.attendance_count

def get_services_date_range(services, first_date, second_date):
    return services.filter(date__range=[second_date, first_date])

def get_services_count_data(services):
    data = list(services.values_list('date', 'attendance_count'))
    data = list(map(list, data))
    for set in data:
        set[0] = set[0].strftime('%m/%d/%y')
    return data
