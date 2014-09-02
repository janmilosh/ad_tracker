from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import datetime
from forms import NewspaperForm
from django.core.context_processors import csrf

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

def create(request):
    if request.POST:
        form = NewspaperForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')
    else:
        form = NewspaperForm

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'newspapers/create-newspaper.html', args)
