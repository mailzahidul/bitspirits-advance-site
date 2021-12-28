from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
# Register your models here.
from .models import CompanyInfo
from .models import ContactConfigure
from .models import Message
from .models import HomeSliderConfigure
from .models import FaqConfigure
from .models import Faq
from .models import SomeFactsConfigure

User = get_user_model()


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')

    class Meta:
        model = CompanyInfo


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read')
    list_editable = ('subject', 'is_read')
    list_per_page = 20

    class Meta:
        model = Message


class HomeSliderConfigureAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'image_tag', 'img')
    list_editable = ('active', 'img')
    list_per_page = 10

    def image_tag(self, obj):
        return format_html('<img src="{}" width="80px" height="100px" />'.format(obj.img.url))

    image_tag.short_description = 'Image'

    class Meta:
        model = HomeSliderConfigure


class FawAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'active', 'position')
    list_editable = ('active','position')

    class Meta:
        model = Faq


admin.site.register(CompanyInfo, CompanyAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(ContactConfigure)
admin.site.register(SomeFactsConfigure)
admin.site.register(HomeSliderConfigure, HomeSliderConfigureAdmin)
admin.site.register(FaqConfigure)
admin.site.register(Faq, FawAdmin)
admin.site.site_header = 'Ravas Web'
admin.site.index_title = 'Ravas Web'
admin.site.site_title = 'Ravas Web administration'
