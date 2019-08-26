from django.db.models import Avg
from datetime import datetime, timedelta
from datetime import datetime, timedelta

def get_service_count_date_range_average(days, services):
    today = datetime.now()
    date_delta = today + timedelta(-30)
    date_range_services = services.filter(date__range=[date_delta, today])
    average = date_range_services.aggregate(Avg('attendance_count'))
    return int(average['attendance_count__avg'])

def get_service_count_date_range_change(days, services):
    today = datetime.now()
    date_delta = today + timedelta(-30)
    date_range_services = services.filter(date__range=[date_delta, today])
    recent_service = date_range_services[(date_range_services.count() - 1)]
    latest_service = date_range_services[0]
    return latest_service.attendance_count - recent_service.attendance_count
