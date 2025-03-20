import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1,4)
    assert result == 5

def test_add_srings():
    result = my_functions.add("i like ","world")
    assert result == "i like world"

def test_div():
    result = my_functions.divide(10,5)
    assert result == 2

def test_div_by_zero():
    with  pytest.raises(ZeroDivisionError):
        my_functions.divide(10,0)
    