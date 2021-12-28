from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField


class ProjectConfigure(models.Model):
    title = models.CharField(max_length=250)
    sub_title = models.CharField(max_length=250, default='')
    anim_img = models.ImageField(upload_to='service')
    bg_hover_box_color = ColorField(default='#000000')
    hover_box_opacity = models.IntegerField(default=80)
    bg_icon_color = ColorField(default='#000000')
    bg_icon_hover_color = ColorField(default='#000000')
    icon_color = ColorField(default='#000000')
    icon_hover_color = ColorField(default='#000000')
    bg_btn_color = ColorField(default='#000000')
    bg_btn_hover_color = ColorField(default='#000000')
    bg_btn_filter_active_hover_color = ColorField(default='#000000')
    btn_filter_active_hover_txt_color = ColorField(default='#000000')
    filter_txt_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    position = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=250)
    client = models.CharField(max_length=150, default='')
    url = models.CharField(max_length=250)
    description = models.TextField(default='')
    img = models.ImageField(upload_to='project')
    logo = models.ImageField(upload_to='project', default='')
    view_count = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, related_name='category')
    facebook = models.CharField(max_length=250, default="", null=True, blank=True)
    twitter = models.CharField(max_length=250, default="", null=True, blank=True)
    youtube = models.CharField(max_length=250, default="", null=True, blank=True)
    linkedin = models.CharField(max_length=250, default="", null=True, blank=True)
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

        return super(Project, self).save(*args, **kwargs)


class Parameter(models.Model):
    title = models.CharField(max_length=300, default='', null=True, blank=True)
    quotes_title = models.CharField(max_length=300, default='', null=True, blank=True)
    quotes_auth = models.CharField(max_length=50, null=True, blank=True)
    img = models.ImageField(upload_to='project', null=True, blank=True)
    description = models.TextField()
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE, related_name='project')
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    create = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.description
