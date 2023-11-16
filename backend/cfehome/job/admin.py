from typing import Any
from django.contrib import admin
from .models import *

# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)


class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy
    list_display = ('name', 'slug', 'model_pic', 'salary', 'body', 'city',
                    'company', 'publish', 'created', 'status', 'user')
    fields = ('name', 'slug', 'model_pic', 'salary', 'body', 'city',
                    'company', 'publish', 'status')
    prepopulated_fields = {'slug': ('name', )}

    def save_form(self, request, form, change):
        obj = form.save(commit=False)
        if not obj.pk:  
            obj.user = request.user
        obj.save()
        return obj


admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
