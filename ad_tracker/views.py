from django.contrib.auth import logout
from django.shortcuts import redirect, render

def home(request):
    return render(request, "home.html", ({
        
    }))
