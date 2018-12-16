from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


MENU_ITEMS = {
    'index': 'Главная',
    'products': 'Продукция',
    'contact': 'Контакты',
}


def index(request):
    context = {
        'title': 'главная',
        'menu': MENU_ITEMS,
    }
    
    return render(request, 'mainapp/index.html', context)


def products(request, category_pk=None):
    title = 'продукция'
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'title': title,
        'menu': MENU_ITEMS,
        'products': products,
        'categories': categories,
    }

    if category_pk:
        if category_pk == '0':
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=category_pk)
            products = Product.objects.filter(category__pk=category_pk).order_by('price')

        context['products'] = products
        context['category'] = category

    return render(request, 'mainapp/products.html', context)


def contact(request):
    contacts = {
        'address': {
        'key': 'Адрес',
        'val': 'Москва, ул. Барклая, 11',
        },
        'phone': {
        'key': 'Телефон',
        'val': '8 (495) 123-45-67'
        },
        'mail': {
        'key': 'Почта',
        'val': 'egallery@mail.egallery.ru',
        },
        'shipping': {
        'key': 'Доставка',
        'val': 'Все города России',
        },
    }

    context = {
        'title': 'контакты',
        'menu': MENU_ITEMS,
        'contacts': contacts,
    }
    
    return render(request, 'mainapp/contact.html', context)
