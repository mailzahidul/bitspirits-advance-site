from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField


class BlogConfigure(models.Model):
    btn_start_color = ColorField(default='#000000')
    btn_end_color = ColorField(default='#000000')
    btn_start_hover_color = ColorField(default='#000000')
    btn_end_hover_color = ColorField(default='#000000')
    btn_txt_color = ColorField(default='#000000')
    btn_txt_hover_color = ColorField(default='#000000')
    item_calender_icon_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=250)
    sort_description = models.TextField(default='')
    img = models.FileField(upload_to='post')
    read_count = models.BigIntegerField(default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE, related_name='category')
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    create = models.DateTimeField(editable=False)
    create_date = models.DateField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.create = timezone.now()
            self.create_date = timezone.now()
        self.update = timezone.now()
        return super(Blog, self).save(*args, **kwargs)


class Parameter(models.Model):
    title = models.CharField(max_length=300, default='', null=True, blank=True)
    quotes_title = models.CharField(max_length=300, default='', null=True, blank=True)
    quotes_auth = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    blog = models.ForeignKey(Blog,
                             on_delete=models.CASCADE, related_name='blog')
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    create = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.description
