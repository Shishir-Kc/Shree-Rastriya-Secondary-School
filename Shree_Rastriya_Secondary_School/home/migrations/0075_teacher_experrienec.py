# Generated by Django 5.1.7 on 2025-03-27 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0074_remove_teacher_fcm_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='experrienec',
            field=models.IntegerField(default=0),
        ),
    ]
