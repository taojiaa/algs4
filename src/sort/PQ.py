from .Base import Sort


class PQ:
    def __init__(self, N=2):
        self.pq = [None] * (N + 1)
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def insert(self, val):
        if self._size >= len(self.pq) - 1:
            self._resize(len(self.pq) * 2)
        self._size += 1
        self.pq[self._size] = val
        self._swim(self._size)

    def _resize(self, capacity):
        assert capacity >= self._size
        temp_pq = [None] * capacity
        for i in range(len(self.pq)):
            temp_pq[i] = self.pq[i]
        self.pq = temp_pq

    def _swim(self, size):
        pass

    def _sink(self, size):
        pass


class MaxPQ(PQ):

    def __init__(self, N=2):
        super().__init__(N)

    def del_max(self):
        max_val = self.pq[1]
        self.pq[1], self.pq[self._size] = self.pq[self._size], self.pq[1]
        self.pq[self._size + 1] = None
        self._size -= 1
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
    def __init__(self, N=2):
        super().__init__(N)

    def del_min(self):
        min_val = self.pq[1]
        self.pq[1], self.pq[self._size] = self.pq[self._size], self.pq[1]
        self.pq[self._size + 1] = None
        self._size -= 1
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


class IndexMinPQ(MinPQ):

    def __init__(self, max_n):
        self._maxn = max_n
        self._size = 0
        # _ind is a priority queue that we always maintains.
        self._ind = [None] * (self._maxn + 1)
        # _map stores the mapping from index k to the position i in _ind.
        self._map = [None] * (self._maxn + 1)
        # _val stores the value, putting it in the "index" position it links to.
        self._val = [None] * (self._maxn + 1)

    def insert(self, k, val):
        self._size += 1
        self._ind[self._size] = k
        self._map[k] = self._size
        self._val[k] = val
        self._swim(self._size)

    def change(self, k, val):
        self._val[k] = val
        self._swim(self._map[k])
        self._sink(self._map[k])

    def _swim(self, k):
        while k > 1:
            j = k // 2
            ind_1, ind_2 = self._ind[k], self._ind[j]
            if self._val[ind_1] < self._val[ind_2]:
                self._exch(k, j)
            else:
                break
            k = j

    def _sink(self, k):
        while (k * 2) <= self._size:
            j = k * 2
            ind_1, ind_2 = self._ind[j], self._ind[j + 1]
            if j < self._size and self._val[ind_1] > self._val[ind_2]:
                j = j + 1
            ind_1, ind_2 = self._ind[k], self._ind[j]
            if self._val[ind_1] > self._val[ind_2]:
                self._exch(k, j)
            else:
                break
            k = j

    def _exch(self, i, j):
        self._ind[i], self._ind[j] = self._ind[j], self._ind[i]
        # _ind[i] stores the new index at the position i in _ind,
        # so we need to map the new index to position i.
        self._map[self._ind[i]] = i
        self._map[self._ind[j]] = j

    def contains(self, k):
        if self._val[k] is not None:
            return True
        return False

    def delete(self, k):
        pos = self._map[k]
        self._exch(pos, self._size)
        self._size -= 1
        self._swim(pos)
        self._sink(pos)
        self._val[k] = None
        self._map[k] = None
    
    def del_min(self):
        ind = self._ind[1]
        self._exch(1, self._size)
        self._size -= 1
        self._sink(1)
        self._val[ind] = None
        self._map[ind] = None
        return ind

    def min(self):
        return self._val[self._ind[1]]

    def min_index(self):
        return self._ind[1]


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
