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
    ads_all = newspaper.ad_set.all()

    return render(request, 'newspapers/newspaper-detail.html', ({
        'newspaper': newspaper,
        'ads': ads,
        'ads_all': ads_all,
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

def edit(request, newspaper_id=1):
    newspaper = get_object_or_404(Newspaper, id=newspaper_id)
    
    if request.POST:
        form = NewspaperForm(request.POST, instance=newspaper)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewspaperForm(instance=newspaper)

    return render(request, 'newspapers/edit-newspaper.html', ({
        'form': form, 'newspaper': newspaper
    }))

def confirm_delete(request, newspaper_id=1):
    newspaper = get_object_or_404(Newspaper, id=newspaper_id)

    return render(request, 'newspapers/delete-newspaper.html', ({
        'newspaper': newspaper,
    }))

def delete(request, newspaper_id=1):
    newspaper = get_object_or_404(Newspaper, id=newspaper_id)

    newspaper.delete()

    return redirect('/')