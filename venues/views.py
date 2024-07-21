from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Venue

class VenueList(generic.ListView):
     """
     Lists all venues
     """
     model = Venue
     template_name = 'venue_list.html'
     
     def get_queryset(self):
          return Venue.objects.all()
     
     def get_context(self, **kwargs):
          context = super().get_conext_data(**kwargs)
          categories = [choice[0] for choice in Venue.CATEGORY]
          venue_category = {
               category: self.get_queryset().filter(category=category) for category in categories
               }
          
          context['categories'] = categories
          context['venue_category'] = venue_category
          return context
    
     
class VenueDetail(generic.DetailView):
     """
     Venue detail view
     """
     model = Venue
     template_name = 'venue.html'
     queryset = Venue.objects.all()
     
     
