# Generated by Django 3.2.7 on 2021-10-01 07:09

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(blank=True, max_length=500, null=True, verbose_name='City Name')),
                ('country_code', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_image', models.ImageField(blank=True, null=True, upload_to='Course Image')),
                ('course_title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Course Title')),
                ('course_description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Course Description')),
                ('course_objective', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Course Objectives')),
                ('course_eligibility', models.TextField(blank=True, null=True, verbose_name='Who can take the course')),
                ('course_outline', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Course Outline')),
                ('professionals_linkedIn', models.URLField(blank=True, null=True, verbose_name='Blockchain Professionals in Seattle on LinkedIn')),
                ('companies_linkedIn', models.URLField(blank=True, null=True, verbose_name='Blockchain Companies in Seattle on LinkedIn')),
                ('jobs', models.URLField(blank=True, null=True, verbose_name='Blockchain Jobs in Seattle')),
                ('LinkedIn_group_called', models.URLField(blank=True, null=True, verbose_name='Join LinkedIn group called Blockchain in Seattle')),
                ('Facebook_group_called', models.URLField(blank=True, null=True, verbose_name='Join Facebook group called Blockchain in Seattle')),
                ('Meetup_called', models.URLField(blank=True, null=True, verbose_name='Join Meetup called Blockchain Meetup in Seattle')),
                ('status', models.BooleanField(default=False)),
                ('course_city', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.city', verbose_name='Course City')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_start_date', models.DateField(blank=True, null=True, verbose_name='Batch Starting Date')),
                ('batch_end_date', models.DateField(blank=True, null=True, verbose_name='Batch Ending Date')),
                ('batch_status', models.BooleanField(default=False)),
                ('batch_city', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.city', verbose_name='Batch For City')),
            ],
        ),
    ]
