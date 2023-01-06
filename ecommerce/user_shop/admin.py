from django.contrib import admin

# Register your models here.
from . models import user_login,user_details, product_master, seller_details



admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(product_master)
admin.site.register(seller_details)