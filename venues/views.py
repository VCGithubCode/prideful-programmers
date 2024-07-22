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
     
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          category = self.request.GET.get('category', 'Café')
          context['selected_category'] = category
          context['cafes'] = Venue.objects.filter(category='Café')
          context['clubs'] = Venue.objects.filter(category='Club')
          context['support_centers'] = Venue.objects.filter(category='Support Center')
          return context
       
class VenueDetail(generic.DetailView):
     """
     Venue detail view
     """
     model = Venue
     template_name = 'venue.html'
     queryset = Venue.objects.all()
     
     
