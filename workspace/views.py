from django.shortcuts import render
from .models import Element

def home(request):
    return render(request, "home.html")

def workspace(request):
    # Fetch all elements from the database
    elements = Element.objects.all()

    # Check if there are any elements
    if elements:
        context = {'elements': elements}
    else:
        # Custom string when no elements exist
        context = {'message': 'No elements yet.'}

    # Pass context to the template
    return render(request, "workspace.html", context)