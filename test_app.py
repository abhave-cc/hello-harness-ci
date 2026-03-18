from app import greet

def test_default_greeting():
    message = greet()
    print(message)
    assert message == "Hello, world!"

def test_named_greeting():
    message = greet("Harness")
    print(message)
    assert message == "Hello, Harness!"
