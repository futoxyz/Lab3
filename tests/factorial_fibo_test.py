import pytest
from src.factorial_fibo import *
from src.constants import FIBO_VALUES, FACTORIAL_VALUES

def fibo_test():
    with pytest.raises(ValueError):
        fibo(-5)

    with pytest.raises(ValueError):
        fibo(0)

    for i in range(1, 50):
        assert fibo(i) == FIBO_VALUES[i]

def fibo_recursive_test():
    with pytest.raises(ValueError):
        fibo_recursive(-5)

    with pytest.raises(ValueError):
        fibo_recursive(0)

    for i in range(1, 50):
        assert fibo_recursive(i) == FIBO_VALUES[i]


def factorial_test():
    with pytest.raises(ValueError):
        factorial(-5)
    assert factorial(0) == 1
    for i in range(35):
        assert factorial(i) == FACTORIAL_VALUES[i]

def factorial_recursive_test():
    with pytest.raises(ValueError):
        factorial_recursive(-5)
    assert factorial_recursive(0) == 1
    for i in range(35):
        assert factorial_recursive(i) == FACTORIAL_VALUES[i]

factorial_test(), factorial_recursive_test(), fibo_test(), fibo_recursive_test()