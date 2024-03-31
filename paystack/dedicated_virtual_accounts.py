from .base import PaystackBase

class PaystackDedicatedVirtualAccount(PaystackBase):
    async def create_dedicated_virtual_account(self, customer, preferred_bank=None, subaccount=None, split_code=None, first_name=None, last_name=None, phone=None):
        payload = {
            "customer": customer,
            "preferred_bank": preferred_bank,
            "subaccount": subaccount,
            "split_code": split_code,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone
        }
        return await self._make_request("POST", "/dedicated_account", payload)
    
    async def assign_dedicated_account(self, email, first_name, last_name, phone, preferred_bank, country, account_number=None, split_code=None, bvn=None, bank_code=None, subaccount=None):
        payload = {
            "email": email,
            "preferred_bank": preferred_bank,
            "subaccount": subaccount,
            "split_code": split_code,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "country": country,
            "account_number": account_number,
            "bvn": bvn,
            "bank_code": bank_code
        }
        return await self._make_request("POST", "/dedicated_account/assign", payload)
    
    async def list_dedicated_account(self, active, currency, customer, provider_slug=None, bank_id=None):
        payload = {
            "customer": customer,
            "active": active,
            "currency": currency,
            "bank_id": bank_id,
            "provider_slug": provider_slug,
        }
        return await self._make_request("GET", "/dedicated_account", payload)
    
    async def fetch_dedicated_account(self, dedicated_account_id):
        return await self._make_request("GET", f"/dedicated_account/{dedicated_account_id}")
    
    async def query_dedicated_account(self, account_number, provider_slug, date=None):
        params = {
            "account_number": account_number,
            "provider_slug": provider_slug,
            "date": date
        }
        return await self._make_request("GET", "/dedicated_account", params=params)
    
    async def split_dedicated_account(self, customer, subaccount, split_code, preferred_bank):
        payload = {
            "customer": customer,
            "subaccount": subaccount,
            "split_code": split_code,
            "preferred_bank": preferred_bank
        }
        return await self._make_request("GET", "/dedicated_account/split", payload)
    
    async def remove_split_dedicated_account(self, account_number):
        payload = {
            "account_number": account_number
        }
        return await self._make_request("DEL", "/dedicated_account/split", payload)
    
    async def fetch_bank_providers(self):
        return await self._make_request("GET", "/dedicated_account/available_providers")
    
    async def deactivate_dedicated_account(self, dedicated_account_id):
        return await self._make_request("DEL", f"/dedicated_account/{dedicated_account_id}")