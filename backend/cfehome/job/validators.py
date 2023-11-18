from rest_framework.validators import UniqueValidator
from .models import Vacancy, Company, City
from rest_framework import serializers


# unique_vacancy_title = UniqueValidator(queryset=Vacancy.PUBLISHED, lookup='iexact')
