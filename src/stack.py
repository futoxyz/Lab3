class Node:
    def __init__(self, value: int, next: int | None = None) -> None:
        self.value = value
        self.next = next


class Stack:
    def __init__(self) -> None:
        self.tail: Node | None = None
        self.length: int = 0


    def is_empty(self) -> bool:
        return not self.tail


    def __len__(self):
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
