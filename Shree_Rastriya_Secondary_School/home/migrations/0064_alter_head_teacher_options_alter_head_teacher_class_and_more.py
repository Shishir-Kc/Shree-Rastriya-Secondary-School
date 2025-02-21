# Generated by Django 5.1.5 on 2025-02-21 10:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_alter_head_teacher_class_alter_head_teacher_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='head_teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Class_Teacher'},
        ),
        migrations.AlterField(
            model_name='head_teacher',
            name='Class',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.class', verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='head_teacher',
            name='Teacher',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.teacher', verbose_name='Teacher'),
        ),
    ]
