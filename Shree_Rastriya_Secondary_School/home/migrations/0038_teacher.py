# Generated by Django 5.1.5 on 2025-01-29 11:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_delete_teacher'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.IntegerField()),
                ('subject', models.TextField()),
                ('teacher_image', models.ImageField(blank=True, upload_to='teacher_image')),
                ('classs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.class')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
