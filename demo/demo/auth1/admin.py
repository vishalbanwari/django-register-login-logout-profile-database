from django.contrib import admin

# Register your models here.
from .models import Employees, Department

admin.site.register(Employees)
admin.site.register(Department)
