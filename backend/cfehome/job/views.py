from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _


from rest_framework import generics, viewsets, mixins, authentication, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from .permissions import *
from .paginations import *
from .forms import *

# Create your views here.


class BaseVacancyView(generics.ListCreateAPIView):
    """Родительский класс для получение (активных) и создание вакансии. Для списка вакансии включена пагинация"""
    serializer_class = VacancySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = VacancyPagination

    def get_queryset(self):
        return Vacancy.objects.filter(status=Vacancy.PUBLISHED)


class VacancyListView(BaseVacancyView):
    """Класс полностью наследуется от BaseVacancyView"""
    pass


class VacancyDetailtView(generics.RetrieveAPIView, BaseVacancyView):
    """Класс для детальной страницы вакансии. Наследуется от BaseVacancyView"""
    lookup_field = 'slug'


# @method_decorator(csrf_protect, name='dispatch')
class LiteContactView(APIView):
    """Получает данные с формы и возвращет статус действии (с предварительной защитой CSRF)"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LiteContactSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data['email'], serializer.validated_data['action_type'])
            message = _('Ваше сообщение успешно отправлено')
            return Response({'message': message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


vacancy_list_view = VacancyListView.as_view()
vacancy_detail_view = VacancyDetailtView.as_view()
main_lite_form = LiteContactView.as_view()


# class VacancyViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
#     """Для получения списка вакансии (активных) и возможность перехода к детальной странице с использованием slug"""
#     serializer_class = VacancySerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]
#     pagination_class = VacancyPagination


#     def get_queryset(self):
#         return Vacancy.objects.filter(status=Vacancy.PUBLISHED)
