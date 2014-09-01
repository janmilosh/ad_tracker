from django.shortcuts import redirect, render, render_to_response
from django.contrib import auth
from django.contrib.auth import logout
from django.core.context_processors import csrf
from django.utils import timezone
import datetime

from ads.models import Ad
from newspapers.models import Newspaper

def home(request):
    today = datetime.date.today()
    ads = Ad.objects.filter(end_date__gte=today)
    newspapers = Newspaper.objects.all()
    
    return render(request, 'home.html', ({
        'ads': ads,
        'newspapers': newspapers,
    }))

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/accounts/loggedin')
    else:
        return redirect('/accounts/invalid')

def loggedin(request):
    return render(request, 'login/loggedin.html', ({
        'full_name': request.user.username
    }))

def invalid_login(request):
    return render(request, 'login/invalid-login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login/logout.html')
