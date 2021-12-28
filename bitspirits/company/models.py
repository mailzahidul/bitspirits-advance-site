from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from colorfield.fields import ColorField
from django.utils import timezone
from service.models import Service


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_superuser=False, is_active=True):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a Password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            is_superuser=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    fast_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=60)
    img = models.ImageField(upload_to='user', default='')
    password = models.CharField(max_length=90)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_fullname(self):
        return self.fast_name + " " + self.last_name


class CompanyInfo(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    title = models.CharField(max_length=250, default="Tech Leo || Your best choice")
    sub_title = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250, default="", null=True, blank=True)
    twitter = models.CharField(max_length=250, default="", null=True, blank=True)
    youtube = models.CharField(max_length=250, default="", null=True, blank=True)
    linkedin = models.CharField(max_length=250, default="", null=True, blank=True)
    about = models.TextField()
    descriptions = models.TextField(max_length=1000, default="")
    icon = models.ImageField(upload_to='company')
    logo = models.ImageField(upload_to='company')
    footer_logo = models.ImageField(upload_to='company', default="")
    video_img = models.ImageField(upload_to='company', default="")
    opening_day = models.CharField(max_length=250, default="")
    opening_time = models.CharField(max_length=250, default="")
    video = models.CharField(max_length=250, default="")
    holiday = models.CharField(max_length=250, default="")
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    create = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ContactConfigure(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250)
    bg_contact_config_icon_start_color = ColorField(default='#000000')
    bg_contact_config_icon_end_color = ColorField(default='#000000')
    contact_config_icon_color = ColorField(default='#000000')
    contact_form_icon_color = ColorField(default='#000000')
    btn_contact_form_start_color = ColorField(default='#000000')
    btn_contact_form_end_color = ColorField(default='#000000')
    btn_contact_form_start_hover_color = ColorField(default='#000000')
    btn_contact_form_end_hover_color = ColorField(default='#000000')
    btn_contact_form_txt_color = ColorField(default='#000000')
    btn_contact_form_txt_hover_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    subject = models.CharField(max_length=250, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    is_read = models.BooleanField(default=False)
    post_time = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.post_time = timezone.now()
        return super(Message, self).save(*args, **kwargs)


class SomeFactsConfigure(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=250)
    img = models.ImageField(upload_to='fact', default='')
    item_bg_img = models.ImageField(upload_to='fact', default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class HomeSliderConfigure(models.Model):
    title = models.CharField(max_length=50)
    video = models.CharField(max_length=250)
    img = models.ImageField(upload_to='video')
    description = models.CharField(max_length=250)
    social_box_color = ColorField(default='#000000')
    bg_start_color = ColorField(default='#000000')
    bg_end_color = ColorField(default='#000000')
    bg_btn_start_color = ColorField(default='#000000')
    bg_btn_end_color = ColorField(default='#000000')
    bg_btn_hov_start_color = ColorField(default='#000000')
    bg_btn_hov_end_color = ColorField(default='#000000')
    bg_play_btn_color = ColorField(default='#000000')
    border_play_btn_color = ColorField(default='#000000')
    triangle_play_btn_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class FaqConfigure(models.Model):
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50, default='')
    img = models.ImageField(upload_to='video')
    title_active_color = ColorField(default='#000000')
    icon_color = ColorField(default='#000000')
    icon_active_color = ColorField(default='#000000')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()
    position = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.question
