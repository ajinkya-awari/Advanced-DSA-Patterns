from typing import List, Optional, Final
from dataclasses import dataclass

@dataclass
class Vehicle:
    """Represents a vehicle in the parking lot."""
    license_plate: str
    model: str

class ParkingLot:
    """
    Enterprise-grade Parking Lot Manager using Stack-based LIFO logic.
    
    Attributes:
        _capacity (int): Maximum vehicles allowed in the lane.
        _stack (List[Vehicle]): The primary parking lane.
    """

    def __init__(self, capacity: int = 10):
        self._capacity: Final[int] = capacity
        self._stack: List[Vehicle] = []

    def park_vehicle(self, license_plate: str, model: str) -> None:
        """
        Parks a vehicle at the end of the lane.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if len(self._stack) >= self._capacity:
            raise MemoryError("Parking lot is full.")
        
        # Check for duplicate plates in the lot
        for v in self._stack:
            if v.license_plate == license_plate:
                raise ValueError(f"Vehicle with plate {license_plate} is already parked.")

        self._stack.append(Vehicle(license_plate, model))

    def retrieve_vehicle(self, license_plate: str) -> Vehicle:
        """
        Retrieves a specific vehicle, moving others if necessary.
        
        Time Complexity: O(N) where N is the number of vehicles in the lane.
        Space Complexity: O(N) for the temporary buffer stack.
        """
        if not self._stack:
            raise IndexError("Parking lot is empty.")

        temp_buffer: List[Vehicle] = []
        target_vehicle: Optional[Vehicle] = None

        # Move vehicles to buffer until target is found
        while self._stack:
            current = self._stack.pop()
            if current.license_plate == license_plate:
                target_vehicle = current
                break
            temp_buffer.append(current)

        # Restore the obstructing vehicles back to the lane
        while temp_buffer:
            self._stack.append(temp_buffer.pop())

        if not target_vehicle:
            raise KeyError(f"Vehicle with plate {license_plate} not found in the lot.")

        return target_vehicle

    def get_lane_occupancy(self) -> int:
        """Returns the current number of parked vehicles."""
        return len(self._stack)

    def peek_last_parked(self) -> Optional[Vehicle]:
        """Returns the vehicle closest to the exit (top of stack)."""
        return self._stack[-1] if self._stack else None
