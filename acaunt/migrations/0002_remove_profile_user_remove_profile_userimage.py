# Generated by Django 4.2.7 on 2023-11-06 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acaunt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='userimage',
        ),
    ]
