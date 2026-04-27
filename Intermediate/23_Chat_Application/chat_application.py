from typing import List, Dict, Optional, Final
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class ChatMessage:
    """Immutable entity representing a single message."""
    sender_id: str
    recipient_id: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)

class ChatUser:
    """Represents a chat participant with a dedicated inbox queue."""
    def __init__(self, user_id: str):
        self.user_id: Final[str] = user_id
        self._inbox: deque[ChatMessage] = deque()

    def receive(self, message: ChatMessage) -> None:
        """Adds a message to the user's private inbox queue."""
        self._inbox.append(message)

    def fetch_messages(self) -> List[ChatMessage]:
        """Retrieves and clears all pending messages from the inbox."""
        messages = list(self._inbox)
        self._inbox.clear()
        return messages

    @property
    def pending_count(self) -> int:
        return len(self._inbox)

class MessageBroker:
    """
    Central Message Broker simulating asynchronous message distribution.
    
    Attributes:
        _global_queue (deque[ChatMessage]): The main queue for incoming traffic.
        _users (Dict[str, ChatUser]): Registry of active users.
    """

    def __init__(self):
        self._global_queue: deque[ChatMessage] = deque()
        self._users: Dict[str, ChatUser] = {}

    def register_user(self, user_id: str) -> ChatUser:
        """Registers a new user with the broker."""
        if user_id in self._users:
            raise ValueError(f"User {user_id} is already registered.")
        user = ChatUser(user_id)
        self._users[user_id] = user
        return user

    def enqueue_message(self, sender_id: str, recipient_id: str, content: str) -> None:
        """
        Submits a message to the broker's global queue.
        Time Complexity: O(1)
        """
        if sender_id not in self._users or recipient_id not in self._users:
            raise KeyError("One or more users not registered in the system.")
            
        message = ChatMessage(sender_id, recipient_id, content)
        self._global_queue.append(message)

    def process_queue(self) -> int:
        """
        Dispatches all messages from the global queue to recipient inboxes.
        Time Complexity: O(N) where N is the number of pending messages.
        Returns: Number of messages delivered.
        """
        count = 0
        while self._global_queue:
            msg = self._global_queue.popleft()
            recipient = self._users.get(msg.recipient_id)
            if recipient:
                recipient.receive(msg)
                count += 1
        return count

    def get_user(self, user_id: str) -> ChatUser:
        if user_id not in self._users:
            raise KeyError(f"User {user_id} not found.")
        return self._users[user_id]
