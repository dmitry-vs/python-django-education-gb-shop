from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    title = 'Админка | Пользователи'
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    title = 'Админка | Категории'
    categories_list = ProductCategory.objects.all()

    context = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda x: x.is_superuser)
def products(request, category_pk):
    title = 'Админка | Продукты'
    category = get_object_or_404(ProductCategory, pk=category_pk)
    products_list = category.product_set.all().order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)