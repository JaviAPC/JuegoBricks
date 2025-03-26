import pytest
from src.conversor_km_millas import km_a_millas

def test_km_a_millas():
    assert km_a_millas(1) == pytest.approx(0.621371, 0.0001)
    assert km_a_millas(10) == pytest.approx(6.21371, 0.0001)
    assert km_a_millas(0) == 0