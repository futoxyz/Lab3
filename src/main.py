from src.constants import FUNCTIONS
from src.option import option


def main() -> None:
    """
    Запуск программы
    :return: Данная функция ничего не возвращает
    """
    while inp := input(f"Choose the operation (only a number) {FUNCTIONS}\n> "):
        option(inp)


if __name__ == "__main__":
    main()
