import pytest
from airline_flight_scheduler import FlightScheduler

def test_flight_routing():
    fs = FlightScheduler()
    fs.add_flight("NYC", "LON", 7.0)
    fs.add_flight("LON", "DXB", 6.5)
    fs.add_flight("NYC", "DXB", 15.0)
    path, time = fs.find_optimal_route("NYC", "DXB")
    assert path == ["NYC", "LON", "DXB"]
    assert time == 13.5
