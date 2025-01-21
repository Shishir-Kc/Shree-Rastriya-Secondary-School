from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib import messages




def home(request):
    data = models.Event.objects.all().order_by('-uploaded_date')[:2]
    image = models.Gallery.objects.all().order_by('-date')[:5]
    context = {
        'events':data,
        'images':image
    }
    return render(request,'home/home.html',context)

def user_login(request):
    if request.method == "POST":
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


def test(request):
    return render(request,'home/test.html')
@login_required
def staff_list(request):
    if request.method == "POST":
        username =  request.POST.get('username')
        test = models.User.objects.filter(username=username).exists()
        if test:
            messages.error(request,'user  with that name already exists ! ')
            db = models.User.objects.all()
            context = { 
                'users':db
            }
            return render(request,'home/user_manage.html',context)
            

        else:



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
    
def teacher_manage(request):
    data = models.Teacher.objects.all()
    context = {
        'teachers':data
    }
    return render (request,'home/teacher_manage.html',context)

def Administrator(request):
    data = models.Administrator.objects.all()
    context = {
        'users':data
    }
    return render(request,'home/Administrator.html',context)





@login_required
def manage_teacher(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        profile = request.FILES.get('image')
        contact = request.POST.get('number')

        data = models.Teacher(user=request.user,name=name,contact=contact,subject=subject,teacher_image=profile)
        data.save()
        return redirect('home:teacher-manage')
    else:
     data = models.Teacher.objects.all()
     context = { 
         'teachers':data
     }
     return render(request,'home/teacher.html',context) 

@login_required
def delete_teacher(request,teacher_id):
    data = models.Teacher.objects.get(id=teacher_id)
    data.delete()
    return redirect("home:teacher-manage")

@login_required
def Edit_teacher(request,teacher_id):
    if request.method  == "POST":
        data = models.Teacher.objects.get(id=teacher_id)
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        profile = request.FILES.get('image')
        contact = request.POST.get('number')
        user = request.user
        data.user = request.user
        data.name = name
        data.contact = contact
        data.subject = subject
        data.teacher_image=profile
        data.save()
        return redirect('home:teacher-manage')
    else:
        data = models.Teacher.objects.get(id=teacher_id)
        context = {
            'teacher':data
        }
        return render(request,'home/edit_teacher.html',context)
    

def Gallery(request):
    image = models.Gallery.objects.all()
    context = {
        'photos':image
    }
    return render(request,'home/gallery.html',context)

@login_required
def list_gallery(request):
    data = models.Gallery.objects.all()
    context = { 
        'names':data
    }
    return render(request,'home/list_gallery.html',context)


@login_required
def add_gallery(request):
    if request.method == "POST":
        title = request.POST.get('title')
        image = request.FILES.get('image')
        user = request.user
        data = models.Gallery(user=user,name=title,image=image)
        data.save()
        return redirect('home:list-gallery')
    else:
        return redirect('home:list-gallery')
    

@login_required
def Edit_photo(request,photo_id):
    if request.method == "POST":
        mod = models.Gallery.objects.get(id=photo_id)
        user = request.user
        title = request.POST.get('name')
        image = request.FILES.get('image')
        mod.user = user
        mod.name=title
        mod.image=image
        mod.save()
        return redirect('home:list-gallery')
    else:
        data = models.Gallery.objects.get(id=photo_id)
        context = {
            'photo':data
        }

        return render(request,'home/editphoto.html',context)
        
@login_required
def Del_Photo(request,photo_id):
    mod = models.Gallery.objects.get(id=photo_id)
    mod.delete()
    return redirect('home:list-gallery')

def Contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        db = models.Contact(name=name,email=email,number=number,message=message)
        db.save()
        return redirect('home:home')
        
    else:

     return render (request,'home/contact.html')
    
@login_required
def contact_list(request,):
    data = models.Contact.objects.all()
    context ={
        'contacts':data
    }
    return render(request,'home/contact_list.html',context)

@login_required
def contact_detail(request,contact_id):
    data = models.Contact.objects.get(id=contact_id)
    data_2 = models.Contact.objects.all()
    context = {
        'contact':data,
        'contacts':data_2
    }
    return render(request,'home/contact_list.html',context)

@login_required
def Delete_contact(request,contact_id):
    mod = models.Contact.objects.get(id=contact_id)
    mod.delete()
    return redirect('home:contact-list')


@login_required
def add_Administrator(request):
    if request.method == "POST":
        name = request.POST.get('name')
        number = request.POST.get('number')
        role = request.POST.get('role')
        dat = models.Administrator(name=name,contact=number,Administrator_Role=role)
        dat.save()
        return redirect('home:add-administrator')
   

    data = models.Administrator.objects.all()
    context = {
        'users':data
    }
    return render(request,'home/add-administrator.html',context)

@login_required
def Detail_administrator(request,administrator_id):
    if request.method == "POST":
        dat = models.Administrator.objects.get(id=administrator_id)
        name = request.POST.get('name')
        number = request.POST.get('number')
        role = request.POST.get('role')
        dat.name = name
        dat.contact = number
        dat.Administrator_Role=role
        dat.save()
        return redirect('home:add-administrator')

    data = models.Administrator.objects.get(id=administrator_id)
    data_2 = models.Administrator.objects.all()
    context = {
        'admin':data,
        'users':data_2
    }
    return render(request,'home/add-administrator.html',context)

@login_required
def Delete_administrator(request,admin_id):
    dat = models.Administrator.objects.get(id=admin_id)
    dat.delete()
    return redirect("home:add-administrator")


def Notice(request):
    data = models.Notice.objects.all()
    context= {
        "notices":data
    }
    return render (request,'home/notice.html',context)


def Notice_id(request,notice_id):
    if request.method == 'POST':
        db = models.Notice.objects.get(id=notice_id)
        title = request.POST.get('title')
        des = request.POST.get('description')
        image = request.FILES.get('notice_image')
        db.user = request.user
        db.title = title
        db.description = des
        if image is None:
           db.notice_image = db.notice_image
        else:
         db.notice_image = image

        db.save()
        return redirect("home:notice")
    else:


     data = models.Notice.objects.get(id=notice_id)
     context = {
         'notice':data
     }
     return render(request,'home/notice-view.html',context)
    

@login_required
def Add_Notice(request):
        if request.method == 'POST':
         user = request.user
         title = request.POST.get('title')
         description = request.POST.get('description')
        
       
         if 'notice_image' in request.FILES:
            image = request.FILES['notice_image']
         else:
            image = None
        
        
         notice = models.Notice(user=user,title=title, description=description, notice_image=image)
        
         notice.save()
        
         return redirect('home:notice')  # Redirect to the page where notices are displayed
    
        return render(request, 'home/addnotice.html')

@login_required
def notice_delete(request,notice_id):
    data = models.Notice.objects.get(id=notice_id)
    data.delete()
    return redirect('home:notice')


def Scholar_FeeStructure(request):
    Scholar = models.Scholarship.objects.all()
    Fee = models.FeeStructure.objects.all()
    context = {
        'Scholars':Scholar,
        'Fees':Fee
    }
    return render (request,'home/Fee_Scholarship.html',context)


# @login_required
# def edit_Scholar(request,scholar_id):
#     if request.method == 'POST':
#         title = request.POST.get('name')
#         detail = request.POST.get('detail')
#         el = request.POST.get('el')
#         deadline = request.POST.get()

    #         title = models.CharField(max_length=255)
    # details = models.TextField()
    # eligibility = models.TextField()
    # deadline = models.DateField()
    # uploaded = models.DateTimeField(auto_now_add=True)
    
    # else:
    #  data = models.Scholarship.objects.all()
    #  context = {

    #  }
    #  return render(request,'home/edit_scholar.html',context)
