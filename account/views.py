from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile
from courses.models import Courses
from .models import Cart,CartItems
from django.http import HttpResponseRedirect


def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')




def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    

def profile(request):
        # if request.user == False:
        #   messages.success(request, 'Plz Login First')
        #   return redirect('login')
        profile=Profile.objects.get(user=request.user)
        return render(request ,'accounts/profile.html',{'profile':profile})   
def logout_user(request):
    print("logout called")
    logout(request)
    return redirect('login')   

def cart(request):
        if not request.user.is_authenticated:
          messages.success(request, 'Plz Login First')
          return redirect('login')
        context={'cart':CartItems.objects.filter(cart__is_paid=False,cart__user=request.user)}
        cart=CartItems.objects.filter(cart__is_paid=False,cart__user=request.user)
        sum=0
        for i in cart:
                sum=sum+i.course.course_price 
             
        print(sum) 
        context['before_discount']=sum 
        context['total_price']=sum 
        discount_price=0
        for i in cart:
            if i.course.discout_price >= 0:
             sum=sum-i.course.discout_price
             discount_price=discount_price+i.course.discout_price
            else:
             context['total_price']=sum
        context['total_price']=sum  
        context['discount_price']=discount_price
        return render(request, 'accounts/cart.html', context)
def remove_Cart(request, uid):
     cart=CartItems.objects.get(uid=uid)
     cart.delete()
     return redirect('cart')

def add_to_cart(request , uid):   #this is uid of course
        print(request.user)
        if not request.user.is_authenticated:
             messages.success(request, 'Plz Login First')
             return redirect('login')
        course= Courses.objects.get(uid=uid)
        user=request.user
        cart,_=Cart.objects.get_or_create(user=user,is_paid=False)
        CartItems.objects.create(cart=cart,course=course, )
        return redirect('cart')  
           

