from .base import PaystackBase

class PaystackIntegration(PaystackBase):
    async def fetch_payment_session_timeout(self):
        return await self._make_request("GET", "/integration/payment_session_timeout")
    
    async def update_payment_session_timeout(self, timeout):
        payload = {
            "timeout": timeout
        }
        return await self._make_request("PUT", "/integration/payment_session_timeout", payload)