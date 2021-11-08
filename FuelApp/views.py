from django.http.response import HttpResponse


from django.http import HttpResponse

def index(request):
    return HttpResponse("<center><h1>Please check the url in the petrol app</h1></center>")