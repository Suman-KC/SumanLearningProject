# from csv import list_dialects
from django.contrib import admin

# Register your models here.

from .models import Courses,Course_Description




admin.site.register(Courses)



admin.site.register(Course_Description)


