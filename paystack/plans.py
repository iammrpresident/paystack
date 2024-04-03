from .base import PaystackBase

class PaystackPlans(PaystackBase):
    async def create_plan(self, name, amount, interval, description=None, send_invoices=None, send_sms=None, currency=None, invoice_limit=None):
        payload = {
            "name": name,
            "amount": amount,
            "interval": interval,
            "description": description,
            "send_invoices": send_invoices,
            "send_sms": send_sms,
            "currency": currency,
            "invoice_limit": invoice_limit
        }
        return await self._make_request("POST", "/plan", payload)
    
    async def list_plans(self, perPage, page, status=None, interval=None, amount=None):
        params = {
            "perPage": perPage,
            "page": page,
            "status": status,
            "interval": interval,
            "amount": amount
        }
        return await self._make_request("GET", "/plan" ,params=params)
    
    async def fetch_plan(self, id_or_code):
        return await self._make_request("GET", f"/plan/{id_or_code}")
    
    async def update_plan(self, id_or_code, name, amount, interval, description=None, send_invoices=None, send_sms=None, currency=None, invoice_limit=None):
        payload = {
            "name": name,
            "amount": amount,
            "interval": interval,
            "description": description,
            "send_invoices": send_invoices,
            "send_sms": send_sms,
            "currency": currency,
            "invoice_limit": invoice_limit
        }
        return await self._make_request("PUT", f"/plan/{id_or_code}", payload)