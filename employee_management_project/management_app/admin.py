from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Job)
admin.site.register(WorkPlace)
admin.site.register(Employee)
admin.site.register(WorkTime)
admin.site.register(Statistics)