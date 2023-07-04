from django.shortcuts import render
from courses.models import Courses

# Create your views here.
def home(request):
    allcourses=Courses.objects.all()
    return render(request, "home/home.html",{'allcourses':allcourses})
def about(request):
    return render(request, "home/about.html")
def contact(request):
    return render(request, "home/contact.html")
def blog(request):
    return render(request, "home/blog.html")
