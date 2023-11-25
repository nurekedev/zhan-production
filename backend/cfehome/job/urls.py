from django.urls import path, include
from .views import *

urlpatterns = [
    path('', vacancy_list_view),
    path('<slug:slug>/', vacancy_detail_view, name='vacancy-detail'),
    path('<slug:slug>/submit/', ResponseVacnacyView.as_view(), name='submit-response-to-vacancy'),
]