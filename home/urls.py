from django.urls import path
from home.views import home,about,contact,blog

urlpatterns = [
   
    path('' , home, name="home"),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
]