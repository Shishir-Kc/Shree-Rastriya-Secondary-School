# Generated by Django 5.1.5 on 2025-01-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_other_charges_eduaction_year_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduaction',
            name='description',
            field=models.TextField(default=1),
        ),
    ]
