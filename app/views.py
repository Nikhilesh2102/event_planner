from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def birthday(request):
    return render(request, 'birthday.html')

def babyshower(request):
    return render(request, 'babyshower.html')

def canopy(request):
    return render(request, 'canopy.html')

def gate(request):
    return render(request, 'gate.html')

def festivals(request):
    return render(request, 'festivals.html')

def events(request):
    return render(request, 'events.html')
