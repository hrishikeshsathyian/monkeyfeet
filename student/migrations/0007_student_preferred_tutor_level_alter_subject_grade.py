# Generated by Django 4.2 on 2023-04-20 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_tutorlevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='preferred_tutor_level',
            field=models.ManyToManyField(to='student.tutorlevel'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='grade',
            field=models.CharField(choices=[('Primary 1', 'Primary 1'), ('Primary 2', 'Primary 2'), ('Secondary 1', 'Secondary 1'), ('Secondary 2', 'Secondary 2')], max_length=50),
        ),
    ]
