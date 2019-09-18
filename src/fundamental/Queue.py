class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:

    def __init__(self, capacity=2):
        self._size = 0
        self.first = None
        self.last = None

    def enqueue(self, val):
        if val is None:
            raise ValueError('Nonetype is not allowed to enqueue.')
        self.old_last = self.last
        self.last = Node(val)
        if self.is_empty():
            self.first = self.last
        else:
            self.old_last.next = self.last
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('The Queue is already empty.')
        else:
            item = self.first.val
            self.first = self.first.next
            if self.is_empty():
                self.last = None
            self._size -= 1
            return item

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def __iter__(self):
        current = self.first
        while True:
            if current is None:
                return
            else:
                yield current.val
                current = current.next
