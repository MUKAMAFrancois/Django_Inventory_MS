# Generated by Django 4.1.3 on 2023-07-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='person.png', upload_to='Profile_Images'),
        ),
    ]
