import httpx

class RequestBuilder:
    """
    Class for building payload data for API requests.
    """

    @staticmethod
    def build_initialize_transaction_payload(amount, email, currency=None, reference=None, callback_url=None, **kwargs):
        """
        Build payload for initializing a transaction.
        """
        payload = {
            'amount': amount,
            'email': email,
            'currency': currency,
            'reference': reference,
            'callback_url': callback_url,
            **kwargs,
        }
        return payload

    @staticmethod
    def build_charge_authorization_payload(amount, email, authorization_code, reference=None, **kwargs):
        """
        Build payload for charging an authorization.
        """
        payload = {
            'amount': amount,
            'email': email,
            'authorization_code': authorization_code,
            'reference': reference,
            **kwargs,
        }
        return payload

    @staticmethod
    async def async_build_initialize_transaction_payload(amount, email, currency=None, reference=None, callback_url=None, **kwargs):
        """
        Asynchronously build payload for initializing a transaction.
        """
        payload = {
            'amount': amount,
            'email': email,
            'currency': currency,
            'reference': reference,
            'callback_url': callback_url,
            **kwargs,
        }
        return payload

    @staticmethod
    async def async_build_charge_authorization_payload(amount, email, authorization_code, reference=None, **kwargs):
        """
        Asynchronously build payload for charging an authorization.
        """
        payload = {
            'amount': amount,
            'email': email,
            'authorization_code': authorization_code,
            'reference': reference,
            **kwargs,
        }
        return payload
