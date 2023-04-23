# Generated by Django 4.2 on 2023-04-19 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_additional_information_student_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='longitude',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='preferred_gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('NO PREFERENCE', 'NO PREFERENCE')], max_length=50, null=True),
        ),
    ]
