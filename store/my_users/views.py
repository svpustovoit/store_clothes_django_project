from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from my_users.forms import UserLoginForm, UserRegisterForm, ProfileForm


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
                #messages.success(request, f"{username}, Ви увійшли до аккаунту!")
                #redirect_page = request.POST.get("next", None)
                #if redirect_page and redirect_page != reverse("my_user:logout"):
                    #return
                return HttpResponseRedirect(request.POST.get("next"))
    else:
        form = UserLoginForm()

    context = {
       "title": "Clothing - Авторізація",
        "form": form
    }
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{username}, Ви зареєструвались та увійшли до аккаунту!")
            return HttpResponseRedirect(reverse("main:index"))
    else:
        form = UserRegisterForm()

    context = {
       "title": "Clothing - Регістрація",
        "form" : form
    }
    return render(request, "users/registration.html", context)

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл оновлено!")
            return HttpResponseRedirect(reverse("my_user:profile"))
    else:
        form = ProfileForm(instance=request.user)

    context = {
       " title": "Clothing - Кабінет",
        "form": form
    }
    return render(request, "users/profile.html", context)


def users_cart(request):
    return render(request, "users/users_cart.html")

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, f"{request.user.username} Ви вийшли з аккаунту!")
    return HttpResponseRedirect(reverse("main:index"))


