from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def workspace(request):
    return render(request, "workspace.html")