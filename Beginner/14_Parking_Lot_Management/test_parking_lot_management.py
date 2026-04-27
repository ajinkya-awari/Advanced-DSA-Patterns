import pytest
from parking_lot_management import ParkingLot, Vehicle

@pytest.fixture
def lot():
    return ParkingLot(capacity=5)

def test_park_vehicle(lot):
    """Verify vehicles are parked correctly."""
    lot.park_vehicle("ABC-123", "Tesla")
    assert lot.get_lane_occupancy() == 1
    assert lot.peek_last_parked().license_plate == "ABC-123"

def test_lifo_retrieval_top(lot):
    """Verify O(1) retrieval of the top vehicle."""
    lot.park_vehicle("CAR-1", "Model 1")
    lot.park_vehicle("CAR-2", "Model 2")
    
    retrieved = lot.retrieve_vehicle("CAR-2")
    assert retrieved.license_plate == "CAR-2"
    assert lot.get_lane_occupancy() == 1
    assert lot.peek_last_parked().license_plate == "CAR-1"

def test_deep_retrieval_with_buffer(lot):
    """Verify that moving cars to reach a deep vehicle preserves order."""
    lot.park_vehicle("A", "M1")
    lot.park_vehicle("B", "M2")
    lot.park_vehicle("C", "M3")
    
    # Retrieve 'A' (bottom of stack)
    retrieved = lot.retrieve_vehicle("A")
    assert retrieved.license_plate == "A"
    assert lot.get_lane_occupancy() == 2
    # 'C' should still be at the top, then 'B'
    assert lot.peek_last_parked().license_plate == "C"

def test_capacity_limit(lot):
    """Verify parking lot enforces max capacity."""
    for i in range(5):
        lot.park_vehicle(f"P-{i}", "Model")
    
    with pytest.raises(MemoryError, match="full"):
        lot.park_vehicle("EXTRA", "Model")

def test_duplicate_plate_prevention(lot):
    """Verify that duplicate license plates are rejected."""
    lot.park_vehicle("XYZ", "Truck")
    with pytest.raises(ValueError, match="already parked"):
        lot.park_vehicle("XYZ", "Van")

def test_retrieve_missing_vehicle(lot):
    """Verify that order is restored even if search fails."""
    lot.park_vehicle("A", "M1")
    lot.park_vehicle("B", "M2")
    
    with pytest.raises(KeyError, match="not found"):
        lot.retrieve_vehicle("GHOST")
    
    # Check that 'B' is still at the top
    assert lot.get_lane_occupancy() == 2
    assert lot.peek_last_parked().license_plate == "B"
