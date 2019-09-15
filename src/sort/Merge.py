from .Base import Sort


class Merge(Sort):
    def __init__(self):
        super(Merge, self).__init__()

    def sort(self, array):
        # The first high passed in is the one can be achieved (not len(array)).
        self._sort(array, 0, len(array) - 1)
        return array

    def _sort(self, array, lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self._sort(array, lo, mid)
        self._sort(array, mid + 1, hi)
        self._merge(array, lo, mid, hi)

    def _merge(self, array, lo, mid, hi):
        pi, pj = lo, mid + 1
        # The elements in array won't be replaced if aux changes.
        aux = array.copy()
        # The high can be achieved, so it should be hi + 1 here.
        for k in range(lo, hi + 1):
            if pi > mid:
                array[k] = aux[pj]
                pj = pj + 1
            elif pj > hi:
                array[k] = aux[pi]
                pi = pi + 1
            elif aux[pi] < aux[pj]:
                array[k] = aux[pi]
                pi = pi + 1
            else:
                array[k] = aux[pj]
                pj = pj + 1


class MergeBU(Merge):
    def __init__(self):
        super(MergeBU, self).__init__()

    def sort(self, array):
        N = len(array)
        size = 1
        while size < N:
            # merge method sort two consecutive arrays,
            # so we can jump lo by size * 2 steps.
            for lo in range(0, N - size, size * 2):
                self._merge(array, lo, lo + size - 1,
                            min(lo + size * 2 - 1, N - 1))
            size = size * 2
        return array


class MergeX(Merge):
    # Improment 3: TODO

    def __init__(self):
        super(MergeX, self).__init__()

    def _sort(self, array, lo, hi, cut_off=5):
        # Improvement 1: Use insertion to sort small subarrays.
        if hi - lo + 1 <= cut_off:
            self._insert_sort(array, lo, hi)
            return
        mid = lo + (hi - lo) // 2
        self._sort(array, lo, mid)
        self._sort(array, mid + 1, hi)

        # Improment 2: If two sub arrays are already sorted, we just skip the merge.
        if array[mid] > array[mid + 1]:
            self._merge(array, lo, mid, hi)

    def _insert_sort(self, array, lo, hi):
        for i in range(lo, hi + 1):
            for j in range(i, lo, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
                else:
                    break

