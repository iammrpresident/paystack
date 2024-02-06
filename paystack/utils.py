import re
import asyncio

def validate_email(email):
    """
    Validate if the provided email is in a valid format.
    """
    # Use a simple regular expression for basic email validation
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(re.match(email_pattern, email))

def format_amount(amount):
    """
    Format the amount according to the API requirements.
    """
    # Assuming the API expects amounts in subunits, multiply by 100
    formatted_amount = int(amount * 100)
    return formatted_amount

async def async_validate_email(email):
    """
    Asynchronously validate if the provided email is in a valid format.
    """
    return validate_email(email)

async def async_format_amount(amount):
    """
    Asynchronously format the amount according to the API requirements.
    """
    return format_amount(amount)

