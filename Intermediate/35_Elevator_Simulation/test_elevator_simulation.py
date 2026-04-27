import pytest
from elevator_simulation import Elevator

def test_elevator_batching():
    elevator = Elevator(10)
    elevator.request_floor(5)
    elevator.request_floor(2)
    elevator.request_floor(8)
    
    stops = elevator.process_all_requests()
    # Starting at 0, going up: should stop at 2, 5, 8
    assert stops == [2, 5, 8]

def test_direction_switch():
    elevator = Elevator(10)
    elevator.request_floor(1)
    # Start at 5, direction up
    elevator._current_floor = 5
    elevator.request_floor(3)
    
    stops = elevator.process_all_requests()
    # Direction is UP (1), but requests are at 1 and 3 (DOWN). 
    # System should switch to DOWN and stop at 3 then 1.
    assert stops == [3, 1]
