from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import *

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