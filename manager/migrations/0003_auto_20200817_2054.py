# Generated by Django 3.0.8 on 2020-08-17 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_manager_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='answer',
            new_name='content',
        ),
    ]
