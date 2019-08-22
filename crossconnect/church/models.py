from django.db import models

# Create your models here.
class Church(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=30)

class ServiceTemplate(models.Model):

    DAYS_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )

    church = models.ForeignKey(Church, on_delete="CASCADE")
    name = models.CharField(max_length=200, blank=True)
    time = models.TimeField()
    day = models.IntegerField(choices=DAYS_OF_WEEK)

class Service(models.Model):
    template = models.ForeignKey(ServiceTemplate, on_delete="CASCADE")
    attendance_count = models.IntegerField()
    date = models.DateField()
