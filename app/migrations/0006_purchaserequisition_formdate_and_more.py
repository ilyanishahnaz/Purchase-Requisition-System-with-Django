# Generated by Django 4.1.4 on 2023-01-09 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_financeofficer_vendor_alter_item_item_id_quo_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserequisition',
            name='formDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='purchaserequisition',
            name='requiredBy',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
