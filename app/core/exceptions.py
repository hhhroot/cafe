from rest_framework import status
from rest_framework.exceptions import APIException

DEFAULT_BAD_REQUEST = 10000
ALREADY_EXIST_INSTANCE = 10001


class BaseAPIException(APIException):
    """
    https://hakibenita.com/working-with-apis-the-pythonic-way
    Used as BaseValidationException
    """

    status_code = status.HTTP_400_BAD_REQUEST


class DefaultBadRequest(BaseAPIException):
    default_detail = "400. That's an error - we'll investigate what went wrong. Thank you for your patience."
    default_code = DEFAULT_BAD_REQUEST


class AlreadyExistInstance(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Instance already exist."
    default_code = ALREADY_EXIST_INSTANCE
