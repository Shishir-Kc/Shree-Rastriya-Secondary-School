from django.db import models
from django.contrib.auth.models import User


class Notice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notice_file = models.FileField(upload_to='notice_files', blank=True, null=True)
  
    def __str__(self):
        return self.title 


class NoticeImage(models.Model):
    notice = models.ForeignKey(Notice, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='notice_images')

    def __str__(self):
        return f"Image for {self.notice.title}"


class Event(models.Model):
    Title = models.CharField(max_length=100)
    date = models.DateField()
    Time = models.CharField(max_length=10)
    Location = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Title
