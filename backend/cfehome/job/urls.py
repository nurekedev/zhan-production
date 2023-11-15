from django.urls import path, include
from .views import *

urlpatterns = [
    path('', VacancyAPIList.as_view()),
]