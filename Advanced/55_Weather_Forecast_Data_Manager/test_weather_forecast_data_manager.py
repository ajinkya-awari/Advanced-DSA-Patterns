import pytest
from weather_forecast_data_manager import WeatherTree

def test_weather_range_query():
    temps = [22.5, 25.0, 19.0, 30.5, 28.0]
    wt = WeatherTree(temps)
    assert wt.query_max(0, 2) == 25.0
    assert wt.query_max(2, 4) == 30.5
    assert wt.query_max(0, 4) == 30.5
