import httpx 
from .pagination import Pagination
from .http_client import PyStackApiClient
from .request_builder import RequestBuilder

class TransactionManager:
    """
    Manager class for handling transactions in the Paystack API.
    """

    def __init__(self, api_client):
        """
        Initialize the TransactionManager with the API client.
        """
        self.api_client = api_client

    def initialize_transaction(self, amount, email, currency=None, reference=None, callback_url=None, **kwargs):
        """
        Initialize a transaction.
        """
        payload = RequestBuilder.build_initialize_transaction_payload(
            amount, email, currency, reference, callback_url, **kwargs
        )
        response = self.api_client.make_request(httpx.post, 'transaction/initialize', data=payload)
        return response

    def charge_authorization(self, amount, email, authorization_code, reference=None, **kwargs):
        """
        Charge an authorization.
        """
        payload = RequestBuilder.build_charge_authorization_payload(
            amount, email, authorization_code, reference, **kwargs
        )
        response = self.api_client.make_request(httpx.post, 'transaction/charge_authorization', data=payload)
        return response

    def verify_transaction(self, reference):
        """
        Verify the status of a transaction.
        """
        response = self.api_client.make_request(httpx.get, f'transaction/verify/{reference}')
        return response

    def list_transactions(self, per_page=50, page=1, **kwargs):
        """
        List transactions with optional parameters for filtering.
        """
        params = {'per_page': per_page, 'page': page, **kwargs}
        response = self.api_client.make_request(httpx.get, 'transaction', params=params)
        total = response['meta']['total']
        page_count = response['meta']['pageCount']
        return response['data'], Pagination(total, per_page, page, page_count)

    def fetch_transaction(self, transaction_id):
        """
        Fetch details of a specific transaction.
        """
        response = self.api_client.make_request(httpx.get, f'transaction/{transaction_id}')
        return response

    def view_transaction_timeline(self, transaction_id):
        """
        View the timeline of a transaction.
        """
        response = self.api_client.make_request(httpx.get, f'transaction/timeline/{transaction_id}')
        return response

    def get_transaction_totals(self, per_page=50, page=1, **kwargs):
        """
        Get total amount received on your account with optional parameters for filtering.
        """
        params = {'per_page': per_page, 'page': page, **kwargs}
        response = self.api_client.make_request(httpx.get, 'transaction/totals', params=params)
        total = response['meta']['total']
        page_count = response['meta']['pageCount']
        return response['data'], Pagination(total, per_page, page, page_count)

    def export_transactions(self, per_page=50, page=1, **kwargs):
        """
        Export a list of transactions with optional parameters for filtering.
        """
        params = {'per_page': per_page, 'page': page, **kwargs}
        response = self.api_client.make_request(httpx.get, 'transaction/export', params=params)
        return response
