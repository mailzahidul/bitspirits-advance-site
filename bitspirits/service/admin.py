from django.contrib import admin
from django.utils.html import format_html
from .models import Service
from .models import Parameter
from .models import ServiceConfigure


class ParameterTabularInner(admin.TabularInline):
    model = Parameter


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ParameterTabularInner,]
    list_display = ('name', 'title', 'active', 'icon_tag', 'thumbnail')
    list_editable = ('active', 'thumbnail')
    readonly_fields = ["view_count", ]
    list_per_page = 10

    def icon_tag(self, obj):
        return format_html('<img src="{}" width="80px" height="100px" />'.format(obj.icon.url))

    icon_tag.short_description = 'Image'

    class Meta:
        model = Service


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceConfigure)