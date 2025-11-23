import random


def rand_int_array(n: int, lo: int, hi: int, distinct=False, seed=None) -> list[int]:
    '''
    Генератор неотсортированного списка n целых чисел.
    :param n: Количество чисел в списке.
    :param lo: Нижняя граница чисел.
    :param hi: Верхняя граница чисел.
    :param distinct: Отсутствие совпадений чисел в списке (True/False).
    :param seed: Сид генерации.
    :return: Список.
    '''
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
    '''
    Генератор списка, который почти отсортирован, и отличается от сортированного малым количеством смен пары чисел.
    :param n: Количество чисел в списке.
    :param swaps: Количество случайно сменённых пар в конечном списке.
    :param seed: Сид генерации.
    :return: Список.
    '''
    if seed:
        random.seed(seed)

    array = list(range(n))
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        while i == j:
            j = random.randint(0, n - 1)
        array[i], array[j] = array[j], array[i]

    return array


def many_duplicates(n: int, k_unique=5, seed=None) -> list[int]:
    '''
    Генератор списка, в котором значительное количество повторений среди чисел.
    :param n: Количество чисел в списке.
    :param k_unique: Количество уникальных чисел, которые будут повторяться в списке.
    :param seed: Сид генерации.
    :return: Список.
    '''
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
    '''
    Генерирует обратно отсортированный список последовательных чисел от n-1 до 0 включительно.
    :param n: Количество чисел в списке.
    :return: Список.
    '''
    return list(range(n-1, -1, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, seed=None) -> list[float]:
    '''
    Генерирует список чисел с плавающей точкой.
    :param n: Количество чисел в списке.
    :param lo: Нижняя граница чисел.
    :param hi: Верхняя граница чисел.
    :param seed: Сид генерации.
    :return: Список float.
    '''
    if seed:
        random.seed(seed)

    array = []
    while len(array) < n:
        array.append(random.uniform(lo, hi))

    return array


def dynamic_benchmark_arrays() -> dict:
    '''
    :return: Словарь сгенерированных списков для бенчмарка.
    '''
    arrays = {}
    arrays["Distinct int"] = rand_int_array(100, 0, 1000, distinct=True, seed=None)
    arrays["Duplicates int"] = many_duplicates(100, 35, seed=None)
    arrays["Nearly sorted int"] = nearly_sorted(100, 35, seed=None)
    arrays["Reversed int"] = reverse_sorted(100)
    return arrays