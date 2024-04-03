from .base import PaystackBase

class PaystackPaymentPages(PaystackBase):
    async def create_payment_pages(self, name, description=None, amount=None, split_code=None, slug=None, metadata=None, redirect_url=None, custom_fields=None):
        payload = {
            "name": name,
            "description": description,
            "amount": amount,
            "split_code": split_code,
            "slug": slug,
            "metadata": metadata,
            "redirect_url": redirect_url,
            "custom_fields": custom_fields
        }
        return await self._make_request("POST", "/page", payload)
    
    async def list_payment_pages(self, perPage, page, customer, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "customer": customer,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/page", params=params)
    
    async def fetch_payment_page(self, id_or_slug):
        return await self._make_request("GET", f"/page/{id_or_slug}")
    
    async def update_payment_page(self, id_or_slug, name, description, amount=None, active=None):
        payload = {
            "name": name,
            "description": description,
            "amount": amount,
            "active": active
        }
        return await self._make_request("PUT", f"/page/{id_or_slug}", payload)
    
    async def check_slug_availability(self, slug):
        return await self._make_request("GET", f"/page/check_slug_availability/{slug}")
    
    async def add_products(self, id, product):
        payload = {
            "product": product
        }
        return await self._make_request("POST", f"/page/{id}/product", payload)