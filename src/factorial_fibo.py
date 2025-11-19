from src.constants import ROOT

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Input can't be negative integer")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Input can't be negative integer")

    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n: int) -> int:
    '''
    Вычисляется через формулу Бине.
    '''
    if n <= 0:
        raise ValueError("Input must me positive integer")

    return round(((1 + ROOT) ** n - (1 - ROOT) ** n) / (ROOT * 2 ** n))


def fibo_recursive(n: int) -> int:
    if n <= 0:
        raise ValueError("Input must me positive integer")

    if n == 1 or n == 2:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
