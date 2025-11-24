import time
from src.constants import STATIC_DICT, ALGOS
from typing import Callable
from src.arrays_generator import dynamic_benchmark_arrays

def timeit_once(func, *args, **kwargs) -> float:
    '''
    Измерение времени работы сортировки для некоторого массива.
    :param func: Фукнция (метод) сортировки.
    :param args: Список для сортировки.
    :param kwargs: Дополнительный аргумент для сортировки (для radix sort: base и bucket sort: buckets)
    :return: Время, за которое завершилась сортировка.
    '''
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, Callable]) -> dict[str, dict[str, float]]:
    '''
    Запуск бенчмарка для разных алгоритмов сортировки на различных заданных массивах.
    :param arrays: Словарь измеряемых массивов.
    :param algos: Словарь проверяемых алгоритмов.
    :return: Словарь результатов.
    '''
    result: dict[str, dict[str, float]] = {}
    for arr_name, arr in arrays.items():
        result[arr_name] = {}
        for algo_name, algo_func in algos.items():
            test_arr = arr.copy()
            time_taken = timeit_once(algo_func, test_arr)
            result[arr_name][algo_name] = time_taken

    return result

def run_benchmark(dynamic=True) -> None:
    '''
    Функция запуска и вывода бенчмарка.
    :param dynamic: True, если нужен бенчмарк с генерируемыми массивами, False для заданных массивов.
    :return: Отчёт бенчмарка.
    '''
    match dynamic:
        case True:
            arrays = dynamic_benchmark_arrays()
        case False:
            arrays = STATIC_DICT
    result: dict[str, dict[str, float]] = benchmark_sorts(arrays, ALGOS)
    for lst, res in result.items():
        print(f"\n{lst}")
        print("_")
        for alg, tm in res.items():
            print(f"{alg} - {tm}s")
    return
