from django.utils.translation import gettext as _

from rest_framework.reverse import reverse
from rest_framework import serializers, validators


from .models import *
from .validators import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор вакансии. Для отображение всех полей вакансии"""
    city = CitySerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='vacancy-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Vacancy
        fields = ('name', 'slug', 'url', 'model_pic', 'salary', 'city', 'company',
                  'responsibility_text', 'working_condition_text', 'accommodation', 'nutrition', 'additional_text', 'publish',)

    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('vacancy-detail', kwargs={'slug': obj.slug}, request=request)


class LiteContactSerializer(serializers.Serializer):
    """Форма для получения контактной информации"""
    full_name = serializers.CharField(
        max_length=100, write_only=True, help_text=_("Enter your full name"))
    phone_number = serializers.CharField(
        validators=[validate_phone_number], help_text=_("Enter your phone number"))


class ResponseVacancySerializer(serializers.Serializer):
    """Формя для получени отклика. Поля 'phone_number', 'cv_filed' имеют дополнительную валидацию"""
    full_name = serializers.CharField(
        max_length=100, help_text=_("Enter your full name"))
    phone_number = serializers.CharField(
        validators=[validate_phone_number], help_text=_("Enter your phone number"))
    email = serializers.EmailField(help_text=_("Enter your email"))
    cv_field = serializers.FileField(
        validators=[validate_file_size, validate_file_extension], help_text=_("Upload your CV"))
    additional_text = serializers.CharField(
        max_length=300, allow_blank=True, help_text=_("Enter additional text (optional)"))


class QuestionContactSerializer(serializers.Serializer):
    """Форма для получения вопроса в разделе 'Контакты'"""
    full_name = serializers.CharField(
        max_length=100, write_only=True, help_text=_("Enter your full name"))
    phone_number = serializers.CharField(
        validators=[validate_phone_number], help_text=_("Enter your phone number"))
    email = serializers.EmailField(help_text=_("Enter your email"))
    question_text = serializers.CharField(
        max_length=300, help_text=_("Enter your question text (optional)"))


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзыва. Для отображение всех полей отзывов"""
   
    class Meta:
        model = Review
        fields = ('author', 'author_pic', 'body_text')



