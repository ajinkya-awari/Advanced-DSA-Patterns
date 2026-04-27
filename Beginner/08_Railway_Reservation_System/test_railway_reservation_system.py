import pytest
from railway_reservation_system import RailwayReservationSystem

@pytest.fixture
def system():
    # Coach with only 2 seats for easy testing of waitlist logic
    return RailwayReservationSystem(total_seats=2)

def test_booking_and_waitlist(system):
    """Verify that bookings exceed capacity correctly enter the waitlist."""
    p1 = system.book_ticket("Alice")
    p2 = system.book_ticket("Bob")
    p3 = system.book_ticket("Charlie")
    
    assert p1.status == "CONFIRMED"
    assert p2.status == "CONFIRMED"
    assert p3.status == "WAITLIST"
    assert system.confirmed_count == 2
    assert system.waitlist_count == 1

def test_cancellation_and_promotion(system):
    """Verify that cancelling a confirmed ticket promotes the first waitlisted passenger."""
    p1 = system.book_ticket("Alice")
    system.book_ticket("Bob")
    p3 = system.book_ticket("Charlie") # Waitlist
    
    assert system.cancel_ticket(p1.passenger_id) is True
    assert system.confirmed_count == 2
    assert system.waitlist_count == 0
    
    # Check if p3 (Charlie) is now confirmed
    assert system.get_status(p3.passenger_id) == "CONFIRMED"

def test_waitlist_cancellation(system):
    """Verify that cancelling a ticket directly from the waitlist works."""
    system.book_ticket("Alice")
    system.book_ticket("Bob")
    p3 = system.book_ticket("Charlie")
    
    assert system.cancel_ticket(p3.passenger_id) is True
    assert system.confirmed_count == 2
    assert system.waitlist_count == 0

def test_cancel_non_existent(system):
    """Ensure system handles invalid cancellation IDs gracefully."""
    assert system.cancel_ticket(999) is False

def test_get_status_missing(system):
    """Verify status retrieval for non-existent IDs."""
    assert system.get_status(500) is None
