def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def fibo(n: int) -> int:
    root = 5 ** 0.5
    return int(((1 + root) ** n - (1 - root) ** n) / (root * 2 ** n))


def fibo_recursive(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)