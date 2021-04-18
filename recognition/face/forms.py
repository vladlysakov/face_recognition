from django import forms

from face.common.regex.validators import STUDENT_CARD, PHONE

__all__ = ['User']


class User(forms.ModelForm):
    address = forms.CharField(max_length=30, empty_value='', required=False)
    birthday = forms.DateField(required=False)
    email = forms.EmailField()
    phone_number = forms.CharField(validators=[PHONE], required=False)
    student_id = forms.CharField(validators=[STUDENT_CARD], required=False)
