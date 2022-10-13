from numbers import Integral
import math
import stripe
import uuid 
from random import randrange
from decimal import Decimal
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Jewelry, Order, Topic, Comment, User, CartItem, Color, Tag
from .forms import  MyUserCreationForm, CartItemForm, EditProfileForm

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'home/login_register.html', context)

def logoutUser(request):
    
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'home/login_register.html', {'form': form})

def home(request):
    
    populars = Jewelry.objects.all().order_by('-views')[:5]
    topics = Topic.objects.all()
    
    context = {'populars': populars, 'topics' : topics}
    
    return render(request, 'home/index.html', context)

def products(request, pk):
    
    page_down = (int(pk) - 1) * 12
    page_up = int(pk) * 12

    
    q = request.GET.get('q')
    c = request.GET.get('c')
    h = request.GET.get('h')
    
    products_all = Jewelry.objects.all()
    
    if q != None:
        products = products_all.filter(Q(topics__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)).order_by('-updated')[page_down:page_up]
    elif c != None:
        products = products_all.filter(Q(color__name__icontains=c)).order_by('-updated')[page_down:page_up]
    elif h != None:
        products = products_all.filter(Q(tag__name__icontains=h)).order_by('-updated')[page_down:page_up]
    else:
        products = products_all.order_by('-updated')[page_down:page_up]
        
    product_count = products.count()

    topics = []
    colors = []
    
    tags = Tag.objects.all()
    
    for topic in Topic.objects.all():
        topics.append({"name":topic.name, "number": Jewelry.objects.filter(topics=topic).count()},)
        
    for color in Color.objects.all():
        colors.append({"name":color.name, "number": Jewelry.objects.filter(color=color).count()},)
    
    
    pages = math.ceil(product_count / 12)

    context = {'products': products, 'topics' : topics, 'product_count' : product_count, 'pages':pages, 'colors':colors, 'tags':tags}
    return render(request, 'home/products.html', context)

def product(request, pk):
    
    item = Jewelry.objects.get(id=pk)
    
    context = {'item':item}
    return render(request, 'home/product.html', context)

@login_required(login_url='login')
def cart(request):
    
    cart_items = CartItem.objects.filter(user=request.user)
    
    price = 0
    for cart_item in cart_items:
        price += cart_item.totalprice
        
    
    
    context = {'cart_items':cart_items, 'price':price}
    
    return render(request, 'home/cart.html', context)

def quantityadd(request, md):
    
    cart_item = CartItem.objects.get(id=md)
    cart_item.quantity += 1
    cart_item.totalprice = cart_item.Jewelry.price * cart_item.quantity
    
    cart_item.save()
    return redirect('cart')

def quantitysubs(request, md):
    cart_item = CartItem.objects.get(id=md)
    
    if cart_item.quantity > 1: 
        cart_item.quantity -= 1
        cart_item.totalprice = cart_item.Jewelry.price * cart_item.quantity
    else:
        pass
    
    cart_item.save()
    return redirect('cart')

@login_required(login_url='login')
def order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if cart_items.count() <= 0:
        return redirect('cart')
    
    price = 0
    
    for cart_price in cart_items:
        price += cart_price.totalprice
        
    price = price * 100
        
        

    if request.method == 'POST':
        
        stripe.api_key = 'sk_test_51Loj3zGcmIEJkd8G4SNblH61TGQTe9MCyQsLvsYQTzBolLLrLY1TcU9RSNMjq2YRLySwtf8dGu4LsSaP6wAFe0TM009O4eMvt4'
        token = request.POST['stripeToken']
        
        ordernumber = randrange(1000000000,9999999999)
    
        order = Order.objects.create(
            
            user = request.user,
            ordernumber = ordernumber,
            FirstName = request.POST['FirstName'],
            SecondName = request.POST['SecondName'],
            email = request.POST['email'],
            Address = request.POST['Address'],
            Country = request.POST['Country'],
            Zip = request.POST['Zip'],
            
            phonenumber = request.POST['phonenumber'],
        )    
        
        
        for cart_item in cart_items:
            order.ordered_items.add(cart_item.Jewelry.id)
            order.save()
            cart_item.delete()
    
        
        charge = stripe.Charge.create(
            amount=price,
            currency='eur',
            description='order number: ' + str(ordernumber),
            source=token,
        )
        

        return redirect('home')
        
        
    context = {'cart_items':cart_items}
    
    return render(request, 'home/order.html', context)

@login_required(login_url='login')
def addCart(request,pk):
    
    item = Jewelry.objects.get(id=pk)   
    
    if CartItem.objects.all():
        if CartItem.objects.filter(Jewelry__name__contains=item).exists():
            cart = CartItem.objects.get(Jewelry__name__contains=item)
        else:
            cart = ''
    else:
        cart = ''
    
    if cart:
        cart.quantity += 1
        cart.totalprice = cart.quantity * item.price
        cart.save()
    else:
        
        cartitem = CartItem.objects.create(
            
            user = request.user,
            Jewelry=item,
            totalprice = item.price
        )
    
    return redirect('cart')

@login_required(login_url='login')
def userProfile(request, pk):

    if str(request.user.id) != str(pk):
        return redirect('home')        

    profile = User.objects.get(id=pk)
    topics = Topic.objects.all()
    comments = Comment.objects.filter(user=profile)
    comments_count = comments.count()

    
    
    adats = [profile.first_name, profile.last_name, profile.email, profile.Country, profile.Address, profile.phonenumber, profile.avatar]
    filledadat = 0
    for i in adats:
        if i != '' or None:
            filledadat += 1
    filledadat =  math.ceil(filledadat / len(adats)  * 100)
    recommandations = Jewelry.objects.all()
    

    context = {'profile' : profile, 'topics' : topics, 'recommandations':recommandations, 'filledadat':filledadat, 'comments_count' : comments_count}
    return render(request, 'home/profile.html', context)

@login_required
def editProfile(request, pk):
    
    profile = User.objects.get(id=pk)
    
    if request.user != profile:
        return redirect('home')
    
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, files=request.FILES, instance=profile)
        
        form.save()
        return redirect('profile')
    
    context = {'profile':profile, 'form' : form}

    return render(request, 'home/edit.html', context)

@login_required(login_url='login')
def deleteComment(request,pk):
    
    comment = Comment.objects.get(id=pk)

    if request.user != comment.user:
        return redirect('home')
    
    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    
    context = {'obj' : comment}
    return render(request, 'home/delete.html', context)

@login_required(login_url='login')
def deleteItem(request,pk):
    
    item = CartItem.objects.get(id=pk)

    if request.user != item.user:
        return redirect('home')

    item.delete()
    

    
    return redirect('cart')