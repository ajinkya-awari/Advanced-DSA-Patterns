import pytest
from chat_application import MessageBroker, ChatUser, ChatMessage

@pytest.fixture
def broker():
    b = MessageBroker()
    b.register_user("Alice")
    b.register_user("Bob")
    return b

def test_message_flow(broker):
    """Verify that a message flows from sender -> broker -> recipient."""
    broker.enqueue_message("Alice", "Bob", "Hello Bob!")
    assert broker.get_user("Bob").pending_count == 0  # Still in global queue
    
    delivered_count = broker.process_queue()
    assert delivered_count == 1
    
    bob = broker.get_user("Bob")
    assert bob.pending_count == 1
    
    msg = bob.fetch_messages()[0]
    assert msg.content == "Hello Bob!"
    assert msg.sender_id == "Alice"
    assert bob.pending_count == 0

def test_multi_message_order(broker):
    """Verify FIFO order is preserved during delivery."""
    broker.enqueue_message("Alice", "Bob", "Msg 1")
    broker.enqueue_message("Alice", "Bob", "Msg 2")
    
    broker.process_queue()
    messages = broker.get_user("Bob").fetch_messages()
    
    assert messages[0].content == "Msg 1"
    assert messages[1].content == "Msg 2"

def test_unregistered_user_rejection(broker):
    """Verify that the system prevents communication with ghost users."""
    with pytest.raises(KeyError):
        broker.enqueue_message("Alice", "Ghost", "Hey")

def test_duplicate_registration(broker):
    """Verify user uniqueness constraint."""
    with pytest.raises(ValueError, match="already registered"):
        broker.register_user("Alice")

def test_bulk_dispatch(broker):
    """Verify broker handles multiple messages to different recipients."""
    broker.register_user("Charlie")
    
    broker.enqueue_message("Alice", "Bob", "A to B")
    broker.enqueue_message("Bob", "Alice", "B to A")
    broker.enqueue_message("Alice", "Charlie", "A to C")
    
    broker.process_queue()
    
    assert broker.get_user("Alice").pending_count == 1
    assert broker.get_user("Bob").pending_count == 1
    assert broker.get_user("Charlie").pending_count == 1
