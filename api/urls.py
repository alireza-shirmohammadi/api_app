from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('api/user/actknowlage',views.user_exist_actknowlage),
    path('api/user/create',views.create_user),
    path('api/user/login',views.user_login),
    path('api/user/test',views.test),
]
