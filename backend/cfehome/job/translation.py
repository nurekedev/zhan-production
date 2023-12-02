from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Vacancy)
class VacancyTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'responsibility_text',
        'requirement_text',
        'schedule',
        'working_condition_text',
        'accommodation',
        'nutrition',
        'additional_text',
    )


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )

@register(Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )

@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = (
        'body_text',
    )


