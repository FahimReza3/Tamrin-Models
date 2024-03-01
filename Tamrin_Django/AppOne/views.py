from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.

def Home(request):
    return render(request=request , template_name="Home.html" , context={})

def AddUser(request):
    data=User(Name="FahimReza" , Family="Hosseini" , Email="FahimReza20200@gmail.com" , Password="Fahim123")
    data.save()
    return HttpResponse("User Add Shod")

def UserAll(request):
    AllData=User.objects.all()
    return render(request=request , template_name="AllUser.html" , context={"AllData" : AllData})