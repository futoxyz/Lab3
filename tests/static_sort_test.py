import pytest
from src.sorting import *
from src.constants import INT_DISTINCT_LIST, INT_DUPLICATES_LIST, INT_FLOAT_LIST, ALGOS_LIST


def is_sorted(func, *args, **kwargs) -> bool:
    '''
    Подтверждение, что после работы функции возвращается отсортированный список.
    :param func: Проверяемая функция.
    :param args: Массив.
    :param kwargs: Дополнительный аргумент для сортировки (для radix sort: base и bucket sort: buckets).
    :return: True/False.
    '''
    array = func(*args, **kwargs)
    n = len(array)

    for i in range(n - 1):
        if array[i] > array[i + 1]:
            return False
    return True


def test_static_sort() -> None:
    '''
    Проверка всех алгоритмов сортировки на заданных массивах на 100 чисел.
    :return: Ничего не возвращает.
    '''
    ALGOS = [globals()[name] for name in ALGOS_LIST]
    for func in ALGOS:
        assert is_sorted(func, INT_DISTINCT_LIST) == True

    for func in ALGOS:
        assert is_sorted(func, INT_DUPLICATES_LIST) == True

    '''Отдельно для bucket sort массив с числами с плавающей точкой.'''
    assert is_sorted(bucket_sort, INT_FLOAT_LIST) == True
