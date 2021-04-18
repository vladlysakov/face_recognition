from django.core.validators import RegexValidator

from face.common.regex.constants import Phone, StudentCard

__all__ = ['PHONE', 'STUDENT_CARD']

PHONE = RegexValidator(regex=Phone.RE, message=Phone.EXCEPTION_MESSAGE)
STUDENT_CARD = RegexValidator(regex=StudentCard.RE, message=StudentCard.EXCEPTION_MESSAGE)
