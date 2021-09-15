from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .models import Product, Offer, Order
import string
from random import choice
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def tekshir(request,password):
    isapper = 0
    isdigit = 0
    if len(password) < 8:
        messages.error(request, "Belgilar soni kamida 8 ta bo'lishi kerak")
        return False
    for i in str(password):
        if  i.isdigit():
            isdigit += 1
        if  i.isupper():
            isapper += 1
    if isapper == 0 or isdigit == 0:
        if isapper == 0:
            messages.error(request, "Bosh harf bo'lishi kerak")
            return False
        if isdigit == 0:
            messages.error(request, "Raqam bo'lishi kerak")
            return False
    return True
def get_url():
    url = ''
    llist = [string.ascii_lowercase, string.digits,string.ascii_uppercase]
    for i in range(5):
        url += choice(choice(llist))
    return url

def index(request):
    category = Category.objects.all()
    product =  Product.objects.all()
    c = {"category":category,"product":product}
    return render(request,"index.html",c)
def loginPage(request):
    if request.method == "POST":
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request,user)
            try:
                Profile.objects.get(user=request.user)
            except:
                Profile(user=request.user).save()
            return redirect('/')
        else:
            messages.info(request, 'Username yoki Parol xato')

    return render(request, 'login.html',{})
def logoutPage(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, 'logout.html')
def signupPage(request):
    form = CreateUserForm()
    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog:login')
    return render(request,'register.html',{'form':form,})
def eltuvchiPage(request):

    return render(request, 'eltuvchi.html')
@login_required(login_url='blog:login')
def offerDetailPage(request, pk):
    product = get_object_or_404(Product, id=pk)
    contex = {
        "product":product
    }
    if request.method == "POST" and not Offer.objects.filter(product=product,vendor=request.user):
        name = request.POST['offername']
        data = Offer(offer_name=name, vendor=request.user, product=product, db_link= get_url())
        data.save()
        print(data)
    return render(request, 'offer_detail.html', contex)
def productDetail(request, slug):
    offer = get_object_or_404(Offer, db_link=slug)
    offer.visits += 1
    offer.save()
    contex = {'offer':offer, 'product':offer.product}
    if request.method == "POST":
        if request.POST['tel']:
            data = request.POST
            user_data = Order(name=data['ism'], region=data['region'],vendor=request.user, tel=data['tel'], product_quantity=data['quantity'], product=offer.product)
            user_data.save()
            offer.orders += int(data['quantity'])
            offer.visits -= 1
            offer.save()
            messages.info(request, "Tez orada operatorlar aloqaga chiqishadi!")
        else:
            messages.error(request, "Telefon raqam kiritish shart")
    return render(request, 'product_detail.html', contex)
def logoutPage(request):
    logout(request)
    return redirect('blog:index')
def user_info(request, username):
    user_ = get_object_or_404(User, username = username)
    offers = Offer.objects.filter(vendor=user_)
    data = {}
    visits_ = 0
    orders_ = 0
    sold_ = 0
    for i in offers:
        visits_ += i.visits
        orders_ += i.orders
        sold_ += i.sold
    data['visits'] = visits_
    data['orders'] = orders_
    data['sold'] = sold_
    return HttpResponse(f"{data}")
@login_required(login_url='blog:login')
def profile(request):
    contex = {
        'username': request.user.username,

    }
    if request.method == "POST":
        data = request.POST
        uSer = get_object_or_404(User, id=request.user.id)
        try:
            pRofile = Profile.objects.get(user=uSer)
        except:
            pRofile = Profile

        if "save_profile" in dict(data).keys():
            ism = data['ism']
            familiya = data['familiya']
            tel = data['tel']
            if len(tel) != 13:
                messages.error(request, "Telefon raqam noto'g'ri")
                return render(request, 'profile.html', contex)
            uSer.first_name = ism
            uSer.last_name = familiya
            pRofile.phone_number = tel
            pRofile.user = uSer
            uSer.save()
            pRofile.save()
        if 'save_card' in dict(data).keys():
            card_number = data['card_number']
            card_vendor = data['card_vendor']
            if len(card_number) != 16:
                messages.error(request, "Karta raqam noto'g'ri")
                return render(request, 'profile.html', contex)
            pRofile.card_number = card_number
            pRofile.card_vendor = card_vendor
            uSer.save()
            pRofile.save()
        if 'save_password' in dict(data).keys():
            password1 = data['password1']
            password2 = data['password2']
            if password1 == password2 and tekshir(request,password1):
                uSer.set_password(password1)
                messages.info(request, "Parol o'zgartirildi")
            else:
                return render(request, 'profile.html', contex)
            uSer.save()
            pRofile.save()

    return render(request, 'profile.html', contex)
@login_required(login_url='blog:login')
def ishxonaPage(request):
    products_len = len(Product.objects.all())
    user_ = Profile.objects.get(user=request.user)

    contex = {
        "Products":products_len,
        'User':user_

    }
    return render(request, 'ishxona.html', contex)
@login_required(login_url='blog:login')
def balansPage(request):
    orders = Order.objects.filter(complete=True)
    balans = 0
    for i in orders:
        balans += int(i.product.payment) * i.product_quantity
    print(balans)
    if request.GET and balans != 0:
        orders.delete()
        pRodiel = Profile.objects.get(user=request.user)
        pRodiel.income += balans
        pRodiel.save()
        return redirect('blog:balans')
    user_ = Profile.objects.get(user=request.user)
    hold = user_.hold
    contex = {
        "Balans": balans,
        'User':user_

    }
    return render(request, 'balans.html', contex)
