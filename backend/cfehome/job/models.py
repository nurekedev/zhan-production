from collections.abc import Iterable
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import QuerySet
from PIL import Image

# Create your models here.


class City(models.Model):
    """Выбор города работодателя"""
    name = models.CharField('Название города', max_length=255)

    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Города'
        db_table = 'city'

    def __str__(self):
        return f"{self.name}"


class Company(models.Model):
    """Выбор компании работодателя"""
    name = models.CharField('Название компании', max_length=255)

    class Meta:
        verbose_name = 'Компаний'
        verbose_name_plural = 'Компаний'
        db_table = 'company'

    def __str__(self):
        return f"{self.name}"
    


class Vacancy(models.Model):
    """Модель вакансии работодателя. Переопределен метод сохрание титульной фотографии"""

    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    name = models.CharField('Название вакансии', max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    model_pic = models.ImageField(
        'Фотография вакансии', upload_to='jobs', blank=True, null=True)
    salary = models.DecimalField(
        'Заработная плата', max_digits=15, decimal_places=2)

    responsibility_text = models.TextField(
        'Обязанности', blank=True, null=True)
    requirement_text = models.TextField('Требования', blank=True, null=True)
    schedule = models.TextField('График работы', blank=True, null=True)
    working_condition_text = models.TextField(
        'Условия работы', blank=True, null=True)
    accommodation = models.TextField('Проживание', blank=True, null=True)
    nutrition = models.TextField('Питание', blank=True, null=True)
    additional_text = models.TextField(
        'Дополнительная информация', blank=True, null=True)

    city = models.ForeignKey(
        to='City', related_name='cities', verbose_name='Город', on_delete=models.CASCADE)
    company = models.ForeignKey(
        to='Company', related_name='companies', verbose_name='Компания', on_delete=models.CASCADE)
    publish = models.DateTimeField('Дата', default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField('Статус активности',
                              max_length=20, choices=STATUS_CHOICES, default=PUBLISHED)

    user = models.ForeignKey(
        User, verbose_name='Пользователь', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'
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

    # def save(self, *args, **kwargs):
    #     super().save()
    #     image = Image.open(self.model_pic.path)

    #     if image.height > 500 or image.width > 500:
    #         croped_image = (500, 500)
    #         image.thumbnail(croped_image)
    #         image.save(self.model_pic.path)


class Review(models.Model):
    """Модель для Отзыва пользователей"""
    author = models.CharField('Автор отзыва', max_length=100)
    body_text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
        db_table = 'review'

    def __str__(self):
        return f"{self.author} - {self.body_text}"
