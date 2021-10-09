class ApiException(Exception):
    """
    Base class for all custom exceptions.
    """

    def __init__(self, message=None):
        if message is None:
            message = "An Api application level exception occurred."
        super(ApiException, self).__init__(message)


class TableFormatException(ApiException):
    """
    This class is for handling Invalid Table format given in tcon file.
    """

    def __init__(self, message=None):
        if message is None:
            message = "The tcon file is incorrect."
        super(ApiException, self).__init__(message)


