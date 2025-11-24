import pytest
from src.constants import INT_DISTINCT_LIST, INT_DUPLICATES_LIST, INT_FLOAT_LIST, ALGOS


def is_sorted(func, *args) -> bool:
    '''
    Подтверждение, что после работы функции возвращается отсортированный список.
    :param func: Проверяемая функция.
    :param args: Массив.
    :return: True/False.
    '''
    array = func(*args)
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
    for func in ALGOS.values():
        assert is_sorted(func, INT_DISTINCT_LIST)

    for func in ALGOS.values():
        assert is_sorted(func, INT_DUPLICATES_LIST)

    '''Отдельно для bucket sort массив с числами с плавающей точкой.'''
    assert is_sorted(ALGOS["Bucket sort"], INT_FLOAT_LIST)


    '''Тесты для неправильного ввода'''
    for func in ALGOS.values():
        with pytest.raises(ValueError):
            func("abc")
        with pytest.raises(ValueError):
            func(123)
        with pytest.raises(ValueError):
            func(["a", "b"])
        with pytest.raises(ValueError):
            func([[1, 2], [3]])
