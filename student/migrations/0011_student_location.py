# Generated by Django 4.2 on 2023-05-18 15:50

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_remove_student_city_remove_student_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
