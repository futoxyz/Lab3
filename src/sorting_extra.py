def is_correct(a: list[int]) -> None:
    '''
    Проверка ввода в функцию.
    :param a: Ввод в функцию. Ожидается массив с целыми числами.
    :return: Ничего, если подали массив с целыми числами, иначе ошибка программы.
    '''
    if type(a) is not list:
        raise ValueError(f"Not a list: {a}")
    for el in a:
        if type(el) is not int:
            raise ValueError(f"Not an integer in list: {el}")

def is_correct_float(a) -> None:
    '''
    Аналогичная функция, но для массива с числами с плавающей точкой.
    :param a: Ввод в функцию. Ожидается массив с float.
    :return: Ничего, если подали массив с float, иначе ошибка программы.
    '''
    if type(a) is not list:
        raise ValueError(f"Not a list: {a}")
    for el in a:
        if type(el) is not float and type(el) is not int:
            raise ValueError(f"Not a list of float: {el}")

def partition(a: list[int], low: int, high: int) -> int:
    '''
    Quick sort - Распределение элементов относительного опорного.
    :param a: Сортируемый список.
    :param low: Нижняя грань проверяемых элементов.
    :param high: Верхняя грань проверяемых элементов.
    :return: Индекс опроного элемента.
    '''
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def quick_sort_step(a: list[int], low: int, high: int) -> None:
    '''
    Quick sort - Шаг распределения для левой и правой сторон.
    :param a: Сортируемый список.
    :param low: Нижняя грань проверяемых элементов.
    :param high: Верхняя грань проверяемых элементов.
    :return: Ничего не возвращает.
    '''
    if low < high:
        i = partition(a, low, high) - 1
        quick_sort_step(a, low, i)
        quick_sort_step(a, i + 2, high)


def digit(n: int, exp: int, base: int) -> int:
    '''
    Radix sort - Выделение разряда при текущем показателе.
    :param n: Число для выделения разряда.
    :param exp: Текущее значение показателя.
    :param base: Основание в сортировке.
    :return:
    '''
    if n >= 0:
        return (n // exp) % base
    return - ((abs(n) // exp) % base)


def counting_digit_sort(digit_a: list[int], a: list[int]) -> list[int]:
    '''
    Radix sort - Сортирует основной список, сортируя соотвественный список с раздярами при текущем показателе.
    :param digit_a: Список разрядов.
    :param a: Основной сортируемый список.
    :return: Отсортированный по разрядам основной список.
    '''
    n = len(digit_a)
    largest = max(digit_a)
    count_a = [0] * (largest + 1)
    for i in digit_a:
        count_a[i] += 1
    for j in range(1, largest + 1):
        count_a[j] += count_a[j - 1]
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        x = digit_a[i]
        ans[count_a[x] - 1] = a[i]
        count_a[x] -= 1
    return ans

def quick_sort_bucket(a: list[int]) -> list[int]:
    '''
    Обычный quick sort для сортировки бакетов.
    '''
    quick_sort_step(a, 0, len(a) - 1)
    return a

def heapify(a: list[int], n: int, i: int) -> None:
    '''
    Heap sort - Шаг сортировки поддерева.
    :param a: Список.
    :param n: Размер поддерева.
    :param i: Индекс узла поддерева.
    :return:
    '''
    largest = i
    lf = 2 * i + 1
    rg = 2 * i + 2
    if lf < n and a[lf] > a[largest]:
        largest = lf
    if rg < n and a[rg] > a[largest]:
        largest = rg

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heapify(a, n, largest)
