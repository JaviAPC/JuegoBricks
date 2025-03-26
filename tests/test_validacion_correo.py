import pytest
from src.validaciones import es_email_valido

def test_es_email_valido():
    assert es_email_valido("correo@example.com") is True
    assert es_email_valido("usuario@dominio.co") is True
    assert es_email_valido("correo@com") is False
    assert es_email_valido("sin_arroba.com") is False
    assert es_email_valido("") is False
