from django.shortcuts import render

# Renders the home page
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


# Custom 404 error page view
def custom_404(request, exception):
    return render(request, '404.html', status=404)

# Custom 500 error page view
def custom_500(request):
    return render(request, '500.html', status=500)

# def test_500(request):
    # raise Exception("Test 500 error")
