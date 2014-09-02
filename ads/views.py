from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import datetime
from forms import AdForm
from django.core.context_processors import csrf

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

def create(request):
    if request.POST:
        form = AdForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = AdForm

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'ads/create-ad.html', args)
