import httpx
from .errors import ApiRequestError, ApiResponseError

class PyStackApiClient:
    """
    HTTP Client class for making requests to Paystack.
    """

    def __init__(self, base_url, headers):
        """
        Initialize the HTTP client with the base URL and headers.
        """
        self.base_url = base_url
        self.headers = headers

    async def make_request(self, method, endpoint, data=None, params=None):
        """
        Make an asynchronous HTTP request to the API.
        """
        url = f"{self.base_url}{endpoint}"

        try:
            async with httpx.AsyncClient() as client:
                response = await method(url, json=data, headers=self.headers, params=params)

                # Check for HTTP errors and raise an exception if necessary
                response.raise_for_status()

                return response.json()

        except httpx.HTTPError as http_err:
            # Handle HTTP errors (e.g., 400, 401, 404, 500)
            raise ApiRequestError(response.status_code, str(http_err))

        except httpx.RequestError as req_err:
            # Handle general request errors
            raise ApiRequestError(0, str(req_err))

        except Exception as err:
            # Handle other unexpected errors
            raise ApiRequestError(0, str(err))
