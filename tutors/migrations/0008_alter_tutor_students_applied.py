# Generated by Django 4.2 on 2023-05-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_student_location'),
        ('tutors', '0007_tutor_students_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='students_applied',
            field=models.ManyToManyField(related_name='applied_tutors', to='student.student'),
        ),
    ]
