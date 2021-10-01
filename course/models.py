from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class City(models.Model):
    city_name = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="City Name",
    )
    country_code = models.CharField(
        max_length=200, null=True, blank=True
    )

    def __str__(self):
        return self.city_name


class Course(models.Model):
    course_city = models.OneToOneField(City, unique=True,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Course City")
    course_image = models.ImageField(
        upload_to="Course Image", null=True, blank=True
    )
    course_title = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Course Title",
    )
    course_description = HTMLField(
        null=True,
        blank=True,
        verbose_name="Course Description",
    )
    course_objective = HTMLField(
        null=True,
        blank=True,
        verbose_name="Course Objectives",
    )
    course_eligibility = models.TextField(
        null=True,
        blank=True,
        verbose_name="Who can take the course",
    )
    course_outline = HTMLField(
        null=True, blank=True, verbose_name="Course Outline"
    )
    professionals_linkedIn = models.URLField(
        null=True,
        blank=True,
        verbose_name="Blockchain Professionals in Seattle on LinkedIn",
    )
    companies_linkedIn = models.URLField(
        null=True,
        blank=True,
        verbose_name="Blockchain Companies in Seattle on LinkedIn",
    )
    jobs = models.URLField(
        null=True,
        blank=True,
        verbose_name="Blockchain Jobs in Seattle",
    )
    LinkedIn_group_called = models.URLField(
        null=True,
        blank=True,
        verbose_name="Join LinkedIn group called Blockchain in Seattle",
    )
    Facebook_group_called = models.URLField(
        null=True,
        blank=True,
        verbose_name="Join Facebook group called Blockchain in Seattle",
    )
    Meetup_called = models.URLField(
        null=True,
        blank=True,
        verbose_name="Join Meetup called Blockchain Meetup in Seattle",
    )
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.course_title


class Batch(models.Model):
    batch_city = models.OneToOneField(
        City,
        unique=True,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Batch For City",
    )
    batch_start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Batch Starting Date",
    )
    batch_end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Batch Ending Date",
    )
    batch_status = models.BooleanField(default=False)

    def __str__(self):
        return self.batch_city.city_name
