from django.db import models
from tinymce.models import HTMLField

# Create your models here.

CHOICES_CITY = (
    ("Seattle", "Seattle"),
    ("New York", "New York"),
    ("Philadelphia", "Philadelphia"),
    ("Boston", "Boston"),
    ("Chicago", "Chicago"),
    ("Los Angeles", "Los Angeles"),
    ("San Diego", "San Diego"),
    ("Dallas", "Dallas"),
    ("Houston", "Houston"),
    ("Atlanta", "Atlanta"),
    ("Miami", "Miami"),
)


class Course(models.Model):
    city_name = models.CharField(
        max_length=100,
        choices=CHOICES_CITY,
        default=CHOICES_CITY[0],
        verbose_name="City Name",
    )
    course_title = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name="Course Title",
    )
    course_start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Course Starting Date",
    )
    course_end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Course Ending Date",
    )
    course_image = models.ImageField(
        upload_to="Course Image", null=True, blank=True
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
