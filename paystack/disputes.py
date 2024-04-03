from .base import PaystackBase

class PaystackDisputes(PaystackBase):
    async def list_disputes(self, _from, to, perPage=None, page=None, transaction=None, status=None):
        params = {
            "from": _from,
            "to": to,
            "perPage": perPage,
            "page": page,
            "transaction": transaction,
            "status": status
        }
        return await self._make_request("GET", "/dispute", params=params)
    
    async def fetch_dispute(self, id):
        return await self._make_request("GET", f"/dispute/{id}")
    
    async def list_transaction_disputes(self, id):
        return await self._make_request("GET", f"/dispute/transaction/{id}")
    
    async def update_dispute(self, id, refund_ammount, uploaded_filename):
        payload = {
            "refund_amount": refund_ammount,
            "uploaded_filename": uploaded_filename
        }
        return await self._make_request("PUT", f"/dispute/{id}", payload)
    
    async def add_evidence(self, id, customer_email, customer_name, customer_phone, service_details, delivery_address=None, delivery_date=None):
        payload = {
            "customer_email": customer_email,
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "service_details": service_details,
            "delivery_address": delivery_address,
            "delivery_date":delivery_date
        }
        return await self._make_request("POST", f"/dispute/{id}/evidence", payload)
    
    async def get_upload_url(self, id, uploaded_filename):
        params = {
            "uploaded_filename": uploaded_filename
        }
        return await self._make_request("GET", f"/dispute/{id}/upload_url", params=params)
    
    async def resolve_dispute(self, id, resolution, message, refunded_amount, uploaded_filename, evidence=None):
        payload = {
            "resolution": resolution,
            "message": message,
            "refunded_amount": refunded_amount,
            "uploaded_filename": uploaded_filename,
            "evidence": evidence
        }
        return await self._make_request("PUT", f"/dispute/{id}/resolve", payload)
    
    async def export_diuspute(self, _from, to, perPage=None, page=None, transaction=None, status=None):
        params = {
            "from": _from,
            "to": to,
            "perPage": perPage,
            "page": page,
            "transaction": transaction,
            "status": status
        }
        return await self._make_request("GET", "/dispute/export", params=params)