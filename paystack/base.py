import asyncio
import httpx
from .config import PyStackConfig

class PyStackBase:
    """
    Shared state using the Borg design pattern
    """
    _instance_state = {}

    def __init__(self, **kwargs):
        """
        Ensure shared state is maintained among instances.
        Retrieve secret key and authorization from kwargs or config.
        Initialize headers and API base URL.
        Create PyStackRequests instance if not already present.
        """

        self.__dict__ = self._instance_state

        authorization_header = PyStackConfig.HEADERS.get('Authorization', '')
        secret_key = kwargs.get('secret_key', PyStackConfig.SECRET_KEY)
        authorization = kwargs.get('authorization', f"{authorization_header.format(secret_key)}")


        self.headers = {'Authorization': authorization}
        self.api_base_url = kwargs.get('api_url', PyStackConfig.API_URL)
        self.async_requests = None  

    async def get_requests_instance(self):
        if self.async_requests is None:
            self.async_requests = await self._create_requests_instance()
        return self.async_requests

    async def _create_requests_instance(self):
        return PyStackRequests(api_base_url=self.api_base_url, headers=self.headers)


class PyStackRequests:
    def __init__(self, api_base_url='', headers=None):
        """
        Initialize API base URL and headers.
        """
        self.API_BASE_URL = api_base_url
        self.headers = headers or {}
        self.client = httpx.AsyncClient()

    async def _request(self, method, resource_uri, **kwargs):
        """
        Perform a method on a resource.
        Make HTTP request using the specified method.
        Check for HTTP errors and raise an exception if necessary.
        Return the JSON response.
        """
        data = kwargs.get('data')
        qs = kwargs.get('qs')

        response = await method(
            f"{self.API_BASE_URL}{resource_uri}",
            json=data, headers=self.headers,
            params=qs
        )

        response.raise_for_status()
        return response.json()

    async def get(self, endpoint, **kwargs):
        """
        Get a resource using the specified endpoint.
        """
        return await self._request(self.client.get, endpoint, **kwargs)

    async def post(self, endpoint, **kwargs):
        """
        Create a resource using the specified endpoint.
        """
        return await self._request(self.client.post, endpoint, **kwargs)

    async def put(self, endpoint, **kwargs):
        """
        Update a resource using the specified endpoint.
        """
        return await self._request(self.client.put, endpoint, **kwargs)
