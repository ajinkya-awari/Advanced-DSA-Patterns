import pytest
from electricity_grid_optimizer import ElectricityGridOptimizer

def test_mst_grid_optimization():
    # Stations: S1, S2, S3
    # Options: S1-S2 (10), S2-S3 (5), S1-S3 (20)
    # Optimal: S2-S3 and S1-S2 (Total 15)
    optimizer = ElectricityGridOptimizer(["S1", "S2", "S3"])
    optimizer.add_cable_option("S1", "S2", 10)
    optimizer.add_cable_option("S2", "S3", 5)
    optimizer.add_cable_option("S1", "S3", 20)
    
    mst, cost = optimizer.get_optimal_grid()
    assert cost == 15.0
    assert len(mst) == 2
