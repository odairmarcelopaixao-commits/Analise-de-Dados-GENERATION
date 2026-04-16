import pytest
from app import send_message, get_all_messages, send_multiple_messages, get_last_message

def test_send_message():
    # Testa o envio de uma mensagem individual
    assert send_message("testuser", "testuser@example.com") is None

def test_get_all_messages():
    # Testa se a planilha retorna uma lista de dados
    messages = get_all_messages()
    assert isinstance(messages, list)

def test_send_multiple_messages():
    # Testa o envio de várias linhas de uma vez
    data = [
        {"name": "testuser2", "email": "testuser2@example.com"},
        {"name": "testuser3", "email": "testuser3@example.com"}
    ]
    assert send_multiple_messages(data) is None

def test_get_last_message():
    # Testa se a função de buscar o último registro funciona
    messages = get_all_messages()
    if len(messages) > 0:
        assert get_last_message() is None