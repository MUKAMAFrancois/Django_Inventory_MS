# Generated by Django 4.1.3 on 2023-07-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='time_of_order',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='time_of_purchase',
            field=models.DateField(auto_created=True),
        ),
    ]
