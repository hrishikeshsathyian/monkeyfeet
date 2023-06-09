# Generated by Django 4.2 on 2023-05-05 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0009_alter_student_additional_information_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=50, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='users/profile_pictures')),
                ('address', models.CharField(max_length=250, null=True)),
                ('zip_code', models.CharField(max_length=6)),
                ('latitude', models.CharField(blank=True, max_length=50)),
                ('longitude', models.CharField(blank=True, max_length=50)),
                ('dob', models.DateField(null=True)),
                ('certificate_credential', models.FileField(blank=True, upload_to='users/tutors/certificate')),
                ('is_verified', models.BooleanField(default=False)),
                ('additional_information', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('subjects', models.ManyToManyField(to='student.subject')),
                ('tutor_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.tutorlevel')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
