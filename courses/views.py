
from django.shortcuts import render,redirect
from .models import Course_Description,Courses

def all_courses(request):
    allcourses=Courses.objects.all()
    return render(request, "courses/all_courses.html",{'allcourses':allcourses})
def get_course(request , slug):
        course= Courses.objects.get(slug =slug)
        course_Description=Course_Description.objects.get(course=course)
        # if request.GET.get('size'):
        #         size=request.GET.get('size')
        #         price=product.get_updated_price(size)
        #         context['selected_size']=size
        #         context['updated_price']=price
        #         print(price)
        return render(request  , 'courses/course.html' ,{'course_Description':course_Description})
