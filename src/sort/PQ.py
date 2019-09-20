from .Base import Sort


class PQ:
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

    def _resize(self, capacity):
        assert capacity >= self._size
        temp_pq = [None] * capacity
        for i in range(len(self.pq)):
            temp_pq[i] = self.pq[i]
        self.pq = temp_pq

    def _swim(self):
        pass

    def _sink(self):
        pass


class MaxPQ(PQ):

    def __init__(self, N):
        super().__init__(N)

    def del_max(self):
        max_val = self.pq[1]
        self.pq[1], self.pq[self._size] = self.pq[self._size], self.pq[1]
        self.pq[self._size + 1] = None
        self._size = self._size - 1
        self._sink(self.pq, 1, self.size())
        return max_val

    def _swim(self, k):
        while k > 1:
            j = k // 2
            if self.pq[k] > self.pq[j]:
                self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            else:
                break
            k = j

    def _sink(self, array, k, N):
        while (k * 2) <= N:
            j = k * 2
            if j < N and array[j] < array[j + 1]:
                j = j + 1
            if array[k] < array[j]:
                array[k], array[j] = array[j], array[k]
            else:
                break
            k = j


class MinPQ(PQ):
    def __init__(self, N):
        super().__init__(N)

    def del_min(self):
        min_val = self.pq[1]
        self.pq[1], self.pq[self._size] = self.pq[self._size], self.pq[1]
        self.pq[self._size + 1] = None
        self._size = self._size - 1
        self._sink(self.pq, 1, self.size())
        return min_val

    def _swim(self, k):
        while k > 1:
            j = k // 2
            if self.pq[k] < self.pq[j]:
                self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            else:
                break
            k = j

    def _sink(self, array, k, N):
        while (k * 2) <= N:
            j = k * 2
            if j < N and array[j] > array[j + 1]:
                j = j + 1
            if array[k] > array[j]:
                array[k], array[j] = array[j], array[k]
            else:
                break
            k = j


class HeapSort(Sort, MaxPQ):

    def __init__(self):
        pass

    def sort(self, array):
        N = len(array)
        array = [None] + array
        # Make the heap-ordered.
        for k in range(N // 2, 0, -1):
            self._sink(array, k, N)
        # Make the heap sorted.
        while N > 1:
            array[1], array[N] = array[N], array[1]
            self._sink(array, 1, N - 1)
            N = N - 1
        return array[1:]
