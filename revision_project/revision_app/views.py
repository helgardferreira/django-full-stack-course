from django.shortcuts import render


# Create your views here.
def index(request):
    var_dict = {"greetings": "Hello I'm from firstapp!"}

    return render(request, "revision_app/index.html", context=var_dict)
