from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Makeyourorder
from django.contrib import messages

# Create your views here.
def makeyourorder(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        date = request.POST['date']

        makeyourorder = Makeyourorder.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message,
            date=date,
        )
        makeyourorder.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {name} for making an appointment - {phone} - {message}")
        return HttpResponse("request.path successfully")

    return render(request,'makeyourorder.html', {})

"""
#eldahfxb_rest5	user:hudaismail pw:hudaismail1234 mysql namecheap user:eldahfxb_hudaismail Database: eldahfxb_rest5

import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'manage/wsgi.py')
application = wsgi.application
"""