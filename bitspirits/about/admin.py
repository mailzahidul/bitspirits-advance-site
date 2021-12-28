from django.contrib import admin
from .models import TeamConfigure
from .models import Team
from .models import TestimonialConfigure
from .models import Testimonial
from .models import VideoConfig
from .models import Technology
from .models import TechnologyConfig
from .models import Support
from .models import SupportConfig
from .models import About
from .models import MissionConfigure
from .models import Mission
from .models import HowWeDoItConfigure
from .models import HowWeDoIt
from .models import WhyUsConfigure
from .models import Feature
from .models import WhyUs
from .models import Counter


class TeamTabularInner(admin.TabularInline):
    model = Team


class TeamConfigureAdmin(admin.ModelAdmin):
    inlines = [TeamTabularInner]
    list_display = ('title', 'active')
    list_editable = ('active',)

    class Meta:
        model = TeamConfigure


class FeatureTabularInner(admin.TabularInline):
    model = Feature


class WhyUsTabularInner(admin.TabularInline):
    model = WhyUs


class WhyUsConfigureAdmin(admin.ModelAdmin):
    inlines = [FeatureTabularInner, WhyUsTabularInner]
    list_display = ('title', 'active')
    list_editable = ('active',)

    class Meta:
        model = WhyUsConfigure


class MissionInner(admin.TabularInline):
    model = Mission


class MissionConfigureAdmin(admin.ModelAdmin):
    inlines = [MissionInner]
    list_display = ('title', 'active')
    list_editable = ('active',)

    class Meta:
        model = MissionConfigure


class HowWeDoItInner(admin.TabularInline):
    model = HowWeDoIt


class HowWeDoItConfigureAdmin(admin.ModelAdmin):
    inlines = [HowWeDoItInner]
    list_display = ('title', 'active')
    list_editable = ('active',)

    class Meta:
        model = HowWeDoItConfigure


class TestimonialInner(admin.TabularInline):
    model = Testimonial


class TestimonialConfigureAdmin(admin.ModelAdmin):
    inlines = [TestimonialInner]
    list_display = ('title', 'active')
    list_editable = ('active',)

    class Meta:
        model = TestimonialConfigure


class VideoConfigAdmin(admin.ModelAdmin):
    list_display = ('title','is_active')
    list_editable = ('is_active',)
    list_per_page = 20

    class Meta:
        model = VideoConfig


class CounterAdmin(admin.ModelAdmin):
    list_display = ('title','active', 'position')
    list_editable = ('active','position')
    list_per_page = 20

    class Meta:
        model = Counter


admin.site.register(TeamConfigure, TeamConfigureAdmin)
admin.site.register(WhyUsConfigure, WhyUsConfigureAdmin)
admin.site.register(HowWeDoItConfigure, HowWeDoItConfigureAdmin)
admin.site.register(MissionConfigure, MissionConfigureAdmin)
admin.site.register(TestimonialConfigure, TestimonialConfigureAdmin)
admin.site.register(VideoConfig, VideoConfigAdmin)
admin.site.register(Technology)
admin.site.register(TechnologyConfig)
admin.site.register(Support)
admin.site.register(SupportConfig)
admin.site.register(About)
admin.site.register(Counter, CounterAdmin)
