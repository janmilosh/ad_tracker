from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime

from ads.models import Ad

def ad(request, ad_id=1):
    ad = get_object_or_404(Ad, id=ad_id)

    return render(request, 'ads/ad-detail.html', ({
        'ad': ad,
    }))

def archive_ads(request):
    today = datetime.date.today()
    ads = Ad.objects.filter(end_date__lt=today).order_by('-end_date')

    return render(request, 'ads/ad-archive.html', ({
        'ads': ads,
    }))