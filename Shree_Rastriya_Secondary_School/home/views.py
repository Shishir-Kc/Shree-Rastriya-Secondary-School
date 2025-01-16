from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required , permission_required



def home(request):
    data = models.Event.objects.all()
    context = {
        'events':data
    }
    return render(request,'home/home.html',context)

def user_login(request):
    if request.method == "POST":
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        user = authenticate(request,username=user_name,password=user_pass)
        if user is not None:
            login(request,user)
            return redirect('home:home')
    return render(request,'home/login.html')

def about_us(request):
    return render(request,'home/about.html')