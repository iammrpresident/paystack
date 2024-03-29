import aiohttp
from .errors import APIError
from .constants import BASE_URL

class PaystackTransactions:
    """Wrapper class for interacting with the Paystack Transactions API."""

    def __init__(self, secret_key, session=None):
        """Initialize the PaystackTransactions instance.
        
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
        self.session = session or aiohttp.ClientSession()  # Create a session for making requests
        
    async def initialize_transaction(self, email, amount, reference=None, callback_url=None, plan=None, invoice_limit=None, metadata=None, subaccount=None, transaction_charge=None, bearer=None, channels=None):
        """Initialize a new transaction.
        
        Args:
            email (str): The email address of the customer.
            amount (int): The amount to charge the customer in kobo.
            reference (str, optional): A unique reference for the transaction.
            callback_url (str, optional): URL to redirect to after payment.
            plan (str, optional): ID of the payment plan.
            invoice_limit (int, optional): The maximum number of invoices that can be generated against this transaction.
            metadata (dict, optional): Additional data to attach to the transaction.
            subaccount (str, optional): ID of the subaccount that owns the payment.
            transaction_charge (int, optional): The transaction charge in kobo.
            bearer (str, optional): Who bears the transaction charges.
            channels (list, optional): List of payment channels to restrict the transaction to.
        
        Returns:
            dict: The initialized transaction response.
        """
        if not email:
            raise ValueError("Email is required for initializing a transaction")
        if not amount or amount <= 0:
            raise ValueError("Amount must be a positive number")
        
        payload = {
            "email": email,
            "amount": amount,
            "reference": reference,
            "callback_url": callback_url,
            "plan": plan,
            "invoice_limit": invoice_limit,
            "metadata": metadata,
            "subaccount": subaccount,
            "transaction_charge": transaction_charge,
            "bearer": bearer,
            "channels": channels,
        }
        return await self._make_request("POST", "/transaction/initialize", payload)
    
    async def verify_transaction(self, reference):
        
        return await self._make_request("GET", f"/transaction/verify/{reference}")
    
    async def list_transactions(self, perPage=None, page=None, customer=None, status=None, _from=None, to=None, amount=None):
        payload = {
            "perPage": perPage,
            "page": page,
            "customer": customer,
            "status": status,
            "from": _from,
            "to": to,
            "amount": amount
        }
        return await self._make_request("GET", "/transaction", payload)
    
    async def fetch_transaction(self, id):
        return await self._make_request("GET", f"/transaction/{id}")
    
    async def charge_authorization(self, email, amount, authorization_code, reference=None, plan=None, currency=None, metadata=None, subaccount=None, transaction_charge=None, bearer=None):
        payload = {
            "reference": reference,
            "authorization_code": authorization_code,
            "amount": amount,
            "plan": plan,
            "currency": currency,
            "email": email,
            "metadata": metadata,
            "subaccount": subaccount,
            "transaction_charge": transaction_charge,
            "bearer": bearer
        }
        return await self._make_request("POST", "/transaction/charge_authorization", payload)
    
    async def view_transaction_timeline(self, id_or_reference):
        return await self._make_request("GET", f"/transaction/timeline/:{id_or_reference}")
    
    async def transaction_totals(self, perPage=None, page=None): 
        payload = {
            "perPage": perPage,
            "page": page
        }
        return await self._make_request("GET", "/transaction/totals", payload)
    
    async def export_transactions(self, perPage, page, settled=None, payment_page=None, customer=None, currency=None, settlement=None, amount=None, status=None, _from=None, to=None):
        payload = {
            "perPage": perPage,
            "page": page,
            "settled": settled,
            "payment_page": payment_page,
            "customer": customer,
            "currency": currency,
            "settlement": settlement,
            "amount": amount,
            "status": status,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/transaction/export", payload)
    
    async def request_reauthorization(self, email, authorization_code, amount, currency=None,  reference=None, metadata=None):
        payload = {
            "reference": reference,
            "authorization_code": authorization_code,
            "amount": amount,
            "currency": currency,
            "email": email,
            "metadata": metadata
        }
        return await self._make_request("POST", "/transaction/request_reauthorization", payload)
    
    async def _make_request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        async with self.session.request(method=method, url=url, json=data, headers=self.headers, params=params) as response:
            response_data = await response.json()
            if not response_data:
                raise APIError("No response received", status_code=response.status)
            if response.status == 400:
                raise APIError(response_data, status_code=response.status)
            return response_data
