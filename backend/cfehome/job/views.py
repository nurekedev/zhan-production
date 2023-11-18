from django.shortcuts import render
from django.core.mail import send_mail

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
    serializer_class = VacancySerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = VacancyPagination

    def get_queryset(self):
        return Vacancy.objects.filter(status=Vacancy.PUBLISHED)


class VacancyListView(BaseVacancyView):
    pass

class VacancyDetailtView(generics.RetrieveAPIView, BaseVacancyView):
    lookup_field = 'slug'



class LiteContactView(APIView):
    def post(self, request):
        serializer = LiteContactSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            send_mail('SUBJECT', 'MESSAGE', 'noreplay@zhan.team', ['kuanyshbek135@gmail.com', 'snurzan21@gmail.com'], 'fer')
            return Response({'message': 'Ваше сообщение успешно отправлено'}, status=status.HTTP_200_OK)
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
