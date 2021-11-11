from django.shortcuts import redirect, render

# Create your views here.


def view_cart(request):
    """
    Render the items users added to cart
    """
    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """
    Add a quantity of the specified item to the shopping cart
    """
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    dimensions = None

    if "product_dimensions" in request.POST:
        dimensions = request.POST["product_dimensions"]
    cart = request.session.get("cart", {})

    if dimensions:
        if item_id in list(cart.keys()):
            if dimensions in cart[item_id]["items_by_dimension"].keys():
                cart[item_id]["items_by_dimension"][dimensions] += quantity
            else:
                cart[item_id]["items_by_dimension"][dimensions] = quantity
        else:
            cart[item_id] = {"items_by_dimension": {dimensions: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session["cart"] = cart
    return redirect(redirect_url)
