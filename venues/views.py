from django.shortcuts import render
from django.views import generic
from .models import Venue

class VenueList(generic.ListView):
     """
     Lists all venues
     """
     model = Venue
     template_name = 'venue_list.html'
     queryset = Venue.objects.all()
    
     
class VenueDetail(generic.DetailView):
     """
     Venue detail view
     """
     model = Venue
     template_name = 'venue.html'
     queryset = Venue.objects.all()
     
     
