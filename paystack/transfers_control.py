from .base import PaystackBase

class PaystackTransferControl(PaystackBase):
    async def check_balance(self):
        return await self._make_request("GET", "/balance")
    
    async def fetch_balance_ledger(self):
        return await self._make_request("GET", "/balance/ledger")
    
    async def resend_transfer_otp(self, transfer_code, reason):
        payload = {
            "transfer_code": transfer_code,
            "reason": reason
        }
        return await self._make_request("POST", "/transfer/resend_otp", payload)
    
    async def disable_transfer_otp(self):
        return await self._make_request("POST", "/transfer/disable_otp")
    
    async def finalize_disable_otp(self, otp):
        payload = {
            "otp": otp
        }
        return await self._make_request("POST", "/transfer/disable_otp_finalize", payload)
    
    async def enable_transfer_otp(self):
        return await self._make_request("POST", "/transfer/enable_otp")