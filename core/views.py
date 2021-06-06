from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .models import Item, OrderItem, Order
from django.views.generic import DetailView
from django.utils import timezone
from django.contrib import messages


def product(request):
    items = Item.objects.all().exclude(quantity_type='Bags')[0:6]
    items2 = Item.objects.all()[6:]
    items_bags = Item.objects.filter(quantity_type='Bags')[0:6]
    context = {
        'items': items,
        'items2': items2,
        'items_bags': items_bags
    }
    return render(request, "core/product.html", context)


class ProductDetailView(View):

    def get(self, *args, **kwargs):
        return render(self.request, "core/order_summary.html")


class OrderSummaryView(DetailView):
    model = Order
    template_name = "core/order_summary.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # checking if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:details", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart")
            return redirect("core:details", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info("This item was created and added to your cart")
        return redirect("core:details", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the item
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False).first()
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "The item was removed from the cart")
            return redirect("core:details", slug=slug)
        else:
            # add a message showing that the user doesn't have the order
            messages.info(request, "The item was not in your cart")
            return redirect("core:details", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:details", slug=slug)


def checkout(request):
    return render(request, "core/checkout.html")
