from django.db import models

# Create your models here.
class Contact(models.Model):
    owner = models.ForeignKey('church.Church', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
