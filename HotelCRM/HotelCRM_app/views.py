from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request)
    return render(request, 'about.html')

def booking(request)
    return render(request, 'booking.html')

def contact(request)
    return render(request, 'contact.html')
    
def destination(request)
    return render(request, 'destination.html')

def home(request)
    return render(request, 'home.html')
        
def package(request)
    return render(request, 'package.html')

def service(request)
    return render(request, 'service.html')

def team(request)
    return render(request, 'team.html')

def testimonial(request)
    return render(request, 'testimonial.html')
