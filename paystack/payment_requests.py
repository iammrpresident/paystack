from .base import PaystackBase

class PaystackPaymentRequest(PaystackBase):
    async def create_payment_request(self, customer, amount, due_date=None, description=None, line_items=None, tax=None, currency=None, send_notification=None, draft=None, has_invoice=None, invoice_number=None, split_code=None):
        payload = {
            "customer": customer,
            "amount": amount,
            "due_date": due_date,
            "description": description,
            "line_items": line_items,
            "tax": tax,
            "currency": currency,
            "send_notification": send_notification,
            "draft": draft,
            "has_invoice": has_invoice,
            "invoice_number": invoice_number,
            "split_code": split_code
        }
        return await self._make_request("POST", "/paymentrequest", payload)
    
    async def list_payment_request(self, perPage, page, customer, status, currency, include_archive, _from=None, to=None):
        params = {
            "perPage": perPage,
            "page": page,
            "customer": customer,
            "status": status,
            "currency": currency,
            "include_archive": include_archive,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/paymentrequest", params=params)
    
    async def fetch_payment_request(self, id_or_code):
        return await self._make_request("GET", f"/paymentrequest/{id_or_code}")
    
    async def verify_payment_request(self, code):
        return await self._make_request("POST", f"/paymentrequest/verify/{code}")
    
    async def send_notification(self, code):
        return await self._make_request("POST", f"/paymentrequest/notify/{code}")
    
    async def payment_request_total(self):
        return await self._make_request("GET", "/paymentrequest/totals")
    
    async def finalize_payment_request(self, code, send_notification):
        payload = {
            "send_notification": send_notification
        }
        return await self._make_request("POST", f"/paymentrequest/finalize/{code}", payload)
    
    async def update_payment_request(self, id_or_code, customer, amount, due_date=None, description=None, line_items=None, tax=None, currency=None, send_notification=None, draft=None, has_invoice=None, invoice_number=None, split_code=None):
        payload = {
            "customer": customer,
            "amount": amount,
            "due_date": due_date,
            "description": description,
            "line_items": line_items,
            "tax": tax,
            "currency": currency,
            "send_notification": send_notification,
            "draft": draft,
            "has_invoice": has_invoice,
            "invoice_number": invoice_number,
            "split_code": split_code
        }
        return await self._make_request("PUT", f"/paymentrequest/{id_or_code}", payload)
    
    async def archive_payment_request(self, code):
        return await self._make_request("POST", f"/paymentrequest/archive/{code}")