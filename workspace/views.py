from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Workspace
from django.http import JsonResponse

def home(request):
    return render(request, "home.html")

#======Workspace=====================
def workspace_list(request):
    workspaces = Workspace.objects.all()
    return render(request, 'workspace.html', {'workspaces': workspaces})

def create_workspace(request):
    if request.method == "POST":
        title = request.POST.get("title")
        logo = request.FILES.get("logo")

        # create and save Workspace object
        workspace = Workspace(title=title, logo=logo)
        workspace.save()

        return JsonResponse({"status":"success"})
    else:
        return JsonResponse({"status":"error", "message":"Invalid request method."})