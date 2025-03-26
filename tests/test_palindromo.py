import pytest
from src.palindromo import es_palindromo

def test_es_palindromo():
    assert es_palindromo("Anita lava la tina") is True
    assert es_palindromo("Hola mundo") is False
    assert es_palindromo("oso") is True