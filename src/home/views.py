from django.shortcuts import render, redirect

def home_view(request):
    return render(request, "home.html")

def development_view(request):
    return render(request, "development.html")
