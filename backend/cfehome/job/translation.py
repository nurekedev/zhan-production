from .models import Vacancy
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


