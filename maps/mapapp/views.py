from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def map(request):
    return render(request,"mapapp/map.html")
def station(request):
    return render(request,"mapapp/station.html")   
def trends(request):
    return render(request,"mapapp/trends.html")
def park(request):
    return render(request,"mapapp/park.html")
def hotel(request):
    return render(request,"mapapp/hotel.html")
def church(request):
    return render(request,"mapapp/church.html")
