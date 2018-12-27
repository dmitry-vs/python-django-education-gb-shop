from django.shortcuts import render
from authapp.models import ShopUser


def index(request):
    title = 'Админка | Пользователи'
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list,
    }

    return render(request, 'adminapp/users.html', context)