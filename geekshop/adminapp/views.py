from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from authapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import Product, ProductCategory
from adminapp.forms import ShopUserRegisterAdminForm, ShopUserEditAdminForm


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
def user_create(request):
    title = 'Пользователи | Создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterAdminForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:index'))
    else:
        user_form = ShopUserRegisterAdminForm()
    
    context = {
        'title': title,
        'form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, user_pk):
    title = 'Пользователи | Редактирование'
    user = get_object_or_404(ShopUser, pk=user_pk)

    if request.method == 'POST':
        user_form = ShopUserEditAdminForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:index'))
    else:
        user_form = ShopUserEditAdminForm(instance=user)
    
    context = {
        'title': title,
        'form': user_form,
    }

    return render(request, 'adminapp/user_update.html', context)


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
    products_list = Product.objects.filter(category__pk=category_pk).order_by('name')

    context = {
        'title': title,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)