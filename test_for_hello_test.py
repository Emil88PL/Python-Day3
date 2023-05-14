from hello_for_test import hello

def test_default():
    assert hello() == "Hello, world!" ## No return in hello function
    
def test_arguments():
    assert hello("David") == "Hello, David"

    # asserts test arguments in to functions and return values there from





