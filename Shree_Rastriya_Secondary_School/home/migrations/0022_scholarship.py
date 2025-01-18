# Generated by Django 5.1.5 on 2025-01-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_delete_scholarship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('eligibility', models.TextField()),
                ('deadline', models.DateField()),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
