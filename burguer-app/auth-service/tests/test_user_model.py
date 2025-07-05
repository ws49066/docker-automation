import pytest
import os
import sys

# Adiciona o diretório pai ao sys.path para facilitar importação local
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user_model import serialize_user  # ajuste conforme sua estrutura

# -------------------------
# ✅ TESTES FUNCIONAIS VÁLIDOS
# -------------------------

@pytest.mark.parametrize("user, esperado", [
    (
        # Caso 1: todos os campos presentes
        {
            "email": "teste@exemplo.com",
            "name": "Fulano",
            "address": "Rua A, 123",
            "role": "admin"
        },
        {
            "email": "teste@exemplo.com",
            "name": "Fulano",
            "address": "Rua A, 123",
            "role": "admin"
        }
    ),
    (
        # Caso 2: campos ausentes (exceto email)
        {
            "email": "teste@exemplo.com"
        },
        {
            "email": "teste@exemplo.com",
            "name": "",
            "address": "",
            "role": "cliente"
        }
    ),
    (
        # Caso 3: todos os campos ausentes
        {},
        {
            "email": None,
            "name": "",
            "address": "",
            "role": "cliente"
        }
    ),
    (
        # Caso 4: campos com None como valor
        {
            "email": None,
            "name": None,
            "address": None,
            "role": None
        },
        {
            "email": None,
            "name": None,
            "address": None,
            "role": None
        }
    ),
    (
        # Caso 5: campos com tipos incomuns
        {
            "email": 123,
            "name": ["Nome", "Sobrenome"],
            "address": {"rua": "A"},
            "role": True
        },
        {
            "email": 123,
            "name": ["Nome", "Sobrenome"],
            "address": {"rua": "A"},
            "role": True
        }
    )
])
def test_serialize_user_valido(user, esperado):
    resultado = serialize_user(user)
    assert resultado == esperado

# -------------------------
# ❌ TESTES DE ENTRADAS INVÁLIDAS (NÃO DICIONÁRIO)
# -------------------------

@pytest.mark.parametrize("entrada", [
    None,
    "string",
    12345,
    [],
])
def test_serialize_user_entradas_invalidas(entrada):
    with pytest.raises(AttributeError):
        serialize_user(entrada)
