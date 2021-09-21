from django.shortcuts import render
from .models import Course

# Create your views here.

def course_detail(request):
    return render(request, 'course-details.html')


def demo(request):
    data = Course.objects.all()
    return render(request, 'demo.html',{'data':data})
