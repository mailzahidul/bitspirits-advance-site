from django.shortcuts import render
from django.db.models import Prefetch, Subquery
from company.models import CompanyInfo
from .models import TeamConfigure
from .models import Team
from .models import Testimonial
from .models import TestimonialConfigure
from .models import VideoConfig
from .models import TechnologyConfig
from .models import SupportConfig
from .models import Feature
from .models import WhyUsConfigure
from .models import WhyUs
from .models import Counter


def AboutView(request):
    context = {}
    context['testimonial_config'] = TestimonialConfigure.objects.prefetch_related(Prefetch(
        'testimonial',
        queryset=Testimonial.objects.order_by('id'),
        to_attr='testimonials'
    )).filter(active=True).last()

    subqry = Subquery(Feature.objects.order_by('id').values_list('id', flat=True)[:4])

    context['why_us_config'] = WhyUsConfigure.objects.prefetch_related(Prefetch(
        'feature',
        queryset=Feature.objects.filter(id__in=subqry),
        to_attr='features'
    ), Prefetch(
        'why_us',
        queryset=WhyUs.objects.order_by('id'),
        to_attr='why_uss'
    )).filter(active=True).last()

    context['counters'] = Counter.objects.order_by('-position')[:3]

    return render(request, 'about/about.html', context)
