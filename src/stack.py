class Node:
    '''
    Класс для создания массива, каждый из элементов которого имеет только ссылку next, чтобы обращаться
    к следующему элементу.
    '''
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Node | None = None


class Stack:
    def __init__(self) -> None:
        '''
        :param tail: Элемент в конце стека.
        :param length: Длина стека.
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
        node = Node(x)
        node.next = self.tail
        self.tail = node
        self.length += 1

    def pop(self) -> int:
        if self.tail:
            x = self.tail.value
            self.tail = self.tail.next
            self.length -= 1
            return x
        else:
            raise IndexError("Stack is empty")

    def peek(self) -> int:
        '''
        Обращается к элементу в конце стека, но не достает его.
        :return: Значение элемента в конце стека.
        '''
        if self.tail:
            return self.tail.value
        else:
            raise IndexError("Stack is empty")
