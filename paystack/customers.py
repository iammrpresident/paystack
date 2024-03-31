from .base import PaystackBase

class PaystackCustomers(PaystackBase):
    """Wrapper class for interacting with the Paystack Customers API."""
    
    async def create_customer(self, email, first_name=None, last_name=None, phone=None, metadata=None):
        """Create a new customer.
        
        Args:
            email (str): The email address of the customer (required).
            first_name (str, optional): The first name of the customer.
            last_name (str, optional): The last name of the customer.
            phone (str, optional): The phone number of the customer.
            metadata (dict, optional): Additional data to attach to the customer.
        
        Returns:
            dict: The created customer data.
        """
        payload = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "metadata": metadata
        }
        return await self._make_request("POST", "/customer", payload)
    
    async def list_customer(self, perPage=None, page=None, _from=None, to=None):
        """List customers with optional pagination parameters.
        
        Args:
            perPage (int): Number of customers to return per page.
            page (int): Page number to return.
            from (datetime): A timestamp from which to start listing customers
            to (datetime): A timestamp from which to stop listing customers
        
        Returns:
            dict: The list of customers.
        """
        params = {
            "perPage": perPage,
            "page": page,
            "from": _from,
            "to": to
        }
        return await self._make_request("GET", "/customer", params=params)
    
    async def fetch_customer(self, email_or_code):
        """Fetch a customer by ID.
        
        Args:
            email_or_code (str): An email or customer code you want to fetch.
        
        Returns:
            dict: The fetched customer data.
        """
        return await self._make_request("GET", f"/customer/{email_or_code}")
    
    async def update_customer(self, first_name, last_name, code, phone=None, metadata=None):
        """Update an existing customer.
        
        Args:
            code (str): The code of the customer to update.
            first_name (str, optional): The updated first name of the customer.
            last_name (str, optional): The updated last name of the customer.
            phone (str, optional): The updated phone number of the customer.
            metadata (dict, optional): Updated metadata for the customer.
        
        Returns:
            dict: The updated customer data.
        """
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "code": code,
            "phone": phone,
            "metadata": metadata
        }
        return await self._make_request("PUT", f"customer/{code}", payload)
    
    async def validate_customer(self, code, first_name, last_name, type, value, country, bvn, bank_code, account_number, middle_name=None):
        payload = {
            "code": code,
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
            "type": type,
            "value": value,
            "country": country,
            "bvn": bvn,
            "bank_code": bank_code,
            "account_number": account_number
        }
        return await self._make_request("POST", f"customer/{code}/identification")
    
    async def whitelist_or_blacklist_customer(self, customer, risk_action=None):
        payload = {
            "customer": customer,
            "risk_actions": risk_action
        }
        return await self._make_request("POST", "customer/set_risk_action", payload)
    
    async def deactivate_authorization(self, authorization_code):
        """Deactivate a customer's authorization.
        
        Args:
            authorization_code (str): The authorization code of the customer to deactivate.
        
        Returns:
            dict: Confirmation of customer deactivation.
        """
        payload = {
            "authorization_code": authorization_code
        }
        return await self._make_request("POST", "customer/deactivate_authorization", payload)