from django.db import models
from django.contrib.auth.models import User


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
    

# Test code are Below ! 


class Subject(models.Model):
    name = models.CharField(max_length=50, verbose_name="Subject Name")
    is_specialized = models.BooleanField(default=False, verbose_name="Is Specialized Subject?")

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class Class(models.Model):
    GRADE_CHOICES = [(i, f"Grade {i}") for i in range(1, 13)]  
    grade = models.PositiveIntegerField(choices=GRADE_CHOICES, verbose_name="Grade/Class")
    section = models.CharField(max_length=30, verbose_name="Section")
    subjects = models.ManyToManyField(Subject, verbose_name="Subjects")

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        unique_together = ('grade', 'section')

    def get_subjects(self):
     
        if self.grade <= 10:
            return self.subjects.filter(is_specialized=False)
        return self.subjects.filter(is_specialized=True)

    def __str__(self):
        return f"Grade {self.grade} - Section {self.section}"



class Teacher(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20)
    contact = models.IntegerField()
    subject = models.ManyToManyField(Subject)
    classs = models.ManyToManyField(Class)
    email = models.EmailField(("Email Address"), max_length=254,  default="user@gmail.com" )
  
    teacher_image = models.ImageField(upload_to='teacher_image',blank=True)

    def __str__(self):
        return self.name


class StudentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Associated User")
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.CharField(max_length=20, verbose_name="Last Name")
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number")
    profile_picture = models.ImageField(upload_to='student_profiles', blank=True, verbose_name="Profile Picture")
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE,default=1)
    class Meta:
        verbose_name = "Student Info"
        verbose_name_plural = "Student Infos"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Enrollment(models.Model):
    student = models.OneToOneField(StudentInfo, on_delete=models.CASCADE, verbose_name="Student")
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name="Enrolled Class")

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} in {self.enrolled_class}"



class Notes(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': "Teacher"})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    classs = models.ForeignKey(Class, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='notes_pdfs', null=True, blank=True)


    def __str__(self):
        return f"{self.title} - {self.classs} - {self.subject}"
    
