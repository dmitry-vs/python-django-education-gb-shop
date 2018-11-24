from django.shortcuts import render

# Create your views here.

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

def products(request):
  goods = [
    {
      'name': 'Отдых на пляже',
      'price': 5000,
      'img_name': '1',
    },
    {
      'name': 'Торжество жизни',
      'price': 10000,
      'img_name': '2',
    },
    {
      'name': 'Прогулка на исходе дня',
      'price': 15000,
      'img_name': '3',
    },
    {
      'name': 'Домик у моря',
      'price': 5000,
      'img_name': '4',
    },
    {
      'name': 'Жизнь на воде',
      'price': 10000,
      'img_name': '5',
    },
    {
      'name': 'Накануне шторма',
      'price': 15000,
      'img_name': '6',
    },
  ]
  
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
