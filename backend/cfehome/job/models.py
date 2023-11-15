from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class City(models.Model):
    """Выбор города работодателя"""
    name = models.CharField('Название города', max_length=255)

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'
        db_table = 'city'


class Company(models.Model):
    """Выбор компании работодателя"""
    name = models.CharField('Название компании', max_length=255)

    class Meta:
        verbose_name = 'Компаний'
        verbose_name_plural = 'Компаний'
        db_table = 'company'


class Vacancy(models.Model):
    """Модель вакансии работодателя"""

    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    name = models.CharField('Название вакансии', max_length=255)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    salary = models.DecimalField(
        'Заработная плата', max_digits=15, decimal_places=2)
    body = models.TextField('Описание')
    city = models.ForeignKey(
        to='City', related_name='cities', verbose_name='Город', on_delete=models.CASCADE)
    company = models.ForeignKey(
        to='Company', related_name='companies', verbose_name='Компания', on_delete=models.CASCADE)
    publish = models.DateTimeField('Дата', default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PUBLISHED)

    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        db_table = 'vacancy'
