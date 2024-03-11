import aiohttp
from .errors import APIError
from .utils import parse_response
from .constants import BASE_URL

class PaystackTransactions:
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.base_url = BASE_URL 
        self.headers = {
            'Authorization': f'Bearer {secret_key}',
            'Content-Type': 'application/json'
        }
        
    async def initialize_transaction(self, email, amount, reference=None, callback_url=None, plan=None, invoice_limit=None, metadata=None, subaccount=None, transaction_charge=None, bearer=None, channels=None):
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
    
    async def list_transactions(self, per_page=None, page=None, customer=None, status=None, _from=None, to=None, amount=None):
        params = {
            "perPage": per_page,
            "page": page,
            "customer": customer,
            "status": status,
            "from": _from,
            "to": to,
            "amount": amount
        }
        return await self._make_request("GET", "/transaction", params=params)
    
    async def fetch_transaction(self, transaction_id):
        return await self._make_request("GET", f"/transaction/{transaction_id}")
    
    async def charge_authorization(self, reference, authorization_code, amount, plan=None, currency=None, email=None, metadata=None, subaccount=None, transaction_charge=None, bearer=None):
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
        return await self._make_request("GET", f"/transaction/timeline/{id_or_reference}")
    
    async def transaction_totals(self, _from=None, to=None): 
        params = {
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/transaction/totals", params=params)
    
    async def export_transactions(self, _from, to, settled, payment_page, customer, currency, settlement, amount, status):
        params = {
            "from": _from,
            "to": to,
            "settled": settled,
            "payment_page": payment_page,
            "customer": customer,
            "currency": currency,
            "settlement": settlement,
            "amount": amount,
            "status": status
        }
        return await self._make_request("GET", "/transaction/export", params=params)
    
    async def request_reauthorization(self, reference, authorization_code, amount, currency=None, email=None, metadata=None):
        payload = {
            "reference": reference,
            "authorization_code": authorization_code,
            "amount": amount,
            "currency": currency,
            "email": email,
            "metadata": metadata
        }
        return await self._make_request("POST", "/transaction/request_reauthorization", payload)
    
    async def check_authorization(self, authorization_code, amount, email, currency=None):
        payload = {
            "authorization_code": authorization_code,
            "amount": amount,
            "email": email,
            "currency": currency
        }
        return await self._make_request("POST", "/transaction/check_authorization", payload)
    
    async def _make_request(self, method, endpoint, data=None, params=None):
        url = f"{self.base_url}{endpoint}"
        async with aiohttp.ClientSession() as session:
            async with session.request(method=method, url=url, json=data, headers=self.headers, params=params) as response:
                response_data = await response.json()  # Parse response as JSON
                if not response_data:
                    raise APIError("No response received", status_code=response.status)
                if response.status == 400:
                    raise APIError(response_data, status_code=response.status)
                return response_data

