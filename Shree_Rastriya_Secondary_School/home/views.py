from django.shortcuts import render
from django.http import HttpResponse
from . import models



def home(request):
    data = models.Event.objects.all()
    context = {
        'events':data
    }
    return render(request,'home/home.html',context)

def user_login(request):
    return render(request,'home/login.html')

def about_us(request):
    return render(request,'home/about.html')