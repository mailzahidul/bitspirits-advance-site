from django.contrib import admin
from django.utils.html import format_html
from .models import Project
from .models import Category
from .models import Parameter
from .models import ProjectConfigure


class ParameterTabularInner(admin.TabularInline):
    model = Parameter


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ParameterTabularInner,]
    list_display = ('title', 'active', 'image_tag', 'img')
    list_editable = ('active', 'img')
    readonly_fields = ["view_count", ]
    list_per_page = 10

    def image_tag(self, obj):
        return format_html('<img src="{}" width="80px" height="100px" />'.format(obj.img.url))

    image_tag.short_description = 'Image'

    class Meta:
        model = Project


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    class Meta:
        model = Category


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProjectConfigure)
