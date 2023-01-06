from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, 'admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, 'admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)


############################################USER#####################################################

from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        # print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname


            pr_l = product_master.objects.all().order_by('-id')
            context = {'uname': request.session['user_name'], 'pr_l': pr_l}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'user_login.html',context)
    else:
        return render(request, 'user_login.html')


def user_home(request):
    pr_l = product_master.objects.all().order_by('-id')

    context = {'uname':request.session['user_name'], 'pr_l': pr_l}
    return render(request,'user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')


def user_details_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, dob=dob,addr=addr, pin=pin, contact=contact, email=email )
        ud.save()

        # print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'user_login.html', context)

    else:
        return render(request, 'user_details_add.html')


def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)




###################################################################################
############################### SELLER #######################################

def seller_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='seller')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'seller_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'seller_login.html',context)
    else:
        return render(request, 'seller_login.html')


def seller_home(request):

    context = {'uname':request.session['user_name']}
    return render(request,'seller_home.html',context)
    #send_mail("heoo", "hai", '**@gmail.com')



def seller_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return seller_login_check(request)
    else:
        return seller_login_check(request)


from .models import product_master
from django.core.files.storage import FileSystemStorage
from datetime import datetime
def seller_product_master_add(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        pic = fs.save(uploaded_file.name, uploaded_file)

        product_name = request.POST.get('product_name')
        seller_id = request.session['user_id']
        description = request.POST.get('description')
        price = float(request.POST.get('price'))

        pm = product_master(product_name=product_name, seller_id=int(seller_id), pic=pic, description=description, price=price)
        pm.save()

        context = {'msg':'Record added'}
        return render(request, 'seller_product_master_add.html',context)

    else:
        return render(request, 'seller_product_master_add.html')


def seller_product_master_delete(request):
    id = request.GET.get('id')
    print("id="+id)

    pm = product_master.objects.get(id=int(id))
    pm.delete()

    seller_id = request.session['user_id']

    pm_l = product_master.objects.filter(seller_id=int(seller_id))


    context ={'product_list':pm_l,'msg':'Record deleted'}
    return render(request,'seller_product_master_view.html',context)


def seller_product_master_view(request):
    seller_id = request.session['user_id']

    pm_l = product_master.objects.filter(seller_id=int(seller_id))


    context = {'product_list': pm_l, 'msg': ''}
    return render(request, 'seller_product_master_view.html', context)


from .models import shopping_cart
def user_shopping_cart_add(request):
    product_id = request.GET.get('product_id')
    user_id = request.session['user_id']
    qty = 1
    dt = datetime.today().strftime('%Y-%m-%d')
    tm = datetime.today().strftime('%H:%M:%S')
    status = 'ok'
    prd = product_master.objects.get(id=int(product_id))

    pr_l = shopping_cart.objects.filter(product_id=product_id,user_id=user_id)
    if len(pr_l) == 0:
        pr = shopping_cart(product_id=int(product_id), user_id=int(user_id), qty=int(qty),
                           price=float(prd.price),dt=dt, tm=tm, status=status)
        pr.save()
    else:
        pr = shopping_cart.objects.get(product_id=product_id,user_id=user_id)
        qty = pr.qty
        pr.qty = qty+1
        pr.price=float(prd.price*pr.qty)
        pr.save()
    pr_l = product_master.objects.all().order_by('-id')
    context = {'msg':'Added to cart', 'pr_l': pr_l}
    return render(request, 'user_home.html',context)


def user_shopping_cart_view(request):
    user_id = request.session['user_id']
    pr_l = shopping_cart.objects.filter(user_id=int(user_id))
    pm_l = product_master.objects.all()
    context = {'cart_list': pr_l, 'product_list': pm_l, 'msg': ''}
    return render(request, 'user_shopping_cart_view.html', context)



from .models import seller_details
def  seller_details_add(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        about = request.POST.get('about')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('passwd')
        status = "new"

        uname = email

        ul = user_login(uname=uname, passwd=password, u_type='seller')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = seller_details(user_id=user_id, name=name, about=about, addr=addr, pin=pin, contact=contact, email=email,
                            status=status)
        ud.save()

        print(user_id)
        context = {'msg': 'Seller Added'}
        return render(request, 'seller_login.html',context)

    else:
        return render(request, 'seller_details_add.html')


def product_search(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        pd = ''
        try:
            pd = product_master.objects.filter(price=price)
        except:
            pass
        context  = {'pr_l': pd}
        return render(request, 'user_home.html', context)
        
    else:
        return render(request, 'user_home.html')