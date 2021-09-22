from django.shortcuts import render
from .models import Course, CHOICES_CITY
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.template.loader import render_to_string


# Create your views here.


def course_detail(request):
    data = Course.objects.all()
    return render(
        request, "course-details.html", {"data": data}
    )


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
