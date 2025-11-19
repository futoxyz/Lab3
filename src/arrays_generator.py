import random


def rand_int_array(n: int, lo: int, hi: int, distinct=False, seed=None) -> list[int]:
    if seed:
        random.seed(seed)
    if not distinct:
        array = [random.randint(lo, hi) for _ in range(n)]
    else:
        if  hi - lo + 1 < n:
            raise ValueError(f"Cannot generate {n} distinct numbers in given range")

        array = set()
        while len(array) < n:
            array.add(random.randint(lo, hi))
        array = list(array)
        random.shuffle(array)

    return array


def nearly_sorted(n: int, swaps: int, seed=None) -> list[int]:
    if seed:
        random.seed(seed)

    array = list(range(n))
    for _ in range(swaps):
        i = random.randint(0, n)
        j = random.randint(0, n)
        while i == j:
            j = random.randint(0, n - 1)
        array[i], array[j] = array[j], array[i]

    return array


def many_duplicates(n: int, k_unique=5, seed=None) -> list[int]:
    if seed:
        random.seed(seed)

    array = []
    unique = set()
    while len(unique) < k_unique:
        unique.add(random.randint(0,n))
    unique = list(unique)

    while len(array) < n:
        array.append(random.choice(unique))

    return array


def reverse_sorted(n: int) -> list[int]:
    return list(range(n-1, -1, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, seed=None) -> list[float]:
    if seed:
        random.seed(seed)

    array = []
    while len(array) < n:
        array.append(random.uniform(lo, hi))

    return array
