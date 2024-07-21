from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Contact
from .forms import ContactForm

class ContactFormView(SuccessMessageMixin, CreateView):
    """
    Displays the contact form.
    """
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/thank-you'

    def form_valid(self, form):
        self.request.session['message_received'] = True
        return super().form_valid(form)
    
def thank_you(request):
    """
    Displays the thank you page after form submission.
    Redirects the user to the contact page if they 
    attempt to access the thank you page without 
    submitting the form.
    """
    if not request.session.get('message_received', False):
        return redirect('contact')
    
    request.session['message_received'] = False

    return render(request, 'thankyou.html')
