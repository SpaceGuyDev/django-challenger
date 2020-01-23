# Generated by Django 2.2 on 2020-01-07 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0006_challenges_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenges',
            old_name='donatorApproved',
            new_name='donator_approved',
        ),
        migrations.RenameField(
            model_name='challenges',
            old_name='priceGoal',
            new_name='price_goal',
        ),
        migrations.RenameField(
            model_name='challenges',
            old_name='priceReached',
            new_name='price_reached',
        ),
        migrations.RenameField(
            model_name='challenges',
            old_name='proofImg',
            new_name='proof_img',
        ),
        migrations.RenameField(
            model_name='challenges',
            old_name='proofVideo',
            new_name='proof_video',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='profilePhoto',
            new_name='profile_photo',
        ),
    ]
