from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField


class About(models.Model):
    img = models.ImageField(default='')
    active_clients = models.IntegerField(default=0)
    team_members = models.IntegerField(default=0)
    projects_done = models.IntegerField(default=0)
    glorious_year = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    start_company = models.IntegerField()

    def __str__(self):
        return self.best_security


class WhyUsConfigure(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250)
    bg_img = models.ImageField(upload_to='about', default='')
    bg_start_color = ColorField(default='#000000')
    bg_end_color = ColorField(default='#000000')
    bg_btn_start_color = ColorField(default='#000000')
    bg_btn_end_color = ColorField(default='#000000')
    bg_btn_hov_start_color = ColorField(default='#000000')
    bg_btn_hov_end_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='about', default='')
    white_img = models.ImageField(upload_to='about', default='')
    description = models.CharField(max_length=250, default='')
    counter_text_color = ColorField(default='#000000')
    counter_border_color = ColorField(default='#000000')
    bg_color = ColorField(default='#000000')
    radius = models.IntegerField(default=50)
    border_width = models.IntegerField(default=10)
    why_us_config = models.ForeignKey(WhyUsConfigure,
                                      on_delete=models.CASCADE, related_name='feature', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class WhyUs(models.Model):
    title = models.CharField(max_length=50)
    why_us_config = models.ForeignKey(WhyUsConfigure,
                                      on_delete=models.CASCADE, related_name='why_us', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Counter(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='about', default='')
    count = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class MissionConfigure(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to='who_we_are', default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Mission(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='mission', default='')
    mission_config = models.ForeignKey(MissionConfigure,
                                       on_delete=models.CASCADE, related_name='mission', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class TeamConfigure(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=250)
    img = models.ImageField(upload_to='team')
    team_configuration = models.ForeignKey(TeamConfigure,
                                           on_delete=models.CASCADE, related_name='team')
    facebook = models.CharField(max_length=250, default="", null=True, blank=True)
    twitter = models.CharField(max_length=250, default="", null=True, blank=True)
    youtube = models.CharField(max_length=250, default="", null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class HowWeDoItConfigure(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, default='')
    title_text_color = ColorField(default='#000000')
    sub_title_text_color = ColorField(default='#000000')
    item_text_color = ColorField(default='#000000')
    item_icon_text_color = ColorField(default='#000000')
    bg_img = models.ImageField(upload_to='how_to_do_it', default='')
    step_block_1_img = models.ImageField(upload_to='how_to_do_it', default='')
    step_block_2_img = models.ImageField(upload_to='how_to_do_it', default='')
    step_block_3_img = models.ImageField(upload_to='how_to_do_it', default='')
    step_block_4_img = models.ImageField(upload_to='how_to_do_it', default='')
    steps_section_1_img = models.ImageField(upload_to='how_to_do_it', default='')
    steps_section_2_img = models.ImageField(upload_to='how_to_do_it', default='')
    steps_section_3_img = models.ImageField(upload_to='how_to_do_it', default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class HowWeDoIt(models.Model):
    name = models.CharField(max_length=150)
    position = models.IntegerField()
    how_we_do_it_configuration = models.ForeignKey(HowWeDoItConfigure,
                                                   on_delete=models.CASCADE, related_name='how_we_do_it')

    def __str__(self):
        return self.name


class TestimonialConfigure(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    title_txt_color = ColorField(default='#000000')
    designation_txt_color = ColorField(default='#000000')
    description_txt_color = ColorField(default='#000000')
    bg_item_color = ColorField(default='#000000')
    bg_bottom_line_start_color = ColorField(default='#000000')
    bg_bottom_line_end_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    designation = models.CharField(max_length=250, null=False, blank=False)
    testimonial_config = models.ForeignKey(TestimonialConfigure,
                                           on_delete=models.CASCADE, related_name='testimonial', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    post_date = models.DateField(editable=False)
    image = models.ImageField(upload_to='client_image')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.post_date = timezone.now()
        return super(Testimonial, self).save(*args, **kwargs)


class VideoConfig(models.Model):
    title = models.CharField(max_length=100)
    video = models.CharField(max_length=300)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='video_config')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Technology(models.Model):
    title = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.title


class Support(models.Model):
    title = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.title


class TechnologyConfig(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    img = models.ImageField(upload_to='technology')
    technology = models.ManyToManyField(Technology)

    def __str__(self):
        return self.title


class SupportConfig(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    img = models.ImageField(upload_to='support')
    support = models.ManyToManyField(Support)

    def __str__(self):
        return self.title
