from django.shortcuts import render
from django.http import HttpResponse
from . import models


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
    })
