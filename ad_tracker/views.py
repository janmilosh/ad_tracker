from django.contrib.auth import logout
from django.shortcuts import redirect, render

from ads.models import Ad
from newspapers.models import Newspaper

def home(request):
    ads = Ad.objects.all()
    newspapers = Newspaper.objects.all()
    
    return render(request, "home.html", ({
        'ads': ads,
        'newspapers': newspapers,
    }))
