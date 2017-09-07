from rest_framework.exceptions import APIException


class GenericException(APIException):
    detail = None
    exception_code = None
    status_code = 400  # User will always see Bad request 400 HTTP status code

    def __init__(self, detail, http_code=400):
        """
        constructor method which will be called in case error is raised
        we log the error message
        """
        self.detail = detail
