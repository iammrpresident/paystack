from .base import PaystackBase

class PaystackTransactionSplits(PaystackBase):
    async def create_split(self, name, type, currency, subaccounts, bearer_type, bearer_subaccount):
        payload = {
            "name": name,
            "type": type,
            "currency": currency,
            "subaccounts": subaccounts,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount
        }
        return await self._make_request("POST", "/split", payload)
    
    async def list_splits(self, name, active, sort_by=None, perPage=None, page=None, _from=None, to=None):
        params = {
            "name": name,
            "active": active,
            "sort_by": sort_by,
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/split", params=params)
    
    async def fetch_split(self, id):
        return await self._make_request("GET", f"/split/{id}")
    
    async def update_split(self, id, name, active, bearer_type=None, bearer_subaccount=None):
        payload = {
            "name": name,
            "active": active,
            "bearer_type": bearer_type,
            "bearer_subaccount": bearer_subaccount
        }
        return await self._make_request("PUT", f"/split/{id}", payload)
    
    async def update_split_subaccount(self, id, subaccount, share):
        payload = {
            "subaccount": subaccount,
            "share": share
        }
        return await self._make_request("POST", f"/split/{id}/subaccount/add", payload)
    
    async def remove_subaccount_split(self, id, subaccount):
        payload = {
            "subaccount": subaccount
        }
        return await self._make_request("POST", f"/split/{id}/subaccount/remove", payload)