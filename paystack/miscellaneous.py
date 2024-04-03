from .base import PaystackBase

class PaystackMiscellaneous(PaystackBase):
    async def list_banks(self, country, use_cursor, perPage, pay_with_bank_transfer=None, pay_with_bank=None, enabled_for_verification=None, next=None, previous=None, gateway=None, type=None, currency=None):
        params = {
            "country": country,
            "use_cursor": use_cursor,
            "perPage": perPage,
            "pay_with_bank_transfer": pay_with_bank_transfer,
            "pay_with_bank": pay_with_bank,
            "enabled_for_verification": enabled_for_verification,
            "next": next,
            "previous": previous,
            "gateway": gateway,
            "type": type,
            "currency": currency
        }
        return await self._make_request("GET", "/bank", params=params)
    
    async def list_countries(self):
        return await self._make_request("GET", "/country")
    
    async def list_states(self, country):
        params = {
            "country": country
        }
        return await self._make_request("GET", "/address_verification/states", params=params)