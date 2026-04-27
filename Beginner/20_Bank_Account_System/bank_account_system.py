from typing import Optional, List, Final
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

class TransactionType(Enum):
    DEPOSIT = auto()
    WITHDRAWAL = auto()

@dataclass(frozen=True)
class Transaction:
    """Immutable record of a financial transaction."""
    amount: float
    type: TransactionType
    timestamp: datetime
    balance_after: float

class TransactionNode:
    """Node representing an entry in the transaction ledger."""
    def __init__(self, transaction: Transaction):
        self.transaction: Transaction = transaction
        self.next: Optional['TransactionNode'] = None

class BankAccount:
    """
    Enterprise-grade Bank Account System using a Linked List for transaction history.
    
    Attributes:
        _account_holder (str): Name of the account owner.
        _balance (float): Current account balance.
        _head (Optional[TransactionNode]): Oldest transaction in history.
        _tail (Optional[TransactionNode]): Most recent transaction in history.
    """

    def __init__(self, account_holder: str, initial_deposit: float = 0.0):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        
        self._account_holder: str = account_holder
        self._balance: float = 0.0
        self._head: Optional[TransactionNode] = None
        self._tail: Optional[TransactionNode] = None
        
        if initial_deposit > 0:
            self.deposit(initial_deposit)

    def _add_to_history(self, amount: float, t_type: TransactionType) -> None:
        """Appends a transaction to the linked list in O(1) time."""
        transaction = Transaction(
            amount=amount,
            type=t_type,
            timestamp=datetime.now(),
            balance_after=self._balance
        )
        new_node = TransactionNode(transaction)

        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def deposit(self, amount: float) -> None:
        """
        Increases the balance and records the transaction.
        Time Complexity: O(1)
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self._balance += amount
        self._add_to_history(amount, TransactionType.DEPOSIT)

    def withdraw(self, amount: float) -> None:
        """
        Decreases the balance if funds are sufficient.
        Time Complexity: O(1)
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self._balance:
            raise RuntimeError(f"Insufficient funds. Current balance: {self._balance}")
            
        self._balance -= amount
        self._add_to_history(amount, TransactionType.WITHDRAWAL)

    def get_history(self) -> List[Transaction]:
        """
        Retrieves all transactions in chronological order.
        Time Complexity: O(N)
        """
        history = []
        current = self._head
        while current:
            history.append(current.transaction)
            current = current.next
        return history

    @property
    def current_balance(self) -> float:
        return self._balance

    @property
    def account_holder(self) -> str:
        return self._account_holder
