from django.shortcuts import render
from .models import Course, Country, City
from django.views.decorators.csrf import csrf_exempt
from geopy.geocoders import Nominatim
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from datetime import date
from django.core.mail import send_mail


# Create your views here.


def course_detail(request):
    city_list = []
    for code in Country.objects.all():
        city_list.append(code.country_name)
    for i in city_list:
        try:
            data = Country.objects.get(
                country_name=i
            )
            end_date = data.ending_date
            today = date.today()
            if end_date < today:
                data.cont_status = False
                data.save()
            else:
                data.cont_status = True
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
        raw_data = location.raw
        address = raw_data['address']
        country_code = address['country_code']
        converted_country_code = country_code.upper()  # Country code from live location

        first_index = data[0]

        data_country = []  # Data of st_date, end_date, cntry_code after matching Country code
        db_code = Country.objects.all()
        for k in db_code:
            if k.country_name == converted_country_code:
                try:
                    data_country.append({
                        "Country_code": k.country_name,
                        "Starting_date": k.start_date,
                        "Ending_Date": k.ending_date,
                        "Status" : k.cont_status,
                    })
                    break
                except:
                    data_country.append({
                        "Country_code": "Country_code",
                        "Starting_date": "Starting_date",
                        "Ending_Date": "Ending_Date",
                        "Status": "Status",
                    })

            else:
                pass

        city_name = []  # City Name According Live Location
        city_data = City.objects.all()

        for j in city_data:
            if j.city_name in list(first_index.split(',')):
                try:
                    city_name.append({
                        "City_name": j.city_name,
                        "Country_Code": j.country_code
                    })
                except:
                    city_name.append({
                        "City_name": "City_name",
                        "Country_Code": "Country_Code"
                    })

        print(city_name)
        print(data_country)
        check = []
        print("*/***************")
        print(len(data_country[0]["Country_code"]))
        print(len(city_name[0]["Country_Code"]))
        if data_country[0]["Country_code"] == city_name[0]["Country_Code"]:

            check.append({
                "country_code": data_country[0]["Country_code"],
                "st_date": data_country[0]["Starting_date"],
                "end_date": data_country[0]["Ending_Date"],
                "city_name": city_name[0]["City_name"],
                "status": data_country[0]["Status"],
            })

        return JsonResponse(
            {
                "data": check[0],
            }
        )
