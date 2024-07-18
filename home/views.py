from django.shortcuts import render

# Renders the home page
def home(request):
    return render(request, 'index.html')
