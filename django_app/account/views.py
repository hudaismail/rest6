from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .helpers import send_forgot_password_mail
import uuid
from .models import Profile


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('login')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name )
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.info(request,'password not matching....')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not User.objects.filter(username=username):
            messages.success(request,'No user found with this username')
            return redirect('/forgot_password')

        username = User.objects.get(username=username)
        token = str(uuid.uuid4())
        send_forgot_password_mail(username,token)
        messages.success(request,'An email is sent')
        return redirect('/login')
    return render(request,'password_reset_confirm.html')

def reset_password(request):
    context = {}
    try:
        token = str(uuid.uuid4())
        profile = Profile.objects.filter(forgot_password_token=token)
        print(profile)
    except Exception as e:
        print(e)
        return render(request,'password_change.html')

def password_reset_confirm(request):
    return render(request,'password_reset_confirm.html')

def password_reset_complete(request):
    return render(request,'password_reset_complete.html')

#def password_reset_sent(request):
    #return render(request,'password_reset_sent.html')

def password_reset_email(request):
    return render(request,'password_reset_email.html')

def password_reset_form(request):
    return render(request, 'password_reset_form.html')

