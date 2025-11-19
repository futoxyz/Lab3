class Node:
    def __init__(self, value: int, prev: int | None = None, next: int | None = None) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class Queue:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length: int = 0

    def is_empty(self) -> bool:
        return not self.head

    def __len__(self) -> int:
        return self.length

    def enqueue(self, x: int) -> None:
        if self.is_empty():
            self.head = Node(x)
            self.tail = self.head
        elif not self.tail:
            self.tail = Node(x)
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            new_node = Node(x, self.tail)
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Queue is empty")

        x = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        self.length -= 1
        return x

    def front(self) -> int:
        try:
            return self.head.value
        except:
            raise IndexError("Queue is empty")
