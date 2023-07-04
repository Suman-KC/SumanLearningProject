from django.urls import path
from .views import get_course,all_courses

urlpatterns = [
    path('all_courses/',all_courses,name='all_courses'),
    path('<slug>/' , get_course , name="get_course"),

]