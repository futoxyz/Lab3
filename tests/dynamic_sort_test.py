from src.constants import ALGOS
from src import arrays_generator
from tests.static_sort_test import is_sorted


def test_dynamic_sort() -> None:
    '''
    Проверка всех алгоритмов сортировки на генерируемых массивах.
    :return: Ничего не возвращает.
    '''
    for func in ALGOS.values():
        '''Кейс для различных чисел'''
        distinct_arr = arrays_generator.rand_int_array(100, 0, 1000, distinct=True, seed=None)
        assert is_sorted(func, distinct_arr)

    for func in ALGOS.values():
        '''Кейс для значительного числа повторяющихся чисел'''
        duplicates_arr = arrays_generator.many_duplicates(100, 35, seed=None)
        assert is_sorted(func, duplicates_arr)

    for func in ALGOS.values():
        '''Кейс для почти отсортированного массива'''
        nearly_arr = arrays_generator.nearly_sorted(100, 10, seed=None)
        assert is_sorted(func, nearly_arr)

    for func in ALGOS.values():
        '''Кейс для отраженного массива'''
        duplicates_arr = arrays_generator.reverse_sorted(100)
        assert is_sorted(func, duplicates_arr)


    '''Отдельно для bucket sort массив с числами с плавающей точкой.'''
    float_arr = arrays_generator.rand_float_array(100, 0, 25)
    assert is_sorted(ALGOS["Bucket sort"], float_arr)
