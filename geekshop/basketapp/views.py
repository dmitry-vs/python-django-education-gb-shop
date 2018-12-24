from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from basketapp.models import Basket
from mainapp.models import Product


def basket_view(request):
    pass


def add(request, pk):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=pk)
        old_basket_item = Basket.objects.filter(user=request.user, product=product)

        if old_basket_item:
            old_basket_item[0].quantity += 1
            old_basket_item[0].save()
        else:
            new_basket_item = Basket(user=request.user, product=product, quantity=1)
            new_basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request):
    pass
