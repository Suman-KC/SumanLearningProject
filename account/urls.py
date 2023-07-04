from django.urls import path
from .views import login_page,register_page , activate_email,logout_user
from .views import cart,remove_Cart,add_to_cart,profile

urlpatterns = [
   path('login/' , login_page , name="login" ),
   path('register/' , register_page , name="register"),
   path('logout_user/',logout_user,name='logout_user'),
   path('activate/<email_token>/' , activate_email , name="activate_email"),
   path('cart/', cart ,name="cart"),
   path('remove_Cart/<uid>/',remove_Cart,name='remove_Cart'),
   path('add_to_Cart/<uid>/',add_to_cart,name='add_to_cart'),
   path('profile/',profile,name="profile"),
 
]