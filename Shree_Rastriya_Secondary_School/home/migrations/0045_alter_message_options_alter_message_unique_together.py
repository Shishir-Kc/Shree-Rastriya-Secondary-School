# Generated by Django 5.1.5 on 2025-01-30 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set(),
        ),
    ]
