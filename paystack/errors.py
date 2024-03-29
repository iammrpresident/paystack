class PaystackError(Exception):
    """Base class for Paystack API errors."""
    pass

class AuthenticationError(PaystackError):
    """Error raised for authentication-related issues."""
    pass

class APIError(PaystackError):
    """Error raised for API-related issues."""
    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response
        
    def __str__(self):
        if self.status_code == 400:
            return f"Bad Request: {self.response}"
        elif self.status_code == 401:
            return f"Unauthorized: {self.response}"
        elif self.status_code == 404:
            return f"Not Found: {self.response}"
        elif self.status_code == 500:
            return f"Internal Server Error: {self.response}"
        else:
            return f"API Error: {self.response}"