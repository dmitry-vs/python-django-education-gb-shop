from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)

def products(request):
    context = {
        'title': 'продукция',
    }
    return render(request, 'mainapp/products.html', context)

def contact(request):
    context = {
        'title': 'контакты',
    }
    return render(request, 'mainapp/contact.html', context)
