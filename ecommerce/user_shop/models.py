from django.db import models

# Create your models here.
class user_login(models.Model):

    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    dob = models.CharField(max_length=50)
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname


#3. seller_details - id, user_id, name, about, addr, pin, email, contact, status
class seller_details(models.Model):
    #id
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    addr = models.CharField(max_length=500)
    pin = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=15)
    status = models.CharField(max_length=10)


#6. product_master - id, product_name, seller_id, sub_category_id, description, pic, price, stock, dt, tm, keywords, status
class product_master(models.Model):
    id =  models.BigAutoField(auto_created=True, primary_key=True)
    product_name = models.CharField(max_length=50)
    seller_id = models.IntegerField()
    description = models.CharField(max_length=500)
    pic = models.CharField(max_length=500)
    price = models.FloatField()


#8. shopping_cart - id, user_id, product_id, qty, dt, tm, status
class shopping_cart(models.Model):
    # id
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    qty = models.IntegerField()
    price = models.FloatField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=10)

