from django.contrib import admin
from weatherapp.models import *

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Data,DataAdmin)
