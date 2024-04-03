from .base import PaystackBase

class PaystackProducts(PaystackBase):
    async def create_product(self, name, description, price, currency, unlimited=None, quantity=None):
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity
        }
        return await self._make_request("POST", "/product", payload)
    
    async def list_products(self, perPage, page, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/product", params=params)
    
    async def fetch_product(self, id):
        return await self._make_request("GET", f"/product/{id}")
    
    async def fetch_subaccount(self, id, name, description, price, currency, unlimited=None, quantity=None):
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "currency": currency,
            "unlimited": unlimited,
            "quantity": quantity
        }
        return await self._make_request("PUT", f"/product/{id}", payload)