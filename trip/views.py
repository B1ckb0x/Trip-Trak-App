from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.contrib.auth import logout


# Create your views here.
class HomeView(TemplateView):
    template_name = 'trip/index.html'


def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips' : trips
    }
    return render(request, 'trip/trips_list.html', context)


def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
