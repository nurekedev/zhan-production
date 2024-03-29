import os
import requests

from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import  ensure_csrf_cookie, requires_csrf_token
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.utils.translation import gettext as _
from django.conf import settings

from rest_framework import generics, permissions, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import  FormParser, MultiPartParser, FileUploadParser
from threading import Thread  


from .models import *
from .serializers import *
from .permissions import *
from .paginations import *
from .throttling import ContactThrottling

from dotenv import load_dotenv
import os

load_dotenv()

class SocialMediaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    lookup_field = 'name'  

    def get_object(self):
        name = self.kwargs.get(self.lookup_field)
        return self.queryset.get(name=name)


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





@method_decorator(ensure_csrf_cookie, name='dispatch')
class LiteContactView(APIView):
    """Получает данные с формы и возвращает статус действия (с предварительной защитой CSRF)"""
    permission_classes = [permissions.AllowAny]
    throttle_classes = [ContactThrottling]

    def send_email_async(self, html, email_subject):
        email = EmailMessage(
            subject=email_subject,
            body=html,
            from_email=settings.EMAIL_HOST_USER,
            to=[os.getenv('CUSTOMER_EMAIL')]
        )
        email.content_subtype = 'html'
        email.send()

    def post(self, request):
        serializer = LiteContactSerializer(data=request.data)
        if serializer.is_valid():
            applicant_full_name = serializer.validated_data['full_name']
            applicant_phone_number = serializer.validated_data['phone_number']

            html = render_to_string('contact.html', {
                'name': applicant_full_name,
                'phone_number': applicant_phone_number,
            })

            email_subject = f"Клиент оставил контакты ({applicant_full_name})"
            
            # Отправка почты в отдельном потоке
            email_thread = Thread(target=self.send_email_async, args=(html, email_subject))
            email_thread.start()

            message = _('Message was sent successfully')
            return Response({'message': message}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class LiteContactView(APIView):
#     """Получает данные с формы и возвращет статус действии (с предварительной защитой CSRF)"""
#     permission_classes = [permissions.AllowAny]
#     throttle_classes = [ContactThrottling]

#     def post(self, request):

#         serializer = LiteContactSerializer(data=request.data)
#         if serializer.is_valid():

            

#             applicant_full_name = serializer.validated_data['full_name']
#             applicant_phone_number = serializer.validated_data['phone_number']


#             html = render_to_string('contact.html', {
#                 'name': applicant_full_name,
#                 'phone_number': applicant_phone_number,
#             })

#             email_subject = f"Клиент оставил контакты ({applicant_full_name})"

            
#             email = EmailMessage(
#                 subject=email_subject,
#                 body=html,
#                 from_email=settings.EMAIL_HOST_USER,
#                 to=[os.getenv('CUSTOMER_EMAIL')]
#             )

#             email.content_subtype = 'html'
#             email.send()
#             message = _('Message was sent succesfully')
#             return Response({'message': message}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@method_decorator(ensure_csrf_cookie, name='dispatch')
class ResponseVacnacyView(APIView):
    """Получает данные с формы (ФИО, номер телефона, почта, резюме и скрытое поле(название вакансии))Возвращет статус действии (с предварительной защитой CSRF)"""
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.AllowAny]
    throttle_classes = [ContactThrottling]


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

            html = render_to_string('message.html', {
                'title': vacancy_title,
                'name': applicant_full_name,
                'phone_number': applicant_phone_number,
                'email': applicant_email,
                'file_folder': applicant_cv,
                'additional_text': applicant_additional_text,
            })

            email_subject = f"Отклик на вакансию {vacancy_title}"

            email = EmailMessage(
                subject=email_subject,
                body=html,
                from_email=settings.EMAIL_HOST_USER,
                to=[os.getenv('CUSTOMER_EMAIL')]
            )

            if applicant_cv: 
                email.attach(applicant_cv.name, applicant_cv.read(), applicant_cv.content_type)


            email.content_subtype = 'html'
            email.send()

            print(vacancy_title, applicant_full_name,
                  applicant_phone_number, applicant_email,
                  applicant_cv, applicant_additional_text)

            message = _('Message was sent succesfully')
            return Response({'message': message}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class QuestionContactView(APIView):
    """Для получения вопроса с клиента в разделе 'Контакты' (с предварительной защитой CSRF)"""
    permission_classes = [permissions.AllowAny]
    throttle_classes = [ContactThrottling]

    def send_email_async(self, html, email_subject):
        email = EmailMessage(
            subject=email_subject,
            body=html,
            from_email=settings.EMAIL_HOST_USER,
            to=[os.getenv('CUSTOMER_EMAIL')]
        )
        email.content_subtype = 'html'
        email.send()

    def post(self, request):
        serializer = QuestionContactSerializer(data=request.data)
        if serializer.is_valid():
            applicant_full_name = serializer.validated_data['full_name']
            applicant_phone_number = serializer.validated_data['phone_number']
            applicant_email = serializer.validated_data['email']
            applicant_question_text = serializer.validated_data['question_text']

            html = render_to_string('question.html', {
                'name': applicant_full_name,
                'phone_number': applicant_phone_number,
                'email': applicant_email,
                'question': applicant_question_text
            })

            email_subject = f"Вопрос от клиента: {applicant_email}"

            # Отправка почты в отдельном потоке
            email_thread = Thread(target=self.send_email_async, args=(html, email_subject))
            email_thread.start()

            message = _('Message was sent successfully')
            return Response({'message': message}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







vacancy_list_view = VacancyListView.as_view()
vacancy_detail_view = VacancyDetailtView.as_view()
main_lite_form = LiteContactView.as_view()
response_vacancy_form = ResponseVacnacyView.as_view()
question_contact_form = QuestionContactView.as_view()
social_media_list_view = SocialMediaRetrieveAPIView.as_view()


