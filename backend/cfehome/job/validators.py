from rest_framework.validators import UniqueValidator
from .models import Vacancy, Company, City
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import re

from django.utils.translation import gettext as _


"""Не обращать внимание"""
# unique_vacancy_title = UniqueValidator(queryset=Vacancy.PUBLISHED, lookup='iexact')

def validate_phone_number(value):
    """
    Валидатор для проверки номера телефона на содержание цифр и на длину (до 15)
    """
    phone_regex = r'^\+?1?\d{9,15}$'
    if not re.match(phone_regex, value):
        raise ValidationError(_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))

def validate_file_size(value):
    """
    Валидатор для проверки размера файла. Размер не должен превышать 10 MiB 
    """
    limit = 10 * 1024 * 1024 
    if value.size > limit:
        raise ValidationError(_("File too large. Size should not exceed 10 MiB."))
    
def validate_file_extension(value):
    """
    Валидатор для проверки расширения файла. Принимаются форматы: '.pdf', '.png' 
    """
    allowed_extensions = ['pdf', 'png']
    validator = FileExtensionValidator(allowed_extensions)

    try:
        validator(value)
    except ValidationError:
        allowed_extensions_str = ', '.join(allowed_extensions)
        error_message = _("Unsupported file extension. Allowed extensions are %(extensions)s") % {'extensions': allowed_extensions_str}
        raise ValidationError(error_message)