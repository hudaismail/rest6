from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib import messages
import json
from .utils import cookieCart, cartData, guestOrder
import datetime
from django.core.mail import send_mail

# Create your views here.

def index(request):
    data = cartData(request)
    cartItems = data['cartItems']

    ducts = Products.objects.all()
    return render(request,'index.html', {'ducts': ducts, 'cartItems': cartItems})


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request, 'cart.html', {'items': items, 'order': order, 'cartItems': cartItems})


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    return render(request, 'checkout.html', {'items': items, 'order': order, 'cartItems': cartItems})

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItems.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item Was Added successfully', safe=False)


def processOrder(request):

    transaction_id = datetime.datetime.now().timestamp()
    print('Data:', request.body)

    data = json.loads(request.body)

    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            phone=data['shipping']['phone'],

        )

    return JsonResponse('Payment Complete!', safe=False)



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        product = Products.objects.filter(name__contains=searched)
        return render(request, 'search.html', {'searched': searched, 'product': product})
    else:
        return render(request, 'search.html', {})


def category(request,foo):
    # replace hyphens with spaces
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Products.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, ("That category dosn't exist"))
        return redirect('index')
"""
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request, 'checkout.html', {'items': items, 'order': order, 'cartItems': cartItems})

"""



def home(request):
    data = cartData(request)
    cartItems = data['cartItems']

    ducts = Products.objects.all()
    return render(request, 'home.html', {'ducts': ducts, 'cartItems': cartItems})


def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
           New message :{}
           From :{}
           '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['enghudaismail@gmail.com'])
        reply_to = [email]
        print('send Success')
        return HttpResponse("email send Successfully")

    return render(request, 'contact.html', {})




