from django.shortcuts import render
from django.shortcuts import get_object_or_404

from ads.models import Ad

def ad(request, ad_id=1):
    ad = get_object_or_404(Ad, id=ad_id)

    return render(request, 'ads/ad-detail.html', ({
        'ad': ad,
    }))