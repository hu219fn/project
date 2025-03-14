from django.forms import BaseModelForm
from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.forms import *
from app.models import *

def index(request):
    return render(request,'ar/index.html',{'products':Products.objects.all().order_by('-date')})

class SignupView(CreateView):
    model = User
    template_name = 'ar/auth/signup.html'
    form_class = SignupForm
    def form_valid(self, form):
        login(self.request, form.save())
        return redirect('/ar/')

@login_required
def Logout(request):
    logout(request)
    return render(request,'ar/auth/logout.html')

class Search(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'ar/search.html'
    def get_queryset(self):
        search = self.request.GET['search']
        return Products.objects.filter(title__icontains=search).order_by('-date')

def detail(request, id):
    item = Products.objects.get(id=id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            Order.objects.create(
                title=item.title,
                caption=item.caption,
                price=float(item.price) * int(request.POST['count']),
                sell=item.sell,
                category=item.category,
                photo=item.photo,
                count=request.POST['count'],
                number=id,
                user=request.user
            ).save()
            return redirect('/ar/orders/')
        else: 
            return render('')
    return render(request,'ar/detail.html',{'item':item})

@login_required
def orders(request):
    return render(request,'ar/orders.html',{'orders':Order.objects.filter(user=request.user).order_by('-date'),'count':Order.objects.filter(user=request.user).count()})

@login_required
def order_delete(request, id):
    order = Order.objects.get(id=id)
    if request.user == order.user :
        order.delete()
        return redirect('/ar/orders/')
    else:
        return redirect('/ar/orders/')

@login_required
def management(request):
    if request.user.username == 'alaa':
        return render(request,'ar/management.html',{'items':Products.objects.all().order_by('-date')})
    else:
        return redirect('/ar/')

@method_decorator(login_required, name='dispatch')
class Product_add(CreateView):
    model = Products
    fields = '__all__'
    template_name = 'ar/product_add.html'
    success_url = '/ar/'

@login_required
def product_order(request, id):
    if request.user.username == 'alaa':
        items = Order.objects.filter(number=id).order_by('-date')
        return render(request, 'ar/product_order.html', {'items':items,'count':items.count()})
    else:
        return redirect('/ar/')

@method_decorator(login_required, name='dispatch')
class Product_edit(UpdateView):
    model = Products
    fields = ['sell', 'photo']
    template_name = 'ar/product_edit.html'
    success_url = '/ar/management/'

@login_required
def product_delete(request, id):
    if request.user.username == 'alaa':
        item = Products.objects.get(id=id)
        orders = Order.objects.filter(number=id)
        if request.method == 'POST':
            item.delete()
            for order in orders:
                order.delete()
            return redirect('/ar/management/')
        return render(request, '/ar/product_delete.html')
    else:
        return redirect('/ar/')
    
    
###########
@login_required
def mini(request):
    return render(request, 'ar/categories/mini.html', {'products':Products.objects.filter(category='Mini').order_by('-date')})

@login_required
def classic(request):
    return render(request, 'ar/categories/classic.html', {'products':Products.objects.filter(category='Classic').order_by('-date')})

@login_required
def cards(request):
    return render(request, 'ar/categories/cards.html', {'products':Products.objects.filter(category='Cards').order_by('-date')})

@login_required
def wood(request):
    return render(request, 'ar/categories/wood.html', {'products':Products.objects.filter(category='Wood').order_by('-date')})

@login_required
def accessories(request):
    return render(request, 'ar/categories/accessories.html', {'products':Products.objects.filter(category='Accessories').order_by('-date')})

@login_required
def key_chain(request):
    return render(request, 'ar/categories/key_chain.html', {'products':Products.objects.filter(category='Key Chain').order_by('-date')})

@login_required
def phone_bag(request):
    return render(request, 'ar/categories/phone_bag.html', {'products':Products.objects.filter(category='Phone Bag').order_by('-date')})

def users(request):
    if request.user.username == 'alaa':
        return render(request, 'ar/users.html', {'users':User.objects.all()})
    else:
        return redirect('/ar/')
    
def users_delete(request, id):
    if request.user.username == 'alaa':
        item = User.objects.filter(id=id)
        if request.method == 'POST':
            item.delete()
            return redirect('/ar/management/users/')
        return render(request, 'ar/users_delete.html')
    else:
        return redirect('/ar/')
    
def user(request, id):
    if request.user.username == 'alaa':
        item = User.objects.get(id=id)
        orders = Order.objects.filter(user=item)
        return render(request, 'ar/user.html', {'item':item,'orders':orders})
    else:
        return redirect('/ar/')

@method_decorator(login_required, name='dispatch')
class Search_user(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'ar/users_search.html'
    def get_queryset(self):
        search = self.request.GET['search-user']
        return User.objects.filter(username__icontains=search)
    
@method_decorator(login_required, name='dispatch')
class Search_user0(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'ar/users_search.html'
    def get_queryset(self):
        search = self.request.GET['search-user0']
        return User.objects.filter(username__icontains=search)