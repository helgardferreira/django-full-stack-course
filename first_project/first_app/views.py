from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    access_dict = {"access_records": webpages_list}

    return render(request, "first_app/index.html", context=access_dict)
