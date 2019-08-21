from django.contrib import admin
from .models import Church, ServiceTemplate

# Register your models here.
@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ServiceTemplate)
class ServiceTemplateAdmin(admin.ModelAdmin):
    list_display = ('name','day','time')
