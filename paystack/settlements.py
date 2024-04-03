from .base import PaystackBase

class PaystackSettlements(PaystackBase):
    async def list_settlements(self, perPage, page,status=None, subaccount=None, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "status": status,
            "subaccount": subaccount,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/settlement", params=params)
    
    async def list_settlement_transactions(self, id, perPage, page,_from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", f"/settlement/{id}/transactions", params=params)