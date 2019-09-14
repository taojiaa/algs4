from random import shuffle

from .Base import Sort


class Quick(Sort):

    def __init__(self):
        super(Quick, self).__init__()

    def sort(self, array):
        shuffle(array)
        self._sort(array, 0, len(array) - 1)
        return array

    def _sort(self, array, lo, hi):
        if lo >= hi:
            return
        p = self._partition(array, lo, hi)
        # The recursion is after the array processing.
        self._sort(array, lo, p - 1)
        self._sort(array, p + 1, hi)
    
    def _partition(self, array, lo, hi):
        # Scan the array from left to right and right to left,
        # then find the "break" points i and j and exhcange them.
        p = lo
        i, j = lo + 1, hi
        while True:
            while i < hi:
                if array[p] <= array[i]:
                    break
                i = i + 1
            while j > lo:
                if array[p] > array[j]:
                    break
                j = j - 1
            if i >= j:
                break
            array[i], array[j] = array[j], array[i]
        array[p], array[j] = array[j], array[p]
        return j

    def _partition2(self, array, lo, hi):
        # Insert the smaller one before p and larger one in the end.
        p = lo
        p_1, p_2 = lo + 1, hi
        while p_1 <= p_2:
            if array[p_1] <= array[p]:
                array[p_1], array[p] = array[p], array[p_1]
                p = p + 1
                p_1 = p_1 + 1
            else:
                array[p_2], array[p_1] = array[p_1], array[p_2]
                p_2 = p_2 - 1
        return p




