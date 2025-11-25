from src.benchmark import run_benchmark

def main() -> None:
    """
    Запуск программы (два бенчмарка).
    :return: Данная функция ничего не возвращает
    """
    run_benchmark(dynamic=False)
    run_benchmark()
    return


if __name__ == "__main__":
    main()
