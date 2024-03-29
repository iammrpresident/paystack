import pytest
from paystack.transactions import PaystackTransactions, APIError

TEST_SECRET_KEY = ""

@pytest.mark.asyncio
async def test_initialize_transaction_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.initialize_transaction(email="test@email.com", amount=1000)
    
    assert "data" in result
    assert "reference" in result["data"]
    assert "authorization_url" in result["data"]
    
@pytest.mark.asyncio
async def test_initialize_transaction_missing_email():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    
    with pytest.raises(ValueError) as exc_info:
        await transactions.initialize_transaction(email="", amount=1000)
    assert str(exc_info.value) == "Email is required for initializing a transaction"
    
@pytest.mark.asyncio
async def test_list_transactions_pagination_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.list_transactions(perPage=50, page=1)
    assert "data" in result

    
@pytest.mark.asyncio
async def test_fetch_transaction_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.fetch_transaction(id="3662687297")
    assert "status" in result

@pytest.mark.asyncio
async def test_fetch_transaction_invalid_id():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    with pytest.raises(APIError):
        await transactions.fetch_transaction(id="3662687297")

@pytest.mark.asyncio
async def test_charge_authorization_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.charge_authorization(email="customer@email.com", amount=1000, authorization_code="AUTH_gpm8a29kf0")
    assert "status" in result

@pytest.mark.asyncio
async def test_charge_authorization_invalid_reference():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    with pytest.raises(APIError):
        await transactions.charge_authorization(email="customer@email.com", authorization_code="AUTH_gpm8a29kf", amount=1000)
        
        
@pytest.mark.asyncio
async def test_verify_transaction_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.verify_transaction(reference="pj2s2fulc8ra2u8")
    assert "data" in result

@pytest.mark.asyncio
async def test_verify_transaction_invalid_reference():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    with pytest.raises(APIError):
        await transactions.verify_transaction(reference="1rqn9smwq")

@pytest.mark.asyncio
async def test_view_transaction_timeline_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.view_transaction_timeline(id_or_reference="3662687297")
    assert "status" in result

@pytest.mark.asyncio
async def test_view_transaction_timeline_invalid_id():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.view_transaction_timeline(id_or_reference="366268729")
    assert "status" in result
    
@pytest.mark.asyncio
async def test_transaction_totals_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.transaction_totals(perPage=None, page=None)
    assert "status" in result
    
@pytest.mark.asyncio
async def test_export_transaction_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.export_transactions(perPage=None, page=None)
    
@pytest.mark.asyncio
async def test_request_reauthorization_success():
    transactions = PaystackTransactions(secret_key=TEST_SECRET_KEY)
    result = await transactions.request_reauthorization(email="customer@email.com", amount=500000, authorization_code="AUTH_gpm8a29kf0")

