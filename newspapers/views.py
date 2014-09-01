from django.shortcuts import render
from django.shortcuts import get_object_or_404

from newspapers.models import Newspaper
from ads.models import Ad

def newspaper(request, newspaper_id=1):
    newspaper = get_object_or_404(Newspaper, id=newspaper_id)
    ads = newspaper.ad_set.all()

    return render(request, 'newspapers/newspaper-detail.html', ({
        'newspaper': newspaper,
        'ads': ads,
    }))