from .base import PaystackBase

class PaystackSubscriptions(PaystackBase):
    async def create_subscription(self, customer, plan, authorization, start_date=None):
        payload = {
            "customer": customer,
            "plan": plan,
            "authorization": authorization,
            "start_date": start_date
        }
        return await self._make_request("POST", "/subscription", payload)
    
    async def list_subscriptions(self, perPage, page, customer=None, plan=None):
        payload = {
            "customer": customer,
            "plan": plan,
            "perPage": perPage,
            "page": page
        }
        return await self._make_request("GET", "/subscription", payload)
    
    async def fetch_subscription(self, id_or_code):
        return await self._make_request("GET", f"/subscription/{id_or_code}")
    
    async def enable_subscription(self, code, token):
        payload = {
            "code": code,
            "token": token,
        }
        return await self._make_request("POST", "/subscription/enable", payload)
    
    async def disable_subscription(self, code, token):
        payload = {
            "code": code,
            "token": token,
        }
        return await self._make_request("POST", "/subscription/disable", payload)
    
    async def generate_update_subscription_link(self, code):
        return await self._make_request("POST", f"/subscription/{code}/manage/link")
    
    async def send_update_subscription_link(self, code):
        return await self._make_request("POST", f"/subscription/{code}/manage/email")