# Generated by Django 3.2.7 on 2021-09-21 11:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210921_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_objective',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Course Objectives'),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Course Description'),
        ),
    ]
