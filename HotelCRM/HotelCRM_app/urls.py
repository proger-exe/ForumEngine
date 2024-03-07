from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('booking', views.booking, name='booking'),
    path('contact', views.contact, name='contact'),
    path('destination', views.destination, name='destination'),
    path('home', views.home, name='home'),
    path('package', views.package, name='package'),
    path('service', views.service, name'service'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial name='testimonial'),
    
]
git                                                