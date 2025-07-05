import pytest
import os
import sys

# Add the parent directory to the path so we can import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user  # ajuste o import conforme seu arquivo

def test_serialize_user_completo():
    user = {
        "email": "teste@exemplo.com",
        "name": "Fulano",
        "address": "Rua A, 123",
        "role": "admin"
    }
    resultado = serialize_user(user)
    esperado = {
        "email": "teste@exemplo.com",
        "name": "Fulano",
        "address": "Rua A, 123",
        "role": "admin"
    }
    assert resultado == esperado

def test_serialize_user_campos_ausentes():
    user = {
        "email": "teste@exemplo.com"
        # name, address e role ausentes
    }
    resultado = serialize_user(user)
    esperado = {
        "email": "teste@exemplo.com",
        "name": "",
        "address": "",
        "role": "cliente"
    }
    assert resultado == esperado

def test_serialize_user_email_ausente():
    user = {}
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }
    assert resultado == esperado

# -------------------------
# ❌ TESTES DE ENTRADAS INVÁLIDAS (NÃO DICIONÁRIO)
# -------------------------

def test_serialize_user_none():
    """Entrada é None: deve lançar AttributeError"""
    with pytest.raises(AttributeError):
        serialize_user(None)

def test_serialize_user_string():
    """Entrada é string: deve lançar AttributeError"""
    with pytest.raises(AttributeError):
        serialize_user("string")

def test_serialize_user_inteiro():
    """Entrada é número: deve lançar AttributeError"""
    with pytest.raises(AttributeError):
        serialize_user(12345)

def test_serialize_user_lista():
    """Entrada é lista: deve lançar AttributeError"""
    with pytest.raises(AttributeError):
        serialize_user([])

# -------------------------
# 🔄 TESTES DE VALORES COM TIPOS INESPERADOS
# -------------------------

def test_serialize_user_valores_none():
    """Campos presentes mas com valor None: None deve ser mantido"""
    user = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    resultado = serialize_user(user)
    esperado = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }
    assert resultado == esperado

def test_serialize_user_tipos_incomuns():
    """Campos com tipos estranhos: devem ser mantidos como estão"""
    user = {
        "email": 123,
        "name": ["Nome", "Sobrenome"],
        "address": {"rua": "A"},
        "role": True
    }
    resultado = serialize_user(user)
    esperado = {
        "email": 123,
        "name": ["Nome", "Sobrenome"],
        "address": {"rua": "A"},
        "role": True
    }
    assert resultado == esperado