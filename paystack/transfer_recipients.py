from .base import PaystackBase

class PaystackTransferRecipient(PaystackBase):
    async def create_transfer_recipient(self, type, name, account_number, bank_code, description=None, currency=None, authorization_code=None, metadata=None):
        payload = {
            "type": type,
            "name": name,
            "account_number": account_number,
            "bank_code": bank_code,
            "description": description,
            "currency": currency,
            "authorization_code": authorization_code,
            "metadata": metadata
        }
        return await self._make_request("POST", "/transferrecipient", payload)
    
    async def bulk_create_transfer_recipient(self, batch):
        payload = {
            "batch": batch
        }
        return await self._make_request("POST", "/transferrecipient/bulk", payload)
    
    async def list_transfer_recipients(self, perPage, page, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/transferrecipient", params=params)
    
    async def fetch_transfer_recipient(self, id_or_code):
        return await self._make_request("GET", f"/transferrecipient/{id_or_code}")
    
    async def update_transfer_recipient(self, id_or_code, name, email=None):
        payload = {
            "name": name,
            "email": email
        }
        return await self._make_request("PUT", f"/transferrecipient/{id_or_code}", payload)
    
    async def delete_transfer_recipient(self, id_or_code):
        return await self._make_request("DELETE", f"/transferrecipient/{id_or_code}")