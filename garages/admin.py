from django.contrib import admin
from .models import *


# Register your models here.

class GarageAdmin(admin.ModelAdmin):
    model = Garage


# class MakeInLine(admin.TabularInline):
#     model = Make
#     extra = 1
#
#
# class ManufacturerAdmin(admin.ModelAdmin):
#     model = Manufacturer
#     inlines = [MakeInLine]


admin.site.register(Garage, GarageAdmin)
# admin.site.register(Manufacturer, ManufacturerAdmin)
