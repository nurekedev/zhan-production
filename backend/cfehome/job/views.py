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


class BaseVacancyView(generics.ListAPIView):
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
            print(serializer.validated_data['phone_number'],
                  serializer.validated_data['full_name'])
            message = ('Message was sent succesfully')
            return Response({'message': message}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @method_decorator(csrf_protect, name='dispatch')
class ResponseVacnacyView(APIView):
    """Получает данные с формы (ФИО, номер телефона, почта, резюме и скрытое поле(название вакансии))Возвращет статус действии (с предварительной защитой CSRF)"""
    permission_classes = [permissions.AllowAny]

    def post(self, request, slug):
        try:
            vacancy = Vacancy.objects.get(slug=slug)
        except Vacancy.DoesNotExist:
            return Response({'error': 'Vacancy not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ResponseVacancySerializer(data=request.data)
        if serializer.is_valid():
            vacancy_title = vacancy.name
            applicant_full_name = serializer.validated_data['full_name']
            applicant_phone_number = serializer.validated_data['phone_number']
            applicant_email = serializer.validated_data['email']
            applicant_cv = request.FILES.get('cv_field')

            print(vacancy_title, applicant_full_name,
                  applicant_phone_number, applicant_email, applicant_cv)

            message = 'Response submitted successfully'
            return Response({'message': message}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


vacancy_list_view = VacancyListView.as_view()
vacancy_detail_view = VacancyDetailtView.as_view()
main_lite_form = LiteContactView.as_view()
response_vacancy_form = ResponseVacnacyView.as_view()


"""
Хранилище! Не обращать внимание! 
"""
# class VacancyViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
#     """Для получения списка вакансии (активных) и возможность перехода к детальной странице с использованием slug"""
#     serializer_class = VacancySerializer
#     lookup_field = 'slug'
#     permission_classes = [IsAdminOrReadOnly]
#     pagination_class = VacancyPagination


#     def get_queryset(self):
#         return Vacancy.objects.filter(status=Vacancy.PUBLISHED)
