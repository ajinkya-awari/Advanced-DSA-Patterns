import pytest
from network_packet_routing import NetworkRouter, RouteResult

@pytest.fixture
def network():
    nr = NetworkRouter()
    # Build a standard diamond topology
    # A -> B (2), A -> C (5)
    # B -> D (1), C -> D (1)
    nr.add_link("A", "B", 2.0)
    nr.add_link("A", "C", 5.0)
    nr.add_link("B", "D", 1.0)
    nr.add_link("C", "D", 1.0)
    return nr

def test_optimal_routing(network):
    """Verify that the path with least latency is selected."""
    result = network.find_route("A", "D")
    assert result is not None
    assert result.path == ["A", "B", "D"]
    assert result.total_latency == 3.0
    assert result.hops == 2

def test_unreachable_node(network):
    """Verify behavior when no path exists."""
    network.add_link("E", "F", 1.0)
    result = network.find_route("A", "F")
    assert result is None

def test_direct_link():
    """Verify routing between two directly connected nodes."""
    nr = NetworkRouter()
    nr.add_link("Router1", "Router2", 10.5)
    result = nr.find_route("Router1", "Router2")
    assert result.path == ["Router1", "Router2"]
    assert result.total_latency == 10.5

def test_complex_multi_path():
    """Verify Dijkstra efficiency on more complex weights."""
    nr = NetworkRouter()
    nr.add_link("S", "1", 10)
    nr.add_link("S", "2", 2)
    nr.add_link("2", "1", 1)
    nr.add_link("1", "D", 1)
    # Path S->2->1->D (4) is better than S->1->D (11)
    result = nr.find_route("S", "D")
    assert result.path == ["S", "2", "1", "D"]
    assert result.total_latency == 4.0

def test_negative_latency_prevention():
    """Verify validation layer against invalid weights."""
    nr = NetworkRouter()
    with pytest.raises(ValueError, match="cannot be negative"):
        nr.add_link("A", "B", -5.0)

def test_source_is_destination(network):
    """Verify edge case where packet is already at destination."""
    result = network.find_route("A", "A")
    assert result.path == ["A"]
    assert result.total_latency == 0.0
