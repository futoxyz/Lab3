import pytest
from src.constants import ALGOS
from src.arrays_generator import *
from tests.static_sort_test import is_sorted


def test_dynamic_sort() -> None:
    '''
    Проверка всех алгоритмов сортировки на генерируемых массивах.
    :return: Ничего не возвращает.
    '''
    for func in ALGOS.values():
        '''Кейс для различных чисел'''
        distinct_arr = rand_int_array(100, 0, 1000, distinct=True, seed=None)
        assert is_sorted(func, distinct_arr) == True

    for func in ALGOS.values():
        '''Кейс для значительного числа повторяющихся чисел'''
        duplicates_arr = many_duplicates(100, 35, seed=None)
        assert is_sorted(func, duplicates_arr) == True

    for func in ALGOS.values():
        '''Кейс для почти отсортированного массива'''
        nearly_arr = nearly_sorted(100, 10, seed=None)
        assert is_sorted(func, nearly_arr) == True

    for func in ALGOS.values():
        '''Кейс для отраженного массива'''
        duplicates_arr = reverse_sorted(100)
        assert is_sorted(func, duplicates_arr) == True


    '''Отдельно для bucket sort массив с числами с плавающей точкой.'''
    float_arr = rand_float_array(100, 0, 25)
    assert is_sorted(ALGOS["Bucket sort"], float_arr) == True


    '''Тесты для неправильного ввода'''
    for func in ALGOS.values():
        with pytest.raises(ValueError):
            func("abc")
        with pytest.raises(ValueError):
            func(123)
        with pytest.raises(ValueError):
            func(["a", "b"])
        with pytest.raises(ValueError):
            func([[1,2], [3]])
