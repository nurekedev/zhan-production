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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    city = CitySerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='vacancy-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Vacancy
        fields = ('name', 'slug', 'url', 'model_pic', 'salary', 'city', 'company', 'working_condition_text', 'accommodation', 'nutrition', 'additional_text',
        'publish', 'status','user')

    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('vacancy-detail', kwargs={'slug': obj.slug}, request=request)


class LiteContactSerializer(serializers.Serializer):
    """Форма для получения контактной информации"""
    full_name = serializers.CharField(max_length=100, write_only=True)
    phone_number = serializers.CharField(validators=[validate_phone_number])



class ResponseVacancySerializer(serializers.Serializer):
    """Формя для получени отклика. Поля 'phone_number', 'cv_filed' имеют дополнительную валидацию"""
    full_name = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(validators=[validate_phone_number])
    email = serializers.EmailField()
    cv_field = serializers.FileField(validators=[validate_file_size, validate_file_extension])

