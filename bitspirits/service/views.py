from django.shortcuts import render
from django.db.models import Prefetch
from company.models import CompanyInfo
from .models import Service
from .models import ServiceConfigure
from .models import Parameter


def Services(request):
    context = {}
    context['service_config'] = ServiceConfigure.objects.filter(active=True).last()
    return render(request, 'service/services.html', context)


def ServiceDetails(request, id):
    context = {}
    service = Service.objects.prefetch_related(Prefetch(
        'service',
        queryset=Parameter.objects.order_by('id'),
        to_attr='parameters'
    )).get(id=id)
    context['service'] = service
    context['services'] = Service.objects.order_by('-name').all()
    return render(request, 'service/service.html', context)
