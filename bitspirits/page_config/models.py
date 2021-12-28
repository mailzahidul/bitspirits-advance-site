from django.db import models
from colorfield.fields import ColorField


class VideoConfigure(models.Model):
    title = models.CharField(max_length=50)
    video = models.CharField(max_length=250)
    img = models.ImageField(upload_to='video')
    bg = models.ImageField(upload_to='video', default='')
    description = models.CharField(max_length=250)
    bg_btn_start_color = ColorField(default='#000000')
    bg_btn_end_color = ColorField(default='#000000')
    bg_btn_hov_start_color = ColorField(default='#000000')
    bg_btn_hov_end_color = ColorField(default='#000000')
    btn_txt_color = ColorField(default='#000000')
    border_play_btn_color = ColorField(default='#000000')
    border_width = models.IntegerField(default=0)
    triangle_play_btn_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PageBanner(models.Model):
    about_img = models.ImageField(upload_to='banner', default='')
    service_img = models.ImageField(upload_to='banner', default='')
    project_img = models.ImageField(upload_to='banner', default='')
    blog_img = models.ImageField(upload_to='banner', default='')
    contact_img = models.ImageField(upload_to='banner', default='')
    active = models.BooleanField(default=True)


class PageSetup(models.Model):
    back_to_top_color = ColorField(default='#000000')
    back_to_top_after_color = ColorField(default='#000000')
    back_to_top_before_color = ColorField(default='#000000')
    back_to_top_txt_color = ColorField(default='#000000')
    sidebar_search_btn_color = ColorField(default='#000000')
    sidebar_search_color = ColorField(default='#000000')
    pagination_btn_start_color = ColorField(default='#000000')
    pagination_btn_end_color = ColorField(default='#000000')
    quote_btn_one_color = ColorField(default='#000000')
    quote_btn_one_hover_color = ColorField(default='#000000')
    quote_btn_two_color = ColorField(default='#000000')
    quote_btn_two_hover_color = ColorField(default='#000000')
    bg_footer_start_color = ColorField(default='#000000')
    bg_footer_end_color = ColorField(default='#000000')
    title_icon = models.ImageField(upload_to='page_setup', default='')
    active = models.BooleanField(default=True)
