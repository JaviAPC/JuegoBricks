import pytest
from src.operaciones import potencia, es_par

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(10, 2) == 100

def test_es_par():
    assert es_par(4) is True
    assert es_par(7) is False
    assert es_par(0) is True
