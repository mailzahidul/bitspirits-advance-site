from django.shortcuts import render, redirect
from django.db.models import Prefetch, Subquery
from django.contrib import messages
from .forms import ContactForm
from .models import Message
from .models import Faq
from service.models import Service
from about.models import VideoConfig
from about.models import TeamConfigure
from about.models import About
from about.models import Team
from project.models import Project
from blog.models import Blog
from about.models import Feature
from about.models import WhyUsConfigure
from about.models import WhyUs
from .models import HomeSliderConfigure


# Create your views here.
def Home(request):
    context = {}
    context['about'] = About.objects.last()
    context['faqs'] = Faq.objects.filter(active=True).order_by('-position')
    context['home_slider_config'] = HomeSliderConfigure.objects.filter(active=True).last()
    context['services'] = Service.objects.filter(active=True).order_by('-id')[:5]
    context['projects'] = Project.objects.filter(active=True).order_by('-id')[:6]
    context['blogs'] = Blog.objects.order_by('-create_date')[:3]

    subqry = Subquery(Feature.objects.order_by('id').values_list('id', flat=True)[:5])
    context['why_us_config'] = WhyUsConfigure.objects.prefetch_related(Prefetch(
        'feature',
        queryset=Feature.objects.filter(id__in=subqry),
        to_attr='features'
    ), Prefetch(
        'why_us',
        queryset=WhyUs.objects.order_by('id'),
        to_attr='why_uss'
    )).filter(active=True).last()
    return render(request, 'company/index.html', context)


def Contact(request):
    context = {}

    if request.POST:
        forms = ContactForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, "Your message is submitted successfully.", extra_tags='alert-success')
            return redirect('contact')
        else:
            messages.error(request, forms.errors, extra_tags='alert-danger')
    else:
        return render(request, 'company/contact.html', context)
