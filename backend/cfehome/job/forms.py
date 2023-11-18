from django import forms
from django.core.validators import EmailValidator


# class MainPageForm(forms.Form):

#     STUDY = 'study'
#     VACANCY = 'vacancy'

#     ACTION_CHOICES = (
#         (STUDY, 'Учеба'),
#         (VACANCY, 'Работа')
#     )


#     full_name = forms.CharField(max_length=100)
#     email = forms.CharField(validators=[EmailValidator()])

#     action_type = forms.CharField(max_length=20, choices=ACTION_CHOICES)
    