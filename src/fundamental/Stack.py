class Stack:

    def __init__(self, capacity=2):
        self._stack = [None] * capacity
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, val):
        if self._size > len(self._stack) // 2:
            self._resize(len(self._stack) * 2)
        self._stack[self._size] = val
        self._size = self._size + 1

    def pop(self):
        if self.is_empty():
            return None
        self._size = self._size - 1
        pop = self._stack[self._size]
        self._stack[self._size] = None
        if self._size < len(self._stack) // 4:
            self._resize(len(self._stack) // 2)
        return pop

    def size(self):
        return self._size

    def _resize(self, n):
        temp = [None] * n
        for i in range(len(self._stack)):
            temp[i] = self._stack[i]
        self._stack = temp

    def __iter__(self):
        while True:
            if self.is_empty():
                return
            else:
                yield self.pop()
