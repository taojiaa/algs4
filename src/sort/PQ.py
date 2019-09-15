class MaxPQ:

    def __init__(self, N):
        self.pq = [None] * (N + 1)
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def insert(self, val):
        if self._size >= len(self.pq) - 1:
            self._resize(len(self.pq) * 2)
        self._size = self._size + 1
        self.pq[self._size] = val
        self._swim(self._size)
        
    def del_max(self):
        max_val = self.pq[1]
        self.pq[1], self.pq[self._size] = self.pq[self._size], self.pq[1]
        self.pq[self._size + 1] = None
        self._size = self._size - 1
        self._sink(1)
        return max_val

    def _swim(self, k):
        while k > 1:
            j = k // 2
            if self.pq[k] > self.pq[j]:
                self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            else:
                break
            k = j

    def _sink(self, k):
        while (k * 2) <= self._size:
            j = k * 2
            if j < self._size and self.pq[j] < self.pq[j + 1]:
                j = j + 1
            if self.pq[k] < self.pq[j]:
                self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            else:
                break
            k = j

    def _resize(self, capacity):
        assert capacity >= self._size
        temp_pq = [None] * capacity
        for i in range(len(self.pq)):
            temp_pq[i] = self.pq[i]
        self.pq = temp_pq
