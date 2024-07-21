from . import views
from django.urls import path

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('thank-you/', views.thank_you),
]