class PyStackConfig:
    """
    Configuration class for Paystack wrapper
    """

    SECRET_KEY = "secret"
    API_URL = "https://api.paystack.co/"
    
    HEADERS = {
        'Authorization': 'Bearer {secret_key}',
        'Content-Type': 'application/json',
        'cache-control': 'no-cache',
    }