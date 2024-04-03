from .base import PaystackBase

class PaystackTransfers(PaystackBase):
    async def initiate_transfer(self, source, amount, recipient, reason=None, currency=None, reference=None):
        payload = {
            "source": source,
            "amount": amount,
            "recipient": recipient,
            "reason": reason,
            "currency": currency,
            "reference": reference
        }
        return await self._make_request("POST", "/transfer", payload)
    
    async def finalize_transfer(self, transfer_code, otp):
        payload = {
            "transfer_code": transfer_code,
            "otp": otp
        }
        return await self._make_request("POST", "/transfer/finalize_transfer", payload)
    
    async def initiate_bulk_transfer(self, source, transfer):
        payload = {
            "source": source,
            "transfer": transfer
        }
        return await self._make_request("POST", "/transfer/bulk", payload)
    
    async def list_transfer(self, perPage, page, customer, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "customer": customer,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/transfer", params=params)
    
    async def fetch_transfer(self, id_or_code):
        return await self._make_request("GET", f"/transfer/{id_or_code}")
    
    async def verify_transfer(self, reference):
        return await self._make_request("POST", f"/transfer/{reference}")