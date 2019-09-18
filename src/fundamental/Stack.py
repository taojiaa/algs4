class Stack:

    def __init__(self):
        self._stack = []
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, val):
        self._stack.append(val)
        self._size = self._size + 1

    def pop(self):
        if self.is_empty():
            return None
        self._size = self._size - 1
        return self._stack.pop()

    def size(self):
        return self._size

    def __iter__(self):
        while True:
            if self.is_empty():
                return
            else:
                yield self.pop()

