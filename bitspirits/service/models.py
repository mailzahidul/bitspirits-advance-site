from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField


class ServiceConfigure(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    img = models.ImageField(upload_to='service')
    bg = models.ImageField(upload_to='service')
    anim_img = models.ImageField(upload_to='service')
    btn_start_color = ColorField(default='#000000')
    btn_end_color = ColorField(default='#000000')
    btn_start_hover_color = ColorField(default='#000000')
    btn_end_hover_color = ColorField(default='#000000')
    btn_txt_color = ColorField(default='#000000')
    btn_txt_hover_color = ColorField(default='#000000')
    dot_color = ColorField(default='#000000')
    border_color = ColorField(default='#000000')
    learn_more_btn_hover_color = ColorField(default='#000000')
    learn_more_btn_color = ColorField(default='#000000')
    bg_item_start_color = ColorField(default='#000000')
    bg_item_end_color = ColorField(default='#000000')
    bg_item_start_hover_color = ColorField(default='#000000')
    bg_item_end_hover_color = ColorField(default='#000000')
    bg_btn_start_hover_color = ColorField(default='#000000')
    bg_btn_end_hover_color = ColorField(default='#000000')
    bg_btn_icon_color = ColorField(default='#000000')
    bg_btn_boarder_color = ColorField(default='#000000')
    bg_btn_boarder_width = models.IntegerField(default=3)
    learn_more_btn_txt = models.CharField(max_length=50, default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    name = models.CharField(max_length=250, default='')
    title = models.CharField(max_length=250)
    description = models.TextField(default='')
    thumbnail = models.ImageField(upload_to='service')
    icon = models.ImageField(upload_to='service')
    view_count = models.BigIntegerField(default=0)
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    create = models.DateTimeField(editable=False)
    create_date = models.DateField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.create = timezone.now()
            self.create_date = timezone.now()
            self.update = timezone.now()

        return super(Service, self).save(*args, **kwargs)


class Parameter(models.Model):
    title = models.CharField(max_length=250, default="", null=True, blank=True)
    description = models.TextField()
    img = models.ImageField(upload_to='service', default="", null=True, blank=True)
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE, related_name='service')
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    create = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.description
