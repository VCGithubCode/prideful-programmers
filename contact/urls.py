from . import views
from django.urls import path

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact'),
]