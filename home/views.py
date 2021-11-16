from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Render the homepage view
    """
    return render(request, "home/index.html")


def about(request):
    """
    Render the about view
    """
    return render(request, "home/about.html")


def contact(request):
    """
    Render the contact page view
    """
    return render(request, "home/contact.html")
