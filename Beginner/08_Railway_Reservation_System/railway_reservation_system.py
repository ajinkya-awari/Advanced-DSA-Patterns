from typing import List, Optional
from collections import deque
from dataclasses import dataclass

@dataclass
class Passenger:
    """Represents a passenger in the reservation system."""
    passenger_id: int
    name: str
    status: str  # 'CONFIRMED' or 'WAITLIST'

class RailwayReservationSystem:
    """
    Enterprise-grade Railway Reservation System with Waitlist management.
    
    Attributes:
        _total_seats (int): Capacity of the coach.
        _confirmed (List[Passenger]): List of confirmed bookings.
        _waitlist (deque[Passenger]): FIFO queue for overflow.
    """

    def __init__(self, total_seats: int):
        self._total_seats: int = total_seats
        self._confirmed: List[Passenger] = []
        self._waitlist: deque[Passenger] = deque()
        self._id_counter: int = 1

    def book_ticket(self, name: str) -> Passenger:
        """
        Creates a booking and assigns status based on availability.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if len(self._confirmed) < self._total_seats:
            passenger = Passenger(self._id_counter, name, "CONFIRMED")
            self._confirmed.append(passenger)
        else:
            passenger = Passenger(self._id_counter, name, "WAITLIST")
            self._waitlist.append(passenger)
        
        self._id_counter += 1
        return passenger

    def cancel_ticket(self, passenger_id: int) -> bool:
        """
        Cancels a ticket and promotes the next person from waitlist.
        
        Time Complexity: O(N) for search and list/deque removal.
        Space Complexity: O(1)
        """
        # Search in confirmed list
        for i, p in enumerate(self._confirmed):
            if p.passenger_id == passenger_id:
                self._confirmed.pop(i)
                self._promote_from_waitlist()
                return True
        
        # Search in waitlist
        for p in self._waitlist:
            if p.passenger_id == passenger_id:
                self._waitlist.remove(p)
                return True
        
        return False

    def _promote_from_waitlist(self) -> None:
        """Promotes the next passenger in line to confirmed status."""
        if self._waitlist:
            promoted_passenger = self._waitlist.popleft()
            promoted_passenger.status = "CONFIRMED"
            self._confirmed.append(promoted_passenger)

    def get_status(self, passenger_id: int) -> Optional[str]:
        """Retrieves current booking status for a passenger."""
        for p in self._confirmed:
            if p.passenger_id == passenger_id:
                return p.status
        for p in self._waitlist:
            if p.passenger_id == passenger_id:
                return p.status
        return None

    @property
    def confirmed_count(self) -> int:
        return len(self._confirmed)

    @property
    def waitlist_count(self) -> int:
        return len(self._waitlist)
