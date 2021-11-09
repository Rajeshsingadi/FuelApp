from django.http.response import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string

from django.http import HttpResponse

def index(request):
    try:
        return HttpResponse("<center><h1>Please check the url in the petrol app</h1></center>")
    except:
        repsonse_data = render_to_string("404.html")
        return HttpResponseNotFound(repsonse_data)