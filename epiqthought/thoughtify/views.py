from django.shortcuts import render


def home(request):
    return render(request, "thoughtify/home.html")


def register(request):
    return render(request, "thoughtify/register.html")


def login(request):
    return render(request, "thoughtify/login.html")


def dashboard(request):
    return render(request, "thoughtify/dashboard.html")
