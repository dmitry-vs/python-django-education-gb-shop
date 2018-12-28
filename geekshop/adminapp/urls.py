from django.urls import re_path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^$', adminapp.index, name='index'),
    re_path(r'^user/create/$', adminapp.user_create, name='user_create'),
    re_path(r'^user/update/(?P<user_pk>\d+)$', adminapp.user_update, name='user_update'),
    re_path(r'^categories/$', adminapp.categories, name='categories'),
    re_path(r'^products/(?P<category_pk>\d+)$', adminapp.products, name='products'),
]