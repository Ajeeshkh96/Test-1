"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),


    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),


    path('user_shopping_cart_add', views.user_shopping_cart_add, name='user_shopping_cart_add'),
    path('user_shopping_cart_view', views.user_shopping_cart_view, name='user_shopping_cart_view'),



    path('seller_login', views.seller_login_check, name='seller_login'),
    path('seller_logout', views.seller_logout, name='seller_logout'),
    path('seller_home', views.seller_home, name='seller_home'),
    path('seller_details_add', views.seller_details_add, name='seller_details_add'),

    path('seller_product_master_add', views.seller_product_master_add, name='seller_product_master_add'),
    path('seller_product_master_delete', views.seller_product_master_delete, name='seller_product_master_delete'),
    path('seller_product_master_view', views.seller_product_master_view, name='seller_product_master_view'),


    path('product_search', views.product_search, name='product_search'),

]
