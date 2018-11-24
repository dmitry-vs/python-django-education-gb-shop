from django.shortcuts import render
import json
import os

# Create your views here.

MENU_ITEMS = {
  'index': 'Главная',
  'products': 'Продукция',
  'contact': 'Контакты',
}

GOODS_FILE_NAME = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'static', 'json', 'products.json')

def index(request):
  context = {
    'title': 'главная',
    'menu': MENU_ITEMS,
  }
  
  return render(request, 'mainapp/index.html', context)

def products(request):
  with open(GOODS_FILE_NAME, 'r', encoding='utf-8') as f:
    goods = json.load(f)

  context = {
    'title': 'продукция',
    'menu': MENU_ITEMS,
    'goods': goods,
  }
  
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
