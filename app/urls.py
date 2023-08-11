from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('birthday', views.birthday, name='birthday'),
    path('gate', views.gate, name='gate'),
    path('canopy', views.canopy, name='canopy'),
    path('babyshower', views.babyshower, name='babyshower'),
    path('festivals', views.festivals, name='festivals'),
    path('events', views.events, name='events'),
]