import pytest
from src.stack import Stack
from src.queue import Queue


def stack_push():
    a = Stack()
    assert a.is_empty() == True
    a.push(11)
    assert a.is_empty() == False
    a.push(9)
    assert a.is_empty() == False


def stack_fill():
    a = Stack()

    assert a.__len__() == 0

    a.push(15)
    a.push(19)
    a.push(100)

    assert a.__len__() == 3

    a.push(6)
    a.push(9)
    a.push(10)

    assert a.__len__() == 6

    assert a.peek() == 10
    assert a.peek() == 10

    assert a.pop() == 10
    assert a.peek() == 9
    assert a.__len__() == 5

    assert a.pop == 9
    assert a.pop == 6
    assert a.pop == 100
    assert a.pop == 19
    assert a.pop == 15

    with pytest.raises(IndexError):
        a.pop()


def enqueue():
    a = Stack()
    assert a.is_empty() == True
    a.push(11)
    assert a.is_empty() == False
    a.push(9)
    assert a.is_empty() == False


def queue_fill():
    a = Queue()

    assert a.__len__() == 0

    a.enqueue(15)
    a.enqueue(19)
    a.enqueue(100)

    assert a.__len__() == 3

    a.enqueue(6)
    a.enqueue(9)
    a.enqueue(10)

    assert a.__len__() == 6

    assert a.front() == 15
    assert a.front() == 15

    assert a.dequeue() == 15
    assert a.front() == 19
    assert a.__len__() == 5

    assert a.dequeue() == 19
    assert a.dequeue() == 100
    assert a.dequeue() == 6
    assert a.dequeue() == 9
    assert a.dequeue() == 10

    with pytest.raises(IndexError):
        a.dequeue()
