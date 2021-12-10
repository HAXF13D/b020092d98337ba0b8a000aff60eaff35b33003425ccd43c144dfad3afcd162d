from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def main_page(request):
    data = {'data':"ГЛАВНЫЙ ЭКРАН"}
    return render(
        request,
        'test1.html',
        context=data
    )

def auth(request):
    data = {
        'data': "ТУТ БУДЕТ АВТОРИЗАЦИЯ РЕГИСТРАЦИЯ"
    }
    return render(
        request,
        'test1.html',
        context=data
    )