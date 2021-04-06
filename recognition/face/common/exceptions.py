from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _


class EncodingFaceException(APIException):
    status_code = 500
    default_detail = _('Error in face encoding')
    default_code = 'encoding_error'


class RecognitionDataException(APIException):
    status_code = 500
    default_detail = _('There is no data for recognition current user.')
    default_code = 'recognition_error'
