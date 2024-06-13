from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from . import models
import json
from django.utils import timezone
from django.forms.models import model_to_dict


def index(request):
    select_category = int(request.GET.get('cat', 0))
    if select_category != 0:
        services = models.Service.objects.filter(category=select_category).all()[:6]
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
            'success': request.GET.get('message'),
        })
    elif request.method == "POST":
        print(request.POST)
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        services_ids = request.POST.getlist('services')
        request = models.Request(phone=phone, name=name, date=timezone.now())
        request.save()
        services = models.Service.objects.filter(id__in=services_ids)
        request.services.set(services)
        return HttpResponseRedirect('/request?message=success')


def service_info(request):
    if request.method == "GET":
        services = models.Service.objects.all()
        return render(request, 'main/request.html', {
            'services': services,
        })
    elif request.method == "POST":
        ids = request.POST.getlist('serviceIds')
        services = models.Service.objects.filter(id__in=ids)
        result = []
        for service in services:
            result.append({
                'id': service.id,
                'name': service.name,
                'cover': str(service.cover),
            })
        return HttpResponse(json.dumps(result), content_type='application/json')

def service_all(request):
    select_category = int(request.GET.get('cat', 0))
    if select_category != 0:
        services = models.Service.objects.filter(category=select_category).all()
    else:
        services = models.Service.objects.all()

    category = models.ServiceCategory.objects.all()
    return render(request, 'main/services.html', {
        'services': services,
        'categories': category,
        'cat': select_category,
        'promo': models.Promo.objects.last()
    })