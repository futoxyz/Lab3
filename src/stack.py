class Node:
    '''
    Класс для создания массива, каждый из элементов которого имеет только ссылку next, чтобы обращаться
    к следующему элементу.
    '''
    def __init__(self, value: int, next: int | None = None) -> None:
        self.value = value
        self.next = next


class Stack:
    def __init__(self) -> None:
        '''
        :param self.tail: Элемент в конце стека.
        :param self.length: Длина стека.
        '''
        self.tail: Node | None = None
        self.length: int = 0

    def is_empty(self) -> bool:
        '''
        :return: True, если стек пустой, иначе False.
        '''
        return not self.tail

    def __len__(self) -> int:
        return self.length

    def push(self, x: int) -> None:
        self.tail = Node(x, self.tail)
        self.length += 1

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")

        x = self.tail.value
        self.tail = self.tail.next
        self.length -= 1
        return x

    def peek(self) -> int:
        '''
        Обращается к элементу в конце стека, но не достает его.
        :return: Значение элемента в конце стека.
        '''
        try:
            return self.tail.value
        except:
            raise IndexError("Stack is empty")
