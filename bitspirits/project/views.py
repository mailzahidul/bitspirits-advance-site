from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Prefetch, Q
from django.db.models import Count
from blog.models import Blog
from .models import Project
from .models import Parameter
from .models import Category

def Projects(request):
    context = {}
    categories = []

    context['recent_blogs'] = Blog.objects.order_by('-create_date')[:3]
    if 'category' in request.GET:
        projects = Project.objects.filter(category__id=request.GET['category']).order_by('-create_date').all()
    elif 'search' in request.GET:
        srch = request.GET['search']
        if srch:
            projects = Project.objects.filter(Q(title__icontains=srch)).order_by('-id').all()
    else:
        projects = Project.objects.order_by('-create_date').all()

    paginator = Paginator(projects, 12)
    page = request.GET.get('page')
    projects_with_pagination = paginator.get_page(page)
    context['projects'] = projects_with_pagination

    cs = Project.objects.values('category').annotate(dcount=Count('category')).order_by('-category__position')
    for item in cs:
        category = Category.objects.get(id=item['category'])
        categories.append({'category': category, 'dcount': item['dcount']})
    context['categories'] = categories
    return render(request, 'project/projects.html', context)


def details(request, id):
    context = {}
    project = Project.objects.prefetch_related(Prefetch(
        'project',
        queryset=Parameter.objects.order_by('id'),
        to_attr='parameters'
    )).get(id=id)
    context['project'] = project
    context['related_projects'] = Project.objects.exclude(id=id).filter(category__id=id)[:9]
    return render(request, 'project/project.html', context)
