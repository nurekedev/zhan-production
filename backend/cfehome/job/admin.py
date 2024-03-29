from django.contrib import admin, messages
from django.utils.translation import gettext as _

from modeltranslation.admin import TranslationAdmin

from .models import *

# Register your models here.


class JobAdminArea(admin.AdminSite):
    site_header = "Zan-Production"
    site_title = _("Sign in | Administration")


class CityAdmin(TranslationAdmin):
    list_display = ('name',)


class CompanyAdmin(TranslationAdmin):
    list_display = ('name',)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'url',)


BASIC_INFORMATION = """
    <li>Name (Title of vacancy)</li>
    <li>Slug (DO NOT FILL OUT FIELD)</li>
    <li>Picture (Preview Image of vacancy)</li>
    <li>Salary (Numeric field. Ex: 1200, 1200.5 etc)</li>
"""

DEATAILED_INFORMATION = """
    <li>Fill out these fields in 3 languages</li>
"""

SECONDARY_INFORMATION = """
    <li>Status: Select "Published" to display on the site</li>
"""


class VacancyAdmin(TranslationAdmin):
    model = Vacancy
    list_display = ('name', 'slug', 'salary', 'city', 'company',
                    'additional_text', 'publish', 'created', 'status', 'user')

    prepopulated_fields = {'slug': ('name', )}

    fieldsets = (
        ('Basic vacancy info', {
            'fields': ('name', 'slug', 'model_pic', 'salary',),
            'description': BASIC_INFORMATION,
        }),
        ('Vacancy destail (EN)', {
            'fields': ('responsibility_text', 'schedule', 'working_condition_text', 'accommodation', 'nutrition', 'additional_text',),
            'description': DEATAILED_INFORMATION,
        }),
        ('Secondary info', {
            'fields': ('city', 'company', 'publish', 'status',),
            'description': SECONDARY_INFORMATION,
        }),
    )

    list_editable = ('status',)

    list_filter = ('status', 'publish', 'user', 'city', 'company',)
    search_fields = ['name__startswith', 'city__name', 'company__name',]
    ordering = ('salary',)
    actions = ['set_published', 'set_draft',]

    @admin.action(description="Set Published for Vacancies")
    def set_published(self, request, queryset):
        count = queryset.update(status=Vacancy.PUBLISHED)
        self.message_user(request, f"Changed {count} notes")

    @admin.action(description="Set Draft for Vacancies")
    def set_draft(self, request, queryset):
        count = queryset.update(status=Vacancy.DRAFT)
        self.message_user(request, f"Changed {count} notes", messages.WARNING)

    def save_form(self, request, form, change):
        obj = form.save(commit=False)
        if not obj.pk:
            obj.user = request.user
        obj.save()
        return obj


class ReviewAdmin(TranslationAdmin):
    list_display = ('author', 'author_pic', 'body_text',)
    list_filter = ('author',)
    search_fields = ('author', 'body_text', )
    ordering = ('author',)


admin.site.register(City, CityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)

