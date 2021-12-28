from .models import CompanyInfo
from django.db.models import Prefetch, Subquery
from company.models import ContactConfigure
from page_config.models import VideoConfigure
from service.models import ServiceConfigure
from company.models import SomeFactsConfigure
from company.models import FaqConfigure
from page_config.models import PageBanner
from page_config.models import PageSetup
from about.models import Mission
from about.models import MissionConfigure
from about.models import HowWeDoIt
from about.models import HowWeDoItConfigure
from service.models import Service
from about.models import About
from project.models import Category
from project.models import Project
from about.models import Feature
from about.models import WhyUsConfigure
from about.models import WhyUs
from project.models import ProjectConfigure


def company_context(request):
    context = {}
    context['company'] = CompanyInfo.objects.filter(active=True).last()
    context['services'] = Service.objects.order_by('-name').all()
    context['page_banner'] = PageBanner.objects.filter(active=True).last()
    context['page_setup'] = PageSetup.objects.filter(active=True).last()
    context['service_config'] = ServiceConfigure.objects.filter(active=True).last()
    context['contact_config'] = ContactConfigure.objects.filter(active=True).last()
    context['video_config'] = VideoConfigure.objects.filter(active=True).last()
    context['some_facts_config'] = SomeFactsConfigure.objects.filter(active=True).last()
    context['faq_config'] = FaqConfigure.objects.filter(active=True).last()
    context['project_categories'] = Category.objects.filter(active=True)
    context['projects'] = Project.objects.filter(active=True)
    context['about'] = About.objects.filter(active=True).last()
    context['project_config'] = ProjectConfigure.objects.filter(active=True).last()

    context['mission_config'] = MissionConfigure.objects.prefetch_related(Prefetch(
        'mission',
        queryset=Mission.objects.order_by('id'),
        to_attr='missions'
    )).filter(active=True).last()

    context['how_we_do_it_config'] = HowWeDoItConfigure.objects.prefetch_related(Prefetch(
        'how_we_do_it',
        queryset=HowWeDoIt.objects.order_by('id'),
        to_attr='how_we_do_its'
    )).filter(active=True).last()

    return context
