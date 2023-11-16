from django.shortcuts import render
from rest_framework import generics, viewsets, mixins, authentication

from .models import *
from .serializers import *
from .permissions import *
from .paginations import *

# Create your views here.




class VacancyViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """Для получения списка вакансии (активных) и возможность перехода к детальной странице с использованием slug"""
    serializer_class = VacancySerializer
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = VacancyPagination
    

    def get_queryset(self):
        return Vacancy.objects.filter(status=Vacancy.PUBLISHED)
