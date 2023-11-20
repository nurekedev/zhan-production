from rest_framework.validators import UniqueValidator
from .models import Vacancy, Company, City
from rest_framework import serializers

"""Не обращать внимание"""
# unique_vacancy_title = UniqueValidator(queryset=Vacancy.PUBLISHED, lookup='iexact')
