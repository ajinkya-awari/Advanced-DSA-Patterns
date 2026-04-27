import pytest
from traffic_navigation_system import TrafficRouter

def test_traffic_aware_routing():
    router = TrafficRouter()
    # Path A -> B -> D (Distance 10 + 10 = 20)
    # Path A -> C -> D (Distance 15 + 10 = 25)
    router.add_road("A", "B", 10)
    router.add_road("B", "D", 10)
    router.add_road("A", "C", 15)
    router.add_road("C", "D", 10)
    
    # Case 1: No traffic, A-B-D is faster (20 vs 25)
    path, time = router.find_fastest_path("A", "D", {})
    assert path == ["A", "B", "D"]
    
    # Case 2: Heavy traffic on B-D (factor 2.0). 
    # A-B-D time: 10 + (10*2) = 30.
    # A-C-D time: 15 + 10 = 25. Now A-C-D is faster.
    path, time = router.find_fastest_path("A", "D", {("B", "D"): 2.0})
    assert path == ["A", "C", "D"]
    assert time == 25.0
