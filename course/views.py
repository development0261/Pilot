from django.shortcuts import render
from .models import Course, City, Batch
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from datetime import date
from django.core.mail import send_mail


# Create your views here.


def course_detail(request):
    city_list = []
    for code in Batch.objects.all():
        city_list.append(code.id)
    for i in city_list:
        try:
            data = Batch.objects.get(id=i)
            end_date = data.batch_end_date
            today = date.today()
            if end_date < today:
                data.batch_status = False
                data.save()
            else:
                data.batch_status = True
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
        city_data = []
        for city in Batch.objects.all():
            city_data.append(
                {
                    "City_Name": city.batch_city.city_name,
                    "Starting_Date": city.batch_start_date,
                    "Ending_Date": city.batch_end_date,
                    "Status": city.batch_status,
                }
            )

        time_zone_data = []
        for location in city_data:
            if location["City_Name"] in [
                x.strip() for x in first_index.split(",")
            ]:
                try:
                    time_zone_data.append(
                        {
                            "City_Name": location[
                                "City_Name"
                            ],
                            "Starting_Date": location[
                                "Starting_Date"
                            ],
                            "Ending_Date": location[
                                "Ending_Date"
                            ],
                            "Status": location["Status"],
                        }
                    )
                except:
                    time_zone_data.append(
                        {
                            "City_Name": "Unknown",
                            "Starting_Date": "Unknown",
                            "Ending_Date": "Unknown",
                            "Status": "Unknown",
                        }
                    )
            else:
                time_zone_data.append(
                    {
                        "City_Name": "Unknown",
                        "Starting_Date": "Unknown",
                        "Ending_Date": "Unknown",
                        "Status": "Unknown",
                    }
                )

        print(
            "****************************", [x.strip() for x in first_index.split(",")]
        )
        print(
            "****************************", time_zone_data
        )

        return JsonResponse(
            {
                "data": time_zone_data,
            }
        )
