from django.contrib import admin
from . import models

admin.site.register(models.Notice)
admin.site.register(models.Event)
admin.site.register(models.Teacher)
admin.site.register(models.Administrator)
admin.site.register(models.Scholarship)
admin.site.register(models.FeeStructure)


# student
 
admin.site.register(models.Classes)
admin.site.register(models.Student_info)
admin.site.register(models.Subjects)
admin.site.register(models.Students)
