class WTFException(Exception):
    """
    WTF?
    """
    pass

class MissingArg(Exception):
    """
    Raised when a function is
    missing a argument.
    """
    pass

class FailedRequest(Exception):
    """
    Raised on a request that
    returns a HTTP status code
    besides 200.
    """
    pass

class InvalidToken(FailedRequest):
    """
    Raised when a 401 appears in
    a request.
    """
    pass

