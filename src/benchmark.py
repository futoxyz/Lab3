import time

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

def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    '''
    Запуск бенчмарка для разных алгоритмов сортировки на различных заданных массивах.
    :param arrays: Словарь измеряемых массивов.
    :param algos: Словарь проверяемых алгоритмов.
    :return: Словарь результатов.
    '''
    result = {}
    for array_name, array in arrays.items():
        result[array_name] = {}
        for algo_name, algo_func in algos.items():
            test_array = array.copy()
            time_taken = timeit_once(algo_func, test_array)
            result[array_name][algo_name] = time_taken

    return result
