from .base import PaystackBase

class PaystackBulkCharge(PaystackBase):
    async def initiate_bulk_charge(self, authorization_code, amount, reference):
        payload = {
            "authorization_code": authorization_code,
            "amount": amount,
            "reference": reference
        }
        return await self._make_request("POST", "/bulkcharge", payload)
    
    async def list_bulk_charge(self, perPage, page, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/bulkcharge", params=params)
    
    async def fetch_bulk_charge_batch(self, id_or_code):
        return await self._make_request("GET", f"/bulkcharge/{id_or_code}")
    
    async def fetch_charges_in_batch(self, id_or_code, status, perPage, page, _from=None, to=None):
        payload = {
            "id_or_code": id_or_code,
            "status": status,
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", f"bulkcharge/{id_or_code}/charges", payload)
    
    async def pause_bulk_charge_batch(self, batch_code):
        return await self._make_request("GET", f"bulkcharge/pause/{batch_code}")
    
    async def resume_bulk_charge_batch(self, batch_code):
        return await self._make_request("GET", f"bulkcharge/resume/{batch_code}")