# Generated by Django 4.2.7 on 2023-11-26 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acaunt', '0005_masseges'),
    ]

    operations = [
        migrations.RenameField(
            model_name='masseges',
            old_name='content',
            new_name='text',
        ),
    ]