from django.contrib import admin
from django.utils.html import format_html

from .models import BlogConfigure
from .models import Blog
from .models import Parameter
from .models import Category


# Register your models here.


class ParameterTabularInner(admin.TabularInline):
    model = Parameter


class BLogAdmin(admin.ModelAdmin):
    inlines = [ParameterTabularInner]
    list_display = ('title', 'active', 'image_tag', 'img')
    list_editable = ('active', 'img')
    readonly_fields = ["read_count"]
    # search_fields = ["title", "create_date", "menu"]
    list_per_page = 10

    def image_tag(self, obj):
        return format_html('<img src="{}" width="160px" height="100px" />'.format(obj.img.url))

    image_tag.short_description = 'Image'

    class Meta:
        model = Blog


admin.site.register(Blog, BLogAdmin)
admin.site.register(Category)
admin.site.register(BlogConfigure)
