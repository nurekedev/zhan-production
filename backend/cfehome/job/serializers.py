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
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    url = serializers.HyperlinkedIdentityField(
        view_name='vacancy-detail',
        lookup_field='slug'
        )

    class Meta:
        model = Vacancy
        fields = '__all__'
    
    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse('vacancy-detail', kwargs={'slug':obj.slug}, request=request)
    


class LiteContactSerializer(serializers.Serializer):
    """Форма для получения контактной информации c возможностью  выбора (учеба, работа)"""
    STUDY = 'study'
    VACANCY = 'vacancy'

    ACTION_CHOICES = (
        (STUDY, 'Учеба'),
        (VACANCY, 'Работа')
    )

    full_name = serializers.CharField(max_length=100, write_only=True)
    email = serializers.EmailField(max_length=254, write_only=True)
    action_type = serializers.ChoiceField(choices=ACTION_CHOICES, write_only=False)

    
