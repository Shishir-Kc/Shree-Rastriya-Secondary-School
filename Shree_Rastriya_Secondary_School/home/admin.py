from django.contrib import admin
from . import models

admin.site.register(models.Notice)
admin.site.register(models.Event)
admin.site.register(models.Teacher)
admin.site.register(models.Administrator)
admin.site.register(models.Scholarship)
admin.site.register(models.FeeStructure)


# student
 
admin.site.register(models.Class)
admin.site.register(models.StudentInfo)
admin.site.register(models.Subject)
admin.site.register(models.Enrollment)



#for Teacher 

admin.site.register(models.Notes)
