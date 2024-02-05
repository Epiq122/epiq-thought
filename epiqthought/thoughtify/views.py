from django.shortcuts import render


def home(request):
    return render(request, "thoughtify/index.html")


def register(request):
    return render(request, "thoughtify/register.html")


def login(request):
    return render(request, "thoughtify/login.html")


def dashboard(request):
    return render(request, "thoughtify/dashboard.html")
