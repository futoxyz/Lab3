import pytest
from src.factorial_fibo import fibo, fibo_recursive, factorial, factorial_recursive
from src.constants import FIBO_VALUES, FACTORIAL_VALUES

'''
Тест 4 функций на верный результат (Первые 30 чисел по таблице в константах).
'''

def test_fibo() -> None:
    with pytest.raises(ValueError):
        fibo(-5)

    with pytest.raises(ValueError):
        fibo(0)

    for i in range(1, 30):
        assert fibo(i) == FIBO_VALUES[i]

def test_fibo_recursive() -> None:
    with pytest.raises(ValueError):
        fibo_recursive(-5)

    with pytest.raises(ValueError):
        fibo_recursive(0)

    for i in range(1, 30):
        assert fibo_recursive(i) == FIBO_VALUES[i]


def test_factorial() -> None:
    with pytest.raises(ValueError):
        factorial(-5)
    assert factorial(0) == 1
    for i in range(30):
        assert factorial(i) == FACTORIAL_VALUES[i]

def test_factorial_recursive() -> None:
    with pytest.raises(ValueError):
        factorial_recursive(-5)
    assert factorial_recursive(0) == 1
    for i in range(30):
        assert factorial_recursive(i) == FACTORIAL_VALUES[i]
