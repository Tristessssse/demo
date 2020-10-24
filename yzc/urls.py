from django.urls import path
from yzc.views import *
urlpatterns = [
    path('main/', my_login, name='login'),
    path('main2/', my_register, name='register'),
]
