# Generated by Django 4.2 on 2023-05-05 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_student_additional_information_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='city',
        ),
        migrations.RemoveField(
            model_name='student',
            name='country',
        ),
        migrations.RemoveField(
            model_name='student',
            name='state',
        ),
    ]
