from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = {"greeting":"สวัสดี"}
    data["price"] = 3000
    return render(request, "home.html")
# Create your views here.
