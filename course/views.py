from django.shortcuts import render
from geopy.adapters import AdapterHTTPError
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
        print(location.raw)
        raw_data = location.raw
        first_index = data[0]
        address = raw_data['address']
        check = [address[x] for x in address]
        print("Address ****************************",check)
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
        print("city_data ******",city_data)
        city_name_db = []
        for city_name in range(len(city_data)):
            if city_data[city_name]["City_Name"] in check:

                city_name_db.append({
                   "City_Name" : city_data[city_name]["City_Name"],
                    "Starting_Date": city_data[city_name]["Starting_Date"],
                    "Ending_Date" : city_data[city_name]["Ending_Date"],
                    "Status" : city_data[city_name]["Status"],
                })
            else:
                 city_name_db.append({
                   "City_Name" : "Unknown",
                    "Starting_Date": "Unknown",
                    "Ending_Date" : "Unknown",
                    "Status" : "Unknown",
                })
        
        print("city name database **************",city_name_db)


        time_zone_data = []
        for location in city_data:
            if location["City_Name"] in check:
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
                        "City_Name": "else",
                        "Starting_Date": "Unknown",
                        "Ending_Date": "Unknown",
                        "Status": "Unknown",
                    }
                )
                break

        course_detail = []

        print(time_zone_data[0]['City_Name'])
        for crs in Course.objects.all():
            if time_zone_data[0]['City_Name'] in crs.course_city.city_name:
                course_detail.append({
                    "course_img" : crs.course_image.url,
                    "course_title" : crs.course_title,
                    "course_description":crs.course_description,
                    "course_objective" :crs.course_objective,
                    "course_eligibility" :crs.course_eligibility,
                    "course_outline" :crs.course_outline,
                    "professionals_linkedIn" :crs.professionals_linkedIn,
                    "companies_linkedIn" : crs.companies_linkedIn,
                    "jobs":crs.jobs,
                    "LinkedIn_group_called":crs.LinkedIn_group_called,
                    "Facebook_group_called":crs.Facebook_group_called,
                    "Meetup_called":crs.Meetup_called,
                    "status" :crs.status,

                })
            else:
                course_detail.append({
                    "course_img" : "Unknown",
                    "course_title" : "Unknown",
                    "course_description":"Unknown",
                    "course_objective" :"Unknown",
                    "course_eligibility" :"Unknown",
                    "course_outline" :"Unknown",
                    "professionals_linkedIn" :"Unknown",
                    "companies_linkedIn" : "Unknown",
                    "jobs":"Unknown",
                    "LinkedIn_group_called":"Unknown",
                    "Facebook_group_called":"Unknown",
                    "Meetup_called":"Unknown",
                    "status" :"Unknown",

                })
        
                
        
        print(
            "****************************", time_zone_data
        )

        return JsonResponse(
            {
                "data": city_name_db,
                "course_detail" : course_detail,
            }
        )
