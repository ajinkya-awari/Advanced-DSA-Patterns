import pytest
from distributed_file_sharing import P2PNetwork

def test_p2p_connectivity():
    net = P2PNetwork(["A", "B", "C", "D"])
    net.share_file("A", "config.sys")
    net.share_file("C", "data.db")
    
    net.connect("A", "B")
    assert "config.sys" in net.get_accessible_files("B")
    assert "data.db" not in net.get_accessible_files("B")
    
    net.connect("B", "C")
    assert "data.db" in net.get_accessible_files("A")
