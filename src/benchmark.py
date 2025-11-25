import time
from src.constants import STATIC_DICT, ALGOS
from typing import Callable
from src.arrays_generator import dynamic_benchmark_arrays
from rich import print
from rich.table import Table

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
    :return: Ничего не возвращает. Выводит отчёт бенчмарка в консоль.
    '''
    match dynamic:
        case True:
            arrays = dynamic_benchmark_arrays()
            title = "Dynamic benchmark results"
        case False:
            arrays = STATIC_DICT
            title = "Static benchmark results"
    result: dict[str, dict[str, float]] = benchmark_sorts(arrays, ALGOS)
    table = Table(title=title)

    table.add_column("List type",justify="left" , style="magenta", no_wrap=True)
    table.add_column("Algorithm", justify="left")
    table.add_column("Time", justify="left", style="cyan")
    for lst, res in result.items():
        algorithms: list[str] = []
        times: list[str] = []
        for alg, tm in res.items():
            algorithms.append(alg)
            times.append(f"{tm}s")
        table.add_row(lst, "\n".join(algorithms), "\n".join(times))
        table.add_section()
    print(table)
    return
