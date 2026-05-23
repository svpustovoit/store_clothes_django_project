from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
       "title": "Clothing - Авторізація"
    }
    return render(request, "users/login.html", context)


def registration(request):
    context = {
       "title": "Clothing -Регістрація"
    }
    return render(request, "users/registration.html", context)


def profile(request):
    context = {
       " title": "Clothing - Кабінет"
    }
    return render(request, "users/profile.html", context)


def users_cart(request):
    return render(request, "users/users_cart.html")


def logout(request):
    ...


