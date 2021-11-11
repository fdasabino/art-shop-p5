from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Render the homepage view
    """
    return render(request, "home/index.html")
