class Node:
    '''
    Класс для создания массива, каждый из элементов которого имеет ссылки prev и next, чтобы обращаться
    к предыдущему и следующему элементам соответственно.
    '''
    def __init__(self, value: int) -> None:
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class Queue:
    def __init__(self) -> None:
        '''
        :param head: - Элемент в начале очереди.
        :param tail: - Элемент в конце очереди.
        :param length: - Длина массива.
        '''
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def is_empty(self) -> bool:
        '''
        :return: True, если очередь пустая, иначе False.
        '''
        return not self.head

    def __len__(self) -> int:
        return self.length

    def enqueue(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        elif not self.tail:
            self.tail = Node(x)
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            node = Node(x)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self) -> int:
        if self.head:
            x = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None

            self.length -= 1
            return x
        else:
            raise IndexError("Queue is empty")

    def front(self) -> int:
        '''
        Обращается к элементу в начале очереди, но не достает его.
        :return: Значение элемента в начале очереди.
        '''
        if self.head:
            return self.head.value
        else:
            raise IndexError("Queue is empty")
