# Generated by Django 5.1.5 on 2025-01-31 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_message_options_alter_message_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='email',
            field=models.CharField(default='user@gmail.com', max_length=50, verbose_name='Email'),
        ),
    ]
