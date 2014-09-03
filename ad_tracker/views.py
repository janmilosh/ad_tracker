from django.shortcuts import redirect, render, render_to_response
from django.contrib import auth
from django.contrib.auth import logout, login, authenticate 
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.utils import timezone
import datetime

from ads.models import Ad
from newspapers.models import Newspaper

def home(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    
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
    return render(request, 'account/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        return redirect('/invalid/')

def loggedin(request):
    return render(request, 'account/loggedin.html', ({
        'full_name': request.user.username
    }))

def invalid_login(request):
    return render(request, 'account/invalid-login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'account/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register_success/')

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()

    return render(request, 'account/register.html', args)

def register_success(request):
    return render(request, 'account/register-success.html')

