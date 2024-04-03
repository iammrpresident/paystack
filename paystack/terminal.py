from .base import PaystackBase

class PaystackTerminal(PaystackBase):
    async def send_event(self, terminal_id, type, action, data):
        payload = {
            "type": type,
            "action": action,
            "data": data
        }
        return await self._make_request("POST", f"/terminal/{terminal_id}/event", payload)
    
    async def fetch_event_status(self, terminal_id, event_id):
        return await self._make_request("GET", f"/terminal/{terminal_id}/event/{event_id}")
    
    async def fetch_terminal_status(self, terminal_id):
        return await self._make_request("GET", f"/terminal/{terminal_id}/presence")
    
    async def list_terminals(self, perPage, next=None, previous=None):
        params = {
            "perPage": perPage,
            "next": next,
            "previous": previous
        }
        return await self._make_request("GET", "/terminal", params=params)
    
    async def fetch_terminal(self, terminal_id):
        return await self._make_request("GET", f"/terminal/{terminal_id}")
    
    async def update_terminal(self, terminal_id, name, address):
        payload = {
            "name": name,
            "address": address
        }
        return await self._make_request("PUT", f"/terminal/{terminal_id}", payload)
    
    async def commission_terminal(self, serial_number):
        payload = {
            "serial_number": serial_number
        }
        return await self._make_request("POST", "/terminal/commission_device", payload)
    
    async def commission_terminal(self, serial_number):
        payload = {
            "serial_number": serial_number
        }
        return await self._make_request("POST", "/terminal/decommission_device", payload)