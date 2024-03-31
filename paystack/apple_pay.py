from .base import PaystackBase

class PaystackApplePay(PaystackBase):
    async def register_domain(self, domainName):
        payload = {
            "domainName": domainName
        }
        return await self._make_request("POST", "/apple-pay/domain", payload)
    
    async def list_domain(self, use_cursor, next=None, previous=None):
        params = {
            "use_cursor": use_cursor,
            "next": next,
            "previous": previous
        }
        return await self._make_request("GET", "/apple-pay/domain", params=params)
    
    async def unregister_domain(self, domainName):
        payload = {
            "domainName": domainName
        }
        return await self._make_request("POST", "/apple-pay/domain", payload)