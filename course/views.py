from django.shortcuts import render
from .models import Course, CHOICES_CITY
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from datetime import date
from django.core.mail import send_mail

# Create your views here.


def course_detail(request):
    city_list = [
        "Surat",
        "Valsad",
        "Kolkata",
        "Seattle",
        "Unknown",
        "New York City",
        "Miami",
        "Philadelphia",
        "Houston",
        "Atlanta",
        "Boston",
        "Chicago",
        "Los Angeles",
        "Dallas",
        "San Diego",
    ]
    for i in city_list:
        try:
            data = Course.objects.get(
                course_city__city_name=i
            )
            end_date = data.course_end_date
            today = date.today()
            if end_date < today:
                data.status = False
                data.save()
            else:
                data.status = True
                data.save()
        except:
            pass
    return render(request, "course-details.html")


@csrf_exempt
def comments(request):
    if request.method == "POST":
        email = request.POST.get("email")
        comments = request.POST.get("comments")
        from_email = "development0261@gmail.com"
        send_mail(
            f"Contact You from {email}",
            comments,
            email,  # FROM
            [from_email],  # TO
            fail_silently=False,
        )
        return JsonResponse({"data": "Success"})


def demo(request):
    return render(request, "demo.html")


@csrf_exempt
def ajax_filter(request):
    if request.method == "POST":
        lat = request.POST.get("latitude")
        lon = request.POST.get("longitude")
        locator = Nominatim(user_agent="myGeocoder")
        coordinates = "{}, {}".format(lat, lon)
        location = locator.reverse(coordinates)
        data = list(location)
        first_index = data[0]
        split = first_index.split(",")

        city_list = [
            "Surat",
            "Valsad",
            "Kolkata",
            "Unknown",
            "New York City",
            "Miami",
            "Philadelphia",
            "Houston",
            "Atlanta",
            "Boston",
            "Chicago",
            "Los Angeles",
            "Dallas",
            "San Diego",
        ]

        first_add = split[0]
        second_add = split[1]
        print("**********")
        print("**********")
        print(first_index)
        print(first_add)
        print(second_add)
        print("**********")
        print("**********")
        check = [i for i in city_list if i in first_index]
        if check:
            data = Course.objects.get(
                course_city__city_name__in=check
            )
            data_check = serializers.serialize(
                "json", [data], ensure_ascii=False
            )
            return JsonResponse(
                {
                    "data": data_check,
                    "first_index": first_index,
                }
            )

        else:
            return JsonResponse({"data": "Unknown"})
