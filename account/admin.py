from django.contrib import admin
from .models import Cart,CartItems

# Register your models here.
from .models import Profile

admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItems)