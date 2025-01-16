from django.contrib import admin
from . import models

admin.site.register(models.Notice)
admin.site.register(models.NoticeImage)
admin.site.register(models.Event)


