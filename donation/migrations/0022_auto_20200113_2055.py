# Generated by Django 2.2 on 2020-01-14 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0021_auto_20200109_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(default='default-ava.jpg', upload_to=''),
        ),
    ]
