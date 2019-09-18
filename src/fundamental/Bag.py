class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Bag:

    def __init__(self):
        self.first = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, val):
        if self.is_empty():
            self.first = Node(val)
        else:
            temp = self.first
            self.first = Node(val)
            self.first.next = temp
        self._size = self._size + 1

    def __iter__(self):
        node = self.first
        while True:
            if node is None:
                return
            else:
                yield node.val
                node = node.next
