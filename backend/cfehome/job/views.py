import os

from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.conf import settings


from rest_framework import generics, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import *
from .serializers import *
from .permissions import *
from .paginations import *
from .forms import *

from pprint import pprint


class ReviewApiView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()


class BaseVacancyView(generics.ListAPIView):
    """Родительский класс для получение (активных) и создание вакансии. Для списка вакансии включена пагинация"""
    serializer_class = VacancySerializer
    pagination_class = VacancyPagination
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'responsibility_text',
                     'city__name', 'company__name']

    def get_queryset(self):
        return Vacancy.objects.filter(status=Vacancy.PUBLISHED)


class VacancyListView(BaseVacancyView):
    """Класс полностью наследуется от BaseVacancyView"""
    pass


class VacancyDetailtView(generics.RetrieveAPIView, BaseVacancyView):
    """
    Класс для детальной страницы вакансии. Наследуется от BaseVacancyView имеет логику вывода 
    похожих вакансии
    """
    lookup_field = 'slug'

    def get_similar_vacancies(self, vacancy):
        similar_vacancies = Vacancy.objects.filter(
            city=vacancy.city,
            status=Vacancy.PUBLISHED
        ).exclude(id=vacancy.id)[:3]
        return similar_vacancies

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        context = {'request': request}
        serializer = self.get_serializer(instance, context=context)
        similar_vacancies = self.get_similar_vacancies(instance)
        similar_serializer = VacancySerializer(
            similar_vacancies, many=True, context=context)

        data = {
            'vacancy_details': serializer.data,
            'similar_vacancies': similar_serializer.data
        }
        return Response(data)


# @method_decorator(csrf_protect, name='dispatch')
class LiteContactView(APIView):
    """Получает данные с формы и возвращет статус действии (с предварительной защитой CSRF)"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LiteContactSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data['phone_number'],
                  serializer.validated_data['full_name'])
            message = _('Message was sent succesfully')
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
            message = _('Data not found')
            return Response({'message': message}, status=status.HTTP_404_NOT_FOUND)

        serializer = ResponseVacancySerializer(data=request.data)
        if serializer.is_valid():
            """Готовый функционал отправка пиьсем через SMTP"""
            vacancy_title = vacancy.name
            applicant_full_name = serializer.validated_data['full_name']
            applicant_phone_number = serializer.validated_data['phone_number']
            applicant_email = serializer.validated_data['email']
            applicant_cv = request.FILES.get('cv_field')
            applicant_additional_text = serializer.validated_data['additional_text']

            # html = render_to_string('message.html', {
            #     'title': vacancy_title,
            #     'name': applicant_full_name,
            #     'phone_number': applicant_phone_number,
            #     'email': applicant_email,
            #     'file_folder': applicant_cv,
            #     'additional_text': applicant_additional_text,
            #     'logo_url': 'logo.svg'
            # })

            # email_subject = f"Application for {vacancy_title}"

            # # Sending the email with file attachment
            # email = EmailMessage(
            #     subject=email_subject,
            #     body=html,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=['snurzan21@gmail.com']

            # )

            # email.content_subtype = 'html'
            # email.send()

            print(vacancy_title, applicant_full_name,
                   applicant_phone_number, applicant_email,
                   applicant_cv, applicant_additional_text)

            message = _('Message was sent succesfully')
            return Response({'message': message}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @method_decorator(csrf_protect, name='dispatch')
class QuestionContactView(APIView):
    """Для ролучения вопроса с клиента в разделе "Конакты" (с предварительной защитой CSRF)"""
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = QuestionContactSerializer(data=request.data)
        if serializer.is_valid():
            applicant_full_name = serializer.validated_data['full_name']
            applicant_phone_number = serializer.validated_data['phone_number']
            applicant_email = serializer.validated_data['email']
            applicant_question_text = serializer.validated_data['question_text']

            """Готовый функционал отправка пиьсем через SMTP"""
            # html = render_to_string('message.html', {
            #     'name': applicant_full_name,
            #     'phone_number': applicant_phone_number,
            #     'email': applicant_email,
            #     'question': applicant_question_text
            # })

            # email_subject = f"Question from {applicant_email}"

            # # Sending the email with file attachment
            # email = EmailMessage(
            #     subject=email_subject,
            #     body=html,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=['snurzan21@gmail.com']  # Replace with desired recipient(s)
            # )

            # email.content_subtype = 'html'
            # email.send()

            print(applicant_full_name,
                   applicant_phone_number,
                   applicant_email,
                   applicant_question_text)

            message = _('Message was sent succesfully')
            return Response({'message': message}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


vacancy_list_view = VacancyListView.as_view()
vacancy_detail_view = VacancyDetailtView.as_view()
main_lite_form = LiteContactView.as_view()
response_vacancy_form = ResponseVacnacyView.as_view()
question_contact_form = QuestionContactView.as_view()
review_list_view = ReviewApiView.as_view()

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
