# Generated by Django 5.1.5 on 2025-01-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_studentinfo_student_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='notes_pdfs/'),
        ),
    ]
