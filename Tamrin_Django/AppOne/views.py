from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request=request , template_name="Home.html" , context={})