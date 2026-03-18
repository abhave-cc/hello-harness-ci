from app import greet

def test_default_greeting():
    assert greet() == "Hello, world!"

def test_named_greeting():
    assert greet("Harness") == "Hello, Harness!"