from .base import PaystackBase

class PaystackCharge(PaystackBase):
    async def create_charge(self, email, amount, bank=None, bank_transfer=None, qr=None, authorization_code=None, pin=None, metadata=None, reference=None, ussd=None, mobile_money=None, device_id=None):
        payload = {
            "email": email,
            "amount": amount,
            "bank": bank,
            "bank_transfer": bank_transfer,
            "qr": qr,
            "authorization_code": authorization_code,
            "pin": pin,
            "metadata":metadata,
            "reference": reference,
            "ussd": ussd,
            "mobile_money": mobile_money,
            "device_id": device_id
        }
        return await self._make_request("POST", "/charge", payload)
    
    async def submit_pin(self, pin, reference):
        payload = {
            "pin": pin,
            "reference": reference
        }
        return await self._make_request("POST", "charge/submit_pin", payload)
    
    async def submit_otp(self, otp, reference):
        payload = {
            "otp": otp,
            "reference": reference
        }
        return await self._make_request("POST", "charge/submit_otp", payload)
    
    async def submit_phone(self, phone, reference):
        payload = {
            "phone": phone,
            "reference": reference
        }
        return await self._make_request("POST", "charge/submit_phone", payload)
    
    async def submit_birthday(self, birthday, reference):
        payload = {
            "birthday": birthday,
            "reference": reference
        }
        return await self._make_request("POST", "charge/submit_birthday", payload)
    
    async def submit_pin(self, address, reference, city, state, zipcode):
        payload = {
            "address": address,
            "reference": reference,
            "city": city,
            "state": state,
            "zipcode": zipcode
        }
        return await self._make_request("POST", "charge/submit_address", payload)
    
    async def submit_pin(self, reference):
        return await self._make_request("POST", f"charge/{reference}")