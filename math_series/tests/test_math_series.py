from math_series import __version__
from math_series.math_series import *

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci():
    actual = [fibonacci(0) ,fibonacci(1),fibonacci(2),fibonacci(3),fibonacci(-2)]
    expected = [0, 1, 1, 2, "negative num is not allowed"] 
    assert actual == expected

def test_lucas():

    actual = [lucas(0) ,lucas(1),lucas(2),lucas(3),lucas(-2)]
    expected = [2, 1, 3, 4, "negative num is not allowed"] 
    assert actual == expected

