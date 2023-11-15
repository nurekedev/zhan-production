from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.


class VacancyAPIList(generics.ListAPIView):
    queryset = Vacancy.objects.filter(status=Vacancy.PUBLISHED)
    serializer_class = VacancySerializer
    permission_classes = (IsAdminOrReadOnly, )