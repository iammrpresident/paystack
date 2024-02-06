import httpx

class ApiError(Exception):
    """
    Base class for API exceptions.
    """
    pass

class ApiRequestError(ApiError):
    """
    Raised when there is an issue with the API request.
    """
    def __init__(self, status, message):
        self.status = status
        self.message = message
        super().__init__(f"API request failed with status {status}: {message}")

class ApiResponseError(ApiError):
    """
    Raised when the API response is unexpected.
    """
    def __init__(self, status, message):
        self.status = status
        self.message = message
        super().__init__(f"API response error with status {status}: {message}")

class ApiAuthenticationError(ApiError):
    """
    Raised when there is an issue with API authentication.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(f"API authentication error: {message}")

class AsyncApiRequestError(ApiRequestError):
    """
    Raised when there is an issue with the API request in asynchronous code.
    """
    async def async_raise(self):
        raise ApiRequestError(self.status, self.message)

class AsyncApiResponseError(ApiResponseError):
    """
    Raised when the API response is unexpected in asynchronous code.
    """
    async def async_raise(self):
        raise ApiResponseError(self.status, self.message)

class AsyncApiAuthenticationError(ApiAuthenticationError):
    """
    Raised when there is an issue with API authentication in asynchronous code.
    """
    async def async_raise(self):
        raise ApiAuthenticationError(self.message)
