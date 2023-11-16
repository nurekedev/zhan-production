from rest_framework import pagination

class VacancyPagination(pagination.PageNumberPagination):
    """Класс постраничной пагинации"""
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100