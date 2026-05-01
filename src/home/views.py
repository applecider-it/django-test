from django.shortcuts import render, redirect
import json

def home_view(request):
    return render(request, "home.html")

def development_view(request):
    data = {"val1": "テスト"}
    return render(request, "development.html", {
        "data_json": json.dumps(data),
    })
