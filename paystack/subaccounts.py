from .base import PaystackBase

class PaystackSubaccounts(PaystackBase):
    async def create_subaccount(self, business_name, settlement_bank, account_number, percentage_charge, description, primary_contact_email=None, primary_contact_phone=None, primary_contact_name=None, metadata=None):
        payload = {
            "business_name":business_name,
            "settlement_bank": settlement_bank,
            "account_number": account_number,
            "percentage_charge": percentage_charge,
            "description": description,
            "primary_contact_email": primary_contact_email,
            "primary_contact_name": primary_contact_name,
            "primary_contact_phone": primary_contact_phone,
            "metadata": metadata
        }
        return await self._make_request("POST", "/subaccount", payload)
    
    async def list_subaccount(self, perPage, page, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/subaccount", params=params)
    
    async def fetch_subaccount(self, id_or_code):
        return await self._make_request("GET", f"/subaccount/{id_or_code}")
    
    async def update_subaccount(self, id_or_code, business_name, settlement_bank, account_number=None, active=None, percentage_charge=None, description=None, primary_contact_email=None, primary_contact_name=None, primary_contact_phone=None, settlement_schedule=None, metadata=None):
        payload = {
            "business_name":business_name,
            "settlement_bank": settlement_bank,
            "account_number": account_number,
            "percentage_charge": percentage_charge,
            "description": description,
            "primary_contact_email": primary_contact_email,
            "primary_contact_name": primary_contact_name,
            "primary_contact_phone": primary_contact_phone,
            "metadata": metadata,
            "active": active,
            "settlement_schedule": settlement_schedule
        }
        return await self._make_request("PUT", f"/subaccount/{id_or_code}", payload)