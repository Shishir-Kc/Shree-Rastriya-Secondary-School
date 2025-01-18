from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Notice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notice_image= models.ImageField(upload_to='notice_images',blank=True)
  
    def __str__(self):
        return self.title 



class Event(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    Title = models.CharField(max_length=100)
    date = models.DateField()
    Time = models.CharField(max_length=10)
    Location = models.CharField(max_length=100)
    Description = models.TextField()
      
    uploaded_date = models.DateTimeField(auto_now_add=True,)
    
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Title


class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
    subject = models.TextField()
    teacher_image = models.ImageField(upload_to='teacher_image',blank=True)

    def __str__(self):
        return self.name


class Administrator(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField(null=True,blank=True)
    Administrator_Role = models.CharField(max_length=100)

    def _str__(self):
        return self.Administrator_Role
    
class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    eligibility = models.TextField()
    deadline = models.DateField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FeeStructure(models.Model):
    faculty = models.CharField(max_length=255)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    admission_fee = models.DecimalField(max_digits=10, decimal_places=2)
    yearly_charges = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.faculty
    
class Gallery(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    image  = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
    