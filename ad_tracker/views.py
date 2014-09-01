from django.contrib.auth import logout
from django.shortcuts import redirect, render
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
