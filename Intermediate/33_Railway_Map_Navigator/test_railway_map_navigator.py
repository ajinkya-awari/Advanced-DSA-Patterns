import pytest
from railway_map_navigator import RailwayMap

def test_railway_routing():
    rm = RailwayMap()
    rm.add_connection("London", "Paris", 2.5)
    rm.add_connection("Paris", "Berlin", 8.0)
    rm.add_connection("London", "Berlin", 12.0)
    
    path, cost = rm.find_shortest_route("London", "Berlin")
    assert path == ["London", "Paris", "Berlin"]
    assert cost == 10.5
