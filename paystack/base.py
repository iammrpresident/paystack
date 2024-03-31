import aiohttp
from .errors import APIError
from .constants import BASE_URL

class PaystackBase:
    """Base class for interacting with the Paystack API."""
    
    
    def __init__(self, secret_key, session=None):
        """Initialize the PaystackBase instance.
        
        Args:
            secret_key (str): The Paystack secret key.
            session (aiohttp.ClientSession, optional): An existing aiohttp ClientSession
                to reuse for making HTTP requests. If not provided, a new session will be created.
        """
        self.secret_key = secret_key
        self.base_url = BASE_URL 
        self.headers = {
            'Authorization': f'Bearer {secret_key}',
            'Content-Type': 'application/json'
        }
        self.session = session or aiohttp.ClientSession() 
        
        
    async def _make_request(self, method, endpoint, data=None, params=None):
        """Make an HTTP request to the Paystack API."""
        url = f"{self.base_url}{endpoint}"
        async with self.session.request(method=method, url=url, json=data, headers=self.headers, params=params) as response:
            response_data = await response.json()
            if not response_data:
                raise APIError("No response received", status_code=response.status)
            if response.status == 400:
                raise APIError(response_data, status_code=response.status)
            return response_data