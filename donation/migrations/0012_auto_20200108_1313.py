# Generated by Django 2.2 on 2020-01-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0011_challenges_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='status',
            field=models.CharField(default=('A', 'Active'), max_length=20),
        ),
    ]
