from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from base.emails import send_account_activation_email
import uuid
from courses.models import Courses

# Create your models here.

class Profile(BaseModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    profile_image=models.ImageField(null=True,upload_to='profile')

    def __str__(self):
        return self.user.username

    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid=False,cart__user=self.user).count()
class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    # ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)
         

class CartItems(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) 
    course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    discout_price=models.FloatField(null=True)
    quantity = models.IntegerField(default=1)
    
    # def total_price(self):
    #     cart_items=CartItems.objects.get(cart=self.cart)
    #     price=[]
    #     for cart in cart_items:
    #         price.append(cart.product.price)

    #     print(price)
    #     return sum(price)    
    # def __str__(self):
    #     return str(self.user.username) + " " + str(self.product.product_name)
        

@receiver(post_save ,sender = User)
def  send_email_token(sender, instance , created , **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email , email_token)

    except Exception as e:
        print(e)

