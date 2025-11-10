def fibo(n: int) -> int:
    root = 5 ** 0.5
    return int(((1 + root) ** n - (1 - root) ** n) / (root * 2 ** n))


def fibo_recursive(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)