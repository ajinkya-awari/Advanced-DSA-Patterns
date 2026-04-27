import pytest
from bank_account_system import BankAccount, TransactionType

@pytest.fixture
def account():
    return BankAccount("John Doe", initial_deposit=100.0)

def test_initial_deposit(account):
    """Verify account initialization and initial balance."""
    assert account.current_balance == 100.0
    assert len(account.get_history()) == 1
    assert account.get_history()[0].type == TransactionType.DEPOSIT

def test_deposit_flow(account):
    """Verify balance increments and history tracking."""
    account.deposit(50.0)
    assert account.current_balance == 150.0
    history = account.get_history()
    assert len(history) == 2
    assert history[1].amount == 50.0
    assert history[1].balance_after == 150.0

def test_withdrawal_flow(account):
    """Verify balance decrements and history tracking."""
    account.withdraw(40.0)
    assert account.current_balance == 60.0
    history = account.get_history()
    assert len(history) == 2
    assert history[1].type == TransactionType.WITHDRAWAL
    assert history[1].balance_after == 60.0

def test_insufficient_funds(account):
    """Verify that overdrafts are prevented."""
    with pytest.raises(RuntimeError, match="Insufficient funds"):
        account.withdraw(200.0)
    assert account.current_balance == 100.0

def test_negative_input_validation(account):
    """Verify protection against negative transaction amounts."""
    with pytest.raises(ValueError):
        account.deposit(-10.0)
    with pytest.raises(ValueError):
        account.withdraw(-10.0)

def test_chronological_order(account):
    """Verify that transactions are stored in order of arrival."""
    account.deposit(10.0) # Trans 2
    account.withdraw(5.0) # Trans 3
    
    history = account.get_history()
    assert history[0].amount == 100.0
    assert history[1].amount == 10.0
    assert history[2].amount == 5.0
