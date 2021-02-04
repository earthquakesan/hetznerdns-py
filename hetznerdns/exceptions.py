class ApiTokenNotSetException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class ZoneNotExistException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class MultipleZonesReturnedException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class GetRequestException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class PostRequestException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class DeleteRequestException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

class RecordNotExistException(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)

