# Generated by Django 5.1.5 on 2025-02-05 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0055_alter_notes_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='teacher',
            new_name='user',
        ),
    ]
