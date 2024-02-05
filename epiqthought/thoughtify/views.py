from django.shortcuts import render, redirect
from .forms import UserCreateForm


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
    return render(request, "thoughtify/login.html")


def dashboard(request):
    return render(request, "thoughtify/dashboard.html")
