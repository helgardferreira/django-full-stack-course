from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    template_vars = {"insert_me": "Hello I am from first_app/views.py!"}
    return render(request, "first_app/index.html", context=template_vars)
