from hello_for_test import hello

def test_default():
    assert hello() == "Hello, world!"

def test_arguments():
    assert hello("David") == "Hello, David"

