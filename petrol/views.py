from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    try:
        return render(request,"petrol/index.html")

    except:
        repsonse_data = render_to_string("404.html")
        return HttpResponseNotFound(repsonse_data)