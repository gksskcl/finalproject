from django.shortcuts import render, redirect
from .models import Final
# Create your views here.

def home(request):
    return render(request, 'final/home.html')

def new(request):
    return render(request, 'final/new.html')

def new1(request):
    return render(request, 'final/new1.html')

def new2(request):
    return render(request, 'final/new2.html')

def new3(request):
    return render(request, 'final/new3.html')

def new4(request):
    return render(request, 'final/new4.html')

def Africa(request):
    finals = Final.objects
    return render(request, 'final/Africa.html', {'finals':finals})

def Australia(request):
    finals = Final.objects
    return render(request, 'final/Australia.html', {'finals':finals})

def South_America(request):
    finals = Final.objects
    return render(request, 'final/South_America.html', {'finals':finals})

def North_America(request):
    finals = Final.objects
    return render(request, 'final/North_America.html', {'finals':finals})

def Europe(request):
    finals = Final.objects
    return render(request, 'final/Europe.html', {'finals':finals})

def create(request):
    final = Final()
    final.body = request.GET['body']
    final.save()
    return redirect("Europe")

def create1(request):
    final = Final()
    final.body1 = request.GET['body1']
    final.save()
    return redirect("Africa")

def create2(request):
    final = Final()
    final.body2 = request.GET['body2']
    final.save()
    return redirect("Australia")

def create3(request):
    final = Final()
    final.body3 = request.GET['body3']
    final.save()
    return redirect("North_America")

def create4(request):
    final = Final()
    final.body4 = request.GET['body4']
    final.save()
    return redirect("South_America")

