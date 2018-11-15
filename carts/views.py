from django.shortcuts import render, HttpResponseRedirect, reverse
# from django.core.urlresolvers import reverse

# Create your views here.
from .models import Cart, CartItem
from mainapp.models import Product

def view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None

    if the_id:
        cart = Cart.objects.get(id=the_id)
        context = {"cart": cart}
    else:
        context = {"empty": True, "msg": "Your cart is Empty"}
    return render(request, "carts/view.html", context)


def update_cart(request, slug):
    request.session.set_expiry(1800)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if created:
        print("created")

    if update_qty and qty:
        if int(qty) == 0:
            cart_item.delete()
        else:
            cart_item.quantity = qty
            cart_item.save()
    else:
        pass

    # if not cart_item in cart.items.all():
    #     cart.items.add(cart_item)
    # else:
    #     cart.items.remove(cart_item)

    new_total = 0.00
    for item in cart.cartitem_set.all():
        total_for_product = float(item.product.price) * item.quantity
        new_total += total_for_product

    request.session['items_total'] = cart.cartitem_set.count()
    cart.total = new_total
    cart.save()
    return HttpResponseRedirect(reverse("carts:cart"))
