from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "thoughtify/index.html")


def register(request):
    form = UserCreateForm()
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form": form}
    return render(request, "thoughtify/register.html", context)


def login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {"form": form}
    return render(request, "thoughtify/login.html", context)


def dashboard(request):
    return render(request, "thoughtify/dashboard.html")


def logout(request):
    auth.logout(request)
    return redirect("login")
