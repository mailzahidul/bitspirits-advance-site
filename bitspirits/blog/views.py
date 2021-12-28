from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Prefetch
from company.models import CompanyInfo
from .models import Blog
from .models import Category
from .models import Parameter
from .models import BlogConfigure
from page_config.models import PageBanner


def blogs(request):
    context = {}
    categories = []
    context['blog_config'] = BlogConfigure.objects.filter(active=True).last()
    context['recent_blogs'] = Blog.objects.order_by('-create_date')[:3]
    if 'category' in request.GET:
        blogs = Blog.objects.filter(category__id=request.GET['category']).order_by('-create_date').all()
    else:
        blogs = Blog.objects.order_by('-create_date').all()
    paginator = Paginator(blogs, 1)
    page = request.GET.get('page')
    blogs_with_pagination = paginator.get_page(page)
    context['blogs'] = blogs_with_pagination
    cs = Blog.objects.values('category').annotate(dcount=Count('category')).order_by()
    for item in cs:
        category = Category.objects.get(id=item['category'])
        categories.append({'category': category, 'dcount': item['dcount']})
    context['categories'] = categories
    return render(request, 'blog/blogs.html', context)


def blog(request, id):
    context = {}
    categories = []
    context['recent_blogs'] = Blog.objects.order_by('-create_date')[:3]
    cs = Blog.objects.values('category').annotate(dcount=Count('category')).order_by()
    for item in cs:
        category = Category.objects.get(id=item['category'])
        categories.append({'category': category, 'dcount': item['dcount']})
    context['categories'] = categories

    blog = Blog.objects.prefetch_related(Prefetch(
        'blog',
        queryset=Parameter.objects.order_by('id'),
        to_attr='parameters'
    )).get(id=id)
    blog.read_count = blog.read_count + 1
    blog.save()
    context['blog'] = blog

    return render(request, 'blog/blog.html', context)
