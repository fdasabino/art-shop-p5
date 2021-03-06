from django.contrib import messages
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render, reverse
from products.models import Product

# Create your views here.


def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the shopping cart"""

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = request.POST["product_size"] if "product_size" in request.POST else None
    cart = request.session.get("cart", {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]["items_by_size"].keys():
                cart[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}',
                )
            else:
                cart[item_id]["items_by_size"][size] = quantity
                messages.success(request, f"Added size {size.upper()} {product.name} to your cart")
        else:
            cart[item_id] = {"items_by_size": {size: quantity}}
            messages.success(request, f"Added size {size.upper()} {product.name} to your cart")

    elif item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f"Updated {product.name} quantity to {cart[item_id]}")

    else:
        cart[item_id] = quantity
        messages.success(request, f"Added {product.name} to your cart")

    request.session["cart"] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = request.POST["product_size"] if "product_size" in request.POST else None
    cart = request.session.get("cart", {})

    if size:
        if quantity > 0:
            cart[item_id]["items_by_size"][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name} quantity to {cart[item_id]["items_by_size"][size]}',
            )

        else:
            del cart[item_id]["items_by_size"][size]
            if not cart[item_id]["items_by_size"]:
                cart.pop(item_id)
            messages.success(request, f"Removed size {size.upper()} {product.name} from your cart")
    elif quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f"Updated {product.name} quantity to {cart[item_id]}")
    else:
        cart.pop(item_id)
        messages.success(request, f"Removed {product.name} from your cart")

    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST["product_size"] if "product_size" in request.POST else None
        cart = request.session.get("cart", {})

        if size:
            del cart[item_id]["items_by_size"][size]
            if not cart[item_id]["items_by_size"]:
                cart.pop(item_id)
            messages.success(request, f"Removed size {size.upper()} {product.name} from your cart")
        else:
            cart.pop(item_id)
            messages.success(request, f"Removed {product.name} from your cart")

        request.session["cart"] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
