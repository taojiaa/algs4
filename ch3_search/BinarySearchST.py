from utils import FrequencyCounter, compare
from Base import SortedSymbolTable


class BinarySearchST(SortedSymbolTable):
    def __init__(self, capacity):
        self._keys = [None] * capacity
        self._vals = [None] * capacity
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def contains(self, key):
        if self.get(key):
            return True
        return False

    def rank(self, key):
        def rank_helper(key, lo, hi):
            # lo, hi is the number index.
            if lo > hi:
                return lo
            mid = lo + (hi - lo) // 2
            cmpt = compare(key, self._keys[mid])
            if cmpt > 0:
                return rank_helper(key, mid+1, hi)
            elif cmpt < 0:
                return rank_helper(key, lo, mid-1)
            else:
                return mid
        return rank_helper(key, 0, self._size - 1)

    def min(self):
        return self._keys[0]

    def max(self):
        return self._keys[-1]

    def select(self, k):
        return self._keys[k]

    def delete(self, key):
        pass

    def delete_min(self, key):
        pass

    def delete_max(self, key):
        pass

    def floor(self, key):
        pass

    def ceiling(self, key):
        pass

    def keys(self):
        return self._keys

    def range_size(self, lo, hi):
        if lo > hi:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def range_keys(self, lo, hi):
        pass


if __name__ == '__main__':
    st = BinarySearchST()
    FrequencyCounter('./test_data/random_words.txt', st)
