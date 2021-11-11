from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """
    Render the items users added to cart
    """
    return render(request, "cart/cart.html")
