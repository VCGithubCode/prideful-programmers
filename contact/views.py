from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Contact
from .forms import ContactForm

class ContactFormView(SuccessMessageMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'
    success_message = 'Your message has been received.'

    def form_valid(self, form):
        return super().form_valid(form)
