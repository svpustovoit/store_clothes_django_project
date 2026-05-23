
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from my_users.forms import UserLoginForm


# Create your views here.

def login(request):
    if request.method == "POST":
        form = UserLoginForm(data= request.POST)
        print(form.errors)

        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            print(f"user-{user}")
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    context = {
       "title": "Clothing - Авторізація",
        "form": form
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


