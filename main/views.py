from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
import json


def index(request):
    select_category = int(request.GET.get('cat', 0))
    if select_category != 0:
        services = models.Service.objects.filter(category=select_category).all()
    else:
        services = models.Service.objects.all()
        
    category = models.ServiceCategory.objects.all()
    return render(request, 'main/index.html', {
        'services': services,
        'categories': category,
        'cat': select_category,
        'promo': models.Promo.objects.last()
    })


def promo(request):
    return render(request, 'main/promo.html', {
        'promos': models.Promo.objects.all()
    })
    
def promo_info(request, promo_id):
    promo = get_object_or_404(models.Promo, pk=promo_id)
    return render(request, 'main/promo_info.html', {
        'promo': promo
    })


def request(request):
    if request.method == "GET":
        services = models.Service.objects.all()
        return render(request, 'main/request.html', {
            'services': services,
        })
    elif request.method == "POST":
        print(request.POST)
        return HttpResponseRedirect(reverse("request"))


def service_info(request):
    if request.method == "GET":
        services = models.Service.objects.all()
        return render(request, 'main/request.html', {
            'services': services,
        })
    elif request.method == "POST":
        ids = request.POST.getlist('serviceIds')
        result = []
        for id in ids:
            service = models.Service.objects.filter(id=id).first()
            result.append({
                'id': service.id,
                'name': service.name
            })

        return HttpResponse(json.dumps(result), content_type='application/json')