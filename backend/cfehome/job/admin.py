from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from .models import *

# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy
    list_display = ('name', 'slug', 'model_pic', 'salary', 'responsibility_text', 'schedule', 'city',
                    'company', 'working_condition_text', 'accommodation', 'nutrition', 'additional_text', 'publish', 'created', 'status', 'user')
    fields = ('name', 'slug', 'model_pic', 'salary', 'responsibility_text', 'schedule', 'city',
              'company', 'working_condition_text', 'accommodation', 'nutrition', 'additional_text', 'publish', 'status',)
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ('salary', 'name', 'publish', 'user', 'city', 'company',)
    search_fields = ('user', 'salary', 'name', 'publish', 'city', 'company',)
    ordering = ('salary',)

    def save_form(self, request, form, change):
        obj = form.save(commit=False)
        if not obj.pk:
            obj.user = request.user
        obj.save()
        return obj


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'body_text',)
    list_filter = ('author',)
    search_fields = ('author', 'body_text', )
    ordering = ('author',)


admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Review, ReviewAdmin)


# class VacancyAdmin(admin.ModelAdmin):
#     model = Vacancy
#     list_display = ['name', 'slug', 'model_pic', 'salary', 'body', 'city',
#                     'company', 'publish', 'created', 'status', 'user']
#     fields = ['name', 'slug', 'model_pic', 'salary', 'body', 'city',
#                     'company', 'publish', 'status']
#     prepopulated_fields = {'slug': ('name', )}
#     list_filter = ['salary', 'name', 'publish', 'user']
#     search_fields = ['user', 'body_text', 'salary', 'name', 'publish']
#     ordering = ['salary']

#     def save_form(self, request, form, change):
#         obj = form.save(commit=False)
#         if not obj.pk:
#             obj.user = request.user
#         obj.save()
#         return obj

# class ReviewAdmin(admin.ModelAdmin):
#     """Базовые настройки для модели "Отзыв". Для текста было использовано редактор WYSIWYG"""
#     list_display = ['author', 'body_text']
#     list_filter = ['author']
#     search_fields = ['author', 'body_text']
#     ordering = ['author']


# admin.site.register(City, CityAdmin)
# admin.site.register(Company, CompanyAdmin)
# admin.site.register(Vacancy, VacancyAdmin)
# admin.site.register(Review, ReviewAdmin)
