class ApiException(Exception):
    """
    Base class for all custom exceptions.
    """

    def __init__(self, message=None):
        if message is None:
            message = "An Api application level exception occurred."
        super(ApiException, self).__init__(message)


class LocationException(ApiException):
    """
    This class is for handling Invalid Location.
    """

    def __init__(self, message=None):
        if message is None:
            message = "The location is incorrect."
        super(ApiException, self).__init__(message)


class CityNotFoundException(ApiException):
    """
    This can be raised if city name is not found. Not implemented in the climate api.
    """

    def __init__(self, message):
        super(CityNotFoundException, self).__init__(message)


