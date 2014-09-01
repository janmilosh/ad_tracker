from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime

from newspapers.models import Newspaper
from ads.models import Ad

def newspaper(request, newspaper_id=1):
    today = datetime.date.today()
    newspaper = get_object_or_404(Newspaper, id=newspaper_id)
    ads = newspaper.ad_set.filter(end_date__gte=today)

    return render(request, 'newspapers/newspaper-detail.html', ({
        'newspaper': newspaper,
        'ads': ads,
    }))