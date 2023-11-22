from django import forms
from django.core.validators import RegexValidator, FileExtensionValidator
from django.core.exceptions import ValidationError

"""
Ничего полезного!
"""

# def file_size(value):
#     limit = 5 * 1024 * 1024
#     if value.size > limit:
#         raise ValidationError('File too large. Size should not exceed 5 MiB.')


# class MainPageForm(forms.Form):

#     full_name = forms.CharField(initial='Enter the full name', max_length=100)
#     phone_regex = RegexValidator(
#         regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = forms.CharField(
#         validators=[phone_regex], initial='Enter the phone number')
#     email = forms.EmailField(initial='Enter the email address')
#     supported_file_formats = ['pdf', 'png']
#     max_file_size_mb = 20
#     cv_field = forms.FileField(
#         validators=[
#             FileExtensionValidator(allowed_extensions=supported_file_formats), file_size]
#     )
