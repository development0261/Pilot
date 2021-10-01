# Generated by Django 3.2.7 on 2021-10-01 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_course_course_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_city',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.city', verbose_name='Course City'),
        ),
    ]
