from .base import PaystackBase

class PaystackRefund(PaystackBase):
    async def create_refund(self, transaction, amount=None, currency=None, customer_note=None, merchant_note=None):
        payload = {
            "transaction": transaction,
            "amount": amount,
            "currency": currency,
            "customer_note": customer_note,
            "merchant_note": merchant_note
        }
        return await self._make_request("POST", "/refund", payload)
    
    async def list_refund(self, reference, currency, _from=None, to=None, perPage=None, page=None):
        params = {
            "reference": reference,
            "currency": currency,
            "from": _from,
            "to": to,
            "perPage": perPage,
            "page": page
        }
        return await self._make_request("GET", "/refund", params=params)
    
    async def fetch_refund(self, reference):
        return await self._make_request("GET", f"/refund/{reference}")