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
        if self.status_code:
            return f"APIError: {self.status_code} - {self.response}"
        else:
            return f"APIError: {self.response}"