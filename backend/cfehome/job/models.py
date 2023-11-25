from collections.abc import Iterable
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.utils.translation import gettext as _

from PIL import Image

# Create your models here.


class City(models.Model):
    """Выбор города работодателя"""
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Cities')
        verbose_name_plural = _('Cities')
        db_table = 'city'

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    """Выбор компании работодателя"""
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    class Meta:
        verbose_name = _('Companies')
        verbose_name_plural = _('Companies')
        db_table = 'company'

    def __str__(self):
        return f"{self.name}"
    


class Vacancy(models.Model):
    """Модель вакансии работодателя. Переопределен метод сохрание титульной фотографии"""

    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published'))
    )

    name = models.CharField(verbose_name=_('Name'), max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    model_pic = models.ImageField(verbose_name=_('Photo'), upload_to='jobs', blank=True, null=True)
    salary = models.DecimalField(verbose_name=_('Salary'), max_digits=15, decimal_places=2)

    responsibility_text = models.TextField(
        verbose_name=_('Responsibility'), blank=True, null=True)
    requirement_text = models.TextField(verbose_name=_('Requirements'), blank=True, null=True)
    schedule = models.TextField(verbose_name=_('Schedule'), blank=True, null=True)
    working_condition_text = models.TextField(
        verbose_name=_('Working Condition'), blank=True, null=True)
    accommodation = models.TextField(verbose_name=_('Accommodation'), blank=True, null=True)
    nutrition = models.TextField(verbose_name=_('Nutrition'), blank=True, null=True)
    additional_text = models.TextField(verbose_name=_('Additional text'), blank=True, null=True)

    city = models.ForeignKey(
        to='City', related_name='cities', verbose_name=_('City'), on_delete=models.CASCADE)
    company = models.ForeignKey(
        to='Company', related_name='companies', verbose_name=_('Company'), on_delete=models.CASCADE)
    publish = models.DateTimeField(verbose_name=_('Published Time'), default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(verbose_name=_('Status'), max_length=20, choices=STATUS_CHOICES, default=PUBLISHED)

    user = models.ForeignKey(
        User, verbose_name=_('Created by'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Vacancies')
        verbose_name_plural = _('Vacancies')
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish', 'name', 'responsibility_text']),
        ]
        db_table = 'vacancy'

    def __str__(self):
        return f"{self.name}, {self.city}, {self.company}, {self.status}"

    def get_model_picture(self):
        if self.model_pic:
            return settings.WEBSITE_URL + self.model_pic.url
        else:
            return 'https://bulma.io/images/placeholders/1280x960.png'
        
    def get_absolute_url(self):
        return reverse('vacancy-detail', kwargs={'slug': self.slug}) 

    # def save(self, *args, **kwargs):
    #     super().save()
    #     image = Image.open(self.model_pic.path)

    #     if image.height > 500 or image.width > 500:
    #         croped_image = (500, 500)
    #         image.thumbnail(croped_image)
    #         image.save(self.model_pic.path)


class Review(models.Model):
    """Модель для Отзыва пользователей"""
    author = models.CharField(verbose_name=_('Author'), max_length=100)
    body_text = models.TextField(verbose_name=_('Text of review'))

    class Meta:
        verbose_name = _('Reviews')
        verbose_name_plural = _('Reviews')
        db_table = 'review'

    def __str__(self):
        return f"{self.author} - {self.body_text}"
