from unit_testing import square
# pip install pytest



def test_square():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0


# pytest test_unit_testing3.py

