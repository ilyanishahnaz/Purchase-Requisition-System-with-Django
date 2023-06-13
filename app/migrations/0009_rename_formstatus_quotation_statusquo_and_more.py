# Generated by Django 4.1.4 on 2023-01-09 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_vendor_contactnum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation',
            old_name='formStatus',
            new_name='StatusQuo',
        ),
        migrations.AlterField(
            model_name='quotation',
            name='purchaserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.purchaser'),
        ),
    ]
