class Stack:
    """A simple LIFO (last-in, first-out) stack backed by a Python list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __repr__(self):
        return f"Stack({self.items})"


class Queue:
    """A simple FIFO (first-in, first-out) queue backed by a Python list."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

    def __repr__(self):
        return f"Queue({self.items})"

def stack_push_pop(n):
    s = Stack()
    for i in range(n):
        s.push(i)
    while not s.is_empty():
        s.pop()


def queue_enqueue_dequeue(n):
    q = Queue()
    for i in range(n):
        q.enqueue(i)
    while not q.is_empty():
        q.dequeue()


STACK_QUEUE_ALGORITHMS = {
    'stack_push_pop': stack_push_pop,
    'queue_enqueue_dequeue': queue_enqueue_dequeue
}