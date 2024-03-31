from .base import PaystackBase

class PaystackVerification(PaystackBase):
       async def resolve_account_number(self, account_number, bank_code):
           params = {
               "account_number": account_number,
               "bank_code": bank_code
           }
           return await self._make_request("GET", "/bank/resolve", params=params)
       
       async def validate_account(self, account_name, account_number, account_type, bank_code, country_code, document_type, document_number=None):
           payload = {
               "account_name": account_name,
               "account_number": account_number,
               "account_type": account_type,
               "bank_code": bank_code,
               "country_code": country_code,
               "document_type": document_type,
               "document_number": document_number
           }
           return await self._make_request("POST", "/bank/validate", payload)
       
       async def resolve_card_bin(self, bin):
           return await self._make_request("GET", f"/decision/{bin}")