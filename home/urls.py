from . import views
from django.urls import path
# from .views import test_500

urlpatterns = [
    # path('test-500/', views.test_500),
    path('', views.home, name='home')
]